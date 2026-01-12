import discord
import requests
import json


def get_dog():
    response = requests.get('https://some-random-api.com/img/dog')
    json_data = response.json()

    print(f'Respuesta de la api: {json_data}')

    url_dog = json_data.get('link')

    if url_dog:
        return url_dog
    else:
        return 'Lo siento no se puede encontara la imagen en este momento'
    
def joke():
    reponse = requests.get('https://official-joke-api.appspot.com/random_joke')
    json_data = reponse.json()

    print(f'Respuesta de la API: {json_data}')

    return 'type: ' + json_data.get('type')  + ' setup: ' + json_data.get('setup') + ' punchline: ' + json_data.get('punchline')





class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}')

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('$dog'):
            await message.channel.send(get_dog())
        if message.content.startswith('$joke'):
            await message.channel.send(joke())

intents = discord.Intents.default()
intents.message_content = True


client = MyClient(intents=intents)
client.run('MTQ2MDA5MDUzNDcxNzgxNjg0Mw.Gea1vf.BVSb_zJbiQtLrx5KDsRLkkPYG2xMAlYfaBBQek') 

