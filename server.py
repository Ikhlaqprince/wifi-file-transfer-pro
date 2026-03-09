# server.py (Root Directory - Fixed Version)
import http.server
import socketserver
import os
import threading
import cgi
from urllib.parse import unquote

PORT = 8080
UPLOAD_DIR = os.path.expanduser("~")  # Android safe path

class WiFiHandler(http.server.SimpleHTTPRequestHandler):
    
    def do_GET(self):
        # File download handler
        if self.path.startswith("/download/"):
            filename = unquote(self.path.replace("/download/", ""))
            filepath = os.path.join(UPLOAD_DIR, filename)
            
            if os.path.exists(filepath):
                self.send_response(200)
                self.send_header('Content-type', 'application/octet-stream')
                self.send_header('Content-Disposition', f'attachment; filename="{filename}"')
                self.end_headers()
                with open(filepath, "rb") as f:
                    self.wfile.write(f.read())
                return
        return super().do_GET()

    def do_POST(self):
        # File upload handler
        if self.path == "/upload":
            form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD': 'POST'}
            )
            file_item = form['file']
            if file_item.filename:
                file_path = os.path.join(UPLOAD_DIR, file_item.filename)
                with open(file_path, 'wb') as f:
                    f.write(file_item.file.read())
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b"Upload Successful")
                return
        self.send_response(404)
        self.end_headers()

class WiFiServer:
    """Main server class that home_screen.py expects"""
    
    def __init__(self, port=8080):
        self.port = port
        self.httpd = None
        self.thread = None

    def start_in_thread(self):
        """Start server in background thread"""
        handler = WiFiHandler
        self.httpd = socketserver.TCPServer(("", self.port), handler)
        self.thread = threading.Thread(target=self.httpd.serve_forever)
        self.thread.daemon = True  # Auto-close when app closes
        self.thread.start()
        print(f"✅ Server started on port {self.port}")

    def stop(self):
        """Stop the server"""
        if self.httpd:
            self.httpd.shutdown()
            print("✅ Server stopped")
