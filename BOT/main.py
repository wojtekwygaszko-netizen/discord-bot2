import discord
import asyncio
import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

# =========================
# START BOT
# =========================

@bot.event
async def on_ready():
    print(f"✅ Zalogowano jako {bot.user}")

    try:
        synced = await bot.tree.sync()
        print(f"✅ Zsynchronizowano {len(synced)} komend slash")
    except Exception as e:
        print("❌ Błąd sync:", e)


# =========================
# LOAD COGS
# =========================

async def load_cogs():
    cogs = [
        "cogs.clear",
        "cogs.embed",
        "cogs.moderation",
        "cogs.rekrutacja"
    ]

    for cog in cogs:
        try:
            await bot.load_extension(cog)
            print(f"✅ Załadowano {cog}")
        except Exception as e:
            print(f"❌ Błąd {cog}: {e}")


# =========================
# START
# =========================

async def main():
    async with bot:
        await load_cogs()
        await bot.start(TOKEN)


asyncio.run(main())