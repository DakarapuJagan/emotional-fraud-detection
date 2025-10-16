"""
EmotionFAD - Updated Implementation
A web application for real-time emotion and fraud detection with improved WebSocket handling
"""

from flask import Flask, render_template, jsonify, request, session
from flask_socketio import SocketIO, emit, join_room, leave_room
import os
import cv2
import numpy as np
import base64
from io import BytesIO
from PIL import Image
import threading
import webbrowser
import pyngrok.ngrok as ngrok
from datetime import datetime
from dotenv import load_dotenv
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'emotion-fad-secret-key-2025')
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Configure SocketIO
socketio = SocketIO(
    app,
    cors_allowed_origins="*",
    async_mode='eventlet',  # Using eventlet for better WebSocket support
    logger=True,
    engineio_logger=True,
    ping_timeout=60,
    ping_interval=25
)

# Global variables
clients = {}
ngrok_url = None

@app.route('/')
def index():
    """Render the main application page."""
    return render_template('index_new.html')

@socketio.on('connect')
def handle_connect():
    """Handle new WebSocket connection."""
    try:
        clients[request.sid] = {'type': None}
        logger.info(f'Client connected: {request.sid}')
        emit('connection_response', {'data': 'Connected successfully'})
    except Exception as e:
        logger.error(f'Error in handle_connect: {str(e)}')
        emit('error', {'error': 'Connection error'})

@socketio.on('disconnect')
def handle_disconnect():
    """Handle WebSocket disconnection."""
    try:
        if request.sid in clients:
            del clients[request.sid]
        logger.info(f'Client disconnected: {request.sid}')
    except Exception as e:
        logger.error(f'Error in handle_disconnect: {str(e)}')

@socketio.on('start_video')
def handle_start_video():
    """Handle video streaming start request."""
    try:
        if request.sid in clients:
            clients[request.sid]['type'] = 'video'
        emit('video_started', {'status': 'success'})
        logger.info(f'Video streaming started for client: {request.sid}')
    except Exception as e:
        logger.error(f'Error in handle_start_video: {str(e)}')
        emit('error', {'error': 'Failed to start video'})

@socketio.on('start_audio')
def handle_start_audio():
    """Handle audio streaming start request."""
    try:
        if request.sid in clients:
            clients[request.sid]['type'] = 'audio'
        emit('audio_started', {'status': 'success'})
        logger.info(f'Audio streaming started for client: {request.sid}')
    except Exception as e:
        logger.error(f'Error in handle_start_audio: {str(e)}')
        emit('error', {'error': 'Failed to start audio'})

@socketio.on('video_frame')
def handle_video_frame(data):
    """Process video frame from client."""
    try:
        # Process frame here (placeholder)
        # For now, just echo back the frame
        emit('processed_frame', data)
    except Exception as e:
        logger.error(f'Error processing video frame: {str(e)}')
        emit('error', {'error': 'Failed to process video frame'})

@socketio.on('audio_data')
def handle_audio_data(data):
    """Process audio data from client."""
    try:
        # Process audio data here (placeholder)
        # For now, just echo back the data
        emit('processed_audio', data)
    except Exception as e:
        logger.error(f'Error processing audio data: {str(e)}')
        emit('error', {'error': 'Failed to process audio data'})

def start_ngrok():
    """Start ngrok tunnel for public access."""
    global ngrok_url
    try:
        ngrok_auth_token = os.getenv('NGROK_AUTH_TOKEN')
        
        if not ngrok_auth_token:
            logger.info('NGROK_AUTH_TOKEN not found. Running in localhost mode.')
            ngrok_url = 'http://localhost:5000'
            return
            
        try:
            ngrok.set_auth_token(ngrok_auth_token)
            ngrok_tunnel = ngrok.connect(5000, bind_tls=True)
            ngrok_url = ngrok_tunnel.public_url
            
            logger.info('\n' + '='*60)
            logger.info(f'Public URL: {ngrok_url}')
            logger.info('='*60)
            logger.info('\nYour application is now accessible from any device with internet access!')
            logger.info('\nTo stop the application, press Ctrl+C')
            
            webbrowser.open(ngrok_url)
            
        except Exception as e:
            logger.warning(f'Could not start ngrok: {str(e)}')
            logger.info('Running in localhost mode only')
            ngrok_url = 'http://localhost:5000'
            
    except Exception as e:
        logger.error(f'In start_ngrok: {str(e)}')
        ngrok_url = 'http://localhost:5000'

if __name__ == '__main__':
    # Create necessary directories
    os.makedirs('uploads', exist_ok=True)
    os.makedirs('models', exist_ok=True)
    os.makedirs('logs', exist_ok=True)
    
    # Start ngrok in a separate thread
    ngrok_thread = threading.Thread(target=start_ngrok, daemon=True)
    ngrok_thread.start()
    
    logger.info("\nStarting EmotionFAD server...")
    logger.info("Local URL: http://localhost:5000")
    
    try:
        # Start the SocketIO server
        socketio.run(
            app, 
            host='0.0.0.0', 
            port=5000, 
            debug=True, 
            use_reloader=False,
            allow_unsafe_werkzeug=True
        )
    except Exception as e:
        logger.error(f"\nFailed to start server: {str(e)}")
        logger.info("\nTroubleshooting:")
        logger.info("1. Make sure port 5000 is not in use by another application")
        logger.info("2. Try running the application as administrator")
        logger.info("3. Check your firewall settings")
        input("\nPress Enter to exit...")
