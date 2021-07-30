import tkinter as tk
import threading
import time

root = tk.Tk()

def autosave():
    while True:
        time.sleep(10)

saver = threading.Thread(target=autosave)
saver.start()
root.mainloop()