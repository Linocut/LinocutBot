from discord.ext import commands
from random import randint

@commands.command(help= "You must have commas seperating each item follow your list after the ~wheel. Example ~wheel heads, tails", brief= "Gives you a random pick of a list")
async def wheel(ctx,*,arg):
    wheelList = arg.split(",")
    randomNumber = randint(0, (len(wheelList)-1))
    wheelAnswer = wheelList[randomNumber]
    await ctx.channel.send(wheelAnswer)
