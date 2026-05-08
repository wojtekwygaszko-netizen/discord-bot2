import discord

from discord.ext import commands
from discord import app_commands
from datetime import timedelta


class Moderation(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # =========================
    # BAN
    # =========================

    @app_commands.command(
        name="ban",
        description="Banuje użytkownika"
    )
    @app_commands.checks.has_permissions(
        ban_members=True
    )
    async def ban(
        self,
        interaction: discord.Interaction,
        member: discord.Member,
        powod: str = "Brak powodu"
    ):

        await member.ban(reason=powod)

        embed = discord.Embed(
            title="🔨 Użytkownik zbanowany",
            color=discord.Color.red()
        )

        embed.add_field(
            name="Użytkownik",
            value=member.mention,
            inline=False
        )

        embed.add_field(
            name="Moderator",
            value=interaction.user.mention,
            inline=False
        )

        embed.add_field(
            name="Powód",
            value=powod,
            inline=False
        )

        await interaction.response.send_message(
            embed=embed
        )

    # =========================
    # KICK
    # =========================

    @app_commands.command(
        name="kick",
        description="Wyrzuca użytkownika"
    )
    @app_commands.checks.has_permissions(
        kick_members=True
    )
    async def kick(
        self,
        interaction: discord.Interaction,
        member: discord.Member,
        powod: str = "Brak powodu"
    ):

        await member.kick(reason=powod)

        embed = discord.Embed(
            title="👢 Użytkownik wyrzucony",
            color=discord.Color.orange()
        )

        embed.add_field(
            name="Użytkownik",
            value=member.mention,
            inline=False
        )

        embed.add_field(
            name="Moderator",
            value=interaction.user.mention,
            inline=False
        )

        embed.add_field(
            name="Powód",
            value=powod,
            inline=False
        )

        await interaction.response.send_message(
            embed=embed
        )

    # =========================
    # MUTE
    # =========================

    @app_commands.command(
        name="mute",
        description="Wycisza użytkownika"
    )
    @app_commands.checks.has_permissions(
        moderate_members=True
    )
    async def mute(
        self,
        interaction: discord.Interaction,
        member: discord.Member,
        minuty: int,
        powod: str = "Brak powodu"
    ):

        czas = timedelta(minutes=minuty)

        await member.timeout(
            czas,
            reason=powod
        )

        embed = discord.Embed(
            title="🔇 Użytkownik wyciszony",
            color=discord.Color.blurple()
        )

        embed.add_field(
            name="Użytkownik",
            value=member.mention,
            inline=False
        )

        embed.add_field(
            name="Czas",
            value=f"{minuty} minut",
            inline=False
        )

        embed.add_field(
            name="Powód",
            value=powod,
            inline=False
        )

        embed.add_field(
            name="Moderator",
            value=interaction.user.mention,
            inline=False
        )

        await interaction.response.send_message(
            embed=embed
        )


async def setup(bot):
    await bot.add_cog(
        Moderation(bot)
    )