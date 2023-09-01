import discord
from discord.ext import commands
from datetime import datetime, timedelta
import time
import aiosqlite

# Staff Commands Class
class StaffCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db_conn = None
    
    # Creating table on startup   
    @commands.Cog.listener()
    async def on_ready(self):
        await self.create_table()
        await self.initialize_database()
    
    # Creates database table if one doesn't exist
    async def create_table(self):
        async with aiosqlite.connect("dbs/warnlist.db") as db:
            await db.execute('''
                CREATE TABLE IF NOT EXISTS warns (
                    user_id INTEGER,
                    reason TEXT
                )
            ''')
            await db.commit()
            
    # Fetches warns for a user
    async def get_warns(self, user_id):
        async with aiosqlite.connect("dbs/warnlist.db") as db:
            cursor = await db.execute("SELECT reason FROM warns WHERE user_id = ?", (user_id,))
            warns = await cursor.fetchall()
            return warns
    
    # Initialize logging database
    async def initialize_database(self):
        self.db_conn = await aiosqlite.connect("dbs/logging.db")
    
    # Get the logging channel
    async def get_logging_channel(self, guild_id):
        async with self.db_conn.execute(
            "SELECT channel_id FROM logging_channels WHERE guild_id = ?", (guild_id,)
        ) as cursor:
            result = await cursor.fetchone()
            return result[0] if result else None
    
    # Purge Command
    @commands.hybrid_command(description="Purge messages", pass_context=True)
    async def purge(self, ctx, limit:int):
        if discord.utils.get(ctx.author.roles, name="💠 Sergeant"):
            await ctx.message.delete()
            await ctx.channel.purge(limit=limit)
        else:
            e = discord.Embed(color=0xc700ff)
            e.description = "🚨 That is a **High Staff** command! You don't have the required perms! 🚨"
            await ctx.send(embed=e)
            await ctx.message.delete()

    # Ban Command
    @commands.hybrid_command(description="Ban a user")
    async def ban(self, ctx, member:discord.Member, *, reason=None):
        if discord.utils.get(ctx.author.roles, name="🔆 Detective"):
            e = discord.Embed(color=0xFf0000)
            e.description = f"<:BanHammer:1123773333947813898> {member.mention} has been banned! <:BanHammer:1123773333947813898> \n**Reason:** {reason}"
            await ctx.channel.send(embed=e)
            await member.ban()
        else:
            e = discord.Embed(color=0xc700ff)
            e.description = "🚨 That is a **High Staff** command! You don't have the required perms! 🚨"
            await ctx.send(embed=e)
        
    # Unban Command
    @commands.hybrid_command(description="Unban a user")
    async def unban(self, ctx, id:int):
        member = await self.bot.fetch_user(id)
        if discord.utils.get(ctx.author.roles, name="🔆 Detective"):
            e = discord.Embed(color=0xc700ff)
            e.description = f":pray: {member.mention} has been unbanned! :pray:"
            await ctx.guild.unban(member)
            await ctx.channel.send(embed=e)
        else:
            e = discord.Embed(color=0xc700ff)
            e.description = "🚨 That is a **High Staff** command! You don't have the required perms! 🚨"
            await ctx.send(embed=e)

    # Kick Command
    @commands.hybrid_command(description="Kick a user")
    async def kick(self, ctx, member:discord.Member, *, reason=None):
        if discord.utils.get(ctx.author.roles, name="💠 Sergeant"):
            e = discord.Embed(color=0xc700ff)
            e.description = f"{member.mention} has been kicked! \n**Reason:** {reason}"
            await member.kick()
            await ctx.channel.send(embed=e)
            
            # Sending kick log to log channel
            logging_channel_id = await self.get_logging_channel(ctx.guild.id)
            channel = self.bot.get_channel(logging_channel_id)
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
    @commands.hybrid_command(description="Put a user in timeout")
    async def timeout(self, ctx, member:discord.Member, duration, *, reason=None):
        time_units = {"s": 1, "m": 60, "h": 3600, "d": 86400}  # Mapping time units to seconds
        unit = duration[-1]
        amount = int(duration[:-1])
        seconds = amount * time_units[unit]
        if discord.utils.get(ctx.author.roles, name="🧸 Officer"):
            e = discord.Embed(color=0xc700ff)
            e.set_author(name="⏳ Timeout ⏳")
            e.description = f"**User:** {member.mention} \n **Reason:** {reason} \n **Time:** {duration}"
            await member.timeout(timedelta(seconds=seconds), reason=reason)
            await ctx.send(embed=e)
            
            # Sending timeout log to log channel
            logging_channel_id = await self.get_logging_channel(ctx.guild.id)
            channel = self.bot.get_channel(logging_channel_id)
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
    @commands.hybrid_command(description="Warn a user")
    async def warn(self, ctx, member: discord.Member, *, reason=None):
        if discord.utils.get(ctx.author.roles, name="🧸 Officer"):
            async with aiosqlite.connect("dbs/warnlist.db") as db:
                await db.execute("INSERT INTO warns (user_id, reason) VALUES (?, ?)", (member.id, reason))
                await db.commit()
            e = discord.Embed(color=0xc700ff)
            e.description = f"⚠️ Warning ️⚠️"
            e.add_field(name=f"**User:**", value=member.mention, inline=False)
            e.add_field(name=f"**Reason:**", value=reason, inline=False)
            e.timestamp = datetime.utcnow()
            await ctx.send(embed=e)
            
            # Sending warn log to log channel
            logging_channel_id = await self.get_logging_channel(ctx.guild.id)
            channel = self.bot.get_channel(logging_channel_id)
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
    @commands.hybrid_command(description="See a users warns")
    async def warnlist(self, ctx, member:discord.Member):
        if discord.utils.get(ctx.author.roles, name="🧸 Officer"):
            warns = await self.get_warns(member.id)
            if warns:
                e = discord.Embed(color=0xc700ff)
                warn_list_str = "\n\n".join([f"__**Warn {index}**__ \n> {warn[0]}" for index, warn in enumerate(warns, start=1)])
                e.set_author(name=f"🧾 {member.name}'s Warns 🧾")
                e.description = warn_list_str
                e.timestamp = datetime.utcnow()
                await ctx.send(embed=e)
            else:
                await ctx.send(f"No warns found for **{member.name}**.")
        else:
            e = discord.Embed(color=0xc700ff)
            e.description = "🚨 That is a **Staff** command! You don't have the required perms! 🚨"
            await ctx.send(embed=e)

    # Delwarn Command
    @commands.hybrid_command(description="Delete a users warns")
    async def delwarn(self, ctx, member:discord.Member, warn_index:int):
        if discord.utils.get(ctx.author.roles, name="🔆 Detective"):
            warns = await self.get_warns(member.id)
            if not warns:
                await ctx.send(f"No warns found for `{member.name}`.")
                return

            if 1 <= warn_index <= len(warns):
                warn_to_remove = warns[warn_index - 1][0]
                async with aiosqlite.connect("dbs/warnlist.db") as db:
                    await db.execute('DELETE FROM warns WHERE user_id = ? AND reason = ?', (member.id, warn_to_remove))
                    await db.commit()
                e = discord.Embed(color=0xc700ff)
                e.set_author(name="♻️ Warn Removed ♻️")
                e.description = f"**Warn #:** {warn_index} \n**Member:** {member.mention}"
                e.timestamp = datetime.utcnow()
                await ctx.send(embed=e)
                
                # Sending delwarn log to log channel
                logging_channel_id = await self.get_logging_channel(ctx.guild.id)
                channel = self.bot.get_channel(logging_channel_id)
                unwarned = member.mention
                unwarner = ctx.author.mention
                e = discord.Embed(color=0xc700ff)
                e.set_author(name="♻️ User Warn Removed")
                e.set_thumbnail(url=member.avatar.url)
                e.add_field(name="__**Member**__", value=f"> {unwarned}", inline=False)
                e.add_field(name="__**Staff Member**__", value=f"> {unwarner}", inline=False)
                e.timestamp = datetime.utcnow()
                await channel.send(embed=e)
            else:
                await ctx.send("Invalid warn number. Do `!delwarn <user> <warn number>`")
        else:
            e = discord.Embed(color=0xc700ff)
            e.description = "🚨 That is a **High Staff** command! You don't have the required perms! 🚨"
            await ctx.send(embed=e)
            

async def setup(bot):
    await bot.add_cog(StaffCog(bot))
