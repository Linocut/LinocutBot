import pandas as pd
import numpy as np
from discord.ext import commands
import re

@commands.command(brief= "Solves math.", help=("You must make equations that look like x+y, x+(y-z), 3(1+2), or multiple operations like 2+2+3. Multiplication is * and division is /"))
async def solve(ctx,*, arg):
    give = arg
    
    # Handle implicit multiplication like 3(1+2) -> 3*(1+2)
    give = re.sub(r'(\d)\(', r'\1*(', give)
    give = re.sub(r'\)(\d)', r')*\1', give)
    
    # Remove spaces
    give = give.replace(" ", "")
    
    try:
        # Use eval for all expressions - it handles order of operations correctly
        # Validate that it only contains safe mathematical characters
        if re.match(r'^[\d+\-*/.()]+$', give):
            result = eval(give)
            await ctx.channel.send(result)
        else:
            print("Error: Expression contains invalid characters. Use only numbers and +, -, *, /, (, )")
        
    except Exception as e:
        print("Error: Could not solve this equation. Please check your syntax.")


@solve.error
async def on_command_error(ctx, error):
    await ctx.send(
        "I can solve problems like: x*y, x+(y-z), 3(1+2), 2+2+3, or 7*6+9. Use "
        "decimals for fractions and * for multiplication. Don't divide by 0!"
    )


@solve.error
async def on_command_error(ctx, error):
    await ctx.send(
        "I can only solve problems that look like: x*y OR x-(y+z) Where x y and z are numbers. Use "
        "decimals if you are using fractions and use asterisks for multiplication. Finally, don't divide by 0, that's illegal."
    )
