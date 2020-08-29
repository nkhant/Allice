from chatterbot import ChatBot
from chatterbot import trainers
from chatterbot.trainers import ChatterBotCorpusTrainer

import discord 
from discord.ext import commands
from discord.ext.commands import Bot

## Chat Bot Library 
alliceChatBot = ChatBot("Allice")

## Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

## Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.english")

## Get a response to an input statement
# chatbot.get_response("Hello, how are you today?")


# This denotes when Allice will understand the person using a command of hers for specific commands
# Example You: >help
bot = commands.Bot(command_prefix='>')

# Give bot ability to read people's messages
# Make it reply like a normal person
# Constantly reads what people type and checks database
# if there is a match reply
def checkDatabase(userMessage):
    return chatbot.get_reponse(userMessage)

# All commands start with bot.command(). bot.client() for client related things
# ctx = context
@bot.command()
async def ping(ctx):
    await ctx.send('pong')
 
# Does not need prefix to read message. Bit will use this to reply to user messages
# Dont forget need to have checks so it doesnt reply to itself
@bot.event
async def on_message(message):
    if message.author != bot.user:
        await message.channel.send(checkDatabase(message.content))

    await bot.process_commands(message)


# Removed on upload. Can replace with own user's input
bot.run('TOken')

