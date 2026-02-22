import discord
import os

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'✅ Bot đã đăng nhập với tên {client.user}')

@client.event
async def on_member_join(member):
    channel = member.guild.system_channel
    if channel:
        await channel.send(f'👋 Chào mừng {member.mention} đến với server!')

client.run(os.getenv("TOKEN"))