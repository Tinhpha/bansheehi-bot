import discord
from discord.ext import commands

import os
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} đã online!")

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="xin-chào")
    if channel:
        await channel.send(f"👻 Chào mừng {member.mention} đến với server!")

bot.run(TOKEN)