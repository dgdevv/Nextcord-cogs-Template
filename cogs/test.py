import nextcord
from nextcord.ext import commands

from main import GUILD_ID

class testing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @nextcord.slash_command(guild_ids=[GUILD_ID], description="Test command", name="test")
    async def test(self, interaction: nextcord.Interaction):
        await interaction.response.send_message("HIII")

def setup(bot):
    bot.add_cog(testing(bot))