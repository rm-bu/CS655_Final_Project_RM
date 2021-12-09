import socket
import hashlib
import threading
import re
from md5_solver import divide_string_range


solutions = []

def wait_for_solution(address, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((address, port))
    s.listen()
    connection, address = s.accept()
    total_data = b""
    while True:
        data = connection.recv(2048)
        if len(data) == 0:
            break
        total_data += data
    s.close()
    solutions.append(total_data.decode('ascii'))

def send_hashed_value(x, start, end, address, port):
    string = "Value: {0}, Start: {1}, End: {2}".format(x,start,end)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((address, port))
    s.sendall(bytes(string, encoding='ascii'))
    s.close()



class Worker:
    def __init__(self, sending_address, sending_port, receiving_address, receiving_port):
        self.sending_address = sending_address
        self.sending_port = sending_port
        self.receiving_address = receiving_address
        self.receiving_port = receiving_port


query_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
query_socket.bind(("10.10.1.2", 8999))
query_socket.listen()
connection, address = query_socket.accept()
total_data = b""
while True:
    data = connection.recv(2048)
    if len(data) == 0:
        break
    total_data += data
query_socket.close()
m = re.match("Value: (.*), Workers: (.*)", total_data.decode('ascii'))
target_string = m[1]
workers_to_use = int(m[2])

w = []
w.append(Worker("10.10.2.2", 9000, "10.10.2.1", 9001))
w.append(Worker("10.10.3.2", 9002, "10.10.3.1", 9003))
w.append(Worker("10.10.4.2", 9004, "10.10.4.1", 9005))
w.append(Worker("10.10.5.2", 9006, "10.10.5.1", 9007))
w.append(Worker("10.10.6.2", 9008, "10.10.6.1", 9009))
w.append(Worker("10.10.7.2", 9010, "10.10.7.1", 9011))
w.append(Worker("10.10.8.2", 9012, "10.10.8.1", 9013))


t = []

for i in range(workers_to_use):
    t.append(threading.Thread(target=wait_for_solution, args=(w[i].receiving_address, w[i].receiving_port)))
    t[i].start()

ranges = divide_string_range("AAAAA", "zzzzz", workers_to_use)
for i in range(workers_to_use):
    send_hashed_value(target_string, ranges[i][0], ranges[i][1], w[i].sending_address, w[i].sending_port)

for i in range(workers_to_use):
    t[i].join()

final_answer = ""
for solution in solutions:
    m = re.match("Solution: (.*)", solution)
    if(m != None):
        final_answer = m[1]


solution_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
solution_socket.connect(("10.10.1.1", 8998))
solution_socket.sendall(bytes(final_answer, encoding='ascii'))
solution_socket.close()
