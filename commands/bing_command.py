from discord.ext import commands

@commands.command(help="Use ~bing to see the client latency in miliseconds, lower latency is faster.", brief="Basic Ping function")
async def bing(ctx):
    await ctx.send(f"Bong very strong {round(ctx.bot.latency * 1000)}ms")
