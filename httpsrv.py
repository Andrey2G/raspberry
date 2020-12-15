from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib
import json
import requests

host = ""
port = 8080

class HandleRequests(BaseHTTPRequestHandler):
    def send_response(self, code, message=None):
        self.log_request(code)
        self.send_response_only(code)
        self.send_header('Server','Raspy python3 http.server ')     
        self.send_header('Date', self.date_time_string())
        self.end_headers()  

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length) 
        json_data=json.loads(post_data)
        print(json_data["dice"])


        self.send_response(200)
        self.wfile.write(b'success')

HTTPServer((host, port), HandleRequests).serve_forever()






