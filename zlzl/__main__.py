"""
Main entry point for the Flex Userbot
"""

import os
import sys
import time
import logging
import asyncio
from . import client, logger
from .webserver import init_webserver

async def send_startup_message():
    """Send startup message to saved messages"""
    try:
        await client.send_message("me", "**Flex Userbot is now running!**\n\n" + 
                                 f"Python version: {sys.version}\n" +
                                 f"Telethon version: {client.__version__}\n" +
                                 "Type `.help` in any chat to see available commands.")
        logger.info("Startup message sent")
    except Exception as e:
        logger.error(f"Failed to send startup message: {str(e)}")

async def main():
    """Main function to run the bot"""
    logger.info("Flex main module started")
    
    # Start web server for Render port binding
    webserver_thread = init_webserver()
    if webserver_thread:
        logger.info("Web server started successfully")
    else:
        logger.warning("Failed to start web server, continuing anyway")
    
    try:
        # Connect to Telegram
        logger.info("Connecting to Telegram...")
        await client.connect()
        
        # Check authorization
        if not await client.is_user_authorized():
            logger.error("User is not authorized. Please check your STRING_SESSION or API credentials")
            return 1
        
        # Get account info
        me = await client.get_me()
        logger.info(f"Logged in as: {me.first_name} (@{me.username})")
        
        # Send startup message
        await send_startup_message()
        
        # Run the client until disconnected
        logger.info("Bot is now running. Press Ctrl+C to stop")
        await client.run_until_disconnected()
        
    except Exception as e:
        logger.error(f"Error in main loop: {str(e)}")
        return 1
    finally:
        # Ensure client is disconnected
        await client.disconnect()
    
    return 0

if __name__ == "__main__":
    # Run the main function
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped by user")
