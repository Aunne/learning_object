import discord
from discord.ext import commands
import asyncio
import os

assert os.path.isfile("TOKEN")
with open("TOKEN", "r") as file:
    TOKEN = file.read().strip()


client = discord.Client()
bot = commands.Bot(command_prefix="//")  # 設定//為指令

@bot.event
async def on_ready():
    """
    確認機器人上線
    """
    print("Bot is ready.")


@bot.command()
async def clean(self,ctx,num=1):
    await ctx.purge(limit=int(num))
    


bot.run(TOKEN)
