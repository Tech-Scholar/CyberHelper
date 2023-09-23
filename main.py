import discord
from fuzzywuzzy import fuzz
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix='.', intents=intents)
my_secret = input("Add Token: ")

@client.event
async def on_ready():
    print('I am alive')

@client.event
async def on_message(message):
  if message.channel.name == "introduction":
    if fuzz.ratio("Cleveland-Lloyd Dinosaur Quarry", message.content) > 90 and "Junior Archeologist" not in message.author.roles:
      await message.channel.purge(limit=1)
      await message.channel.send(f"Congratulations {message.author.name} for finding the location!")
      role = discord.utils.get(message.guild.roles, name="Junior Archeologist")
      await message.author.add_roles(role)
    elif not "Congratulations" in message.content:
      await message.channel.purge(limit=1)
      
  if message.channel.name == "first-dig":
    if fuzz.ratio("Ali3nsAreAm0ngUs", message.content) > 90 and "Archeologist" not in message.author.roles:
      await message.channel.purge(limit=1)
      await message.channel.send(f"Congratulations {message.author.name} for finding the hidden secret!")
      original_role = discord.utils.get(message.guild.roles, name="Junior Archeologist")
      new_role = discord.utils.get(message.guild.roles, name="Archeologist")
      await message.author.remove_roles(original_role) 
      await message.author.add_roles(new_role) 
    elif not "Congratulations" in message.content:
      await message.channel.purge(limit=1)
    
  
client.run(my_secret)