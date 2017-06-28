import tkinter as tk

root = tk.Tk()

def callback(event):
    print("kliknil si na", event.x, event.y)

    

frame = tk.Frame(root, width = 400, height = 400)
frame.bind("<Button-1>", callback)
frame.pack()



root.mainloop()
