import discord
from discord.ext import commands
import random
import asyncio
        
# Fun Commands Class
class FunCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # Coinflip Command
    @commands.hybrid_command(description="Flip a coin")
    async def coinflip(self, ctx):
        choice = ["Heads", "Tails"]
        await ctx.send(f"{random.choice(choice)}!")

    # Ask Command
    @commands.hybrid_command(description="Ask the bot a question")
    async def ask(self, ctx):
        choice = ["Yes", "No", "Obviously", "Wtf??", "I'm not sure..", "Maybe...?", "Stop asking.", "Find out for yourself, smh", "Crabs", "Ask Derp :eyes:"]
        await ctx.send(f"{random.choice(choice)}")

    # Reverse Command
    @commands.hybrid_command(description="Reverse a message")
    async def reverse(self, ctx, *, arg):
        await ctx.send(arg[::-1])

    # Say Command
    @commands.hybrid_command(description="Have the bot say a message")
    async def say(self, ctx, *, arg):
        await ctx.send(arg)
        await ctx.message.delete()

    # Love Test Command
    @commands.hybrid_command(description="Give two users a love test")
    async def lovetest(self, ctx, user1:discord.Member, user2:discord.Member):
    
        love_rate = str(random.randrange(0, 100))
        derp_id = 532706491438727169
        oni_id = 700958482454806574
        
        e = discord.Embed(color=0xc700ff)
        e.title = "❤️ Love Test"
        
        if user1.id == derp_id and user2.id == oni_id or user1.id == oni_id and user2.id == derp_id:
            e.description = f"**{user1.mention}** and **{user2.mention}** are a **100%** match! :flushed:"
            await ctx.send(embed=e)
        else:
            e.description = f"**{user1.mention}** and **{user2.mention}** are a **{love_rate}%** match! :flushed:"
            await ctx.send(embed=e)
    
    # Cute Command
    @commands.hybrid_command(description="Sends a cute animal picture")
    async def cute(self, ctx):
        e = discord.Embed(color=0xc700ff)
        e.set_author(name="Cute", icon_url=ctx.author.avatar.url)
        with open("txts/cute.txt") as f:
            cute = f.readlines()
        e.set_image(url=random.choice(cute))
        await ctx.send(embed=e)
    
async def setup(bot):
    await bot.add_cog(FunCog(bot))
