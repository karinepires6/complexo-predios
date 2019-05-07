import time
import zmq
import sys

                               
context = zmq.Context()
socket = context.socket(zmq.REP) 
socket.bind("tcp://*:5557")                   


while True:

    coisa = socket.recv_string()
    print(coisa)
    socket.send_string("Permitido")