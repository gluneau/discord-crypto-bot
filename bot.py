import discord

from discord.ext.commands import Bot
from discord.ext import commands

import asyncio
import time
import json
import requests

Client = discord.Client()
client = commands.Bot(command_prefix="!")

async def background_loop():
    await client.wait_until_ready()
    while not client.is_closed:
        try:
            r = requests.get(url='https://api.crypto-bridge.org/api/v1/ticker')
            r2 = requests.get(url='https://blockchain.info/it/ticker')
            r.close()
            r2.close()
            data = r.json()
            data2 = r2.json()
            bco = data[0]["last"]
            btcusd = data2["USD"]["last"]
            bcousd = float(bco) * float(btcusd)
            bcousd = round(bcousd, 2)
            btcusd = round(btcusd, 2)
            playing = '฿ ' + str(bco)
            await client.change_presence(game=discord.Game(name=playing))
        except:
            pass
        await asyncio.sleep(360)

client.loop.create_task(background_loop())
client.run("YOURDISCORDTOKEN")

