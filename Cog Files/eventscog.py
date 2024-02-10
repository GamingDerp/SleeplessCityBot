import discord
from discord.ext import commands
from datetime import datetime, timedelta
import time
import aiosqlite

# Bots User ID
bot_id = 1103103994777309205

# Events Commands Class
class EventsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.processed_messages = set()

    # Changes bot's Discord activity when loaded and syncs commands
    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(activity=discord.Game(name="Helping SN Users..."))
        await self.bot.tree.sync()
        await self.create_starboard_table()
        
    # Creates database table if one doesn't exist
    async def create_starboard_table(self):
        async with aiosqlite.connect("dbs/star.db") as db:
            await db.execute(
                """
                CREATE TABLE IF NOT EXISTS starboard (
                    server_id INTEGER PRIMARY KEY,
                    channel_id INTEGER
                )
                """
            )
            await db.commit()
    
    # SetStar Command
    @commands.hybrid_command(description="Set the starboard channel")
    async def setstar(self, ctx, channel: discord.TextChannel):
        if discord.utils.get(ctx.author.roles, name="🔐 Assistant Chief"):
            def check(message):
                return message.author == ctx.author and message.channel == ctx.channel
            await ctx.send(f"Is {channel.mention} the correct channel? [Yes/No]")
            try:
                reply = await self.bot.wait_for("message", timeout=30.0, check=check)
                if reply.content.lower() == "yes":
                    async with aiosqlite.connect("dbs/star.db") as db:
                        await db.execute("INSERT OR REPLACE INTO starboard (server_id, channel_id) VALUES (?, ?)", (ctx.guild.id, channel.id))
                        await db.commit()
                    await ctx.send(f"Starboard channel set to {channel.mention}!", ephemeral=True)
                else:
                    await ctx.send("Please retry the command and mention the correct channel!", ephemeral=True)
            except asyncio.TimeoutError:
                await ctx.send("Timed out. Starboard channel setting cancelled.", ephemeral=True)
        else:
            e = discord.Embed(color=0xc700ff)
            e.description = "🚨 That is a **High Staff** command! You don't have the required perms! 🚨"
            await ctx.send(embed=e, ephemeral=True)
    
    # Starboard Event
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if reaction.emoji == "⭐" and reaction.count >= 3 and reaction.message.id not in self.processed_messages:
            async with aiosqlite.connect("dbs/star.db") as db:
                async with db.execute("SELECT channel_id FROM starboard WHERE server_id = ?", (reaction.message.guild.id,)) as cursor:
                    result = await cursor.fetchone()
                    if result:
                        starboard_channel_id = result[0]
                        starboard_channel = self.bot.get_channel(starboard_channel_id)
                        if starboard_channel:
                            e = discord.Embed(color=0xF7c11e)
                            e.set_author(name=reaction.message.author.display_name, icon_url=reaction.message.author.avatar.url)
                            e.description = reaction.message.content
                            if reaction.message.attachments:
                                e.set_image(url=reaction.message.attachments[0].url)   
                            e.add_field(name="**Posted In**", value=reaction.message.channel.mention)
                            jump_url = reaction.message.jump_url
                            e.add_field(name="**Jump URL**", value=f"[Message Link]({jump_url})")
                            e.timestamp = datetime.utcnow()
                            await starboard_channel.send(embed=e)
                            self.processed_messages.add(reaction.message.id)
    
    # Bot Mention Message Event / Counting Reaction Event
    @commands.Cog.listener()
    async def on_message(self, message):
        if str(bot_id) in message.content:
            await message.channel.send("I've been summoned! If you need me do `!help` <:CatWave:1123898399557693470>")
        if message.author.bot:
            return
        else:
            if message.channel.id == 1065502975499440168 and "69" in message.content:
                await message.add_reaction('<:Troll:1141846474108436550>')
                await self.bot.process_commands(message)
            
    # User Joined Message Event
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(1065466402447826984)
        e = discord.Embed(color=0xc700ff)
        e.set_author(name=f"✨ Welcome to Sleepless Nights! ✨")
        e.description = "*~ The city of the restless ~*"
        e.set_image(url="https://media.discordapp.net/attachments/1070206894800638003/1078900669865525328/WelcomeGif.gif"),
        await channel.send(f"{member.mention} has joined! Checkout <#1065472726158037002> and <#1065473461272715344>!", embed=e)
        role = discord.utils.get(member.guild.roles, name="👌 Member")
        await member.add_roles(role)

    # User Leave Message Event
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(1065466402447826984)
        e = discord.Embed(color=0xc700ff)
        e.description = f"👋 {member.name} left! 👋"
        await channel.send(embed=e)
    
    # Boost Message Event
    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        if before.premium_since is None and after.premium_since is not None:
            channel = self.bot.get_channel(1065473991940247624)
            e = discord.Embed(color=0xff73fa)
            e.title = f"<a:DiscordBoost:1121298549657829436> {after.name} boosted the server!"
            e.set_thumbnail(url=after.avatar.url)
            e.description = f"Thank you {after.mention}! \nYou'll now recieve these perks: \n> Image Perms \n> Embed Perms \n> Video Perms \n> Streaming Perms \n*and access to the exclusive <#1065651827703554109>!*"
            await channel.send(embed=e)


async def setup(bot):
    await bot.add_cog(EventsCog(bot))
