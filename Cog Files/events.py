import discord
from discord.ext import commands
from discord.ui import Button, View

# Bots User ID
bot_id = 1103103994777309205

# Events Commands Class
class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Changes bot's Discord activity when loaded and syncs slash commands
    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(activity=discord.Game(name="Helping SN Users..."))
        await self.bot.tree.sync()
    
    # Bot Mention Message Event / Counting Reaction Event
    @commands.Cog.listener()
    async def on_message(self, message):
        if str(bot_id) in message.content:
            await message.channel.send("I've been summoned! If you need me do `!help` <:CatWave:1123898399557693470>")
        if message.channel.id == 1065502975499440168:
            if message.content == '69':
                await message.add_reaction('<:Troll:1065453655588884520>')
                await self.bot.process_commands(message)
            
    # User Joined Message Event
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(1065466402447826984)
        e = discord.Embed(color=0xc700ff)
        e.set_author(name=f"✨ Welcome to Sleepless Nights! ✨")
        e.description = "*~ The city that never sleeps ~*"
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
            e.set_thumbnail(url=after.avatar_url)
            e.description = f"Thank you {after.mention}! \nYou'll now recieve these perks: \n> Image Perms \n> Embed Perms \n> Video Perms \n> Streaming Perms \n*and access to the exclusive <#1065651827703554109>!*"
            e.add_field(name="Boost Level", value=after.premium_since.boost_level)
            await channel.send(embed=e)


async def setup(bot):
    await bot.add_cog(Events(bot))
