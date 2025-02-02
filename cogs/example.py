from discord.ext import commands

class Example(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='example', description='Example command!')
    async def example(self, ctx):
        await ctx.send('Example!')

async def setup(bot):
    await bot.add_cog(Example(bot))