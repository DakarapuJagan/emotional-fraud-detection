"""
Simple EmotionFAD - Minimal Implementation
A simplified version with basic WebSocket functionality
"""

from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import os
import logging

# Basic configuration
app = Flask(__name__)
app.config['SECRET_KEY'] = 'simple-secret-key-2025'

# Initialize SocketIO with basic configuration
socketio = SocketIO(app, 
                   cors_allowed_origins="*",
                   async_mode='threading',  # Use threading for maximum compatibility
                   logger=True,
                   engineio_logger=True)

# Routes
@app.route('/')
def index():
    return render_template('index_simple.html')

# WebSocket event handlers
@socketio.on('connect')
def handle_connect():
    print('Client connected')
    emit('connection_response', {'status': 'connected'})

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('message')
def handle_message(message):
    print('Received message:', message)
    emit('response', {'data': 'Message received: ' + str(message)})

if __name__ == '__main__':
    print("\nStarting Simple EmotionFAD server...")
    print("Local URL: http://localhost:5000")
    print("\nPress Ctrl+C to stop the server\n")
    
    try:
        socketio.run(app, 
                    host='0.0.0.0', 
                    port=5000, 
                    debug=True,
                    use_reloader=False)
    except Exception as e:
        print(f"\nError: {str(e)}")
        print("\nTroubleshooting:")
        print("1. Make sure port 5000 is not in use")
        print("2. Try running as administrator")
        print("3. Check your firewall settings")
        input("\nPress Enter to exit...")
