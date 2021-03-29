#!/usr/bin/env python 

import socket 
ip = " "
port = " "


connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect((ip, port))
