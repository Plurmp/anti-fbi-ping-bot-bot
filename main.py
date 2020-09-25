from os import environ as cred

import discord

client = discord.Client()


@client.event
async def on_message(message):
    if message.author.id == 758904021678424075:  # fbi ping bot
        await message.delete()


client.run(cred['DISCORD_TOKEN'])
