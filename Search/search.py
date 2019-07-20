import discord
from discord.ext import commands

class search(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.errorcolor = 0xFF2B2B
        self.blurple = 0x7289DA

    #Google search command
    @commands.command()
    async def google(self, ctx, *, search = None):
        if search == None:
            embed = discord.Embed(
                title = "Google Search Error",
                description = "Please provide something to search!",
                color = self.errorcolor
            )
            await ctx.send(embed = embed)
        else:
            embed = discord.Embed(
                title = f"**{search}**",
                color = self.blurple,
                url = f"https://www.google.com/search?q={search}"
            )
            embed.set_author(name = "Google Search", icon_url = "https://cdn.discordapp.com/attachments/600914805619949588/601930101952741377/google-logo-icon-PNG-Transparent-Background-768x768.png")
            await ctx.send(embed = embed)

    #Youtube search command
    @commands.command()
    async def youtube(self, ctx, *, search = None):
        if search == None:
            embed = discord.Embed(
                title = "Youtube Search Error",
                description = "Please provide something to search!",
                color = self.errorcolor
            )
            await ctx.send(embed = embed)
        else:
            embed = discord.Embed(
                title = f"**{search}**",
                color = self.blurple,
                url = f"https://www.youtube.com/results?search_query={search}"
            )
            embed.set_author(name = "Youtube Search", icon_url = "https://cdn.discordapp.com/attachments/600914805619949588/601931433879273482/social-youtube-circle-512.png")
            await ctx.send(embed = embed)

    #Webster search command
    @commands.command()
    async def webster(self, ctx, *, search = None):
        if search == None:
            embed = discord.Embed(
                title = "Webster Search Error",
                description = "Please provide something to search!",
                color = self.errorcolor
            )
            await ctx.send(embed = embed)
        else:
            embed = discord.Embed(
                title = f"**{search}**",
                color = self.blurple,
                url = f"https://www.merriam-webster.com/dictionary/{search}"
            )
            embed.set_author(name = "Youtube Search", icon_url = "https://cdn.discordapp.com/attachments/600914805619949588/601932002522038283/1200px-Merriam-Webster_logo.png")
            await ctx.send(embed = embed)

    @commands.command()
    async def webster(self, ctx, *, search = None):
        if search == None:
            embed = discord.Embed(
                title = "Webster Search Error",
                description = "Please provide something to search!",
                color = self.errorcolor
            )
            await ctx.send(embed = embed)
        else:
            embed = discord.Embed(
                title = f"**{search}**",
                color = self.blurple,
                url = f"https://www.merriam-webster.com/dictionary/{search}"
            )
            embed.set_author(name = "Webster's Search")
            await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(search(bot))
