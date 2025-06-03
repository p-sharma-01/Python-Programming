import tkinter as tk
class ItemListApp:
  def __init__(self,root):
    self.root=root
    self.root.title("List Items")
    self.createapp()
  def createapp(self):
      self.e1=tk.Entry(root)
      self.e1.pack()
      tk.Button(root,text='Add',command=self.addItem).pack()
      tk.Button(root,text='Remove',command=self.removeItem).pack()
      self.list=tk.Listbox(root)
      self.list.pack()
  def addItem(self):
      if self.e1.get() != "":
        self.list.insert(tk.END,self.e1.get())
        self.e1.delete(0,tk.END)
  def removeItem(self):
      self.list.delete(tk.ANCHOR)
if __name__=="__main__":
  root=tk.Tk()
  i=ItemListApp(root)
  root.geometry("200x200")
  root.mainloop()
