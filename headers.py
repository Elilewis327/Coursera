import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect(('data.pr4e.org', 80))
  s.send('GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode())

  while True:
    data = s.recv(1024)
    if not data:
      break
    print(data.decode())
