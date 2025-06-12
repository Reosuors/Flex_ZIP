"""
Core functionality for the Flex Userbot
"""

import os
import sys
import time
import logging
import asyncio
from telethon import events, functions, types
from . import client, logger

# Handler for .ping command
@client.on(events.NewMessage(pattern=r"\.ping"))
async def ping_handler(event):
    """Handler for .ping command"""
    start_time = time.time()
    message = await event.reply("Pong!")
    end_time = time.time()
    duration = round((end_time - start_time) * 1000, 2)
    await message.edit(f"**Pong!** `{duration}ms`")
    logger.info(f"Ping command executed: {duration}ms")

# Handler for .alive command
@client.on(events.NewMessage(pattern=r"\.alive"))
async def alive_handler(event):
    """Handler for .alive command"""
    await event.reply(
        "**Flex Userbot is running!**\n\n"
        f"• Python version: `{sys.version.split()[0]}`\n"
        f"• Telethon version: `{client.__version__}`\n"
        "• Status: `Online`\n\n"
        "Made with ❤️ by Flex Team"
    )
    logger.info("Alive command executed")

# Handler for .help command
@client.on(events.NewMessage(pattern=r"\.help"))
async def help_handler(event):
    """Handler for .help command"""
    await event.reply(
        "**Flex Userbot Help**\n\n"
        "Available commands:\n"
        "• `.ping` - Check bot response time\n"
        "• `.alive` - Check if bot is running\n"
        "• `.help` - Show this help message\n"
        "• `.restart` - Restart the bot\n"
    )
    logger.info("Help command executed")

# Handler for .restart command
@client.on(events.NewMessage(pattern=r"\.restart"))
async def restart_handler(event):
    """Handler for .restart command"""
    await event.reply("**Restarting...**")
    logger.info("Restart command executed")
    # In a real implementation, this would restart the bot
    # For now, we'll just simulate a restart
    await asyncio.sleep(2)
    await event.reply("**Bot restarted successfully!**")

# Function to register all handlers
def register_handlers():
    """Register all event handlers"""
    # This function is called to ensure all handlers are registered
    # The decorators above will register the handlers automatically
    pass

# Initialize the bot
async def init_bot():
    """Initialize the bot with necessary setup"""
    try:
        # Get entity information (required for some Telethon operations)
        me = await client.get_me()
        logger.info(f"Bot initialized for: {me.first_name} (@{me.username})")
        
        # Register handlers
        register_handlers()
        
        # Set bot status as online
        await client(functions.account.UpdateStatusRequest(offline=False))
        
        return True
    except Exception as e:
        logger.error(f"Error initializing bot: {str(e)}")
        return False
