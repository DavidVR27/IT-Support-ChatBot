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

        # Verify if request contains audio files
        if 'audio' in request.files:
            logger.info("Processing audio...")
            return handle_audio_request()
        else:
            logger.info("Processing text...")
            return handle_text_request()

    except Exception as e:
        logger.info(f"Error processing chat request: {e}")
        return jsonify({'error': str(e)}), 500

def handle_audio_request():
    """Handles audio requests"""
    try:
        data = request.get_json(force=True)
        if not data:
            logger.error("No JSON data received")
            return jsonify({'error': 'No JSON data received'}), 400

        logger.info(f"Received audio request: {data}")

        session_id = data.get("session_id") or session.get("session_id")
        if not session_id:
            session_id = str(uuid.uuid4())
            session["session_id"] = session_id

        query = data.get("query")
        if not query:
            logger.error("No query received")
            return jsonify({'error': 'No query received'}), 400

        response = asyncio.run(orchestrator.run(query, session_id))
        return response
    except KeyError as e:
        logger.error(f"Missing key in JSON data: {e}")
        return jsonify({'error': f"Missing key in JSON data: str(e)"}), 400
def handle_text_request():
    """Handles text requests"""
