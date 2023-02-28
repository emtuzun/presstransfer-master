import mysql.connector
import socket
import threading
import tkinter as tk
from tkinter import ttk

HEADER = 8
HOST = "0.0.0.0"
PORT = 12345
FORMAT = "utf-8"
ADDR = (HOST, PORT)
DISCONNECT_MESSAGE = "!DISCONNECT"

app = tk.Tk()
app.title("Press Transfer Control Pannel")

app.mainloop()
