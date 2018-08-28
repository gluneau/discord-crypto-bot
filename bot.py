import discord
import os
import asyncio
import time
import json
import requests

from discord.ext.commands import Bot
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
Client = discord.Client()
client = commands.Bot(command_prefix="!")

async def background_loop():
    await client.wait_until_ready()
    while not client.is_closed:
        try:
            # Get all pairs from CryptoBridge exchange
            tok_response = requests.get(url='https://api.crypto-bridge.org/api/v1/ticker')
            tok_response.close()
            tok_data = tok_response.json()

            for line in tok_data:
                if line["id"] == os.getenv("BOTPAIR"):
                    print(line)
                    lst = line["last"]
                    vol = line["volume"]
                    ask = line["ask"]

            # Get fiat value versus BTC
            fiat_response = requests.get(url='https://blockchain.info/it/ticker')
            fiat_response.close()
            fiat_data = fiat_response.json()

            # Get the last price for selected fiat and calculate the value of the token in fiat.
            btcfia = fiat_data[os.getenv("BOTFIAT")]["last"]
            tokfia = round(float(lst) * float(btcfia), 2)

            # Calculate the token volume
            tokvol = round(float(vol) / float(ask), 3)

            # Grab the first half of the pair
            toksym = os.getenv("BOTPAIR").split('_', 1)[0]

            playing = []
            playing.append('฿ ' + str(lst) + ' BTC')
            playing.append('$ ' + str(tokfia) + ' ' + os.getenv("BOTFIAT"))
            playing.append('฿ ' + str(vol) + ' VOL 24h')
            playing.append(toksym + ' ' + str(tokvol) + ' VOL 24h')

            # This loop is there to space out the request to the API for an avarage of 5 minutes.
            for time in range(5):
                print(time)
                for play in playing:
                  print(play)
                  # The magical update of the playing bot status happens here!
                  await client.change_presence(game=discord.Game(name=play))
                  # This is the time the bot will sleep between playing statuses
                  await asyncio.sleep(int(os.getenv("BOTSLEEP")))
        except:
            pass

client.loop.create_task(background_loop())
client.run(os.getenv("YOURDISCORDTOKEN"))
