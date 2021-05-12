import discord, datetime, time
import asyncio
from discord.ext import commands
import pyfiglet
import discord


perfix = "-"
TOKEN = ""

def get_prefix(client, message):

    prefixes = [perfix]

    return commands.when_mentioned_or(*prefixes)(client, message)

client = commands.Bot(command_prefix = get_prefix)

@client.event
async def on_ready():
    print('Bot Is Online And Ready To Roll!')
    print('----------------Info----------------')
    print('Username:', client.user.name)
    print('ID:', client.user.id)

client.remove_command('help')

@client.command()
async def figlet(ctx, figlet = None, *, text = None):
  if figlet == None and text == None:
    embed = discord.Embed(title=f"**Nothing given**", description="Please type `-figlet help` or try `-figlet <figlet> <text>`")
    await ctx.send(embed=embed)
  elif figlet == "help":
    embed = discord.Embed(title=f"**Help**", description="Please try our figlets 1-17. They are listed below by name. Ex `-figlet 1 hi`")
    embed.add_field(name="Figlet List", value="`1` - Normal figlet. \n `2` - Slant Figlet. \n `3` - 3D \n `4` \n `5` \n `6` \n `7` \n `8` \n `9` \n `10` \n `11` \n `12` \n `13` \n `14` \n `15` \n `16` \n `17`")
    await ctx.send(embed=embed)
  elif text == None:
    embed = discord.Embed(title=f"**Text not give**", description=f"Please do `-figlet {figlet} <text>`")
    await ctx.send(embed=embed)
  elif len(text) > 5:
    if len(text) > 50:
      await ctx.send(f'Please make <text> into 100 charctars or less')
    elif figlet == "1":
      result = pyfiglet.figlet_format(f"{text}")
      embed = discord.Embed(title=f"**Normal Figlet**", description=f"Here is the {figlet} figlet.")
      await ctx.send(embed=embed)
      await ctx.send(f"```{result}```")
    elif figlet == "2":
      result = pyfiglet.figlet_format(f"{text}", font = "slant")
      embed = discord.Embed(title=f"**Slant Figlet**", description=f"Here is the {figlet} figlet.")
      await ctx.send(embed=embed)
      await ctx.send(f"```{result}```")
    elif figlet == "3":
      result = pyfiglet.figlet_format(f"{text}", font = "3-d")
      embed = discord.Embed(title=f"**3D Figlet**", description=f"Here is the {figlet} figlet.")
      await ctx.send(embed=embed)
      await ctx.send(f"```{result}```")
    elif figlet == "4":
      result = pyfiglet.figlet_format(f"{text}", font = "3x5")
      embed = discord.Embed(title=f"**3x5 Figlet**", description=f"Here is the {figlet} figlet.")
      await ctx.send(embed=embed)
      await ctx.send(f"```{result}```")
    elif figlet == "5":
      result = pyfiglet.figlet_format(f"{text}", font = "5lineoblique")
      embed = discord.Embed(title=f"**lineoblique Figlet**", description=f"Here is the {figlet} figlet.")
      await ctx.send(embed=embed)
      await ctx.send(f"```{result}```")
    elif figlet == "6":
      result = pyfiglet.figlet_format(f"{text}", font = "alphabet")
      embed = discord.Embed(title=f"**Alphabet Figlet**", description=f"Here is the {figlet} figlet.")
      await ctx.send(embed=embed)
      await ctx.send(f"```{result}```")
    elif figlet == "7":
      result = pyfiglet.figlet_format(f"{text}", font = "banner3-D")
      embed = discord.Embed(title=f"**3DBanner Figlet**", description=f"Here is the {figlet} figlet.")
      await ctx.send(embed=embed)
      await ctx.send(f"```{result}```")
    elif figlet == "8":
      result = pyfiglet.figlet_format(f"{text}", font = "doh")
      embed = discord.Embed(title=f"**Doh Figlet**", description=f"Here is the {figlet} figlet.")
      await ctx.send(embed=embed)
      await ctx.send(f"```{result}```")
    elif figlet == "9": 
      result = pyfiglet.figlet_format(f"{text}", font = "isometric1")
      embed = discord.Embed(title=f"**Isometric Figlet**", description=f"Here is the {figlet} figlet.")
      await ctx.send(embed=embed) 
      await ctx.send(f"```{result}```")
    elif figlet == "10":
      result = pyfiglet.figlet_format(f"{text}", font = "letters")
      embed = discord.Embed(title=f"**Letters Figlet**", description=f"Here is the {figlet} figlet.")
      await ctx.send(embed=embed)
      await ctx.send(f"```{result}```")
    elif figlet == "11":
      result = pyfiglet.figlet_format(f"{text}", font = "alligator")
      embed = discord.Embed(title=f"**Alligator Figlet**", description=f"Here is the {figlet} figlet.")
      await ctx.send(embed=embed)
      await ctx.send(f"```{result}```")
    elif figlet == "12":
      result = pyfiglet.figlet_format(f"{text}", font = "dotmatrix")
      embed = discord.Embed(title=f"**Dotmatrix Figlet**", description=f"Here is the {figlet} figlet.")
      await ctx.send(embed=embed)
      await ctx.send(f"```{result}```")
    elif figlet == "13":
      result = pyfiglet.figlet_format(f"{text}", font = "bubble")
      embed = discord.Embed(title=f"**Bubble Figlet**", description=f"Here is the {figlet} figlet.")
      await ctx.send(embed=embed)
      await ctx.send(f"```{result}```")
    elif figlet == "14":
      result = pyfiglet.figlet_format(f"{text}", font = "bulbhead")
      embed = discord.Embed(title=f"**Bulbhead Figlet**", description=f"Here is the {figlet} figlet.")
      await ctx.send(embed=embed)
      await ctx.send(f"```{result}```")
    elif figlet == "15":
      result = pyfiglet.figlet_format(f"{text}", font = "digital")
      embed = discord.Embed(title=f"**Digital Figlet**", description=f"Here is the {figlet} figlet.")
      await ctx.send(embed=embed)
      await ctx.send(f"```{result}```")
    else:
      result = pyfiglet.figlet_format(f"Error")
      embed = discord.Embed(title=f"**Not Valid**", description=f"Figlet {figlet} is not a valid figlet.")
      embed.add_field(name="󠀠", value=f"```{result}```")
      await ctx.send(embed=embed)
  elif figlet == "1":
    result = pyfiglet.figlet_format(f"{text}")
    embed = discord.Embed(title=f"**Normal Figlet**", description=f"Here is the {figlet} figlet.")
    embed.add_field(name="󠀠",  value=f"```{result}```")
    await ctx.send(embed=embed)
  elif figlet == "2":
    result = pyfiglet.figlet_format(f"{text}", font = "slant")
    embed = discord.Embed(title=f"**Slant Figlet**", description=f"Here is the {figlet} figlet.")
    embed.add_field(name="󠀠", value=f"```{result}```")
    await ctx.send(embed=embed)
  elif figlet == "3":
    result = pyfiglet.figlet_format(f"{text}", font = "3-d")
    embed = discord.Embed(title=f"**3D Figlet**", description=f"Here is the {figlet} figlet.")
    embed.add_field(name="󠀠", value=f"```{result}```")
    await ctx.send(embed=embed)
  elif figlet == "4":
    result = pyfiglet.figlet_format(f"{text}", font = "3x5")
    embed = discord.Embed(title=f"**3x5 Figlet**", description=f"Here is the {figlet} figlet.")
    embed.add_field(name="󠀠", value=f"```{result}```")
    await ctx.send(embed=embed)
  elif figlet == "5":
    result = pyfiglet.figlet_format(f"{text}", font = "5lineoblique")
    embed = discord.Embed(title=f"**lineoblique Figlet**", description=f"Here is the {figlet} figlet.")
    embed.add_field(name="󠀠", value=f"```{result}```")
    await ctx.send(embed=embed)
  elif figlet == "6":
    result = pyfiglet.figlet_format(f"{text}", font = "alphabet")
    embed = discord.Embed(title=f"**Alphabet Figlet**", description=f"Here is the {figlet} figlet.")
    embed.add_field(name="󠀠", value=f"```{result}```")
    await ctx.send(embed=embed)
  elif figlet == "7":
    result = pyfiglet.figlet_format(f"{text}", font = "banner3-D")
    embed = discord.Embed(title=f"**3DBanner Figlet**", description=f"Here is the {figlet} figlet.")
    embed.add_field(name="󠀠", value=f"```{result}```")
    await ctx.send(embed=embed)
  elif figlet == "8":
    result = pyfiglet.figlet_format(f"{text}", font = "doh")
    embed = discord.Embed(title=f"**Doh Figlet**", description=f"Here is the {figlet} figlet.")
    embed.add_field(name="󠀠", value=f"```{result}```")
    await ctx.send(embed=embed)
  elif figlet == "9": 
    result = pyfiglet.figlet_format(f"{text}", font = "isometric1")
    embed = discord.Embed(title=f"**Isometric Figlet**", description=f"Here is the {figlet} figlet.")
    embed.add_field(name="󠀠", value=f"```{result}```")
    await ctx.send(embed=embed) 
  elif figlet == "10":
    result = pyfiglet.figlet_format(f"{text}", font = "letters")
    embed = discord.Embed(title=f"**Letters Figlet**", description=f"Here is the {figlet} figlet.")
    embed.add_field(name="󠀠", value=f"```{result}```")
    await ctx.send(embed=embed)
  elif figlet == "11":
    result = pyfiglet.figlet_format(f"{text}", font = "alligator")
    embed = discord.Embed(title=f"**Alligator Figlet**", description=f"Here is the {figlet} figlet.")
    embed.add_field(name="󠀠", value=f"```{result}```")
    await ctx.send(embed=embed)
  elif figlet == "12":
    result = pyfiglet.figlet_format(f"{text}", font = "dotmatrix")
    embed = discord.Embed(title=f"**Dotmatrix Figlet**", description=f"Here is the {figlet} figlet.")
    embed.add_field(name="󠀠", value=f"```{result}```")
    await ctx.send(embed=embed)
  elif figlet == "13":
    result = pyfiglet.figlet_format(f"{text}", font = "bubble")
    embed = discord.Embed(title=f"**Bubble Figlet**", description=f"Here is the {figlet} figlet.")
    embed.add_field(name="󠀠", value=f"```{result}```")
    await ctx.send(embed=embed)
  elif figlet == "14":
    result = pyfiglet.figlet_format(f"{text}", font = "bulbhead")
    embed = discord.Embed(title=f"**Bulbhead Figlet**", description=f"Here is the {figlet} figlet.")
    embed.add_field(name="󠀠", value=f"```{result}```")
    await ctx.send(embed=embed)
  elif figlet == "15":
    result = pyfiglet.figlet_format(f"{text}", font = "digital")
    embed = discord.Embed(title=f"**Digital Figlet**", description=f"Here is the {figlet} figlet.")
    embed.add_field(name="󠀠", value=f"```{result}```")
    await ctx.send(embed=embed)
  elif figlet == "16":
    result = pyfiglet.figlet_format(f"{text}", font = "4x4_offr")
    embed = discord.Embed(title=f"**4x4_offr Figlet**", description=f"Here is the {figlet} figlet.")
    embed.add_field(name="󠀠", value=f"```{result}```")
    await ctx.send(embed=embed)
  elif figlet == "17":
    result = pyfiglet.figlet_format(f"{text}", font = "5x7")
    embed = discord.Embed(title=f"**5x7 Figlet**", description=f"Here is the {figlet} figlet.")
    embed.add_field(name="󠀠", value=f"```{result}```")
    await ctx.send(embed=embed)
  elif figlet == "18":
    result = pyfiglet.figlet_format(f"{text}", font = "5x8")
    embed = discord.Embed(title=f"**5x8 Figlet**", description=f"Here is the {figlet} figlet.")
    embed.add_field(name="󠀠", value=f"```{result}```")
    await ctx.send(embed=embed)
  else:
    result = pyfiglet.figlet_format(f"Error")
    embed = discord.Embed(title=f"**Not Valid**", description=f"Figlet {figlet} is not a valid figlet.")
    embed.add_field(name="󠀠", value=f"```{result}```")
    await ctx.send(embed=embed)


@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    a = error.retry_after
    b = time.strftime('%H:%M:%S', time.gmtime(a))
    embed = discord.Embed(title="403 Application Cooldown!", description=f"Try again in **{b}**.")
    await ctx.send(embed=embed)
  else:
    raise error

client.run(TOKEN)
