"""
Bot utilities and helper functions
"""

import os
import sys
import logging
from . import client, logger

async def check_environment_variables():
    """Check if all required environment variables are set"""
    required_vars = ["APP_ID", "API_HASH"]
    optional_vars = ["STRING_SESSION", "TG_BOT_TOKEN"]
    
    missing_vars = []
    for var in required_vars:
        if not os.environ.get(var):
            missing_vars.append(var)
    
    if missing_vars:
        logger.error(f"Missing required environment variables: {', '.join(missing_vars)}")
        return False
    
    # Check if at least one authentication method is available
    if not os.environ.get("STRING_SESSION") and not os.environ.get("TG_BOT_TOKEN"):
        logger.error("Either STRING_SESSION or TG_BOT_TOKEN must be provided")
        return False
    
    logger.info("All required environment variables are set")
    return True

def get_config(name, default=None):
    """Get configuration from environment variables"""
    return os.environ.get(name, default)

def setup_environment():
    """Setup the environment for the bot"""
    # Add the root directory to the path
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if root_dir not in sys.path:
        sys.path.append(root_dir)
    
    # Create necessary directories if they don't exist
    os.makedirs(os.path.join(root_dir, "downloads"), exist_ok=True)
    os.makedirs(os.path.join(root_dir, "logs"), exist_ok=True)
    
    return True
