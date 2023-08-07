import os
import discord
from discord.ext import commands
from datetime import datetime, timedelta
import time
import aiosqlite

# Stores when the bot was started
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
bot.launch_time = datetime.utcnow()

# General Commands Embed
ge = discord.Embed(color=0xc700ff)
ge.add_field(
    name="📌 __General Commands__",
    value=f"> • `Help`"
          f"\n> • `Info`"
          f"\n> • `Test`"
          f"\n> • `Ping`"
          f"\n> • `Suggest`"
          f"\n> • `Poll` - Slash",
)

# Fun Commands Embed
fe = discord.Embed(color=0xc700ff)
fe.add_field(
    name="🎉 __Fun Commands__",
    value=f"> • `Coinflip`"
          f"\n> • `Ask`"
          f"\n> • `Reverse`"
          f"\n> • `Say`"
          f"\n> • `Lovetest`"
          f"\n> • `Cute`"
          f"\n> • `Duel`"
          f"\n> • `Rps`",
)

# Action Commands Embed
ae = discord.Embed(color=0xc700ff)
ae.add_field(
    name="🎯 __Action Commands__",
    value=f"> • `Sniff`"
          f"\n> • `Bite`"
          f"\n> • `Bonk`"
          f"\n> • `Vomit`"
          f"\n> • `Slap`"
          f"\n> • `Punch`"
          f"\n> • `Throw`"
          f"\n> • `Stalk`"
          f"\n> • `Kidnap`"
          f"\n> • `Punt`"
          f"\n> • `Strangle`"
          f"\n> • `Stab`"
          f"\n> • `Shoot`"
          f"\n> • `Deathnote`"
          f"\n> • `Highfive`"
          f"\n> • `Poke`"
          f"\n> • `Pat`"
          f"\n> • `Lick`"
          f"\n> • `Hug`"
          f"\n> • `Kiss`"
          f"\n> • `Cuddle`",
)

# Misc Commands Embed
me = discord.Embed(color=0xc700ff)
me.add_field(
    name="🧮 __Misc Commands__",
    value=f"> • `Whois`"
          f"\n> • `Avatar`"
          f"\n> • `Snipe`"
          f"\n> • `Deathhelp`"
          f"\n> • `Pickle` - /slash"
          f"\n> • `Remind`",
)

# Staff Commands Embed
se = discord.Embed(color=0xc700ff)
se.add_field(
    name="🔰 __Staff Commands__",
    value=f"> • `Purge`"
          f"\n> • `Ban`"
          f"\n> • `Unban`"
          f"\n> • `Kick`"
          f"\n> • `Timeout`"
          f"\n> • `Warn`"
          f"\n> • `WarnList`"
          f"\n> • `DelWarn`",
)

# Config Commands Embed
ce = discord.Embed(color=0xc700ff)
ce.add_field(
    name="⚙️ __Config Commands__",
    value=f"> • `SetPrefix`"
          f"\n> • `SetLog`",
)

# Help Menu Dropdown
class Dropdown(discord.ui.Select):
    def __init__(self):

        options = [
            discord.SelectOption(label="General Commands",description="Help, Info, Test, Ping, Suggest +1 More", emoji="📌"),
            discord.SelectOption(label="Fun Commands", description="Coinflip, Ask, Reverse, Say, Lovetest +2 More", emoji="🎉"),
            discord.SelectOption(label="Action Commands", description="Sniff, Bite, Bonk, Vomit, Slap +16 More", emoji="🎯"),
            discord.SelectOption(label="Misc Commands", description="Whois, Avatar, Snipe, Deathhelp, Pickle +1 More", emoji="🧮"),
            discord.SelectOption(label="Staff Commands", description="Purge, Ban, Unban, Kick, Timeout +3 More", emoji="🔰"),
            discord.SelectOption(label="Config Commands", description="SetPrefix, SetLog", emoji="⚙️"),
        ]

        super().__init__(min_values=1, max_values=1, options=options)

    async def callback(self,interaction:discord.Interaction):
        if self.values[0] == "General Commands":
            await interaction.response.send_message(embed=ge, ephemeral=True)
        if self.values[0] == "Fun Commands":
            await interaction.response.send_message(embed=fe, ephemeral=True)
        if self.values[0] == "Action Commands":
            await interaction.response.send_message(embed=ae, ephemeral=True)
        if self.values[0] == "Misc Commands":
            await interaction.response.send_message(embed=me, ephemeral=True)
        if self.values[0] == "Staff Commands":
            await interaction.response.send_message(embed=se, ephemeral=True)
        if self.values[0] == "Config Commands":
            await interaction.response.send_message(embed=ce, ephemeral=True)

# DropdownView Class
class DropdownView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(Dropdown())      
        
# General Commands Class
class GeneralCog(commands.Cog):
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
        async with aiosqlite.connect("dbs/prefix.db") as conn:
            await conn.execute(
                """
                CREATE TABLE IF NOT EXISTS prefixes (
                    server_id INTEGER PRIMARY KEY,
                    prefix TEXT NOT NULL
                )
                """
            )
    
    # Grabs the current server's prefix
    async def get_prefix(self, message):
        async with aiosqlite.connect("dbs/prefix.db") as conn:
            async with conn.execute("SELECT prefix FROM prefixes WHERE server_id = ?", (message.guild.id,)) as cursor:
                result = await cursor.fetchone()
                return result[0] if result else "!"  
    
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
    
    # SetPrefix Command
    @commands.command(aliases=["xiferptes", "SetPrefix", "xiferPteS", "SETPREFIX", "XIFERPTES"])
    async def setprefix(self, ctx, new_prefix):
        if discord.utils.get(ctx.author.roles, name="🔐 Assistant Chief"):
            self.bot.command_prefix = new_prefix
            async with aiosqlite.connect("dbs/prefix.db") as conn:
                await conn.execute("REPLACE INTO prefixes (server_id, prefix) VALUES (?, ?)", (ctx.guild.id, new_prefix))
                await conn.commit()
            await ctx.send(f"**{ctx.guild.name}** server prefix is now: `{new_prefix}`")
        else:
            e = discord.Embed(color=0xc700ff)
            e.description = "🚨 That is a **High Staff** command! You don't have the required perms! 🚨"
            await ctx.send(embed=e)
    
    # Help Command
    @commands.command(aliases=["pleh", "Help", "pleH", "HELP", "PLEH"])
    async def help(self, ctx):
        e = discord.Embed(color=0xc700ff)
        e.set_author(name="Bot Commands", icon_url=self.bot.user.display_avatar.url)
        e.set_thumbnail(url="https://media.discordapp.net/attachments/1065517294278676511/1078658592024043730/zZJfouNDCkPA.jpg")
        e.add_field(
            name="✧ __Command Menus__",
            value=f"> 📌 `General Commands`"
                  f"\n> 🎉 `Fun Commands`"
                  f"\n> 🎯 `Action Commands`"
                  f"\n> 🧮 `Misc Commands`"
                  f"\n> 🔰 `Staff Commands`"
                  f"\n> ⚙️ `Config Commands`",
        )
        e.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        e.timestamp = datetime.utcnow()
        view = DropdownView()
        await ctx.send(embed=e, view=view)
        
    # Info Command
    @commands.command(aliases=["ofni", "Info", "ofnI", "INFO", "OFNI"])
    async def info(self, ctx):
        logging_channel_id = await self.get_logging_channel(ctx.guild.id)
        logging_channel = self.bot.get_channel(logging_channel_id)
        current_prefix = await self.get_prefix(ctx.message)
        delta_uptime = datetime.utcnow() - bot.launch_time
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        member_count = len(ctx.guild.members) # includes bots
        true_member_count = len([m for m in ctx.guild.members if not m.bot]) # doesn't include bots
        total_lines = 24
        cog_directory = "./cogs"
        for filename in os.listdir(cog_directory):
            if filename.endswith(".py"):
                with open(os.path.join(cog_directory, filename), "r") as file:
                    lines = file.readlines()
                    non_empty_lines = [line.strip() for line in lines if line.strip()]
                    total_lines += len(non_empty_lines)
        e = discord.Embed(color=0xc700ff)
        e.set_author(name="Bot Information", icon_url="https://media.discordapp.net/attachments/1065517294278676511/1078658592024043730/zZJfouNDCkPA.jpg")
        e.set_thumbnail(url="https://media.discordapp.net/attachments/1065517294278676511/1078658592024043730/zZJfouNDCkPA.jpg")
        e.add_field(
            name="✧ __Server__",
            value=f"> **Prefix:** {current_prefix}"
                  f"\n> **Logging:** {logging_channel.mention}",
            inline=False
        )
        e.add_field(
            name="✧ __Statistics__",
            value=f"> **Commands:** [51]"
		  f"\n> **Code:** {total_lines} Lines"
                  f"\n> **Ping:** {round(self.bot.latency * 1000)}ms"
                  f"\n> **Users:** {true_member_count}"
        	  f"\n> **Uptime:** {days}**d** {hours}**h** {minutes}**m** {seconds}**s**",
            inline=False
        )
        e.add_field(
            name="✧ __Credits__",
            value=f"> **Dev:** `gamingderp`",
            inline=False
        )
        e.add_field(
            name="✧ __GitHub__",
            value=f"<:GitHub:1123773190238392504> [Repo Link](https://github.com/GamingDerp/SleeplessNightsBot)",
            inline=False
        )
        e.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        e.timestamp = datetime.utcnow()
        await ctx.send(embed=e)
    
    # Test Command
    @commands.command(aliases=["tset", "Test", "tseT", "TEST", "TSET"])
    async def test(self, ctx):
        await ctx.send("I'm up!")

    # Ping Command
    @commands.command(aliases=["gnip", "Ping", "gniP", "PING", "GNIP"])
    async def ping(self, ctx):
        e = discord.Embed(color=0xc700ff)
        e.add_field(
            name="📶 Ping",
            value=f"Your ping is **{round(self.bot.latency * 1000)}**ms",
    	    inline=False
        )
        await ctx.send(embed=e)

    # Suggest Command
    @commands.command(aliases=["tseggus", "Suggest", "tsegguS", "SUGGEST", "TSEGGUS"])
    async def suggest(self, ctx, *, suggestion):
        await ctx.send("Your suggestion has been added! Check <#1065657740573286523>!")
        se = discord.Embed(color=0xc700ff)
        se.set_author(name=f"Suggested by {ctx.message.author}", icon_url=ctx.author.avatar.url)
        se.set_thumbnail(url=ctx.author.avatar.url)
        se.description = suggestion
        se.timestamp = datetime.utcnow()
        channel = self.bot.get_channel(1065657740573286523)
        vote = await channel.send(embed=se)
        await vote.add_reaction("✅")
        await vote.add_reaction("❌")
        
    # Poll Command - Slash
    @commands.hybrid_command(name="poll", description="Create a poll!")
    async def poll(self, ctx, question:str, option1:str=None, option2:str=None, option3:str=None, option4:str=None, option5:str=None):
        options = [option1, option2, option3, option4, option5]
        options = [option for option in options if option is not None]
        emoji_list = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣"]      
        if not options:
            await ctx.send("Please provide at least two options for the poll.")
            return
        if len(options) > 5:
            await ctx.send("You can only have up to 5 options in the poll.")
            return       
        e = discord.Embed(color=0xc700ff)
        e.title = f"📊 **{question}**"
        description_text = ""
        for i, option in enumerate(options):
            description_text += f"\n{emoji_list[i]} {option}"
        e.description = description_text
        msg = await ctx.send(embed=e)
        for i in range(len(options)):
            await msg.add_reaction(emoji_list[i])
        
        
async def setup(bot):
    await bot.add_cog(GeneralCog(bot))
