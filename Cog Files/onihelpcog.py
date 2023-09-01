import discord
from discord.ext import commands
from datetime import datetime, timedelta
import random
import asyncio

# Oni & Kaoru's User ID's
oni_id = 700958482454806574
kaoru_id = 545792399209660416

# OniHelp Commands Class
class OniHelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # OniHelp Command
    @commands.hybrid_command(description="Sends the help menu for Oni")
    async def onihelp(self, ctx):
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
            e.description = "🚨 That is a **Oni** command! You don't have the required perms! 🚨"
            await ctx.send(embed=e)

    # Vore Command
    @commands.hybrid_command(description="Vore another user")
    async def vore(self, ctx, user:discord.Member):
        if ctx.author.id == oni_id or ctx.author.id == kaoru_id:
            e = discord.Embed(color=0xf28aad)
            e.description = f"{ctx.author.mention} vores {user.mention}!"
            vgifs = [
                "https://media.discordapp.net/attachments/1065475897441914951/1112083252572860517/OniVoreGif1.gif", 
                "https://media.discordapp.net/attachments/1065475897441914951/1112083145974612008/OniVoreGif2.gif", 
                "https://media.discordapp.net/attachments/1065475897441914951/1112083146343723252/OniVoreGif3.gif"
            ]
            voregif = random.choice(vgifs)
            e.set_image(url=voregif),
            await ctx.send(embed=e)
        else:
            e = discord.Embed(color=0xf28aad)
            e.description = "🚨 That is a **Oni** command! You don't have the required perms! 🚨"
            await ctx.send(embed=e)

    # Motorboat Command
    @commands.hybrid_command(description="Motorboat another user")
    async def motorboat(self, ctx, user:discord.Member):
        if ctx.author.id == oni_id or ctx.author.id == kaoru_id:
            e = discord.Embed(color=0xf28aad)
            e.description = f"{ctx.author.mention} motorboats {user.mention}!"
            mgifs = [
                "https://media.discordapp.net/attachments/807071768258805764/1114112965533245481/OniMotorboatGif.gif", 
                "https://media.discordapp.net/attachments/807071768258805764/1132211752914923580/MotorBoat2Gif.gif"
            ]
            motogif = random.choice(mgifs)
            e.set_image(url=motogif),
            await ctx.send(embed=e)
        else:
            e = discord.Embed(color=0xf28aad)
            e.description = "🚨 That is a **Oni** command! You don't have the required perms! 🚨"
            await ctx.send(embed=e)

        
async def setup(bot):
    await bot.add_cog(OniHelpCog(bot))
