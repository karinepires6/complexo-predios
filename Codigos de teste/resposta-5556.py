import time
import zmq
import sys
import credenciados as Credenciados

                               
context = zmq.Context()
socket = context.socket(zmq.REP) 
socket.bind("tcp://*:5556")                   


while True:

    coisa = socket.recv_string()
    print(coisa)
    socket.send_string("Permitido")