import socket

import tkinter as tk

win = tk.Tk()
win.title("Port Scanner")
win.resizable(False, False)

window_height = 500
window_width = 900

screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

xcord = int((screen_width/2)-(window_width))
ycord = int((screen_height/2)-(window_height/2))

win.geometry("{}x{}+{}+{}".format(window_width, window_height, xcord, ycord))
#x = int(startport)
#y = int(endport) + 1

#for port in range(x, y):
 #   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  #  result = sock.connect_ex((Address, port))
   # if result == 0:
   #     print("Port " + str(port) + " is open")
    #else:
     #   print("Port " + str(port) + " is closed")
    #sock.close()
