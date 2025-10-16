"""
WSGI config for EmotionFAD.

This module contains the WSGI application used for production deployments.
"""

import os
import logging
from app_emotion import app, socketio

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# This application object is used by any WSGI server configured to use this file.
application = app

def run():
    """Run the application with Socket.IO support"""
    try:
        port = int(os.environ.get('PORT', 5000))
        logger.info(f"Starting EmotionFAD server on port {port}")
        
        socketio.run(
            app,
            host='0.0.0.0',
            port=port,
            debug=os.environ.get('FLASK_ENV') == 'development',
            use_reloader=False,
            allow_unsafe_werkzeug=True,
            log_output=True
        )
    except Exception as e:
        logger.error(f"Failed to start server: {str(e)}")
        raise

if __name__ == "__main__":
    run()
