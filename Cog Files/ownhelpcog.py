import discord
from discord.ext import commands
from datetime import datetime, timedelta
import asyncio

# Bot Owner User ID
owner_id = 532706491438727169

# OwnHelp Commands Class
class OwnHelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    # Owner Help Command
    @commands.hybrid_command(description="Sends the help menu for the bot Owner")
    async def ownhelp(self, ctx):
        if ctx.author.id == owner_id:
            e = discord.Embed(color=0xe02da9)
            e.set_thumbnail(url="https://media.discordapp.net/attachments/807071768258805764/1114258238335090698/OwnerThumbnail.png")
            e.description = "👾 Owner Commands 👾"
            e.add_field(
                name="✧ __General__",
                value=f"> • `OwnHelp`"
                      f"\n> • `Nuke`"
                      f"\n> • `Revive`",
            )
            e.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url),
            e.timestamp = datetime.utcnow()
            await ctx.send(embed=e)
        else:
            e = discord.Embed(color=0xe02da9)
            e.description = "🚨 That is a **Owner** command! You don't have the required perms! 🚨"
            await ctx.send(embed=e)

    # Nuke Command -- OWNER (joke command)
    @commands.hybrid_command(description="Nuke the server")
    async def nuke(self, ctx):
        if ctx.author.id == owner_id:
            await ctx.send("Nuking server in...3")
            await asyncio.sleep(0.85)
            await ctx.send(content="Nuking server in...2")
            await asyncio.sleep(0.90)
            await ctx.send(content="Nuking server in...1")
            await asyncio.sleep(1.25)
            await ctx.send("https://cdn.discordapp.com/attachments/807071768258805764/1103594669050441788/rick-roll.gif")
        else:
            e = discord.Embed(color=0xe02da9)
            e.description = "🚨 That is a **Owner** command! You don't have the required perms! 🚨"
            await ctx.send(embed=e)

    # Revive Command -- OWNER
    @commands.hybrid_command(description="Revive another user")
    async def revive(self, ctx, user:discord.Member):
        if ctx.author.id == owner_id:
            e = discord.Embed(color=0xe02da9)
            e.description = f"{ctx.author.mention} revives {user.mention}!"
            e.set_image(url="https://media.discordapp.net/attachments/807071768258805764/1114248146986467328/ReviveGif.gif"),
            await ctx.send(embed=e)
        else:
            e = discord.Embed(color=0xe02da9)
            e.description = "🚨 That is a **Owner** command! You don't have the required perms! 🚨"
            await ctx.send(embed=e)

    # Post Color Command
    @commands.command()
    async def postcolor(self, ctx):
        if ctx.author.id == owner_id:
            e = discord.Embed(color=0xc700ff)
            e.title = "✨ Color Roles ✨"
            e.description = "> **1** <@&1065450715335635054> \n> **2** <@&1065450801922834523> \n> **3** <@&1065450888845598770> \n> **4** <@&1065450959993577482> \n> **5** <@&1065451198217465907> \n> **6** <@&1065451625843527831> \n> **7** <@&1065451527348699166> \n> **8** <@&1065451287077986335> \n> **9** <@&1065451382980747385> \n> **10** <@&1065451081758429285>"
            view = discord.ui.View()
            view.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, label="1", custom_id="red"))
            view.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, label="2", custom_id="blue"))
            view.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, label="3", custom_id="green"))
            view.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, label="4", custom_id="yellow"))
            view.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, label="5", custom_id="pink"))
            view.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, label="6", custom_id="purple"))
            view.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, label="7", custom_id="orange"))
            view.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, label="8", custom_id="brown"))
            view.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, label="9", custom_id="gray"))
            view.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, label="10", custom_id="black"))
            await ctx.send(embed=e, view=view)
        else:
            e = discord.Embed(color=0xe02da9)
            e.description = "🚨 That is a **Owner** command! You don't have the required perms! 🚨"
            await ctx.send(embed=e)
    
    # Post DM Command
    @commands.command()
    async def postdm(self, ctx):
        if ctx.author.id == owner_id:
            e = discord.Embed(color=0xc700ff)
            e.title = "✨ DM Roles ✨"
            e.description = "> **1** <@&1065457094444200026> \n> **2** <@&1065457144708743260> \n> **3** <@&1065457177436901396>"
            view = discord.ui.View()
            view.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, label="1", custom_id="open"))
            view.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, label="2", custom_id="closed"))
            view.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, label="3", custom_id="ask"))
            await ctx.send(embed=e, view=view)
        else:
            e = discord.Embed(color=0xe02da9)
            e.description = "🚨 That is a **Owner** command! You don't have the required perms! 🚨"
            await ctx.send(embed=e)

    # Post Pings Command
    @commands.command()
    async def postpings(self, ctx):
        if ctx.author.id == owner_id:
            e = discord.Embed(color=0xc700ff)
            e.title = "✨ Ping Roles ✨"
            e.description = "> **1** <@&1065457241181917226> \n> **2** <@&1065457288082636861> \n> **3** <@&1065457351727005767> \n> **4** <@&1065457387605069834> \n> **5** <@&1080857799543763015> \n> **6** <@&1092614799269048401> \n> **7** <@&1137864662512312421>"
            view = discord.ui.View()
            view.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, label="1", custom_id="announcements"))
            view.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, label="2", custom_id="deadchat"))
            view.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, label="3", custom_id="events"))
            view.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, label="4", custom_id="giveaways"))
            view.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, label="5", custom_id="polls"))
            view.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, label="6", custom_id="partners"))
            view.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, label="7", custom_id="uno"))
            await ctx.send(embed=e, view=view)
        else:
            e = discord.Embed(color=0xe02da9)
            e.description = "🚨 That is a **Owner** command! You don't have the required perms! 🚨"
            await ctx.send(embed=e)

    # Post Gender Command
    @commands.command()
    async def postgender(self, ctx):
        if ctx.author.id == owner_id:
            e = discord.Embed(color=0xc700ff)
            e.title = "✨ Gender Roles ✨"
            e.description = "> **1** <@&1065450369502675034> \n> **2** <@&1065450408652328990> \n> **3** <@&1065452510271258654> \n> **4** <@&1065452860361416776>"
            view = discord.ui.View()
            view.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, label="1", custom_id="male"))
            view.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, label="2", custom_id="female"))
            view.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, label="3", custom_id="nonbinary"))
            view.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, label="4", custom_id="existing"))
            await ctx.send(embed=e, view=view)
        else:
            e = discord.Embed(color=0xe02da9)
            e.description = "🚨 That is a **Owner** command! You don't have the required perms! 🚨"
            await ctx.send(embed=e)

    # Post Pronoun Command
    @commands.command()
    async def postpronoun(self, ctx):
        if ctx.author.id == owner_id:
            e = discord.Embed(color=0xc700ff)
            e.title = "✨ Pronoun Roles ✨"
            e.description = "> **1** <@&1065452632128372756> \n> **2** <@&1065452583403134987> \n> **3** <@&1065452672255275048> \n> **4** <@&1065452706388521051> \n> **5** <@&1065452760230805625>"
            view = discord.ui.View()
            view.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, label="1", custom_id="he"))
            view.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, label="2", custom_id="she"))
            view.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, label="3", custom_id="they"))
            view.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, label="4", custom_id="any"))
            view.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, label="5", custom_id="ask"))
            await ctx.send(embed=e, view=view)
        else:
            e = discord.Embed(color=0xe02da9)
            e.description = "🚨 That is a **Owner** command! You don't have the required perms! 🚨"
            await ctx.send(embed=e)

    # Post Age Command
    @commands.command()
    async def postage(self, ctx):
        if ctx.author.id == owner_id:
            e = discord.Embed(color=0xc700ff)
            e.title = "✨ Age Roles ✨"
            e.description = "> **1** <@&1065450494065119282> \n> **2** <@&1065450630073823314>"
            view = discord.ui.View()
            view.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, label="1", custom_id="above"))
            view.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, label="2", custom_id="under"))
            await ctx.send(embed=e, view=view)
        else:
            e = discord.Embed(color=0xe02da9)
            e.description = "🚨 That is a **Owner** command! You don't have the required perms! 🚨"
            await ctx.send(embed=e)

    # Post Region Command
    @commands.command()
    async def postregion(self, ctx):
        if ctx.author.id == owner_id:
            e = discord.Embed(color=0xc700ff)
            e.title = "✨ Region Roles ✨"
            e.description = "> **1** <@&1065456803615342652> \n> **2** <@&1108645484819664896> \n> **3** <@&1065456858770448384> \n> **4** <@&1065456885437841408> \n> **5** <@&1065456932216913960> \n> **6** <@&1065456993017548810>"
            view = discord.ui.View()
            view.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, label="1", custom_id="na"))
            view.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, label="2", custom_id="sa"))
            view.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, label="3", custom_id="eu"))
            view.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, label="4", custom_id="oc"))
            view.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, label="5", custom_id="as"))
            view.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, label="6", custom_id="af"))
            await ctx.send(embed=e, view=view)
        else:
            e = discord.Embed(color=0xe02da9)
            e.description = "🚨 That is a **Owner** command! You don't have the required perms! 🚨"
            await ctx.send(embed=e)
    
    added_embed = discord.Embed(color=0xc700ff)
    added_embed.title = "✅ Role Added ✅"
    added_embed.description = "The role has been added!"

    removed_embed = discord.Embed(color=0xc700ff)
    removed_embed.title = "❌ Role Removed ❌"
    removed_embed.description = "The role has been removed!"
    
    role_mappings = {
        'red': 'Red',
        'blue': 'Blue',
        'green': 'Green',
        'yellow': 'Yellow',
        'pink': 'Pink',
        'purple': 'Purple',
        'orange': 'Orange',
        'brown': 'Brown',
        'gray': 'Gray',
        'black': 'Black',
        'open': "DM's Open",
        'closed': "DM's Closed",
        'ask': 'Ask to DM',
        'announcements': 'Announcements',
        'deadchat': 'Dead Chat',
        'events': 'Events',
        'giveaways': 'Giveaways',
        'polls': 'Polls',
        'partners': 'Partners',
        'uno': 'Uno',
        'male': 'Male',
        'female': 'Female',
        'nonbinary': 'Non-Binary',
        'existing': 'Existing',
        'he': 'He/Him',
        'she': 'She/Her',
        'they': 'They/Them',
        'any': 'Any/All',
        'ask': 'Ask',
        'above': '18+',
        'under': 'Under 18-',
        'na': 'NA',
        'sa': 'SA',
        'eu': 'EU',
        'oc': 'OC',
        'as': 'AS',
        'af': 'AF',
    }

    @commands.Cog.listener()
    async def on_interaction(self, interaction):
        try:
            if interaction.type == discord.InteractionType.component:
                custom_id = interaction.data['custom_id']
                role_name = self.role_mappings.get(custom_id)
                if role_name:
                    role = discord.utils.get(interaction.guild.roles, name=role_name)
                    if role in interaction.user.roles:
                        await interaction.user.remove_roles(role)
                        await interaction.response.send_message(embed=self.removed_embed, ephemeral=True)
                    else:
                        await interaction.user.add_roles(role)
                        await interaction.response.send_message(embed=self.added_embed, ephemeral=True)
        except Exception as e:
            print(e)
            

async def setup(bot):
    await bot.add_cog(OwnHelpCog(bot))
