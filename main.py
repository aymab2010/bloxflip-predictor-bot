import discord, random, json
from discord.ext import commands

token = open("token.txt", "r").read()
bot = commands.Bot(command_prefix=".")

bot.run(token)
