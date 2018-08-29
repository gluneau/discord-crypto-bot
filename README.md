# discord-crypto-bot

## Installing the prerequisites

```
sudo apt install python-pip
pip install pipenv
```

## Installing the bot:
```
git clone https://github.com/gluneau/discord-crypto-bot.git
cd discord-crypto-bot
pipenv install
```

## Here is a proposed sample for your .env file:
```
YOURDISCORDTOKEN=Nxxxxxxxxxxxxxxxxxxxxxx4.Dxxxxw.mxxxxxxxxxxxxxxxxxxxxxxxxxk
BOTSLEEP=15
BOTPAIR=STONE_BTC
BOTFIAT=USD
```

## Running the bot
```
pipenv run python3 bot.py
```