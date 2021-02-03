import time
from random import randint
from socket import socket

from communicator import MySecret
from communicator.utils import generate_primes


class Client(MySecret):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        primes = generate_primes(542)
        number_of_primes = len(primes) - 1
        p1 = randint(0, number_of_primes - 2)
        self.base = primes[p1]
        p2 = randint(p1, number_of_primes - 1)
        self.prime = primes[p2]

    def start(self):
        """Start communication client to listen for incoming connections
        :return: None
        """
        self.socket = socket()
        self.socket.connect((self.host, self.port))
        #time.sleep(2)
        self.socket.send(b"message")
        self.socket.close()
        #self.__client_key_exchange()
