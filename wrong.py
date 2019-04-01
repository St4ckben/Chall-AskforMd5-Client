import sys
import socket
import re
import hashlib
import time

HOST = '127.0.0.1'
PORT = 22000
DELAY = 1.5
def parse_request(request):
  found = ""
  m = re.search('MD5 of ([a-zA-Z0-9]*) ?', request)
  if m:
    found = m.group(1)
  return found

def get_md5(request):
  return hashlib.md5(request.encode("utf-8")).hexdigest()

def loop_on_requests(s):
  data = s.recv(1024)
  data = data.decode("utf-8").strip()
  parsed = parse_request(data)
  md5 = get_md5(parsed)
  time.sleep(DELAY)
  s.sendall(md5.encode())
  data = s.recv(1024)
  data = data.decode("utf-8").strip()
  parsed = parse_request(data)
  md5 = get_md5(parsed)
  time.sleep(DELAY)
  s.sendall(md5.encode())
  data = s.recv(1024)
  data = data.decode("utf-8").strip()
  parsed = parse_request(data)
  md5 = "6f15828a83a09d8edfa571f78fbedc0b"
  time.sleep(DELAY)
  s.sendall(md5.encode())


if __name__== "__main__":
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'start')
    loop_on_requests(s)
    s.shutdown(socket.SHUT_RDWR)
    s.close() 
