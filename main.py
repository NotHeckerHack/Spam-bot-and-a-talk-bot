import discord
from discord.ext import commands
import random
from discord import Permissions
import asyncio
from threading import Thread
import os
from colorama import init, Fore

client = commands.Bot(command_prefix="%")
token = "Ur bot token"


spam = True

ver = "Daddy bot"

SPAM_MESSAGE = ["DADDDDDDDDDDDS ARE NOISYYYYYYYYYYYYYY"]

@client.command()#spelling errors be like:
async def Error(ctx):#lol
  await ctx.send("Error")
@client.command()
async def send(ctx):
  await ctx.send(ctx.message.content[6:])
 
@client.command()
async def ilovedads(ctx):
  for i in range(20):
    await ctx.send(random.choice(SPAM_MESSAGE))

@client.command()
async def shutup(ctx):
  await client.logout() 
class MyHelp(commands.HelpCommand):
    def get_command_signature(self, command):
        return '' \
               '%s%s %s' % (self.clean_prefix, command.qualified_name, command.signature)

    async def send_bot_help(self, mapping):
        embed = discord.Embed(title=f"Help for dadbot:")
        for cog, commands in mapping.items():
            filtered = await self.filter_commands(commands, sort=True)
            command_signatures = [self.get_command_signature(c) for c in filtered]
            if command_signatures:
                cog_name = getattr(cog, "qualified_name", "Default Commands:")
                embed.add_field(name=cog_name, value="\n".join(command_signatures), inline=False)


        channel = self.context.author
        await channel.send(embed=embed)

    async def on_help_command_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(title="Error", description=str(error))
            await ctx.send(embed=embed)
        else:
            raise error

    async def send_error_message(self, error):
        embed = discord.Embed(title="Error", description=error)
        channel = self.get_destination()
        await channel.send(embed=embed)

    async def send_command_help(self, command):
        embed = discord.Embed(title=self.get_command_signature(command))
        embed.add_field(name="Help", value=command.help)
        alias = command.aliases
        if alias:
            embed.add_field(name="Aliases", value=", ".join(alias), inline=False)

        channel = self.get_destination()
        await channel.send(embed=embed)

client.help_command = MyHelp()

#dayum tysm lol
#u
#its somewhere else lol look at the top of the code
#oh
#me tossing the laptop out the fucking window
client.run(token)
