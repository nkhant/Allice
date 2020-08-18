from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrain

import discord 
from discord.ext import commands

# This denotes when Allice will understand the person using a command of hers
# Example You: >help
bot = commands.Bot(command_prefix='>')

# Give bot ability to read people's messages
# Make it reply like a normal person
# Constantly reads what people type and checks database
# if there is a match reply
# Do this through a function in the command_prefix
# This is function is currently only the idea. it checks for a certain character
# we maybe can change prefix to be entire message and use it as a search
def readMessages(bot, message):
    if message.guild is None:
        return ''
    else:
        return'$'

# All commands start with bot.command(). bot.client() for client related things
# ctx = context
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

# Removed on upload. Can replace with own user's input
bot.run('token')


alliceChatBot = ChatBot("Allice")

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.english")

# Get a response to an input statement
chatbot.get_response("Hello, how are you today?")

#if __name__ == '__main__':
