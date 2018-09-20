from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
bot=ChatBot('Test')
Client=discord.Client()
client=commands.Bot(command_prefix="!")
bot=ChatBot('Test')
bot.set_trainer(ListTrainer)
for _file in os.listdir('files'):
    chats=open('files/'+_file,'r').readlines()
    bot.train(chats)
@client.event
async def on_ready():
    print("Wabz is connected to all servers!")
@client.event
async def on_message(message):
    if not message.author.bot:
        response=bot.get_response(message.content)
        print(message," ",message.content)
        await client.send_message(message.channel,response)
    else:
        return
while True:
    client.run("NDc0OTQ5NDYyMjI2MjM5NDk5.DoGhXQ.tZlLRrGepvcXDbihQtTLY96r5UM")
