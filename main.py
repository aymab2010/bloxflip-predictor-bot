import discord, random
from discord.ext import commands

bot = commands.Bot(command_prefix=".")

token = str(open(".env", "a+")).split("BOT_TOKEN")[1]

@bot.command()
async def crash(ctx):
  await ctx.send("This command is coming soon!")
