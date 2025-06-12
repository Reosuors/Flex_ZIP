"""
Web server module for Render port binding
"""

import os
import logging
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

logger = logging.getLogger("flex_webserver")

class SimpleHandler(BaseHTTPRequestHandler):
    """Simple HTTP request handler for Render port binding"""
    
    def do_GET(self):
        """Handle GET requests"""
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        response = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Flex Userbot</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 40px;
                    text-align: center;
                    background-color: #f5f5f5;
                }
                .container {
                    background-color: white;
                    border-radius: 10px;
                    padding: 20px;
                    box-shadow: 0 0 10px rgba(0,0,0,0.1);
                    max-width: 600px;
                    margin: 0 auto;
                }
                h1 {
                    color: #4CAF50;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Flex Userbot</h1>
                <p>The userbot is running! This web server exists only to satisfy Render's port binding requirements.</p>
                <p>Status: Active</p>
            </div>
        </body>
        </html>
        """
        
        self.wfile.write(response.encode('utf-8'))
    
    def log_message(self, format, *args):
        """Override to use our logger"""
        logger.info("%s - %s", self.client_address[0], format % args)

def start_webserver():
    """Start a simple web server for Render port binding"""
    # Get port from environment variable or use default
    port = int(os.environ.get('PORT', 8080))
    
    server = HTTPServer(('0.0.0.0', port), SimpleHandler)
    logger.info(f"Starting web server on port {port}")
    
    # Run server in a separate thread
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    
    return server_thread

def init_webserver():
    """Initialize the web server"""
    try:
        thread = start_webserver()
        logger.info("Web server initialized successfully")
        return thread
    except Exception as e:
        logger.error(f"Error initializing web server: {str(e)}")
        return None
