from threading import Thread
from time import sleep
from http import client
from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        if post_data == b'Alice':
            self.send_response(200)
            self.end_headers()
            response = f"Thanks for calling with POST request, {post_data.decode()}"
            self.wfile.write(response.encode())
        else:
            self.send_response(403)
            self.end_headers()

def start_server():
    httpd = HTTPServer(('localhost', 8001), SimpleHTTPRequestHandler)
    server = Thread(target=httpd.serve_forever)
    server.start()
    sleep(0.5)
    return httpd

def make_request(method, path, data=None):
    h1 = client.HTTPConnection('localhost', 8001)
    h1.request(method, path, data)

    res = h1.getresponse()
    print(res.status, res.reason)
    data = res.read()
    print(data)

if __name__ == "__main__":
    http_server = start_server()

    make_request("GET", "/")
    make_request("POST", "/", b"Alice")
    make_request("POST", "/", b"Bob")

    http_server.shutdown()