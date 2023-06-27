import discord
from discord.ext import commands

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
    
    # Responds when the bot is mentioned by a user's @, and adds a "Troll Face" emoji in #counting when a user types '69', sends message when server's boosted
    @commands.Cog.listener()
    async def on_message(self, message):
        if str(bot_id) in message.content:
            await message.channel.send("I've been summoned! If you need me do `!help` <:CatWave:1093435504688644137>")
        if message.channel.id == 1065502975499440168: #counting channel id
            if message.content == '69':
                await message.add_reaction('<:Troll:1065453655588884520>')
                await self.bot.process_commands(message)
        if message.type == discord.MessageType.premium_guild_subscription:
            channel = self.bot.get_channel(1119185446950408232)
            e = discord.Embed(color=0xc700ff)
            e.set_author(name="💎 Server Boosted")
            e.add_field(name="Booster", value=message.author)
            await channel.send(embed=e)
        
            chan = self.bot.get_channel(1065473991940247624)
            e = discord.Embed(color=0xc700ff)
            e.set_author(name=f"💎 {message.author} boosted the server!")
            e.description = f"Thank you {message.author.mention}!"
            e.add_field(name="Recieved Perks", value="> Image Perms \n> Embed Perms \n> Video Perms \n> Streaming Perms \n*and access to the exclusive* ***Booster Chat!***")
            e.timestamp = datetime.utcnow()
            await chan.send(embed=e)
            
    # Welcomes new users when they join the server
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(1065466402447826984)
        e = discord.Embed(color=0xc700ff)
        e.set_author(name=f"✨ Welcome to Sleepless Nights! ✨")
        e.set_image(url="https://media.discordapp.net/attachments/1070206894800638003/1078900669865525328/WelcomeGif.gif"),
        await channel.send(f"{member.mention} has joined! Checkout <#1065472726158037002> and <#1065473461272715344>!", embed=e)
        role = discord.utils.get(member.guild.roles, name="👌 Member")
        await member.add_roles(role)

    # Sends a message when a user leaves
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(1065466402447826984)
        e = discord.Embed(color=0xc700ff)
        e.description = f"👋 {member.name} left! 👋"
        await channel.send(embed=e)


async def setup(bot):
    await bot.add_cog(Events(bot))
