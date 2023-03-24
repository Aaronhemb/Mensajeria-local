# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 13:40:48 2023

@author: oax_r
"""

import socket
import tkinter as tk
from tkinter import font
import subprocess
import time

HOST = "192.168.0.135"
PORT = 65432

class CustomMessage(tk.Toplevel):
    def __init__(self, message):
        super().__init__()
        self.geometry("800x600") # Tamaño de la ventana
        self.title("Mensaje del servidor")
        self.text_widget = tk.Text(self, font=font.Font(size=15)) # Fuente del mensaje
        self.text_widget.pack(pady=50)
        self.text_widget.insert(tk.END, message) # Inserta el mensaje con saltos de línea
        self.ok_button = tk.Button(self, text="Aceptar", font=font.Font(size=20), command=self.destroy) # Tamaño del botón
        self.ok_button.pack(pady=50)

subprocess.Popen(["python", "cliente.py"], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

root = tk.Tk()
root.withdraw()

while True:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(socket.gethostbyname(socket.gethostname()).encode('utf-8'))
            while True:
                data = s.recv(1024)
                CustomMessage(data.decode('utf-8')).wait_window() # Mostramos la ventana personalizada
    except socket.error:
        time.sleep(1)
