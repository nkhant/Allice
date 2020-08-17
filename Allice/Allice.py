from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrain

import discord 
from discord.ext import commands

bot = commands.Bot(command_prefix='>')

# All commands start with bot.command(). bot.client() for client related things
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

# Removed on upload. Cant replace with own user's input
bot.run('token')


alliceChatBot = ChatBot("Allice")

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.english")

# Get a response to an input statement
chatbot.get_response("Hello, how are you today?")

#if __name__ == '__main__':
