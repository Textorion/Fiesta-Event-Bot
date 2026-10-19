import os
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID", "1561744832563511316"))

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Fiesta Event Bot ist online: {bot.user}")
    channel = bot.get_channel(CHANNEL_ID)

    if channel:
        await channel.send(
            "✅ **Fiesta Event Bot ist online!**\n"
            "Server: Fiesta Online EU – Kebing\n"
            "Überwachung der Events wird vorbereitet."
        )
    else:
        print("Discord-Kanal nicht gefunden. Bitte Kanal-ID prüfen.")


@bot.command()
async def test(ctx, event="teva"):
    events = {
        "teva": "Teva",
        "cypian": "Cypian",
        "apoline": "Apoline",
    }

    name = events.get(event.lower())

    if not name:
        await ctx.send("Bitte verwende: !test teva, !test cypian oder !test apoline")
        return

    channel = bot.get_channel(CHANNEL_ID)

    if channel:
        await channel.send(
            f"🔔 **TESTMELDUNG – {name}**\n"
            "Fiesta Online EU – Kebing\n"
            "Das ist nur ein Test, kein bestätigter Eventstart."
        )
        await ctx.send(f"Testmeldung für {name} gesendet!")
    else:
        await ctx.send("Fehler: Zielkanal nicht gefunden.")


if not TOKEN:
    raise RuntimeError("Die Umgebungsvariable DISCORD_BOT_TOKEN fehlt.")

bot.run(TOKEN)
