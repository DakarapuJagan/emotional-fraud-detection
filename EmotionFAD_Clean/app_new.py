"""
EmotionFAD - New Implementation
A web application for real-time emotion and fraud detection
"""

from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO, emit
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

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'emotion-fad-secret-key-2025'
socketio = SocketIO(app, cors_allowed_origins="*")

# Global variables
clients = {}
ngrok_url = None

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    clients[request.sid] = {'type': None}
    print(f'Client connected: {request.sid}')

@socketio.on('disconnect')
def handle_disconnect():
    if request.sid in clients:
        del clients[request.sid]
    print(f'Client disconnected: {request.sid}')

@socketio.on('start_video')
def handle_start_video():
    clients[request.sid]['type'] = 'video'
    print(f'Video streaming started for client: {request.sid}')

@socketio.on('start_audio')
def handle_start_audio():
    clients[request.sid]['type'] = 'audio'
    print(f'Audio streaming started for client: {request.sid}')

@socketio.on('video_frame')
def handle_video_frame(data):
    try:
        # Process video frame here
        # For now, just echo back the frame
        emit('processed_frame', data)
    except Exception as e:
        print(f'Error processing video frame: {str(e)}')

@socketio.on('audio_data')
def handle_audio_data(data):
    try:
        # Process audio data here
        # For now, just echo back the data
        emit('processed_audio', data)
    except Exception as e:
        print(f'Error processing audio data: {str(e)}')

def start_ngrok():
    global ngrok_url
    try:
        # Get ngrok auth token from environment variable or use a default one
        ngrok_auth_token = os.getenv('NGROK_AUTH_TOKEN')
        
        if not ngrok_auth_token:
            print('⚠️  NGROK_AUTH_TOKEN not found in environment variables.')
            print('Please set it by running:')
            print('1. Sign up at https://ngrok.com/')
            print('2. Get your auth token from https://dashboard.ngrok.com/get-started/your-authtoken')
            print('3. Set it as an environment variable or in a .env file:')
            print('   NGROK_AUTH_TOKEN=your_auth_token_here')
            print('\nFor now, using localhost only (no public URL)')
            ngrok_url = 'http://localhost:5000'
            return
            
        # Set the auth token
        ngrok.set_auth_token(ngrok_auth_token)
        
        # Start ngrok tunnel
        ngrok_tunnel = ngrok.connect(5000, bind_tls=True)
        ngrok_url = ngrok_tunnel.public_url
        
        print('\n' + '='*60)
        print(f'🚀  Public URL: {ngrok_url}')
        print('='*60)
        print('\nYour application is now accessible from any device with internet access!')
        print('\nTo stop the application, press Ctrl+C')
        
        # Open in default browser
        webbrowser.open(ngrok_url)
        
    except Exception as e:
        print(f'\n❌ Error starting ngrok: {str(e)}')
        print('\n⚠️  Running in localhost mode only (not accessible from other devices)')
        ngrok_url = 'http://localhost:5000'

if __name__ == '__main__':
    # Start ngrok in a separate thread
    threading.Thread(target=start_ngrok, daemon=True).start()
    
    # Start the Flask-SocketIO server
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
