import Tkinter

def unpack(btn):
    btn.pack_forget()

top = Tkinter.Tk()
for i in range(0, 8):
    btn = Tkinter.Button(top, text='Hello', highlightcolor="red")
    btn['command'] = lambda b=btn: unpack(b)
    btn.pack()

top.mainloop()


