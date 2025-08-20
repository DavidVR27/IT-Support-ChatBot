import os
import logging
import sys
import uuid
import asyncio

from flask import Flask, jsonify, request, render_template, session
from flask_cors import CORS
from orchestrator import Orchestrator
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

CORS(app)


# Logging Configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Flask Handler initializer
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route("/chat", methods=['POST'])
def chat():
    """Endpoint for handling chat requests (text or audio)"""
    try:
        logger.info("Processing chat request...")
        if 'audio' in request.files:
            logger.info("Processing audio...")
            return handle_audio_request()
        else:
            logger.info("Processing text...")
            return handle_text_request()

    except Exception as e:
        logger.info(f"Error processing chat request: {e}")
        return jsonify({'error': str(e)})