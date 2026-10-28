"""
OptiWarehouse Web Launcher
Starts a local web server and automatically opens index.html in your default web browser.
"""

import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def start_server():
    os.chdir(DIRECTORY)
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        url = f"http://localhost:{PORT}/index.html"
        print("=" * 65)
        print("   SMART WAREHOUSE INVENTORY OPTIMIZER - WEB APP")
        print("=" * 65)
        print(f"-> Local server running at: {url}")
        print("-> Opening web browser automatically...")
        print("-> Press Ctrl+C in this terminal to stop the server.")
        print("=" * 65)
        webbrowser.open(url)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
            sys.exit(0)

if __name__ == "__main__":
    start_server()
