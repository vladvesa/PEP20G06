from communicator import Server
from communicator import Client

server = Server("localhost", 8080)
client = Client("localhost", 8080)

print(server.base)
print(server.prime)
server.start()
client.start()
