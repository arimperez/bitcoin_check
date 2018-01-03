from Tkinter import *
import getValue

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.getAmount = Entry()
        self.getAmount.pack()
        self.runButton = Button (text = 'Get Bitcoin Worth', command = self.getValue)
        self.runButton.pack()
        self.worthText = Text(height = 2, width = 20)

        self.worthText.insert(END, "Value: ")
        self.worthText.config(state=DISABLED)
        self.worthText.pack()

    def getValue (self):
        self.worthText.config(state=NORMAL)
        self.worthText.delete('1.0', END)
        self.worthText.insert(END, "Value: ")
        temp = self.getAmount.get()
        usd = getValue.getValue(float(temp))

        self.worthText.insert(END, usd)
        self.worthText.config(state=DISABLED)

root = Tk()

app = Window(root)

root.mainloop()
