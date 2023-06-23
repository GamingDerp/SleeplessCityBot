import discord
from discord.ext import commands
from datetime import datetime, timedelta
import random

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)
###################################[ ONI COMMANDS ]###################################
# OniHelp Commands Class
class OniHelp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # OniHelp Command
    @commands.command(aliases=["plehino", "Onihelp", "plehinO"])
    async def onihelp(self, ctx):
    
        oni_id = 700958482454806574

        if ctx.author.id == oni_id:
            e = discord.Embed(color=0xf28aad)
            e.set_thumbnail(url="https://media.discordapp.net/attachments/807071768258805764/1112068793515122728/HelloKitty.png")
            e.description = f"💗 Oni Commands 💗"
            e.add_field(
                name="✧ __General__",
                value=f"> • `OniHelp`"
                      f"\n> • `Vore`"
                      f"\n> • `Motorboat`",
            )
            e.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url),
            e.timestamp = datetime.utcnow()
            await ctx.send(embed=e)
        else:
            e = discord.Embed(color=0xf28aad)
            e.description = "🚨 That is a(n) **Oni command**! You don't have the required perms! 🚨"
            await ctx.send(embed=e)

    # Vore Command
    @commands.command(aliases=["erov", "Vore", "eroV"])
    async def vore(self, ctx, user:discord.Member):
        oni_id = 700958482454806574
        kaoru_id = 545792399209660416

        if ctx.author.id == oni_id or ctx.author.id == kaoru_id:
            e = discord.Embed(color=0xf28aad)
            e.description = f"{ctx.author.mention} vores {user.mention}!"
            with open("vore.txt") as f:
                vore = f.readlines()
                e.set_image(url=random.choice(vore)),
                await ctx.send(embed=e)
        else:
            e = discord.Embed(color=0xf28aad)
            e.description = "🚨 That is a(n) **Oni command**! You don't have the required perms! 🚨"
            await ctx.send(embed=e)

    # Motorboat Command
    @commands.command(aliases=["taobrotom", "Motorboat", "taobrotoM"])
    async def motorboat(self, ctx, user:discord.Member):
        oni_id = 700958482454806574
        kaoru_id = 545792399209660416
    
        if ctx.author.id == oni_id or ctx.author.id == kaoru_id:
            e = discord.Embed(color=0xf28aad)
            e.description = f"{ctx.author.mention} motorboats {user.mention}!"
            e.set_image(url="https://media.discordapp.net/attachments/807071768258805764/1114112965533245481/OniMotorboatGif.gif"),
            await ctx.send(embed=e)
        else:
            e = discord.Embed(color=0xf28aad)
            e.description = "🚨 That is a(n) **Oni command**! You don't have the required perms! 🚨"
            await ctx.send(embed=e)
###################################[ ADDING COG ]###################################
# Adding cog to bot
async def setup(bot):
    await bot.add_cog(OniHelp(bot))