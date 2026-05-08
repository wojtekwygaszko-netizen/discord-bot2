import discord
from discord.ext import commands
from discord import app_commands


class Clear(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="clear",
        description="Usuwa wiadomości z kanału"
    )
    @app_commands.checks.has_permissions(administrator=True)
    async def clear(
        self,
        interaction: discord.Interaction,
        ilosc: int
    ):

        if ilosc <= 0:
            await interaction.response.send_message(
                "❌ Podaj liczbę większą od 0",
                ephemeral=True
            )
            return

        deleted = await interaction.channel.purge(limit=ilosc)

        embed = discord.Embed(
            title="🧹 Czyszczenie czatu",
            description=f"Usunięto `{len(deleted)}` wiadomości",
            color=discord.Color.green()
        )

        await interaction.response.send_message(
            embed=embed,
            ephemeral=True
        )


async def setup(bot):
    await bot.add_cog(Clear(bot))