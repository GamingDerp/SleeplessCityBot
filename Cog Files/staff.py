import discord
from discord.ext import commands
from datetime import datetime, timedelta
import json

# Staff Commands Class
class Staff(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    # Purge Command
    @commands.command(aliases=["egrup", "Purge", "egruP", "PURGE", "EGRUP"], pass_context=True)
    async def purge(self, ctx, limit:int):
        role = discord.utils.get(ctx.guild.roles, name="🔆 Detective")
        user = ctx.author
        if role in user.roles:
            await ctx.message.delete()
            await ctx.channel.purge(limit=limit)
        else:
            e = discord.Embed(color=0xc700ff)
            e.description = "🚨 That is a **High Staff** command! You don't have the required perms! 🚨"
            await ctx.send(embed=e)
            await ctx.message.delete()

    # Ban Command
    @commands.command(aliases=["nab", "Ban", "naB", "BAN", "NAB"])
    async def ban(self, ctx, member:discord.Member, *, reason=None):
        role = discord.utils.get(ctx.guild.roles, name="🔆 Detective")
        user = ctx.author
        if role in user.roles:
            e = discord.Embed(color=0xFf0000)
            e.description = f"<:BanHammer:1120488412558921848> {member.mention} has been banned! <:BanHammer:1120488412558921848> \n**Reason:** {reason}"
            await member.ban()
            await ctx.channel.send(embed=e)
        else:
            e = discord.Embed(color=0xc700ff)
            e.description = "🚨 That is a **High Staff** command! You don't have the required perms! 🚨"
            await ctx.send(embed=e)
        
    # Unban Command
    @commands.command(aliases=["nabnu", "Unban", "nabnU", "UNBAN", "NABNU"])
    async def unban(self, ctx, id:int):
        member = await self.bot.fetch_user(id)
        role = discord.utils.get(ctx.guild.roles, name="🔆 Detective")
        user = ctx.author    
        if role in user.roles:
            e = discord.Embed(color=0xc700ff)
            e.description = f":pray: {member.mention} has been unbanned! :pray:"
            await ctx.guild.unban(member)
            await ctx.channel.send(embed=e)
        else:
            e = discord.Embed(color=0xc700ff)
            e.description = "🚨 That is a **High Staff** command! You don't have the required perms! 🚨"
            await ctx.send(embed=e)

    # Kick Command
    @commands.command(aliases=["kcik", "Kick", "kciK", "KICK", "KCIK"])
    async def kick(self, ctx, member:discord.Member, *, reason=None):
        role = discord.utils.get(ctx.guild.roles, name="💠 Sergeant")
        user = ctx.author
        if role in user.roles:
            e = discord.Embed(color=0xc700ff)
            e.description = f"{member.mention} has been kicked! \n**Reason:** {reason}"
            await member.kick()
            await ctx.channel.send(embed=e)            
            channel = self.bot.get_channel(1119185446950408232)
            staff = ctx.author.mention
            kicked = member.mention
            e = discord.Embed(color=0xc700ff)
            e.set_author(name="🥾 User Kicked")
            e.set_thumbnail(url=member.avatar.url)
            e.add_field(name="__Member__", value=f"> {kicked}")
            e.add_field(name="__Reason__", value=f"> {reason}", inline=False)
            e.add_field(name="__Staff Member__", value=f"> {staff}", inline=False)
            e.timestamp = datetime.utcnow()
            await channel.send(embed=e)
        else:
            e = discord.Embed(color=0xc700ff)
            e.description = "🚨 That is a **Staff** command! You don't have the required perms! 🚨"
            await ctx.send(embed=e)

    # Timeout Command
    @commands.command(aliases=["tuoemit", "Timeout", "tuoemiT", "TIMEOUT", "TUOEMIT"])
    async def timeout(self, ctx, member:discord.Member, duration, *, reason=None):
        role = discord.utils.get(ctx.guild.roles, name="💠 Sergeant")
        user = ctx.author
        time_units = {"s": 1, "m": 60, "h": 3600, "d": 86400}  # Mapping time units to seconds
        unit = duration[-1]
        amount = int(duration[:-1])
        seconds = amount * time_units[unit]
        if role in user.roles:
            e = discord.Embed(color=0xc700ff)
            e.description = f"⏳ Timeout! ⏳ \n **User:** {member.mention} \n **Reason:** {reason} \n **Time:** {duration}"
            await member.timeout(timedelta(seconds=seconds), reason=reason)
            await ctx.send(embed=e)
            channel = self.bot.get_channel(1119185446950408232)
            timed = member.mention
            timer = ctx.author.mention
            time = {seconds}     
            e = discord.Embed(color=0xc700ff)
            e.set_author(name="⏳ User Timed Out")
            e.set_thumbnail(url=member.avatar.url)
            e.add_field(name="__Member__", value=f"> {timed}")
            e.add_field(name="__Reason__", value=f"> {reason}", inline=False)
            e.add_field(name="__Time__", value=f"> {duration}", inline=False)
            e.add_field(name="__Staff Member__", value=f"> {timer}", inline=False)
            e.timestamp = datetime.utcnow()
            await channel.send(embed=e)
        else:
            e = discord.Embed(color=0xc700ff)
            e.description = "🚨 That is a **Staff** command! You don't have the required perms! 🚨"
            await ctx.send(embed=e)

    # Warn Command
    @commands.command(aliases=["nraw", "Warn", "nraW", "WARN", "NRAW"])
    async def warn(self, ctx, member: discord.Member, *, reason=None):
        role = discord.utils.get(ctx.guild.roles, name="🧸 Police Officer")
        user = ctx.author
        if role in user.roles:
            with open('cogs/warns.json', 'r') as file:
                warns = json.load(file)
            if str(member.id) not in warns:
                warns[str(member.id)] = []
            warns[str(member.id)].append(reason)
            with open('cogs/warns.json', 'w') as file:
                json.dump(warns, file, indent=4)
            e = discord.Embed(color=0xc700ff)
            e.description = f"⚠️ Warning! ️⚠️ \n **User:** {member.mention} \n **Reason:** {reason}"
            e.timestamp = datetime.utcnow()
            await ctx.send(embed=e)
            channel = self.bot.get_channel(1119185446950408232)
            warned = member.mention
            warner = ctx.author.mention
            e = discord.Embed(color=0xc700ff)
            e.set_author(name="⚠️ User Warned")
            e.set_thumbnail(url=member.avatar.url)
            e.add_field(name="__Member__", value=f"> {warned}")
            e.add_field(name="__Reason__", value=f"> {reason}", inline=False)
            e.add_field(name="__Staff Member__", value=f"> {warner}", inline=False)
            e.timestamp = datetime.utcnow()
            await channel.send(embed=e)
        else:
            e = discord.Embed(color=0xc700ff)
            e.description = "🚨 That is a **Staff** command! You don't have the required perms! 🚨"
            await ctx.send(embed=e)

    # WarnList Command
    @commands.command(aliases=["tsilnraw", "Warnlist", "tsilnraW", "WARNLIST", "TSILNRAW"])
    async def warnlist(self, ctx, member:discord.Member):
        role = discord.utils.get(ctx.guild.roles, name="🧸 Police Officer")
        user = ctx.author
        if role in user.roles:
            with open("cogs/warns.json", "r") as file:
                warns = json.load(file)
            if str(member.id) not in warns:
                await ctx.send("No warns found for this user.")
                return
            warn_list = warns[str(member.id)]
            warn_count = len(warn_list)
            e = discord.Embed(color=0xc700ff)
            e.set_author(name=f"{member.name}'s Warns")
            e.description=f"Warns: **{warn_count}**"
            for index, reason in enumerate(warn_list, start=1):
                e.add_field(name=f"__Warn {index}__", value=f"> {reason}", inline=False)
            await ctx.send(embed=e)
        else:
            e = discord.Embed(color=0xc700ff)
            e.description = "🚨 That is a **Staff** command! You don't have the required perms! 🚨"
            await ctx.send(embed=e)

    # Delwarn Command
    @commands.command(aliases=["nrawled", "Delwarn", "nrawleD", "DELWARN", "NRAWLED"])
    async def delwarn(self, ctx, member:discord.Member, warn_index:int):
        role = discord.utils.get(ctx.guild.roles, name="🔆 Detective")
        user = ctx.author
        if role in user.roles:
            with open("cogs/warns.json", "r") as file:
                warns = json.load(file)
            if str(member.id) not in warns:
                await ctx.send("No warns found for this user.")
                return
            warn_list = warns[str(member.id)]
            if warn_index < 1 or warn_index > len(warn_list):
                await ctx.send("Invalid warn index.")
                return
            removed_warn = warn_list.pop(warn_index - 1)
            with open("cogs/warns.json", "w") as file:
                json.dump(warns, file, indent=4)
            e = discord.Embed(color=0xc700ff)
            e.add_field(
                name="🔅 Warn Removed",
                value=f"**Warn #:** {warn_index}"
                      f"\n**Member:** {member.mention}"
                      f"\n**Warn:** *{removed_warn}*",
            )
            e.timestamp = datetime.utcnow()
            await ctx.send(embed=e)
            channel = self.bot.get_channel(1119185446950408232)
            unwarned = member.mention
            unwarner = ctx.author.mention
            e = discord.Embed(color=0xc700ff)
            e.set_author(name="🔅 User Warn Removed")
            e.set_thumbnail(url=member.avatar.url)
            e.add_field(name="__Member__", value=f"> {unwarned}")
            e.add_field(name="__Staff Member__", value=f"> {unwarner}", inline=False)
            e.timestamp = datetime.utcnow()
            await channel.send(embed=e)
        else:
            e = discord.Embed(color=0xc700ff)
            e.description = "🚨 That is a **High Staff** command! You don't have the required perms! 🚨"
            await ctx.send(embed=e)


async def setup(bot):
    await bot.add_cog(Staff(bot))
