import os
import logging
import sys
import uuid
import asyncio


# Logging Configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Flask Handler initializer

@app.route("/chat", methods=['POST'])
def chat():
    """Endpoint for handling chat requests (text or audio)"""
    try:
        logger.info("Processing chat request...")

