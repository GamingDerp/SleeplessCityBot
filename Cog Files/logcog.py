import discord
from discord.ext import commands
from datetime import datetime, timedelta

# Logging Events Class
class LogCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Deleted Message Log Event
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        channel = self.bot.get_channel(1119185446950408232)
        e = discord.Embed(color=0xc700ff)
        e.set_author(name="🗑️ Message Deleted")
        e.set_thumbnail(url=f"{message.author.avatar.url}")
        if sniped_message.content:
            e.description = f"A message by {message.author.mention} was deleted \n<:Reply:1123773242327441468> In <#{message.channel.id}> \n \n> {message.content}"
        if sniped_message.attachments:
            attachment_url = sniped_message.attachments[0].url
            e.set_image(url=attachment_url)
        e.timestamp = datetime.utcnow()
        await channel.send(embed=e)

    # Edited Message Log Event
    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if before.author.bot: 
            return
        else:
            channel = self.bot.get_channel(1119185446950408232)
            e = discord.Embed(color=0xc700ff)
            e.set_author(name="📝 Message Edited")
            e.set_thumbnail(url=f"{before.author.avatar.url}")
            e.description = f"{before.author.mention} edited their message \n<:Reply:1123773242327441468> In <#{before.channel.id}>" 
            e.add_field(name="__Before__", value=f"> {before.content}")
            e.add_field(name="__After__", value=f"> {after.content}", inline=False)
            e.timestamp = datetime.utcnow()
            await channel.send(embed=e)

    # Member Join Log Event
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(1119185446950408232)
        e = discord.Embed(color=0x00ff05)
        e.set_author(name="📈 Member Joined")
        e.set_thumbnail(url=f"{member.avatar.url}")
        e.add_field(name="__Member__", value=f"> {member.mention}")
        e.timestamp = datetime.utcnow()
        await channel.send(embed=e)

    # Member Remove Log Event
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(1119185446950408232)
        e = discord.Embed(color=0xFf0e00)
        e.set_author(name="📉 Member Left")
        e.set_thumbnail(url=f"{member.avatar.url}")
        e.add_field(name="__Member__", value=f"> {member.mention}")
        e.timestamp = datetime.utcnow()
        await channel.send(embed=e)
    
    # Member Ban Log Event
    @commands.Cog.listener()
    async def on_member_ban(self, guild, member):
        channel = self.bot.get_channel(1119185446950408232)
        logs = [log async for log in guild.audit_logs(limit=1, action=discord.AuditLogAction.ban)]
        logs = logs[0]
        e = discord.Embed(color=0xFf0e00)
        e.set_author(name="🚨 Member Banned")
        e.set_thumbnail(url=f"{member.avatar.url}")
        e.add_field(name="__Member__", value=f"> {member.mention}")
        e.add_field(name="__Ban Reason__", value=f"> {logs.reason}", inline=False)
        e.add_field(name="__Staff Member__", value=f"> {logs.user.mention}", inline=False)
        e.timestamp = datetime.utcnow()
        await channel.send(embed=e)
    
    # Member Unban Log Event
    @commands.Cog.listener()
    async def on_member_unban(self, guild, member):
        channel = self.bot.get_channel(1119185446950408232)
        e = discord.Embed(color=0x00ff05)
        e.set_author(name="✨ Member Unbanned")
        e.set_thumbnail(url=f"{member.avatar.url}")
        e.add_field(name="__Member__", value=f"> {member.mention}")
        e.timestamp = datetime.utcnow()
        await channel.send(embed=e)

    # Member Update Log Event
    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        channel = self.bot.get_channel(1119185446950408232) 
        if len(before.roles) > len(after.roles):
            droles = next(droles for droles in before.roles if droles not in after.roles)
            e = discord.Embed(color=0xc700ff)
            e.set_author(name="🧮 Role Update")
            e.set_thumbnail(url=f"{before.avatar.url}")
            e.add_field(name="__Member__", value=f"> {before.mention}")
            e.add_field(name="__Role__", value=f"> ❌ {droles}", inline=False)
            e.timestamp = datetime.utcnow()
            await channel.send(embed=e)
        else:
            if len(before.roles) < len(after.roles):
                aroles = next(aroles for aroles in after.roles if aroles not in before.roles)
                e = discord.Embed(color=0xc700ff)
                e.set_author(name="🧮 Role Update")
                e.set_thumbnail(url=f"{before.avatar.url}")
                e.add_field(name="__Member__", value=f"> {before.mention}")
                e.add_field(name="__Role__", value=f"> ✅ {aroles}", inline=False)
                e.timestamp = datetime.utcnow()
                await channel.send(embed=e)          
        if before.display_name != after.display_name:
            e = discord.Embed(color=0xc700ff)
            e.set_author(name="🧾 Nickname Update")
            e.set_thumbnail(url=f"{before.avatar.url}")
            e.add_field(name="__Member__", value=f"> {before.mention}")
            e.add_field(name="__Before__", value=f"> {before.display_name}", inline=False)
            e.add_field(name="__After__", value=f"> {after.display_name}", inline=False)
            e.timestamp = datetime.utcnow()
            await channel.send(embed=e)
        
    # User Update Log Event
    @commands.Cog.listener()
    async def on_user_update(self, before, after):
        channel = self.bot.get_channel(1119185446950408232)
        if before.name != after.name:
            e = discord.Embed(color=0xc700ff)
            e.set_author(name="🧾 Account Name Update")
            e.set_thumbnail(url=f"{before.avatar.url}")
            e.add_field(name="__Member__", value=f"> {before.mention}")
            e.add_field(name="__Before__", value=f"> {before.name}#{before.discriminator}", inline=False)
            e.add_field(name="__After__", value=f"> {after.name}#{after.discriminator}", inline=False)
            e.timestamp = datetime.utcnow()
            await channel.send(embed=e)

    # Channel Created Log Event
    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        chan = self.bot.get_channel(1119185446950408232)
        e = discord.Embed(color=0x00ff05)
        e.set_author(name="📥 Channel Created")
        e.add_field(name="__Name__", value=f"> {channel.name}")
        e.add_field(name="__Mention__", value=f"> {channel.mention}", inline=False)
        e.add_field(name="__Channel ID__", value=f"> {channel.id}", inline=False)
        e.timestamp = datetime.utcnow()
        await chan.send(embed=e)
    
    # Channel Deleted Log Event
    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        chan = self.bot.get_channel(1119185446950408232)
        e = discord.Embed(color=0xFf0e00)
        e.set_author(name="📤 Channel Deleted")
        e.add_field(name="__Name__", value=f"> {channel.name}")
        e.add_field(name="__Mention__", value=f"> {channel.mention}", inline=False)
        e.add_field(name="__Channel ID__", value=f"> {channel.id}", inline=False)
        e.timestamp = datetime.utcnow()
        await chan.send(embed=e)

    # Voice Channel Log Event
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        chan = self.bot.get_channel(1119185446950408232)
        if before.channel and after.channel and before.channel != after.channel:
            e = discord.Embed(color=0xc700ff)
            e.set_author(name="🔊 Moved VC's")
            e.add_field(name="__User__", value=f"> {member.mention}")
            e.add_field(name="__Moved From__", value=f"> {before.channel.name}", inline=False)
            e.add_field(name="__Moved To__", value=f"> {after.channel.name}", inline=False)
            e.timestamp = datetime.utcnow()
            await chan.send(embed=e)
        elif before.channel and not after.channel:
            e = discord.Embed(color=0xc700ff)
            e.set_author(name="🔊 Left VC")
            e.add_field(name="__User__", value=f"> {member.mention}")
            e.add_field(name="__Left__", value=f"> {before.channel.name}", inline=False)
            e.timestamp = datetime.utcnow()
            await chan.send(embed=e)
        elif not before.channel and after.channel:
            e = discord.Embed(color=0xc700ff)
            e.set_author(name="🔊 Joined VC")
            e.add_field(name="__User__", value=f"> {member.mention}")
            e.add_field(name="__Joined__", value=f"> {after.channel.name}", inline=False)
            e.timestamp = datetime.utcnow()
            await chan.send(embed=e)
            
    # Role Create Log Event
    @commands.Cog.listener()
    async def on_guild_role_create(self, role):
        channel = self.bot.get_channel(1119185446950408232)
        e = discord.Embed(color=0x00ff05)
        e.set_author(name="🎭 Role Created")
        e.add_field(name="__Role Mention__", value=f"> {role.mention}")
        e.add_field(name="__Role Name__", value=f"> {role.name}", inline=False)
        e.add_field(name="__Role ID__", value=f"> {role.id}", inline=False)
        e.timestamp = datetime.utcnow()
        await channel.send(embed=e)
        
    # Role Delete Log Event
    @commands.Cog.listener()
    async def on_guild_role_delete(self, role):
        channel = self.bot.get_channel(1119185446950408232)
        e = discord.Embed(color=0xFf0e00)
        e.set_author(name="🎭 Role Deleted")
        e.add_field(name="__Role Mention__", value=f"> {role.mention}")
        e.add_field(name="__Role Name__", value=f"> {role.name}", inline=False)
        e.add_field(name="__Role ID__", value=f"> {role.id}", inline=False)
        e.timestamp = datetime.utcnow()
        await channel.send(embed=e)
        
    # Role Update Log Event
    @commands.Cog.listener()
    async def on_guild_role_update(self, before, after):
        channel = self.bot.get_channel(1119185446950408232)
        if before.name != after.name:
            e = discord.Embed(color=0xc700ff)
            e.set_author(name="🎭 Role Update")
            e.add_field(name="__Before__", value=f"> {before.name}")
            e.add_field(name="__After__", value=f"> {after.name}", inline=False)
            e.add_field(name="__Role ID__", value=f"> {after.id}", inline=False)
            e.timestamp = datetime.utcnow()
            await channel.send(embed=e)
        if before.color != after.color:
            e = discord.Embed(color=0xc700ff)
            e.set_author(name="🎭 Role Update")
            e.add_field(name="__Before__", value=f"> {before.color}")
            e.add_field(name="__After__", value=f"> {after.color}", inline=False)
            e.add_field(name="__Role ID__", value=f"> {after.id}", inline=False)
            e.timestamp = datetime.utcnow()
            await channel.send(embed=e)
    

async def setup(bot):
    await bot.add_cog(LogCog(bot))
