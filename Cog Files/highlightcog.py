import re
import discord
from discord.ext import commands
import aiosqlite
from datetime import datetime

class HighlightCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def create_user_table(self):
        async with aiosqlite.connect("dbs/highlight.db") as db:
            await db.execute("""
                CREATE TABLE IF NOT EXISTS user_highlights (
                    user_id INTEGER PRIMARY KEY,
                    word_list TEXT,
                    ignored_channels TEXT,
                    ignored_users TEXT
                )
            """)
            await db.commit()

    async def get_user_data(self, user_id):
        await self.create_user_table()
        async with aiosqlite.connect("dbs/highlight.db") as db:
            async with db.execute("SELECT word_list, ignored_channels, ignored_users FROM user_highlights WHERE user_id = ?", (user_id,)) as cursor:
                row = await cursor.fetchone()
                if row:
                    return row[0], row[1], row[2]
                else:
                    return "", "", ""

    async def update_user_data(self, user_id, word_list, ignored_channels, ignored_users):
        await self.create_user_table()
        async with aiosqlite.connect("dbs/highlight.db") as db:
            await db.execute("""
                INSERT OR REPLACE INTO user_highlights (user_id, word_list, ignored_channels, ignored_users)
                VALUES (?, ?, ?, ?)
            """, (user_id, word_list, ignored_channels, ignored_users))
            await db.commit()
    
    @commands.hybrid_command(description="Add default words to your highlight list")
    async def defaulthighlights(self, ctx):
        if discord.utils.get(ctx.author.roles, name="🧸 Officer"):
            try:
                default_words = {"nigger", "nigga", "faggot", "fag", "kys"}
                await self.create_user_table()
                word_list, ignored_channels, ignored_users = await self.get_user_data(ctx.author.id)
                existing_words = set(word_list.split(',')) if word_list else set()
                if default_words.issubset(existing_words):
                    await ctx.send("Those words are already in your list!")
                else:
                    updated_words = existing_words.union(default_words)
                    await self.update_user_data(ctx.author.id, ','.join(updated_words), ignored_channels, ignored_users)
                    await ctx.send("Added default words to your highlight list!")
            except Exception as e:
                print(e)
        else:
            e = discord.Embed(color=0xc700ff)
            e.description = "🚨 That is a **Staff** command! You don't have the required perms! 🚨"
            await ctx.send(embed=e)

    @commands.hybrid_command(description="Add a word to your highlight list")
    async def highlightadd(self, ctx, *, word: str = None):
        if discord.utils.get(ctx.author.roles, name="🧸 Officer"):
            try:
                word = word.lower()
                await self.create_user_table()
                word_list, ignored_channels, ignored_users = await self.get_user_data(ctx.author.id)
                words = word_list.split(',') if word_list else []
                if word not in words:
                    words.append(word)
                    await self.update_user_data(ctx.author.id, ','.join(words), ignored_channels, ignored_users)
                    await ctx.send(f"Added **{word}** to your highlight list!")
                else:
                    await ctx.send(f"`**{word}**` is already in your highlight list!")
            except Exception as e:
                print(e)
        else:
            e = discord.Embed(color=0xc700ff)
            e.description = "🚨 That is a **Staff** command! You don't have the required perms! 🚨"
            await ctx.send(embed=e)

    @commands.hybrid_command(description="Remove a word from your highlight list")
    async def highlightremove(self, ctx, *, word: str = None):
        if discord.utils.get(ctx.author.roles, name="🧸 Officer"):
            try:
                word = word.lower()
                await self.create_user_table()
                word_list, ignored_channels, ignored_users = await self.get_user_data(ctx.author.id)
                words = word_list.split(',') if word_list else []
                if word in words:
                    words.remove(word)
                    await self.update_user_data(ctx.author.id, ','.join(words), ignored_channels, ignored_users)
                    await ctx.send(f"Removed **{word}** from your highlight list!")
                else:
                    await ctx.send(f"`**{word}**` is not in your highlight list!")
            except Exception as e:
                print(e)
        else:
            e = discord.Embed(color=0xc700ff)
            e.description = "🚨 That is a **Staff** command! You don't have the required perms! 🚨"
            await ctx.send(embed=e)

    @commands.hybrid_command(description="Clear your highlighted word list")
    async def highlightclear(self, ctx):
        if discord.utils.get(ctx.author.roles, name="🧸 Officer"):
            try:
                await self.create_user_table()
                _, ignored_channels, ignored_users = await self.get_user_data(ctx.author.id)
                await self.update_user_data(ctx.author.id, "", ignored_channels, ignored_users)
                await ctx.send("Cleared your highlight list.")
            except Exception as e:
                print(e)
        else:
            e = discord.Embed(color=0xc700ff)
            e.description = "🚨 That is a **Staff** command! You don't have the required perms! 🚨"
            await ctx.send(embed=e)

    @commands.hybrid_command(description="Block a user or channel from your highlight list")
    async def highlightblock(self, ctx, *, item: str):
        if discord.utils.get(ctx.author.roles, name="🧸 Officer"):
            try:
                await self.create_user_table()
                word_list, ignored_channels, ignored_users = await self.get_user_data(ctx.author.id)
                id_match = re.search(r'\d+', item)
                if id_match:
                    item_id = int(id_match.group(0))
                    channel = self.bot.get_channel(item_id)
                    user = self.bot.get_user(item_id)
                    if channel:
                        ignored_channels_list = ignored_channels.split(',') if ignored_channels else []
                        if str(item_id) not in ignored_channels_list:
                            ignored_channels_list.append(str(item_id))
                            await self.update_user_data(ctx.author.id, word_list, ','.join(ignored_channels_list), ignored_users)
                            await ctx.send(f"Blocked channel <#{item_id}>!")
                        else:
                            await ctx.send(f"Channel <#{item_id}> is already blocked!")
                    elif user:
                        ignored_users_list = ignored_users.split(',') if ignored_users else []
                        if str(item_id) not in ignored_users_list:
                            ignored_users_list.append(str(item_id))
                            await self.update_user_data(ctx.author.id, word_list, ignored_channels, ','.join(ignored_users_list))
                            await ctx.send(f"Blocked user <@{item_id}>!")
                        else:
                            await ctx.send(f"User <@{item_id}> is already blocked!")
                    else:
                        await ctx.send("Invalid user or channel mention.")
                else:
                    await ctx.send("Invalid user or channel mention.")
            except Exception as e:
                print(e)
        else:
            e = discord.Embed(color=0xc700ff)
            e.description = "🚨 That is a **Staff** command! You don't have the required perms! 🚨"
            await ctx.send(embed=e)

    @commands.hybrid_command(description="Unblock a user or channel from your highlight list")
    async def highlightunblock(self, ctx, *, item: str):
        if discord.utils.get(ctx.author.roles, name="🧸 Officer"):
            try:
                await self.create_user_table()
                word_list, ignored_channels, ignored_users = await self.get_user_data(ctx.author.id)
                id_match = re.search(r'\d+', item)
                if id_match:
                    item_id = int(id_match.group(0))
                    channel = self.bot.get_channel(item_id)
                    user = self.bot.get_user(item_id)
                    if channel:
                        ignored_channels_list = ignored_channels.split(',') if ignored_channels else []
                        if str(item_id) in ignored_channels_list:
                            ignored_channels_list.remove(str(item_id))
                            await self.update_user_data(ctx.author.id, word_list, ','.join(ignored_channels_list), ignored_users)
                            await ctx.send(f"Unblocked channel <#{item_id}>!")
                        else:
                            await ctx.send(f"Channel `<#{item_id}>` is not blocked!")
                    elif user:
                        ignored_users_list = ignored_users.split(',') if ignored_users else []
                        if str(item_id) in ignored_users_list:
                            ignored_users_list.remove(str(item_id))
                            await self.update_user_data(ctx.author.id, word_list, ignored_channels, ','.join(ignored_users_list))
                            await ctx.send(f"Unblocked user <@{item_id}>!")
                        else:
                            await ctx.send(f"User <@{item_id}> is not blocked!")
                    else:
                        await ctx.send("Invalid user or channel mention.")
                else:
                    await ctx.send("Invalid user or channel mention.")
            except Exception as e:
                print(e)
        else:
            e = discord.Embed(color=0xc700ff)
            e.description = "🚨 That is a **Staff** command! You don't have the required perms! 🚨"
            await ctx.send(embed=e)

    @commands.hybrid_command(description="Show your highlight list")
    async def highlightshow(self, ctx):
        if discord.utils.get(ctx.author.roles, name="🧸 Officer"):
            try:
                await self.create_user_table()
                word_list, ignored_channels, ignored_users = await self.get_user_data(ctx.author.id)
                words = word_list.split(',') if word_list else []
                channels = ignored_channels.split(',') if ignored_channels else []
                users = ignored_users.split(',') if ignored_users else []
                user = self.bot.get_user(ctx.author.id)
                username = user.name if user else "Unknown User"
                e = discord.Embed(title=f"🔍 {username}'s Highlight List 🔍", color=0xc700ff)
                e.add_field(name="📑 Words", value='\n'.join([f"> - {word}" for word in words]) if words else "None", inline=False)
                e.add_field(name="📰 Blocked Channels", value='\n'.join([f"> - <#{channel}>" for channel in channels]) if channels else "None", inline=False)
                e.add_field(name="👤 Blocked Users", value='\n'.join([f"> - <@{user}>" for user in users]) if users else "None", inline=False)
                await ctx.send(embed=e)
            except Exception as e:
                print(e)
        else:
            e = discord.Embed(color=0xc700ff)
            e.description = "🚨 That is a **Staff** command! You don't have the required perms! 🚨"
            await ctx.send(embed=e)

    @commands.Cog.listener()
    async def on_message(self, message):
        try:
            if message.author.bot:
                return
            async with aiosqlite.connect("dbs/highlight.db") as db:
                async with db.execute("SELECT user_id FROM user_highlights") as cursor:
                    user_ids = await cursor.fetchall()
            for user_id in user_ids:
                user_id = user_id[0]
                word_list, ignored_channels, ignored_users = await self.get_user_data(user_id)
                words = word_list.split(',') if word_list else []
                ignored_channel_ids = [int(cid) for cid in ignored_channels.split(',')] if ignored_channels else []
                ignored_user_ids = [int(uid) for uid in ignored_users.split(',')] if ignored_users else []
                if message.channel.id in ignored_channel_ids or message.author.id in ignored_user_ids:
                    continue
                content = message.clean_content.lower()
                for word in words:
                    if word in content:
                        user = self.bot.get_user(user_id)
                        if user:
                            e = discord.Embed(title=f"🚨 Word Mentioned 🚨", description=f"`{word}` was mentioned!", color=0xc700ff, timestamp=datetime.utcnow())
                            e.add_field(name="👤 Mentioned By", value=f"> {message.author.mention}", inline=False)
                            e.add_field(name="🔗 Jump Link", value=f"> [Message]({message.jump_url})", inline=False)
                            await user.send(embed=e)
                        break
        except Exception as e:
            print(e)

async def setup(bot):
    await bot.add_cog(HighlightCog(bot))
