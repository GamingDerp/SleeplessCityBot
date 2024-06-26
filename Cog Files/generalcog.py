import os
import discord
from discord.ext import commands
from datetime import datetime, timedelta
import time
import aiosqlite
import random
import asyncio

# Stores when the bot was started
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
bot.launch_time = datetime.utcnow()

sc_image = "https://media.discordapp.net/attachments/1065517294278676511/1176668287636090920/SCLogo.jpg?ex=656fb4bd&is=655d3fbd&hm=b87bdcec00843db85984116007a7ab56b44af4491c79e0dadc557e80b392b17f&="

# General Commands Embed
ge = discord.Embed(color=0xc700ff)
ge.set_author(name="Bot Commands", icon_url=sc_image)
ge.set_thumbnail(url=sc_image)
ge.add_field(
    name="📌 __General Commands__",
    value=f"> `Help`, `Info`, `Test`, `Ping`, `Suggest`, `Poll`",
)

# Fun Commands Embed
fe = discord.Embed(color=0xc700ff)
fe.set_author(name="Bot Commands", icon_url=sc_image)
fe.set_thumbnail(url=sc_image)
fe.add_field(
    name="🎉 __Fun Commands__",
    value=f"> `Coinflip`, `Ask`, `Reverse`, `Say`, `Lovetest`, `Cute`",
)

# Action Commands Embed
ae = discord.Embed(color=0xc700ff)
ae.set_author(name="Bot Commands", icon_url=sc_image)
ae.set_thumbnail(url=sc_image)
ae.add_field(
    name="🎯 __Action Commands__",
    value=f"> `Sniff`, `Bite`, `Bonk`, `Vomit`, `Slap`, `Punch` \n> `Throw`, `Stalk`, `Kidnap`, `Punt`, `Strangle`, `Stab` \n> `Shoot`, `Deathnote`, `Highfive`, `Poke`, `Pat`, `Lick` \n> `Hug`, `Kiss`, `Cuddle`",
)

# Misc Commands Embed
me = discord.Embed(color=0xc700ff)
me.set_author(name="Bot Commands", icon_url=sc_image)
me.set_thumbnail(url=sc_image)
me.add_field(
    name="🧮 __Misc Commands__",
    value=f"> `Whois`, `Snipe`, `Deathhelp`, `Remind`, `ESteal`, `Todoadd` \n> `Tododel`, `Todolist`, `Todoclear`, `Giveaway`, `Reroll`, `ClimateClock`",
)

# Staff Commands Embed
se = discord.Embed(color=0xc700ff)
se.set_author(name="Bot Commands", icon_url=sc_image)
se.set_thumbnail(url=sc_image)
se.add_field(
    name="🔰 __Staff Commands__",
    value=f"> `Purge`, `Ban`, `Unban`, `Kick`, `Timeout`, `Warn` \n> `WarnList`, `DelWarn`, `Highlightadd`, `Highlightremove`, `Highlightclear`, `Highlightblock` \n> `Highlightunblock`, `Defaulthighlights`, `Highlightignore`, `Highlightunignore`",
)

# Config Commands Embed
ce = discord.Embed(color=0xc700ff)
ce.set_author(name="Bot Commands", icon_url=sc_image)
ce.set_thumbnail(url=sc_image)
ce.add_field(
    name="⚙️ __Config Commands__",
    value=f"> `SetPrefix`, `SetLog`, `SetStar`, `SetSuggest`",
)

# Help Menu Dropdown
class Dropdown(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="General Commands",description="Help, Info, Test, Ping, Suggest +1 More", emoji="📌"),
            discord.SelectOption(label="Fun Commands", description="Coinflip, Ask, Reverse, Say, Lovetest +1 More", emoji="🎉"),
            discord.SelectOption(label="Action Commands", description="Sniff, Bite, Bonk, Vomit, Slap +16 More", emoji="🎯"),
            discord.SelectOption(label="Misc Commands", description="Whois, Snipe, Deathhelp, Remind, Tdadd +7 More", emoji="🧮"),
            discord.SelectOption(label="Staff Commands", description="Purge, Ban, Unban, Kick, Timeout +11 More", emoji="🔰"),
            discord.SelectOption(label="Config Commands", description="SetPrefix, SetLog, SetStar, SetSuggest", emoji="⚙️"),
        ]
        super().__init__(min_values=1, max_values=1, options=options)

    async def callback(self,interaction:discord.Interaction):
        if self.values[0] == "General Commands":
            await interaction.response.edit_message(embed=ge)
        if self.values[0] == "Fun Commands":
            await interaction.response.edit_message(embed=fe)
        if self.values[0] == "Action Commands":
            await interaction.response.edit_message(embed=ae)
        if self.values[0] == "Misc Commands":
            await interaction.response.edit_message(embed=me)
        if self.values[0] == "Staff Commands":
            await interaction.response.edit_message(embed=se)
        if self.values[0] == "Config Commands":
            await interaction.response.edit_message(embed=ce)   
    
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
    
    @commands.Cog.listener()
    async def on_ready(self):
        await self.create_table() # Prefix DB
        await self.initialize_database() # Logging DB
        await self.create_suggestion_table() # Suggest DB
    
    async def create_table(self):
        async with aiosqlite.connect("dbs/prefix.db") as conn:
            await conn.execute(
                '''
                CREATE TABLE IF NOT EXISTS prefixes (
                    server_id INTEGER PRIMARY KEY,
                    prefix TEXT NOT NULL
                )
                '''
            )
    
    async def get_prefix(self, message):
        async with aiosqlite.connect("dbs/prefix.db") as conn:
            async with conn.execute("SELECT prefix FROM prefixes WHERE server_id = ?", (message.guild.id,)) as cursor:
                result = await cursor.fetchone()
                return result[0] if result else "!"  
    
    async def initialize_database(self):
        self.db_conn = await aiosqlite.connect("dbs/logging.db")
    
    async def get_logging_channel(self, guild_id):
        async with self.db_conn.execute(
            "SELECT channel_id FROM logging_channels WHERE guild_id = ?", (guild_id,)
        ) as cursor:
            result = await cursor.fetchone()
            return result[0] if result else None
    
    async def get_starboard_channel(self, guild_id):
        async with aiosqlite.connect("dbs/star.db") as db:
            async with db.execute("SELECT channel_id FROM starboard WHERE server_id = ?", (guild_id,)) as cursor:
                result = await cursor.fetchone()
                if result:
                    starboard_channel_id = result[0]
                    starboard_channel = self.bot.get_channel(starboard_channel_id)
                    if starboard_channel:
                        return starboard_channel.mention
        return "None"
    
    async def create_suggestion_table(self):
        async with aiosqlite.connect("dbs/suggest.db") as db:
            await db.execute("CREATE TABLE IF NOT EXISTS suggestion_channels (server_id INTEGER, channel_id INTEGER)")
            await db.commit()
    
    async def get_suggestion_channel(self, guild_id):
        async with aiosqlite.connect("dbs/suggest.db") as db:
            cursor = await db.execute("SELECT channel_id FROM suggestion_channels WHERE server_id = ?", (guild_id,))
            suggestion_channel_id = await cursor.fetchone()
        return self.bot.get_channel(suggestion_channel_id[0]) if suggestion_channel_id else None
    
    # SetPrefix Command
    @commands.hybrid_command(description="Set the bot's prefix for the server")
    async def setprefix(self, ctx, new_prefix):
        if discord.utils.get(ctx.author.roles, name="🔐 Assistant Chief"):
            self.bot.command_prefix = new_prefix
            async with aiosqlite.connect("dbs/prefix.db") as conn:
                await conn.execute("REPLACE INTO prefixes (server_id, prefix) VALUES (?, ?)", (ctx.guild.id, new_prefix))
                await conn.commit()
            await ctx.send(f"**{ctx.guild.name}** server prefix is now: `{new_prefix}`", ephemeral=True)
        else:
            e = discord.Embed(color=0xc700ff)
            e.description = "🚨 That is a **High Staff** command! You don't have the required perms! 🚨"
            await ctx.send(embed=e, ephemeral=True)
    
    # SetSuggest Command
    @commands.hybrid_command(description="Set the suggestion channel for the server")
    async def setsuggest(self, ctx, channel: discord.TextChannel):
        if discord.utils.get(ctx.author.roles, name="🔐 Assistant Chief"):
            def check(message):
                return message.author == ctx.author and message.channel == ctx.channel and message.content.lower() in ['yes', 'no']
            await self.create_suggestion_table()
            await ctx.send(f"Is {channel.mention} the correct channel? [Yes/No]")
            try:
                reply = await self.bot.wait_for('message', check=check, timeout=30)
                if reply.content.lower() == 'yes':
                    async with aiosqlite.connect("dbs/suggest.db") as db:
                        await db.execute("DELETE FROM suggestion_channels WHERE server_id = ?", (ctx.guild.id,))
                        await db.execute("INSERT INTO suggestion_channels (server_id, channel_id) VALUES (?, ?)", (ctx.guild.id, channel.id))
                        await db.commit()
                    await ctx.send(f"Suggestion channel has been set to {channel.mention}", ephemeral=True)
                else:
                    await ctx.send("Please retry the command and mention the correct channel!")
            except asyncio.TimeoutError:
                await ctx.send("Timed out. Suggestion channel setting cancelled.", ephemeral=True)
        else:
            e = discord.Embed(color=0xc700ff)
            e.description = "🚨 That is a **High Staff** command! You don't have the required perms! 🚨"
            await ctx.send(embed=e, ephemeral=True)
    
    # Help Command
    @commands.hybrid_command(description="Sends the bots help menu")
    async def help(self, ctx):
        e = discord.Embed(color=0xc700ff)
        e.set_author(name="Bot Commands", icon_url=sc_image)
        e.set_thumbnail(url=sc_image)
        e.add_field(
            name="✧ __Command Menus__",
            value=f"> 📌 General"
                  f"\n> 🎉 Fun"
                  f"\n> 🎯 Action"
                  f"\n> 🧮 Misc"
                  f"\n> 🔰 Staff"
                  f"\n> ⚙️ Config",
        )
        view = DropdownView()
        await ctx.send(embed=e, view=view)
        
    # Info Command
    @commands.hybrid_command(description="Sends information about the bot")
    async def info(self, ctx):
        current_prefix = await self.get_prefix(ctx.message)
        logging_channel_id = await self.get_logging_channel(ctx.guild.id)
        logging_channel = self.bot.get_channel(logging_channel_id)
        starboard_mention = await self.get_starboard_channel(ctx.guild.id)
        suggestion_channel = await self.get_suggestion_channel(ctx.guild.id)
        total_lines = 24
        cog_directory = "./cogs"
        for filename in os.listdir(cog_directory):
            if filename.endswith(".py"):
                with open(os.path.join(cog_directory, filename), "r") as file:
                    lines = file.readlines()
                    non_empty_lines = [line.strip() for line in lines if line.strip()]
                    total_lines += len(non_empty_lines)
        member_count = len(ctx.guild.members) # includes bots
        true_member_count = len([m for m in ctx.guild.members if not m.bot]) # doesn't include bots
        delta_uptime = datetime.utcnow() - bot.launch_time
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        e = discord.Embed(color=0xc700ff)
        e.set_author(name="Bot Information", icon_url=sc_image)
        e.set_thumbnail(url=sc_image)
        e.add_field(
            name="✧ __Server__",
            value=f"> **Prefix:** {current_prefix}"
                  f"\n> **Logging:** {logging_channel.mention if logging_channel else 'None'}"
                  f"\n> **Starboard:** {starboard_mention if starboard_mention else 'None'}"
                  f"\n> **Suggestion:** {suggestion_channel.mention if suggestion_channel else 'None'}",
            inline=False
        )
        e.add_field(
            name="✧ __Statistics__",
            value=f"> **Commands:** [66]"
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
            value=f"<:GitHub:1123773190238392504> [Repo Link](https://github.com/GamingDerp/SleeplessCityBot/tree/main)",
            inline=False
        )
        e.set_footer(text=f"Requested by {ctx.author}")
        e.timestamp = datetime.utcnow()
        await ctx.send(embed=e)

    # Test Command
    @commands.hybrid_command(description="Test if the bot is up")
    async def test(self, ctx):
        await ctx.send("I'm up! <a:DerpPet:1065453721200365629>")

    # Ping Command
    @commands.hybrid_command(description="Sends your ping")
    async def ping(self, ctx):
        e = discord.Embed(color=0xc700ff)
        e.add_field(
            name="📶 Ping",
            value=f"Your ping is **{round(self.bot.latency * 1000)}**ms",
    	    inline=False
        )
        await ctx.send(embed=e)

    # Suggest Command
    @commands.hybrid_command(description="Make a suggestion")
    async def suggest(self, ctx, *, suggestion):
        try:
            await self.create_suggestion_table()
            suggestion_channel = await self.get_suggestion_channel(ctx.guild.id)
            if suggestion_channel:
                await ctx.send(f"Your suggestion has been added! Check {suggestion_channel.mention}!")
                se = discord.Embed(color=0xc700ff)
                se.set_author(name=f"Suggested by {ctx.author}")
                se.set_thumbnail(url=ctx.author.avatar.url)
                se.description = suggestion
                if ctx.message.attachments:
                    attachment_url = ctx.message.attachments[0].url
                    se.set_image(url=attachment_url)
                se.timestamp = datetime.utcnow()
                vote = await suggestion_channel.send(embed=se)
                for emoji in ["👍", "🤷‍♂️", "👎"]:
                    await vote.add_reaction(emoji)
            else:
                await ctx.send("No suggestion channel set!")
        except Exception as e:
            print(e)
    
    # Poll Command
    @commands.hybrid_command(description="Create a poll!")
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
