# Standard library imports
import sys
import os
import logging
from logging.config import fileConfig

# Third party imports
import discord

# Path hack
sys.path.insert(0, os.path.abspath('..'))

# Local application imports
from utils.core import get_env, get_random_quote # bot standard functions

# validate all mandatory files exist before starting
assert os.path.isfile('../utils/logging_config.ini') # Logs config file
assert os.path.isfile('.env')                       # environment variables file

# Instantiate logging in accordance with config file
fileConfig('../utils/logging_config.ini')
logger = logging.getLogger('discord')

# Explicit start of the bot runtime
logger.info("Started Discord bot")

try:
    # Check if it is PROD or TEST environment
    environment = get_env('ENV', __file__)
    logger.info("Running on environment: {}".format(environment))

    # Get TOKEN environment variable
    token = get_env('TOKEN', __file__)
    logger.info("Got Discord token")
except Exception as e:
    logger.exception("Could not get environment variables: {}".format(str(vars(e))))

try:
    # Instatiate Discord client
    client = discord.Client()
    logger.info("Instantiated Discord client")
except Exception as e:
    logger.exception("Error while instantiating Discord client: {}".format(str(vars(e))))

@client.event
async def on_message(message):
    # If running in test environment, do not reply to any calls
    if environment == 'TEST':
        return

    # Do not reply to comments from these users, including itself (client.user)
    blocked_users = [ client.user ]

    # Bot does not reply to itself and only when mentioned
    if client.user.mentioned_in(message) and message.author not in blocked_users:
        logger.info("Replied to message of user '{}' in server '{}' / channel '{}'".format(message.author, message.server, message.channel))
        msg = get_random_quote().format(message)
        await client.send_message(message.channel, msg)
        
@client.event
async def on_server_join(server):
    logger.info("Bot added to server '{}'".format(server.name))
    logger.info("Bot currently running on {} server(s)".format(len(client.guilds)))
    
@client.event
async def on_ready():
    logger.info("Logged in as '{}', client ID '{}'". format(client.user.name, client.user.id))
    logger.info("Bot currently running on {} server(s)".format(len(client.guilds)))

if __name__ == '__main__':
    try:
        # Run Discord bot
        client.run(token)
        logger.info("Started Discord client")
    except Exception as e:
        logger.exception("Error while running Discord client: {}".format(str(vars(e))))
