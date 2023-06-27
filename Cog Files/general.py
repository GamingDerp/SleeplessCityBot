import discord
from discord.ext import commands
from datetime import datetime, timedelta
import time

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
          f"\n> • `Remind`",
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
          f"\n> • `Duel`",
)

# Action Commands Embed
ae = discord.Embed(color=0xc700ff)
ae.add_field(
    name="🎯 __Action Commands__",
    value=f"> • `Bonk`"
          f"\n> • `Slap`"
          f"\n> • `Throw`"
          f"\n> • `Kidnap`"
          f"\n> • `Strangle`"
          f"\n> • `Stab`"
          f"\n> • `Shoot`"
          f"\n> • `Deathnote`"
          f"\n> • `Highfive`"
          f"\n> • `Poke`"
          f"\n> • `Pat`"
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
          f"\n> • `Pickle` - /slash",
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

# Help Menu Dropdown
class Dropdown(discord.ui.Select):
    def __init__(self):

        options = [
            discord.SelectOption(label="General Commands",description="Help, Info, Test, Ping, Suggest +1 More", emoji="📌"),
            discord.SelectOption(label="Fun Commands", description="Coinflip, Ask, Reverse, Say, Lovetest +2 More", emoji="🎉"),
            discord.SelectOption(label="Action Commands", description="Bonk, Slap, Throw, Kidnap, Strangle +9 More", emoji="🎯"),
            discord.SelectOption(label="Misc Commands", description="Whois, Avatar, Snipe, Deathhelp, Pickle", emoji="🧮"),
            discord.SelectOption(label="Staff Commands", description="Purge, Ban, Unban, Kick, Timeout +3 More", emoji="🔰"),
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

class DropdownView(discord.ui.View):
    def __init__(self):
        super().__init__()

        self.add_item(Dropdown()) 

# General Commands Class
class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
    
    # Help Command
    @commands.command(aliases=["pleh", "Help", "pleH"])
    async def help(self, ctx):
        e = discord.Embed(color=0xc700ff)
        e.set_thumbnail(url="https://media.discordapp.net/attachments/1065517294278676511/1078658592024043730/zZJfouNDCkPA.jpg")
        e.description = "✨ Choose the menu you're looking for! ✨"
        e.add_field(
            name="✧ __Command Menus__",
            value=f"> 📌 `General Commands`"
                  f"\n> 🎉 `Fun Commands`"
                  f"\n> 🎯 `Action Commands`"
                  f"\n> 🧮 `Misc Commands`"
                  f"\n> 🔰 `Staff Commands`",
        )
        e.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url),
        e.timestamp = datetime.utcnow()
        view = DropdownView()
        await ctx.send(embed=e, view=view)
        
    # Info Command
    @commands.command(aliases=["ofni", "Info", "ofnI"])
    async def info(self, ctx):
        delta_uptime = datetime.utcnow() - bot.launch_time
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
    
        member_count = len(ctx.guild.members) # includes bots
        true_member_count = len([m for m in ctx.guild.members if not m.bot]) # doesn't include bots
        
        e = discord.Embed(color=0xc700ff)
        e.set_thumbnail(url="https://media.discordapp.net/attachments/1065517294278676511/1078658592024043730/zZJfouNDCkPA.jpg")
        e.description = f"🤖 Bot Information 🤖"
        e.add_field(
            name="✧ __Statistics__",
            value=f"> **Prefix:** !"
                  f"\n> **Commands:** [40]"
			      f"\n> **Code:** 1,306 Lines"
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
            value=f"<:GitHub:1120884125918834779> [Repo Link](https://github.com/GamingDerp/SleeplessNightsBot)",
            inline=False
        )
        e.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url),
        e.timestamp = datetime.utcnow()
        await ctx.send(embed=e)

    # Test Command
    @commands.command(aliases=["tset", "Test", "tseT"])
    async def test(self, ctx):
        await ctx.send("I'm up!")

    # Ping Command
    @commands.command(aliases=["gnip", "Ping", "gniP"])
    async def ping(self, ctx):
        e = discord.Embed(color=0xc700ff)
        e.add_field(
            name="📶 Ping",
            value=f"Your ping is **{round(self.bot.latency * 1000)}**ms",
    	    inline=False
        )
        await ctx.send(embed=e)

    # Suggest Command
    @commands.command(aliases=["tseggus", "Suggest", "tsegguS"])
    async def suggest(self, ctx, *, suggestion):
        se = discord.Embed(color=0xc700ff)
        se.set_author(name=f"Suggested by {ctx.message.author}", icon_url=ctx.author.avatar.url)
        se.description = f"> {suggestion}"
        se.timestamp = datetime.utcnow()
        channel = self.bot.get_channel(1065657740573286523)
        vote = await channel.send(embed=se)
        await vote.add_reaction("✅")
        await vote.add_reaction("❌")


async def setup(bot):
    await bot.add_cog(General(bot))
