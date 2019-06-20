# Bobby B Bot - Discord version
[![Build Status](https://travis-ci.org/bobby-b-bot/discord.svg?branch=master)](https://travis-ci.org/bobby-b-bot/discord) ![GitHub release](https://img.shields.io/github/release/bobby-b-bot/discord.svg) ![GitHub All Releases](https://img.shields.io/github/downloads/bobby-b-bot/discord/total.svg) ![GitHub issues](https://img.shields.io/github/issues-raw/bobby-b-bot/discord.svg) ![GitHub](https://img.shields.io/github/license/bobby-b-bot/discord.svg)

In this repository you can find the Discord version of the Bobby B Bot.  

## How to use it

Simply mention the bot's name in your channel '@Bobby B' after adding it via [this link](https://bit.ly/2C0kogN), and the bot will reply with a random quote.

## How to install

1. Create a virtual environment and activate it (this is optional but when working with Python, I cannot recommend it enough) or create a root folder that will hold all the code;
2. Clone discord repository inside this virtual enviroment folder (let's call it 'root') and then clone [utils](https://github.com/bobby-b-bot/utils.git) repository. The final structure should be somewhat similar to this:

```
+ root
└───+ discord
│     |-- discord_bot.py
└───+ utils
      |-- __init__.py
      |-- core.py
      |-- logging_config.ini
      |-- quotes.json
      |-- triggers.json
```

4. Run command `pip install -r requirements.txt` in discord directory (this should install the requirements for utils as well, otherwise, you can also run the command in utils folder);
5. Done, you are ready to configure it.

#### TL;DR Installation:

```
$ python -m venv <venv_name>
$ cd venv_name
$ source bin/activate
(venv_name) $ git clone https://github.com/bobby-b-bot/discord.git
(venv_name) $ git clone https://github.com/bobby-b-bot/utils.git
(venv_name) $ cd discord
(venv_name) $ pip install -r requirements.txt
```

## How to configure and run

1. Create and maintain the .env file for environment variables in root discord folder (ENV = 'TEST' or 'PROD' and Discord token in variable TOKEN) 
1. Create and mantain a logging_config.ini file in utils folder for logging configuration ([see documentation](https://docs.python.org/3/library/logging.config.html#logging-config-fileformat));
1. Run the bot (`python discord_bot.py`)
1. Have fun!

## How to contribute

Feature requests such as new quotes are welcome via issues on GitHub! Feel free to contribute. You can also contribute by donating via [PayPal](http://paypal.me/felipezanettini) to keep the servers running. 
