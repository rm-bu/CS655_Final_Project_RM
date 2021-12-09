import html
import cgi
import cgitb
import time
import socket


def solve_for_password(fs):
    x = fs.getvalue('hashed_value')
    w = fs.getvalue('worker_count')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("10.10.1.2", 8999))
    s.sendall(bytes("Value: {0}, Workers: {1}".format(x,w), encoding='ascii'))
    s.close()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("10.10.1.1", 8998))
    s.listen()
    connection, address = s.accept()
    total_data = b""
    while True:
        data = connection.recv(2048)
        if len(data) == 0:
            break
        total_data += data
    s.close()
    return total_data.decode('ascii')




print("Content-type: text/html")

print("\n<b>Input the hashed value:</b>")
print("""\n<form method = "post">
    <p>
      <input type = "text" name = "hashed_value">
      <label for="text"></label><br>
      <input type="radio" id="w1" name="worker_count" value="1" checked="checked">
      <label for="html">1 Worker</label><br>
      <input type="radio" id="w2" name="worker_count" value="2">
      <label for="html">2 Workers</label><br>
      <input type="radio" id="w3" name="worker_count" value="3">
      <label for="html">3 Worker</label><br>
      <input type="radio" id="w4" name="worker_count" value="4">
      <label for="html">4 Workers</label><br>
      <input type = "submit">
    </p>
    </form>""")

fs = cgi.FieldStorage()
x = fs.getvalue('hashed_value')
if(x != None):
    password = solve_for_password(fs)
    print("The original password is {0}".format(password))

