import discord
from discord.ext import commands
import random
import asyncio

# Fun Commands Class
class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    # Coinflip Command
    @commands.command(aliases=["pilfnioc", "Coinflip", "plifnioC"])
    async def coinflip(self, ctx):
        choice = ["Heads", "Tails"]
        await ctx.send(f"{random.choice(choice)}!")

    # Ask Command
    @commands.command(aliases=["ksa", "Ask", "ksA"])
    async def ask(self, ctx):
        choice = ["Yes", "No", "Obviously", "Wtf??", "I'm not sure..", "Maybe...?", "Stop asking.", "Find out for yourself, smh", "Crabs", "Ask Derp :eyes:"]
        await ctx.send(f"{random.choice(choice)}")

    # Reverse Command
    @commands.command(aliases=["esrever", "Reverse", "esreveR"])
    async def reverse(self, ctx, *, arg="reverse"): # if user gives no arg, just says "reverse" backwards
        await ctx.send(arg[::-1])

    # Say Command
    @commands.command(aliases=["yas", "Say", "yaS"])
    async def say(self, ctx, *, arg):
        await ctx.send(arg)
        await ctx.message.delete()

    # Love Test Command
    @commands.command(aliases=["tsetevol", "Lovetest", "tsetevoL"])
    async def lovetest(self, ctx, user1:discord.Member, user2:discord.Member):
    
        love_rate = str(random.randrange(0, 100))
        derp_id = 532706491438727169
        oni_id = 700958482454806574
    
        if user1.id == derp_id and user2.id == oni_id or user1.id == oni_id and user2.id == derp_id:
            e = discord.Embed(color=0xc700ff)
            e.add_field(
                name="❤️ Love Test",
                value=f"**{user1.mention}** and **{user2.mention}** are a **100%** match! :flushed:",
                inline=False
            )
            await ctx.send(embed=e)
        else:
            e = discord.Embed(color=0xc700ff)
            e.add_field(
                name="❤️ Love Test",
                value=f"**{user1.mention}** and **{user2.mention}** are a **{love_rate}%** match! :flushed:",
                inline=False
            )
            await ctx.send(embed=e)
    
    # Cute Command
    @commands.command(aliases=["etuc", "Cute", "etuC"])
    async def cute(self, ctx):
        e = discord.Embed(color=0xc700ff)
        e.set_author(name="Cute", icon_url=ctx.author.avatar.url)
        with open("cogs/cute.txt") as f:
            cute = f.readlines()
        e.set_image(url=random.choice(cute))
        await ctx.send(embed=e)
    
    # Duel Command
    @commands.command(aliases=["leud", "Duel", "leuD"])
    async def duel(self, ctx, user:discord.Member):

        challengerid = ctx.author
        challengeeid = user
        
        e = discord.Embed(color=0xc700ff)
        e.description = f"{challengerid.mention} challenges {challengeeid.mention} to a **duel**, do you accept?"
        e.set_image(url="https://media.discordapp.net/attachments/807071768258805764/1107422093940891708/DuelingGif.gif"),
        message = await ctx.channel.send(embed=e)
        await message.add_reaction("✅") # Adding reactions
        await message.add_reaction("❌")
    
        ReactList = ["✅", "❌"]
    
        def check(reaction, user):
            return user.id == challengeeid.id and str(reaction.emoji) in ReactList and reaction.message.id == message.id
        try:
            reaction, user = await self.bot.wait_for("reaction_add", timeout=30.0, check=check)
        except asyncio.TimeoutError:
            await ctx.channel.send(f"{challengeeid.mention} didn't react in time! The duel was called off!")
        else:
            if str(reaction.emoji) == "✅":
                await ctx.channel.send(f"{challengeeid.mention} has accepted the duel!")
            
                numjis = ["1️⃣", "2️⃣", "3️⃣"]
                duel_number = random.choice(numjis)
            
                e = discord.Embed(color=0xc700ff)
                e.title="Reach For Tha' Sky..."
                e.set_thumbnail(url="https://media.discordapp.net/attachments/807071768258805764/1108740936122499152/PistolEmoji.png?width=910&height=910")
                e.description="Click a reaction to guess a number! Good Luck!"
                message = e
                message = await user.send(embed=e)
                await message.add_reaction("1️⃣") # Adding reactions
                await message.add_reaction("2️⃣")
                await message.add_reaction("3️⃣")
                reaction, user = await self.bot.wait_for("reaction_add")
                duel_guess1 = reaction.emoji
            
                e = discord.Embed(color=0xc700ff)
                e.title="Reach For Tha' Sky..."
                e.set_thumbnail(url="https://media.discordapp.net/attachments/807071768258805764/1108740936122499152/PistolEmoji.png?width=910&height=910")
                e.description="Click a reaction to guess a number! Good Luck!"
                message = e
                message = await ctx.author.send(embed=e)
                await message.add_reaction("1️⃣") # Adding reactions
                await message.add_reaction("2️⃣")
                await message.add_reaction("3️⃣")
                reaction, user = await self.bot.wait_for("reaction_add")
                duel_guess2 = reaction.emoji
            
                if duel_number == duel_guess1 and duel_number == duel_guess2: # Comparing if the bot's number equals the user1 guess and the user2 guess
                    e = discord.Embed(color=0xc700ff) # Embed
                    e.description = "Both duelists shot each other!"
                    e.set_image(url="https://media.discordapp.net/attachments/807071768258805764/1108776990284197908/StandoffGif.gif"),
                    message = e
                    await ctx.send(embed=e)
                elif duel_number == duel_guess1 or duel_number == duel_guess2: # Comparing if the bot's number equals the user1 guess or the user2 guess
                    if duel_number == duel_guess1:
                        winner = challengeeid
                    else:
                        winner = challengerid
                    e = discord.Embed(color=0xc700ff) # Embed
                    e.description = f"👑 {winner.mention} has won the duel! 👑"
                    e.set_image(url="https://media.discordapp.net/attachments/807071768258805764/1108761350857040013/GunSmokeGif.gif"),
                    message = e
                    await ctx.send(embed=e)
                else:
                    e = discord.Embed(color=0xc700ff) # Embed
                    e.description = "Both duelists missed!"
                    e.set_image(url="https://media.discordapp.net/attachments/807071768258805764/1108776990284197908/StandoffGif.gif"),
                    message = e
                    await ctx.send(embed=e)
                            
            elif str(reaction.emoji) == "❌":
                await ctx.channel.send(f"{challengeeid.mention} has declined the duel!")


async def setup(bot):
    await bot.add_cog(Fun(bot))
