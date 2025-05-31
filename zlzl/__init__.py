"""
Flex Userbot
A modular Telegram userbot running on Python
"""

import os
import sys
import time

# Setup version and info
__version__ = "1.0.0"
__license__ = "GNU Affero General Public License v3.0"
__author__ = "Flex Team"

# Print startup message
print(f"Flex module initialized - Version {__version__}")

# Define paths
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(ROOT_DIR)

# Import is done here to avoid circular imports
from .core import start_bot
