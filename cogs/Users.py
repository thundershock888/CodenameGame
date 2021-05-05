import discord

from discord.ext import commands

import json


# user id (unchanging)
# game instance ids
# role in each game

# """
# {
#     user id (string) : [
#         (game id (string), role in game),
#         ...
#     ],
#     next user ...
# }
# """


class Users(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        with open("./data/users.json") as file:
            self.user_profiles = json.load(file)

    @commands.command(aliases=["plays", "count"])
    async def get_play_count(self, ctx: commands.Context, player_id: int = None):
        desired_player_id = player_id or ctx.author.id
        player_profile = self.user_profiles.get(str(desired_player_id), [])
        num_games = len(player_profile)
        await ctx.send(f"{desired_player_id} is in {num_games} games!")