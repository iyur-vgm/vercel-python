from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        #request = requests('https://rest.fnar.net/global/countries')
        self.wfile.write('test'.encode('utf-8'))
        return
