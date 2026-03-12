from discord.ext import commands

@commands.command(help= "Counts things in inventory", brief= "Counts Invent")
async def count(ctx,*,arg):
    itemList = arg.split(",")
    amount = len(itemList)
    await ctx.channel.send(amount)
