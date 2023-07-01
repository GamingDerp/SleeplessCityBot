import discord
from discord.ext import commands
from datetime import datetime, timedelta
import asyncio

# Bot Owner User ID
owner_id = 532706491438727169

# OwnHelp Commands Class
class OwnHelp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    # Owner Help Command
    @commands.command(aliases=["plehnwo", "Ownhelp", "plehnwO"])
    async def ownhelp(self, ctx):
        if ctx.author.id == owner_id:
            e = discord.Embed(color=0xe02da9)
            e.set_thumbnail(url="https://media.discordapp.net/attachments/807071768258805764/1114258238335090698/OwnerThumbnail.png")
            e.description = "👾 Owner Commands 👾"
            e.add_field(
                name="✧ __General__",
                value=f"> • `OwnHelp`"
                      f"\n> • `Nuke`"
                      f"\n> • `Revive`",
            )
            e.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url),
            e.timestamp = datetime.utcnow()
            await ctx.send(embed=e)
        else:
            e = discord.Embed(color=0xe02da9)
            e.description = "🚨 That is a **Owner** command! You don't have the required perms! 🚨"
            await ctx.send(embed=e)

    # Nuke Command -- OWNER (joke command)
    @commands.command(aliases=["ekun", "Nuke", "ekuN"])
    async def nuke(self, ctx):
        if ctx.author.id == owner_id:
            await ctx.send("Nuking server in...3")
            await asyncio.sleep(0.85)
            await ctx.send(content="Nuking server in...2")
            await asyncio.sleep(0.90)
            await ctx.send(content="Nuking server in...1")
            await asyncio.sleep(1.25)
            await ctx.send("https://cdn.discordapp.com/attachments/807071768258805764/1103594669050441788/rick-roll.gif")
        else:
            e = discord.Embed(color=0xe02da9)
            e.description = "🚨 That is a **Owner** command! You don't have the required perms! 🚨"
            await ctx.send(embed=e)

    # Revive Command -- OWNER
    @commands.command(aliases=["eviver", "Revive", "eviveR"])
    async def revive(self, ctx, user:discord.Member):
        if ctx.author.id == owner_id:
            e = discord.Embed(color=0xe02da9)
            e.description = f"{ctx.author.mention} revives {user.mention}!"
            e.set_image(url="https://media.discordapp.net/attachments/807071768258805764/1114248146986467328/ReviveGif.gif"),
            await ctx.send(embed=e)
        else:
            e = discord.Embed(color=0xe02da9)
            e.description = "🚨 That is a **Owner** command! You don't have the required perms! 🚨"
            await ctx.send(embed=e)


async def setup(bot):
    await bot.add_cog(OwnHelp(bot))
