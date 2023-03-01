# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 16:03:36 2023

@author: oax_r
"""
import socket
import tkinter as tk
from tkinter import messagebox
import subprocess
import time

HOST = "192.168.0.134"
PORT = 65432

subprocess.Popen(["python", "cliente.py"], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

# Creamos una ventana de Tkinter
root = tk.Tk()
root.withdraw()

while True:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            # Enviamos la dirección IP del cliente al servidor
            s.sendall(socket.gethostbyname(socket.gethostname()).encode('utf-8'))
            while True:
                # Esperamos a recibir un mensaje del servidor
                data = s.recv(1024)
                # Mostramos el mensaje recibido en forma de alerta
                messagebox.showinfo("Mensaje del servidor", data.decode('utf-8'))
    except socket.error:
        time.sleep(1) # Esperamos 1 segundo antes de intentar la conexión nuevamente
