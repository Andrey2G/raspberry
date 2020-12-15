from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib
import json
import requests
import time
import dice

host = ""
port = 8080

class HandleRequests(BaseHTTPRequestHandler):
    def send_response(self, code, message=None):
        self.log_request(code)
        self.send_response_only(code)
        self.send_header('Server','Raspy python3 http.server ')     
        self.send_header('Date', self.date_time_string())
        self.end_headers()  

    def set_indicator(value):
        dice.display_result(value)
        


    def process_dice(value):
        url = "https://api.conducttr.com/v1.1/project/73/result"
        #demo key, will expire at 16.12.2020
        key = "2c7f81e654c7b28fe72fea9fca0af192053959ce2"        
        headers = {'Authorization': "Bearer " + key, }
        
        data = {"value": value}
        
        print("result ready")
        dice.result_ready()
        print("ping back to Conducttr fto activity feed")     
        response = requests.post(url, headers=headers, data=data)
        print(response)
        print("wait 1 second")
        time.sleep(1)
        print("display result")
        dice.display_result(value)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length) 
        json_data=json.loads(post_data)
        print(json_data["dice"])


        self.send_response(200)
        self.wfile.write(b'success')

dice.SETUP()

HTTPServer((host, port), HandleRequests).serve_forever()






