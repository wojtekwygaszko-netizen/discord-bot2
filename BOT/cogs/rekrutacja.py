# cogs/rekrutacja.py

import discord

from discord.ext import commands
from discord import app_commands

# =========================
# ID KANAŁU NA PODANIA
# =========================

KANAL_PODANIA = 1502292070382174439


# =========================
# MODAL PODANIA
# =========================

class PodanieModal(discord.ui.Modal, title="Złóż podanie"):

    nick = discord.ui.TextInput(
        label="Nick w Minecraft",
        placeholder="Np. Steve",
        required=True,
        max_length=30
    )

    wiek = discord.ui.TextInput(
        label="Wiek",
        placeholder="Np. 13",
        required=True,
        max_length=3
    )

    czas_gry = discord.ui.TextInput(
        label="Ile możesz grać?",
        placeholder="Np. 5h dziennie",
        required=True,
        max_length=100
    )

    powod = discord.ui.TextInput(
        label="Dlaczego chcesz dołączyć?",
        style=discord.TextStyle.paragraph,
        placeholder="Napisz dlaczego chcesz dołączyć",
        required=True,
        max_length=1000
    )

    administracja = discord.ui.TextInput(
        label="Czy byłeś kiedyś w administracji?",
        style=discord.TextStyle.paragraph,
        placeholder="Opisz swoje doświadczenie",
        required=True,
        max_length=1000
    )

    async def on_submit(
        self,
        interaction: discord.Interaction
    ):

        kanal = interaction.guild.get_channel(
            KANAL_PODANIA
        )

        embed = discord.Embed(
            title="📨 Nowe podanie",
            color=discord.Color.blurple()
        )

        embed.add_field(
            name="👤 Użytkownik",
            value=interaction.user.mention,
            inline=False
        )

        embed.add_field(
            name="🎮 Nick w Minecraft",
            value=self.nick.value,
            inline=False
        )

        embed.add_field(
            name="🎂 Wiek",
            value=self.wiek.value,
            inline=False
        )

        embed.add_field(
            name="⏰ Ile możesz grać?",
            value=self.czas_gry.value,
            inline=False
        )

        embed.add_field(
            name="⭐ Dlaczego chcesz dołączyć?",
            value=self.powod.value,
            inline=False
        )

        embed.add_field(
            name="🛡️ Czy byłeś kiedyś w administracji?",
            value=self.administracja.value,
            inline=False
        )

        embed.set_thumbnail(
            url=interaction.user.display_avatar.url
        )

        await kanal.send(
            embed=embed
        )

        await interaction.response.send_message(
            "✅ Twoje podanie zostało wysłane!",
            ephemeral=True
        )


# =========================
# BUTTON
# =========================

class RekrutacjaView(discord.ui.View):

    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(
        label="📨 Złóż podanie",
        style=discord.ButtonStyle.green
    )
    async def podanie_button(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        await interaction.response.send_modal(
            PodanieModal()
        )


# =========================
# COG
# =========================

class Rekrutacja(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # =========================
    # OTWÓRZ REKRUTACJE
    # =========================

    @app_commands.command(
        name="otworz_rekrutacje",
        description="Otwiera rekrutacje"
    )
    @app_commands.checks.has_permissions(
        administrator=True
    )
    async def otworz_rekrutacje(
        self,
        interaction: discord.Interaction,
        tytul: str,
        opis: str
    ):

        embed = discord.Embed(
            title=f"📋 {tytul}",
            description=opis,
            color=discord.Color.green()
        )

        embed.add_field(
            name="Status",
            value="🟢 Rekrutacja otwarta",
            inline=False
        )

        embed.set_footer(
            text="Kliknij przycisk poniżej aby złożyć podanie"
        )

        await interaction.response.send_message(
            embed=embed,
            view=RekrutacjaView()
        )

    # =========================
    # AKCEPTUJ
    # =========================

    @app_commands.command(
        name="akceptuj",
        description="Akceptuje użytkownika"
    )
    @app_commands.checks.has_permissions(
        administrator=True
    )
    async def akceptuj(
        self,
        interaction: discord.Interaction,
        member: discord.Member,
        powod: str = "Brak powodu"
    ):

        file = discord.File(
            "images/accept.png",
            filename="accept.png"
        )

        embed = discord.Embed(
            title="✅ Rekrutacja zaakceptowana",
            color=discord.Color.green()
        )

        embed.add_field(
            name="Użytkownik",
            value=member.mention,
            inline=False
        )

        embed.add_field(
            name="Administrator",
            value=interaction.user.mention,
            inline=False
        )

        embed.add_field(
            name="Powód",
            value=powod,
            inline=False
        )

        embed.set_image(
            url="attachment://accept.png"
        )

        await interaction.response.send_message(
            embed=embed,
            file=file
        )

    # =========================
    # ODRZUĆ
    # =========================

    @app_commands.command(
        name="odrzuc",
        description="Odrzuca użytkownika"
    )
    @app_commands.checks.has_permissions(
        administrator=True
    )
    async def odrzuc(
        self,
        interaction: discord.Interaction,
        member: discord.Member,
        powod: str = "Brak powodu"
    ):

        file = discord.File(
            "images/reject.png",
            filename="reject.png"
        )

        embed = discord.Embed(
            title="❌ Rekrutacja odrzucona",
            color=discord.Color.red()
        )

        embed.add_field(
            name="Użytkownik",
            value=member.mention,
            inline=False
        )

        embed.add_field(
            name="Administrator",
            value=interaction.user.mention,
            inline=False
        )

        embed.add_field(
            name="Powód",
            value=powod,
            inline=False
        )

        embed.set_image(
            url="attachment://reject.png"
        )

        await interaction.response.send_message(
            embed=embed,
            file=file
        )


async def setup(bot):
    await bot.add_cog(
        Rekrutacja(bot)
    )
