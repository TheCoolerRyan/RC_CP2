import tkinter as tk

root = tk.Tk()


root.title("Testing")
root.configure(background="orange")

root.minsize(300,300)
root.maxsize(1000,1000)

root.geometry("300x300+100+100")


lable =tk.Label(root, text="This is currently working!", font= ("Times New Roman", 20, "bold"))
lable.config(fg = "blue", background= "orange")
lable.pack()



images = tk.PhotoImage(file = "Notes/GUI with Tkinter/bread4.png")
tk.Label(root, image=images).pack()


#Button stuff
root.count = 0
def add():
    
    root.count += 1
    tk.Label(root, text= root.count).pack()
    


btn = tk.Button(root,text="ADD", command=add)
btn.pack()


root.mainloop()