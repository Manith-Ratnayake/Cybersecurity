import socket

target_host = '127.0.0.1'
target_port = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))

while True:

    request = input("Enter the message : ")
    client.send(request.encode())
    response = client.recv(4096)

    print(response.decode())
