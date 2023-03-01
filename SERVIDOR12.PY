# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 17:30:12 2023

@author: oax_r
"""

import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 65432
clients = {}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print('Servidor escuchando en', (HOST, PORT))
    while True:
        conn, addr = s.accept()
        with conn:
            print('Conectado por', addr)
            print('Clientes conectados:', list(clients.keys()))
            client_ip = conn.recv(1024).decode('utf-8')
            clients[client_ip] = conn
            while True:
                message = input('Ingrese mensaje (escriba "s" para enviar a todos los clientes): ')
                if message == "s":
                    message_all = input('Ingrese mensaje a enviar a todos los clientes: ')
                    for client in clients.values():
                        client.sendall(message_all.encode('utf-8'))
                    print("Mensaje enviado a todos los clientes.")
                else:
                    recipient_ip = input('Ingrese dirección IP del cliente destinatario: ')
                    while recipient_ip not in clients:
                        print(f"No se encontró un cliente con dirección IP {recipient_ip}")
                        recipient_ip = input('Ingrese dirección IP del cliente destinatario: ')
                    s2 = clients[recipient_ip]
                    s2.sendall(message.encode('utf-8'))
                    print("Mensaje enviado.")
