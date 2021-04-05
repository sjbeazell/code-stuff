#! /usr/bin/env python

import socket

s = socket.socket()

s.connect((<ip address>, <port>))

answer = s.recv(1024)

print answer 

s.close
