import discord
from discord.ext import commands
from datetime import datetime
from cogs.greetings import Greeting
from cogs.Users import Users
from config import DISCORD_TOKEN
codename = commands.Bot(command_prefix = "/", description="Codename-0Bot",
                        activity=discord.Activity(type= discord.ActivityType.playing, name="vibin on codename"))
@codename.event
async def on_ready():
    print(f"Codenames logged in as: {codename.user.name} id: {codename.user.id}, at: {datetime.now()}")
codename.add_cog(Greeting(codename))
codename.add_cog(Users(codename))
codename.run(DISCORD_TOKEN)
