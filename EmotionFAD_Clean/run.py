from app_emotion import app, socketio
import os

if __name__ == '__main__':
    # Create uploads directory if it doesn't exist
    os.makedirs('uploads', exist_ok=True)
    
    # Run the application with SocketIO
    print("\nStarting EmotionFAD server...")
    print("Access the application at: http://localhost:5000")
    print("Press Ctrl+C to stop the server\n")
    
    # Run with debug mode on port 5000
    socketio.run(
        app,
        host='0.0.0.0',  # Accessible from any device on the network
        port=5000,       # Default Flask port
        debug=True,      # Enable debug mode for development
        use_reloader=True
    )
