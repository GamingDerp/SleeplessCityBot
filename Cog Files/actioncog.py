import discord
from discord.ext import commands
import random

# Bot Owner User ID
owner_id = 532706491438727169

# Action Commands Class
class ActionCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Sniff Command
    @commands.hybrid_command(description="Sniff another user")
    async def sniff(self, ctx, user:discord.Member):
        e = discord.Embed(color=0xc700ff)
        e.description = f"{ctx.author.mention} sniffs {user.mention}!"
        e.set_image(url="https://media.discordapp.net/attachments/807071768258805764/1131013212331069551/SniffingGif.gif"),
        await ctx.send(embed=e)
    
    # Bite Command
    @commands.hybrid_command(description="Bite another user")
    async def bite(self, ctx, user:discord.Member):
        e = discord.Embed(color=0xc700ff)
        e.description = f"{ctx.author.mention} bites {user.mention}!"
        bitegifs = [
            "https://media.discordapp.net/attachments/807071768258805764/1131664029052588122/AnimeBite3.gif", 
            "https://media.discordapp.net/attachments/807071768258805764/1131664029505556561/AnimeBite1.gif", 
            "https://media.discordapp.net/attachments/807071768258805764/1131664029929189516/AnimeBite2.gif"
        ]
        e.set_image(url=random.choice(bitegifs)),
        await ctx.send(embed=e)
    
    # Bonk Command
    @commands.hybrid_command(description="Bonk another user")
    async def bonk(self, ctx, user:discord.Member):
        e = discord.Embed(color=0xc700ff)
        e.description = f"{ctx.author.mention} bonks {user.mention}!"
        bonkgifs = [
            "https://media.discordapp.net/attachments/807071768258805764/1109240042238513233/BonkGif.gif", 
            "https://media.discordapp.net/attachments/807071768258805764/1124387823076769863/Bonk2Gif.gif"
        ]
        e.set_image(url=random.choice(bonkgifs)),
        await ctx.send(embed=e)
        
    # Vomit Command
    @commands.hybrid_command(description="Vomit on another user")
    async def vomit(self, ctx, user:discord.Member):
        e = discord.Embed(color=0xc700ff)
        e.description = f"{ctx.author.mention} vomits on {user.mention}!"
        vomitgifs = [
            "https://media.discordapp.net/attachments/807071768258805764/1131015043379626144/VomitGif.gif",
            "https://media.discordapp.net/attachments/807071768258805764/1135341052065234964/VomitGif2.gif"
        ]
        e.set_image(url=random.choice(vomitgifs)),
        await ctx.send(embed=e)

    # Slap Command
    @commands.hybrid_command(description="Slap another user")
    async def slap(self, ctx, user:discord.Member):
        e = discord.Embed(color=0xc700ff)
        e.description = f"{ctx.author.mention} slaps {user.mention}!"
        e.set_image(url="https://media.discordapp.net/attachments/807071768258805764/1106847432907685928/AnimeSlappingGif.gif"),
        await ctx.send(embed=e)
        
    # Punch Command
    @commands.hybrid_command(description="Punch another user")
    async def punch(self, ctx, user:discord.Member):
        e = discord.Embed(color=0xc700ff)
        e.description = f"{ctx.author.mention} punches {user.mention}!"
        e.set_image(url="https://media.discordapp.net/attachments/807071768258805764/1131018538577039390/PunchingGif.gif"),
        await ctx.send(embed=e)

    # Throw Command
    @commands.hybrid_command(description="Throw another user")
    async def throw(self, ctx, user:discord.Member):
        e = discord.Embed(color=0xc700ff)
        e.description = f"{ctx.author.mention} throws {user.mention} off a cliff!"
        e.set_image(url="https://media.discordapp.net/attachments/807071768258805764/1116579751897878558/ThrowGif.gif"),
        await ctx.send(embed=e)
        
    # Stalk Command
    @commands.hybrid_command(description="Stalk another user")
    async def stalk(self, ctx, user:discord.Member):
        chance_response = ["they got caught", "they didn't get caught"]
        choice = random.choice(chance_response)
        e = discord.Embed(color=0xc700ff)
        e.description = f"{ctx.author.mention} stalks {user.mention} and {choice}!"
        if choice == "they got caught":
            e.set_image(url="https://cdn.discordapp.com/attachments/807071768258805764/1131011194325569616/CaughtStalkingGif.gif")
        else:
            e.set_image(url="https://media.discordapp.net/attachments/807071768258805764/1131011165644922940/StalkingGif.gif")
        await ctx.send(embed=e)

    # Kidnap Command
    @commands.hybrid_command(description="Kidnap another user")
    async def kidnap(self, ctx, user:discord.Member):
        e = discord.Embed(color=0xc700ff)
        e.description = f"{ctx.author.mention} kidnaps {user.mention}!"
        e.set_image(url="https://media.discordapp.net/attachments/807071768258805764/1107074673361047673/AnimeKidnapGif.gif"),
        await ctx.send(embed=e)
    
    # Punt Command
    @commands.hybrid_command(description="Punt another user")
    async def punt(self, ctx, user:discord.Member):
        e = discord.Embed(color=0xc700ff)
        e.description = f"{ctx.author.mention} punts {user.mention}!"
        e.set_image(url="https://cdn.discordapp.com/attachments/807071768258805764/1123844694888165417/KickGif.gif"),
        await ctx.send(embed=e)

    # Strangle Command
    @commands.hybrid_command(description="Strangle another user")
    async def strangle(self, ctx, user:discord.Member):
        strangle_response = ["they crush their windpipes, killing them! RIP ☠️", f"causes them to faint!", f"they're hands slip, {user.mention} gets away!", f"they grab at {ctx.author.mention}, strangling them back!"]
        strangle_owner_response = ["it kills them! RIP ☠️", f"causes {user.mention} to faint!"]
    
        if ctx.message.author.id == owner_id:
            e = discord.Embed(color=0xc700ff)
            e.description = f"{ctx.author.mention} strangles {user.mention} and {random.choice(strangle_owner_response)}"
            e.set_image(url="https://cdn.discordapp.com/attachments/807071768258805764/1108639607370813440/AnimeStranglingGif.gif"),
            await ctx.send(embed=e)
        else:
            e = discord.Embed(color=0xc700ff)
            e.description = f"{ctx.author.mention} strangles {user.mention} and {random.choice(strangle_response)}"
            e.set_image(url="https://cdn.discordapp.com/attachments/807071768258805764/1108639607370813440/AnimeStranglingGif.gif"),
            await ctx.send(embed=e)
        
    # Stab Command
    @commands.hybrid_command(description="Stab another user")
    async def stab(self, ctx, user:discord.Member):
        stab_response = ["it kills them! RIP ☠️", "they bleed out! RIP ☠️","they missed!", f"due to their momentum, the knife comes back and stabs {ctx.author.mention}!"]
        stab_owner_response = ["it kills them! RIP ☠️", f"{user.mention} bleeds out! RIP ☠️"]
    
        if ctx.message.author.id == owner_id:
            e = discord.Embed(color=0xc700ff)
            e.description = f"{ctx.author.mention} stabs {user.mention} and {random.choice(stab_owner_response)}"
            e.set_image(url="https://media.discordapp.net/attachments/807071768258805764/1106846955612684308/AnimeStabbingGif.gif"),
            await ctx.send(embed=e)
        else:
            e = discord.Embed(color=0xc700ff)
            e.description = f"{ctx.author.mention} stabs {user.mention} and {random.choice(stab_response)}"
            e.set_image(url="https://media.discordapp.net/attachments/807071768258805764/1106846955612684308/AnimeStabbingGif.gif"),
            await ctx.send(embed=e)
    
    # Shoot Command
    @commands.hybrid_command(description="Shoot another user")
    async def shoot(self, ctx, user:discord.Member):
        shoot_response = ["it kills them! RIP ☠️", "it goes straight through their skull! RIP ☠️","it does nothing! They have a body of steel!", f"it ricochets off the wall and kills {ctx.author.mention}! RIP ☠️", "the gun jams!"]
        shoot_owner_response = ["it kills them! RIP ☠️", "it goes straight through their skull! RIP ☠️"]
    
        if ctx.message.author.id == owner_id:
            e = discord.Embed(color=0xc700ff)
            e.description = f"{ctx.author.mention} shoots at {user.mention} and {random.choice(shoot_owner_response)}"
            e.set_image(url="https://cdn.discordapp.com/attachments/807071768258805764/1106843019321282591/AnimeShootingGif.gif"),
            await ctx.send(embed=e)
        else:
            e = discord.Embed(color=0xc700ff)
            e.description = f"{ctx.author.mention} shoots at {user.mention} and {random.choice(shoot_response)}"
            e.set_image(url="https://cdn.discordapp.com/attachments/807071768258805764/1106843019321282591/AnimeShootingGif.gif"),
            await ctx.send(embed=e)
            
    # Deathnote Command
    @commands.hybrid_command(description="Choose how another user dies")
    async def deathnote(self, ctx, user:discord.Member, *, arg):
        deaths = {
            "cliff": ("fell off a cliff and died!", "https://media.discordapp.net/attachments/807071768258805764/1116815474852896890/FallOffCliffGif.gif"),
            "train": ("got ran over by a train and died!", "https://media.discordapp.net/attachments/807071768258805764/1116814851403165726/HitByTrainGif.gif"),
            "drown": ("drowned in a 2-inch pool and died!", "https://media.discordapp.net/attachments/807071768258805764/1116822537272316004/DrowningGif.gif"),
            "crush": ("was crushed by a boulder and died!", "https://media.discordapp.net/attachments/807071768258805764/1116944054052204584/CrushedByBoulderGif.gif"),
            "choke": ("choked on a hot dog and died!", "https://media.discordapp.net/attachments/807071768258805764/1116944567107854336/ChokingGif.gif"),
            "car crash": ("got into a car crash and died!", "https://media.discordapp.net/attachments/807071768258805764/1116944863032787105/CarCrashGif.gif"),
            "murder": ("was murdered!", "https://media.discordapp.net/attachments/807071768258805764/1116945578954334228/MurderGif.gif"),
            "shock": ("was shocked by 10,000 volts of electricity and died!", "https://media.discordapp.net/attachments/807071768258805764/1117941430439120936/ElectricShockGif.gif"),
            "fire": ("got caught in a fire and died!", "https://media.discordapp.net/attachments/807071768258805764/1116946041422495844/FireGif.gif"),
            "explosion": ("swallowed TNT and exploded!", "https://media.discordapp.net/attachments/807071768258805764/1116946286361456750/ExplodingGif.gif"),
            "lightning": ("got struck by lightning and died!", "https://media.discordapp.net/attachments/807071768258805764/1116946562329882725/LightningGif.gif"),
            "volcano": ("fell into a volcano and died!", "https://media.discordapp.net/attachments/807071768258805764/1116946885542936576/VolcanoGif.gif"),
            "tornado": ("got sucked into a tornado and died!", "https://media.discordapp.net/attachments/807071768258805764/1116947245598781576/TornadoGif.gif"),
            "earthquake": ("fell into a crack made by an earthquake and died!", "https://media.discordapp.net/attachments/807071768258805764/1116947453229404301/EarthquakeGif.gif"),
            "hurricane": ("got washed away in a hurricane and died!", "https://media.discordapp.net/attachments/807071768258805764/1116947898169557002/HurricaneGif.gif"),
        }
        arg = arg.lower()
        if arg in deaths:
            death_description, image_url = deaths[arg]
            e = discord.Embed(color=0xc700ff)
            e.description = f"{user.mention} {death_description} RIP ☠️"
            e.set_image(url=image_url)
            await ctx.send(embed=e)
        else:
            await ctx.send("Invalid death method!")

    # Highfive Command
    @commands.hybrid_command(description="Highfive another user")
    async def highfive(self, ctx, user:discord.Member): 
        e = discord.Embed(color=0xc700ff)
        e.description = f"{ctx.author.mention} highfives {user.mention}!"
        e.set_image(url="https://media.discordapp.net/attachments/807071768258805764/1106851182279934072/AnimeHighfiveGif.gif"),
        await ctx.send(embed=e)

    # Poke Command
    @commands.hybrid_command(description="Poke another user")
    async def poke(self, ctx, user:discord.Member):
        e = discord.Embed(color=0xc700ff)
        e.description = f"{ctx.author.mention} pokes {user.mention}!"
        e.set_image(url="https://media.discordapp.net/attachments/807071768258805764/1117137231950401617/PokeGif.gif"),
        await ctx.send(embed=e)

    # Pat Command
    @commands.hybrid_command(description="Pat another user")
    async def pat(self, ctx, user:discord.Member):
        e = discord.Embed(color=0xc700ff)
        e.description = f"{ctx.author.mention} pats {user.mention}!"
        e.set_image(url="https://cdn.discordapp.com/attachments/807071768258805764/1106851615320846386/AnimePatGif.gif"),
        await ctx.send(embed=e)
    
    # Lick Command
    @commands.hybrid_command(description="Lick another user")
    async def lick(self, ctx, user:discord.Member):
        e = discord.Embed(color=0xc700ff)
        e.description = f"{ctx.author.mention} lick {user.mention}!"
        lickgif = [
            "https://media.discordapp.net/attachments/807071768258805764/1131664016289300532/AnimeLick2.gif", 
            "https://media.discordapp.net/attachments/807071768258805764/1131664016868130978/AnimeLick3.gif", 
            "https://media.discordapp.net/attachments/807071768258805764/1131664017476288582/AnimeLick1.gif"
        ]
        e.set_image(url=random.choice(lickgif)),
        await ctx.send(embed=e)

    # Hug Command
    @commands.hybrid_command(description="Hug another user")
    async def hug(self, ctx, user:discord.Member):  
        e = discord.Embed(color=0xc700ff)
        e.description = f"{ctx.author.mention} hugs {user.mention}!"
        e.set_image(url="https://media.discordapp.net/attachments/807071768258805764/1106847914019536926/AnimeHuggingGif.gif"),
        await ctx.send(embed=e)

    # Kiss Command
    @commands.hybrid_command(description="Kiss another user")
    async def kiss(self, ctx, user:discord.Member):
        e = discord.Embed(color=0xc700ff)
        e.description = f"{ctx.author.mention} kisses {user.mention}!"
        e.set_image(url="https://media.discordapp.net/attachments/807071768258805764/1106848342966800404/AnimeKissingGif.gif"),
        await ctx.send(embed=e)

    # Cuddle Command
    @commands.hybrid_command(description="Cuddle with another user")
    async def cuddle(self, ctx, user:discord.Member): 
        e = discord.Embed(color=0xc700ff)
        e.description = f"{ctx.author.mention} cuddles with {user.mention}!"
        e.set_image(url="https://media.discordapp.net/attachments/807071768258805764/1106848675025666128/AnimeCuddlingGif.gif"),
        await ctx.send(embed=e)


async def setup(bot):
    await bot.add_cog(ActionCog(bot))
