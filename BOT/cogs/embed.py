import discord
from discord.ext import commands
from discord import app_commands


class Embed(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="embed",
        description="Tworzy embeda"
    )
    @app_commands.checks.has_permissions(administrator=True)
    async def embed(
        self,
        interaction: discord.Interaction,
        tytul: str,
        opis: str,
        kolor: str = "blue"
    ):

        kolory = {
            "red": discord.Color.red(),
            "green": discord.Color.green(),
            "blue": discord.Color.blue(),
            "orange": discord.Color.orange(),
            "purple": discord.Color.purple()
        }

        embed = discord.Embed(
            title=tytul,
            description=opis,
            color=kolory.get(kolor.lower(), discord.Color.blue())
        )

        embed.set_footer(
            text=f"Stworzone przez {interaction.user}"
        )

        await interaction.channel.send(embed=embed)

        await interaction.response.send_message(
            "✅ Embed został wysłany",
            ephemeral=True
        )


async def setup(bot):
    await bot.add_cog(Embed(bot))