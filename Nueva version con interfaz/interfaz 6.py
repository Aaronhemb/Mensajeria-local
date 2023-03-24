# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 19:00:30 2023

@author: oax_r
"""
        
import socket
import threading
import tkinter as tk

HOST = socket.gethostbyname(socket.gethostname())
PORT = 65432
clients = {}

class ServerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Servidor")
        
        # Frame para enviar mensajes
        self.send_frame = tk.Frame(master)
        self.send_frame.pack(side=tk.TOP, fill=tk.X, padx=20, pady=20)
        self.recipient_label = tk.Label(self.send_frame, text="Destinatario:", font=("Helvetica", 16))
        self.recipient_label.pack(side=tk.LEFT, padx=(0, 10))
        self.recipient_entry = tk.Entry(self.send_frame, width=15, font=("Helvetica", 16))
        self.recipient_entry.pack(side=tk.LEFT, padx=(0, 10))
        self.send_button = tk.Button(self.send_frame, text="Enviar", command=self.send_message, font=("Helvetica", 16))
        self.send_button.pack(side=tk.RIGHT)
        
        # Frame para el cuadro de texto del mensaje
        self.message_frame = tk.Frame(master, width=80, height=80)
        self.message_frame.pack(side=tk.TOP, fill=tk.X)
        self.message_entry = tk.Entry(self.message_frame, font=("Helvetica", 16))
        self.message_entry.pack(side=tk.TOP, fill=tk.X)
        self.message_entry.focus_set()

        # Frame para mostrar la lista de clientes
        self.clients_frame = tk.Frame(master)
        self.clients_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=20, pady=20)
        self.clients_label = tk.Label(self.clients_frame, text="Clientes conectados:", font=("Helvetica", 16))
        self.clients_label.pack(side=tk.TOP, padx=(0, 10), pady=(0, 10))
        self.clients_listbox = tk.Listbox(self.clients_frame, font=("Helvetica", 16))
        self.clients_listbox.pack(side=tk.BOTTOM, fill=tk.X)
        # Botón para actualizar la lista de clientes
        self.update_button = tk.Button(self.clients_frame, text="Actualizar", command=self.update_clients_list, font=("Helvetica", 20))
        self.update_button.pack(side=tk.TOP, padx=10, pady=10)


        # Iniciar el servidor
        threading.Thread(target=self.start_server).start()

    def start_server(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            print('Servidor escuchando en', (HOST, PORT))
            while True:
                conn, addr = s.accept()
                threading.Thread(target=self.handle_client_connection, args=(conn, addr)).start()

    def handle_client_connection(self, conn, addr):
        with conn:
            print('Conectado por', addr)
            print('Clientes conectados:', list(clients.keys()))
            client_ip = conn.recv(1024).decode('utf-8')
            clients[client_ip] = conn
            self.clients_listbox.insert(tk.END, client_ip)
            while True:
                pass # No hacemos nada en el bucle, solo esperamos a que el cliente se desconecte
            del clients[client_ip]
            self.clients_listbox.delete(tk.END, tk.END)
            for client in clients:
                self.clients_listbox.insert(tk.END, client)
                self.clients_listbox.see(tk.END)
                
    def send_message(self):
        recipient_ip = self.recipient_entry.get()
        message = self.message_entry.get()
        if recipient_ip == "":
            for client in clients.values():
                client.sendall(message.encode('utf-8'))
        elif recipient_ip in clients:
            s2 = clients[recipient_ip]
            s2.sendall(message.encode('utf-8'))
        self.message_entry.delete(0)                
                
                
    def update_clients_list(self):
        self.clients_listbox.delete(0, tk.END)
        for client in clients:
            self.clients_listbox.insert(tk.END, client)
            self.clients_listbox.see(tk.END)

root = tk.Tk()
gui = ServerGUI(root)
root.mainloop()        
        