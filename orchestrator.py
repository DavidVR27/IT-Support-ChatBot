import json
import logging
import asyncio
import os
from flask import request, jsonify

logger = logging.getLogger(__name__)

class Orchestrator:
    """Class to handle chat interactions"""

    def __init__(self):
        @staticmethod
        def read_file(file_path, as_json=False):
            """Reads a file and returns its content"""
            try:
                with open(file_path) as file:
                    logger.info(f"File '{file_path}' successfully read")
                    if as_json:
                        return json.load(file)
                    else:
                        return json.load(file)
            except json.JSONDecodeError:
                logger.error(f"File '{file_path}' could not be read")
                return None
            except Exception as e:
                logger.error(f"File '{file_path}' could not be read")
                return None