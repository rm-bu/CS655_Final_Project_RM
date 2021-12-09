import http.server

server = http.server.HTTPServer
handler = http.server.CGIHTTPRequestHandler
address = ("", 8000)
server_instance = server(address, handler)
server_instance.serve_forever()
