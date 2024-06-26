import discord
from discord.ext import commands
from datetime import datetime, timedelta
import time
import asyncio
import aiosqlite
import requests
        
# Misc Commands Class
class MiscCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # Creating table on startup   
    @commands.Cog.listener()
    async def on_ready(self):
        await self.create_todo_table()
        await self.create_remind_table()
    
    async def create_todo_table(self):
        async with aiosqlite.connect("dbs/todo.db") as db:
            await db.execute('''
                CREATE TABLE IF NOT EXISTS todos (
                    user_id INTEGER, 
                    todo TEXT
                )
            ''')
            await db.commit()

    async def create_remind_table(self):
        async with aiosqlite.connect("dbs/remind.db") as db:
            await db.execute('DROP TABLE IF EXISTS reminders')
            await db.execute('''
                CREATE TABLE IF NOT EXISTS reminders (
                    user_id INTEGER,
                    time TEXT,
                    task TEXT
                )
            ''')
            await db.commit()
    
    # WhoIs Command
    @commands.hybrid_command(description="Sends information about a user")
    async def whois(self, ctx, user:discord.Member):
        e = discord.Embed(color=0xc700ff)
        e.set_author(name=f"Gathering Information..."),
        if user.avatar:
            e.set_thumbnail(url=user.avatar.url)
        e.add_field(name="📍 Mention", value=user.mention)
        e.add_field(name="🔖 ID", value=user.id)
        e.add_field(name="📑 Nickname", value=user.display_name)
        e.add_field(name="📅 Created On", value=user.created_at.strftime("`%B %d, %Y %H:%M %p`"))
        e.add_field(name="📅 Joined On", value=user.joined_at.strftime("`%B %d, %Y %H:%M %p`"))
        if user.premium_since:
            e.add_field(name=f"<a:DiscordBoost:1121298549657829436> Boosting", value=user.premium_since.strftime("`%B %d, %Y %H:%M %p`"))
        e.add_field(name="👑 Top Role", value=user.top_role.mention)
        e.add_field(name="🎲 Activity", value=f"{user.activity.name}" if user.activity is not None else None)
        emotes = {
            "hypesquad_brilliance": "<:HypeSquadBrilliance:1123772502024405053>",
            "hypesquad_bravery": "<:HypeSquadBravery:1123772444994437240>",
            "hypesquad_balance": "<:HypeSquadBalance:1123772443069259897>",
            "bug_hunter": "<:BugHunter:1123772432679981057>",
            "bug_hunter_level_2": "<:BugHunterLevel2:1123772435150422086>",
            "early_verified_bot_developer": "<:EarlyVerifiedBotDeveloper:1123772440338776064>",
            "verified_bot_developer": "<:EarlyVerifiedBotDeveloper:1123772440338776064>",
            "active_developer": "<:ActiveDeveloper:1123772429307744287>",
            "hypesquad": "<:HypeSquadEvents:1123772447125155963>",
            "early_supporter": "<:EarlySupporter:1123772438380019762>",
            "discord_certified_moderator": "<:ModeratorProgramsAlumni:1123772518365409370>",
            "staff": "<:Staff:1123772450430267393>",
            "partner": "<:Partner:1123774032932769812>",
        }
        badges = [
            emoji
            for f in user.public_flags.all()
            if (emoji := emotes.get(f.name))
        ]
        if badges:
            e.add_field(name="🧬 Flags", value=" ".join(badges))
        else:
            e.add_field(name="🧬 Flags", value="None")
        e.add_field(name="🤖 Bot?", value=user.bot)
        if user.status != user.mobile_status:
            e.add_field(name="📺 Device", value="Desktop")
        elif user.status != user.desktop_status:
            e.add_field(name="📺 Device", value="Mobile")
        req = await self.bot.http.request(discord.http.Route("GET", "/users/{uid}", uid=user.id))
        banner_id = req["banner"]
        if banner_id:
            banner_url = f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}?size=1024"
            e.add_field(name="📰 Banner", value="**Linked Below**")
            e.set_image(url=banner_url)
        else:
            e.add_field(name="📰 Banner", value="None")
        e.set_footer(text=f"Requested by {ctx.author}"),
        e.timestamp = datetime.utcnow()
        await ctx.send(embed=e)

    # Snipe Events
    sniped_message = None
    
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.author.bot:
            return
        global sniped_message
        sniped_message = message
        
    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if before.author.bot: 
            return
        global sniped_message
        sniped_message = before
    
    # Snipe Command
    @commands.hybrid_command(description="Sends the most recent deleted or edited message")
    async def snipe(self, ctx):
        try:
            global sniped_message
            if sniped_message is None:
                await ctx.send("There are no recently deleted messages to snipe.")
                return
            e = discord.Embed(color=0xc700ff)
            if sniped_message.content:
                e.set_author(name=sniped_message.author.name, icon_url=sniped_message.author.avatar.url)
                e.description = f"> {sniped_message.content}"
                await ctx.send(embed=e)
            elif sniped_message.attachments:
                attachment_url = sniped_message.attachments[0].url
                e.set_author(name=sniped_message.author.name)
                e.set_image(url=attachment_url)
                await ctx.send(embed=e)
            sniped_message = None
        except Exception as e:
            print(e)
    
    # ClimateClock Command
    @commands.hybrid_command(description="Check the Climate Clock")
    async def climateclock(self, ctx):
        url = 'https://api.climateclock.world/v2/clock.json'
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                modules = data.get('data', {}).get('modules', {})
                module_info = modules.get('carbon_deadline_1', None)
                if module_info:
                    module_type = module_info.get('type')
                    module_flavor = module_info.get('flavor')
                    module_description = module_info.get('description')
                    countdown_timestamp = module_info.get('timestamp')
                    countdown_datetime = datetime.fromisoformat(countdown_timestamp.replace('Z', '+00:00')).replace(tzinfo=None)
                    current_datetime = datetime.utcnow()
                    remaining_time = countdown_datetime - current_datetime
                    years = remaining_time.days // 365
                    days = remaining_time.days % 365
                    hours, remainder = divmod(remaining_time.seconds, 3600)
                    minutes, seconds = divmod(remainder, 60)
                    e = discord.Embed(
                        title='⛅️ Climate Clock ⛅️',
                        description=f'[**Climate Clock**](<https://climateclock.world>) shows the time left until irreversible **1.5°C** global temperature rise is reached\n\n'
                                    f'> 📅 {years}**Y** {days}**D** \n'
                                    f'> ⏳ {hours}**H** {minutes}**M** {seconds}**S**',
                        color=0xc700ff
                    )
                    e.set_thumbnail(url='https://media.discordapp.net/attachments/807071768258805764/1252424739788427374/favicon.png?ex=66722aee&is=6670d96e&hm=f3f945285aa7be06be8474376e4b8a05263d4a615ae7fe9d4f46878b2b66d89c&=&format=webp&quality=lossless')
                    e.timestamp = datetime.utcnow()
                    await ctx.send(embed=e)
                else:
                    print("Couldn't find information for the carbon deadline module.")
            else:
                print(f'Failed to fetch data from Climate Clock API. Status code: {response.status_code}')
        except Exception as e:
            print(f'Error fetching data from Climate Clock API: {e}')

    # Deathnote Help Command
    @commands.hybrid_command(description="Sends the options for the deathnote command")
    async def deathhelp(self, ctx):
        e = discord.Embed(color=0xc700ff)
        e.set_author(name="☠️ Available Death Methods ☠️")
        e.add_field(
            name="__Death Options__",
            value=f"\n> 🗻 Cliff"
                  f"\n> 🚝 Train"
                  f"\n> 🏊🏼 Drown"
                  f"\n> 🗿 Crush"
                  f"\n> 🌭 Choke"
                  f"\n> 🚗 Car Crash"
                  f"\n> 🔪 Murder"
                  f"\n> ⚡️ Shock"
                  f"\n> 🔥 Fire"
                  f"\n> 💥 Explosion"
                  f"\n> 🌩 Lightning"
                  f"\n> 🌋 Volcano"
                  f"\n> 🌪 Tornado"
                  f"\n> 🧱 Earthquake"
                  f"\n> 🌊 Hurricane",
        )
        e.set_footer(text=f"Requested by {ctx.author}"),
        e.timestamp = datetime.utcnow()
        await ctx.send(embed=e)
        
    # Remind Command
    @commands.hybrid_command(description="Set a reminder")
    async def remind(self, ctx, time, *, task):
        def convert(time):
            pos = ['s', 'm', 'h', 'd']
            time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600*24}
            unit = time[-1]
            if unit not in pos:
                return -1
            try:
                val = int(time[:-1])
            except:
                return -2
            return val * time_dict[unit]

        converted_time = convert(time)
        if converted_time == -1:
            await ctx.send("You didn't input the time correctly!")
            return
        if converted_time == -2:
            await ctx.send("The time must be an integer!")
            return

        # Timer Embed
        e = discord.Embed(color=0xc700ff)
        e.description = "⏰ **Started Reminder** ⏰"
        e.add_field(name="Time", value=time)
        e.add_field(name="Task", value=task)
        e.set_footer(text=f"Requested by {ctx.author}")
        e.timestamp = datetime.utcnow()
        await ctx.send(embed=e)

        # Save reminder to database
        try:
            async with aiosqlite.connect("dbs/remind.db") as db:
                await db.execute("INSERT INTO reminders (user_id, time, task) VALUES (?, ?, ?)", (ctx.author.id, time, task))
                await db.commit()
        except Exception as e:
            print(e)

        # End Timer Embed
        await asyncio.sleep(converted_time)
        e = discord.Embed(color=0xc700ff)
        e.description = "⏰ **Time's Up** ⏰"
        e.add_field(name="Task", value=f"> {task}")
        await ctx.send(ctx.author.mention, embed=e)

        # Remove reminder from database
        try:
            async with aiosqlite.connect("dbs/remind.db") as db:
                await db.execute("DELETE FROM reminders WHERE user_id = ? AND time = ? AND task = ?", (ctx.author.id, time, task))
                await db.commit()
        except Exception as e:
            print(e)

    # Remind List Command
    @commands.hybrid_command(description="List all your reminders")
    async def remindlist(self, ctx):
        try:
            author_id = ctx.author.id
            async with aiosqlite.connect("dbs/remind.db") as db:
                cursor = await db.execute("SELECT time, task FROM reminders WHERE user_id = ?", (author_id,))
                reminders = await cursor.fetchall()
            if not reminders:
                await ctx.send(f"**{ctx.author.name}** has no reminders set!", ephemeral=True)
            else:
                reminders_list = "\n".join([f"- ⏳ {time} **|** {task}" for time, task in reminders])
                e = discord.Embed(color=0xc700ff)
                e.set_author(name=f"📋 {ctx.author.name}'s Reminders 📋")
                e.description = reminders_list
                await ctx.send(embed=e, ephemeral=True)
        except Exception as e:
            print(e)
        
    # Todo Add Command
    @commands.hybrid_command(description="Add a task to your to-do list")
    async def todoadd(self, ctx, *, task):
        author_id = ctx.author.id
        async with aiosqlite.connect("dbs/todo.db") as db:
            await db.execute("INSERT INTO todos (user_id, todo) VALUES (?, ?)", (author_id, task))
            await db.commit()
        await ctx.send(f"Added **{task}** to your todo list!", ephemeral=True)
    
    # Todo Del Command
    @commands.hybrid_command(description="Remove a task from your to-do list")
    async def tododel(self, ctx, todo_num: int):
        author_id = ctx.author.id
        async with aiosqlite.connect("dbs/todo.db") as db:
            cursor = await db.execute("SELECT rowid, todo FROM todos WHERE user_id = ?", (author_id,))
            rows = await cursor.fetchall()
            if todo_num <= 0 or todo_num > len(rows):
                await ctx.send("Invalid todo number!", ephemeral=True)
                return
            todo_id, todo_text = rows[todo_num - 1]
            await db.execute("DELETE FROM todos WHERE rowid = ?", (todo_id,))
            await db.commit()
        await ctx.send(f"Removed **{todo_text}** from your todo list!", ephemeral=True)
    
    # Todo Clear Command
    @commands.hybrid_command(description="Clear all tasks from your to-do list")
    async def todoclear(self, ctx):
        author_id = ctx.author.id
        async with aiosqlite.connect("dbs/todo.db") as db:
            await db.execute("DELETE FROM todos WHERE user_id = ?", (author_id,))
            await db.commit()
        await ctx.send("Cleared all tasks from your todo list!", ephemeral=True)
    
    # Todo List Command
    @commands.hybrid_command(description="Look at your to-do list")
    async def todolist(self, ctx):
        author_id = ctx.author.id
        async with aiosqlite.connect("dbs/todo.db") as db:
            cursor = await db.execute("SELECT todo FROM todos WHERE user_id = ?", (author_id,))
            todos = await cursor.fetchall()
        if not todos:
            await ctx.send(f"**{ctx.author.name}** has no tasks in their todo list!", ephemeral=True)
        else:
            todo_list = "\n".join([f"> **{idx + 1})** {todo[0]}" for idx, todo in enumerate(todos)])
            e = discord.Embed(color=0xc700ff)
            e.set_author(name=f"📋 {ctx.author.name}'s Todo List 📋")
            e.description = todo_list
            await ctx.send(embed=e, ephemeral=True)
        
    # Emoji Steal Command
    @commands.hybrid_command(description="Get the file link to an emoji")
    async def esteal(self, ctx, emoji: discord.PartialEmoji):
        if emoji.id:
            emoji_url = emoji.url
            await ctx.send(f":link: {emoji_url}")
        else:
            await ctx.send("Please provide a custom emoji.")
        

async def setup(bot):
    await bot.add_cog(MiscCog(bot))
