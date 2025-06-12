"""
Flex Userbot
A modular Telegram userbot running on Python using Telethon library
"""

import os
import sys
import time
import logging
from telethon import TelegramClient
from telethon.sessions import StringSession
import asyncio

# Setup version and info
__version__ = "1.0.0"
__license__ = "GNU Affero General Public License v3.0"
__author__ = "Flex Team"

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger("flex_bot")

# Define paths
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(ROOT_DIR)

# Get environment variables
API_ID = os.environ.get("APP_ID", None)
API_HASH = os.environ.get("API_HASH", None)
STRING_SESSION = os.environ.get("STRING_SESSION", None)
BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", None)

# Initialize the client
if STRING_SESSION:
    client = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)
else:
    # Fallback to bot token if string session is not available
    if BOT_TOKEN:
        client = TelegramClient("flex_bot", API_ID, API_HASH).start(bot_token=BOT_TOKEN)
    else:
        client = TelegramClient("flex_session", API_ID, API_HASH)

# Print startup message
logger.info(f"Flex module initialized - Version {__version__}")
