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
                      f"\n> • `Motorboat`"
                      f"\n> • `Catify`",
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

    # Catify Command
    @commands.hybrid_command(description="Turn another user into a cat")
    async def catify(self, ctx, user:discord.Member):
        if ctx.author.id == oni_id:
            e = discord.Embed(color=0xf28aad)
            e.description = f"{ctx.author.mention} turned {user.mention} into a cat!"
            cgifs = [
                "https://media.discordapp.net/attachments/1065466402447826984/1202851276837224478/CatGifOne.gif?ex=65cef58c&is=65bc808c&hm=26f9b518e176c691d38e8307f29063c82efca6408a70f04b5239459e6d66e4df&=", 
                "https://media.discordapp.net/attachments/1065466402447826984/1202851745806557184/CatGifTwo.gif?ex=65cef5fc&is=65bc80fc&hm=2d39f58b80784efcff3f32215d47037213389e586ec310ed43ac61ae0ee308f5&=",
                "https://media.discordapp.net/attachments/1065466402447826984/1202852110547550238/CatGifThree.gif?ex=65cef653&is=65bc8153&hm=8fd1332d1b4f28a321c65226b9556eaee824acd58ab05c92785e5a78d82c5fa5&=",
                "https://cdn.discordapp.com/attachments/1065466402447826984/1202852356874575872/CatGifFour.gif?ex=65cef68d&is=65bc818d&hm=b87b60d0a4176b132bd111173f3746aa106e51e1a05fedfa011a827a15b8adba&",
                "https://media.discordapp.net/attachments/1065466402447826984/1202852590833111070/CatGifFive.gif?ex=65cef6c5&is=65bc81c5&hm=12147e5a4e1a23c81ef681aed405743df36b8d008248ca22c58469ccad42b097&=",
            ]
            catgif = random.choice(cgifs)
            e.set_image(url=catgif),
            await ctx.send(embed=e)
        else:
            e = discord.Embed(color=0xf28aad)
            e.description = "🚨 That is a **Oni** command! You don't have the required perms! 🚨"
            await ctx.send(embed=e)


async def setup(bot):
    await bot.add_cog(OniHelpCog(bot))
