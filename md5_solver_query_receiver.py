import socket
import re
from md5_solver import * 

def receive_query(receiving_address, receiving_port, sending_address, sending_port):
    status = Status()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((receiving_address, receiving_port))
    s.listen()
    connection, address = s.accept()
    total_query = b""
    while True:
        data = connection.recv(2048)
        if len(data) == 0:
            break
        total_query += data
    s.close()
    string = total_query.decode('ascii')
    fields = re.match("Value: (.*), Start: (.*), End: (.*)", string)
    y = search_for_hash_solution(fields[1], fields[2], fields[3], status)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((sending_address, sending_port))
    message = ""
    if(y is None):
        message = "None"
    else:
        message = "Solution: " + y
    s.sendall(bytes(message, encoding='ascii'))
    s.close()
