import tkinter as tk
def addItem():
  if e1.get() != "":
    listbox.insert(tk.END,e1.get())
    e1.delete(0,tk.END)
def removeItem():
  listbox.delete(tk.ANCHOR)
root=tk.Tk()
root.title("Project")
root.geometry("200x200")
e1=tk.Entry(root)
e1.pack()
tk.Button(root,text='Add',command=addItem).pack()
tk.Button(root,text='Remove',command=removeItem).pack()
listbox=tk.Listbox(root)
listbox.pack()
root.mainloop()