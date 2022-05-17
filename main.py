import discord
import os
# Ele permite que nosso código faça uma solicitação HTTP para obter dados da API.
import requests
import json

client = discord.Client()


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote_string = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote_string)


quote = get_quote()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$inspire'):
        print('entrei aqui')
    await message.channel.send(quote)
    # messages = 'oi', 'ola', 'hellou', 'eai'
    # if message.content.startswith(messages):
    #     await message.channel.send('Hellouuu, bem vindo ao grupo de estudos em React.js =)')
client.run(os.getenv('TOKEN'))
