from http.server import HTTPServer, SimpleHTTPRequestHandler

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Hello from Jenkins CI/CD Pipeline!")

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8080), MyHandler)
    print("Server running on port 8080...")
    server.run()