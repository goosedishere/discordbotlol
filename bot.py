import re
import discord
from discord.ext import commands
client = discord.Client()
bot = commands.Bot(command_prefix="!")
token = "ODYxMzAxOTY1NDM4NDUxNzM1.YOHz9g.kaMRSSWdB5bBl9glhf0EhSMFRI"
#"http[s]?://(?:[a-zA-Z]|[0-9]|[$-@.&+]|[!(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
@client.event
async def on_ready():
    try:
        print(client.user.name)
        print(client.user.id)
        print(discord.version)
    except Exception as e:
        print(e)
words = ["a","e","i","o","u","y"]
@bot.listen()
async def on_message(message):
    channel = bot.get_channel(863214096042950668)
    if message.author == client.user:
        return
    else:
        if "a" in str(message.content):
            await channel.send(str(message.content).replace("a","e"))
link_channel = bot.get_channel(871074726586499102)
@bot.listen()
async def links(message):
    if message.author ==client.user:
        return
    else:
        try:
            linkregex = re.findall("http[s]?://(?:[a-zA-Z]|[0-9]|[$-@.&+]|[!(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",str(message.content))
            await  link_channel.send(f"{str(message.author)[0:-5]} just shared a link")
            await link_channel.send(link_regex[0])
            await message.delete()
        except Exception as  e:
            pass
@bot.command()
async def hello(x):
    await x.send(f"hello {str(x.author)[0:-5]}")
@bot.command()
async def Nice(x):
    await x.send(f"")
bot.run(token)
bot.add_listener(on_message)
client.run(token)
