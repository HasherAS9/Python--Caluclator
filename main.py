from tkinter import Tk, Entry, Button, StringVar


class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.config(bg="black")
        master.geometry("357x410+0+0")
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ""
        Entry(width=25, bg="red", font=("Agency FB", 28), textvariable=self.equation).place(x=0, y=0)

        Button(width=15, height=4, text="(", relief="flat", bg="#FFFFFF", command=lambda: self.show("(")).place(x=0, y=50)
        Button(width=15, height=4, text=")", relief="flat", bg="#FFFFFF", command=lambda: self.show(")")).place(x=90, y=50)
        Button(width=15, height=4, text="C", relief="flat", bg="#FFFFFF", command=lambda: self.clear()).place(x=178, y=50)
        Button(width=15, height=4, text="1", relief="flat", bg="#FFFFFF", command=lambda: self.show(1)).place(x=0, y=122)
        Button(width=15, height=4, text="2", relief="flat", bg="#FFFFFF", command=lambda: self.show(2)).place(x=90, y=122)
        Button(width=15, height=4, text="3", relief="flat", bg="#FFFFFF", command=lambda: self.show(3)).place(x=178, y=122)
        Button(width=15, height=4, text="4", relief="flat", bg="#FFFFFF", command=lambda: self.show(4)).place(x=0, y=194)
        Button(width=15, height=4, text="5", relief="flat", bg="#FFFFFF", command=lambda: self.show(5)).place(x=90, y=194)
        Button(width=15, height=4, text="6", relief="flat", bg="#FFFFFF", command=lambda: self.show(6)).place(x=178, y=194)
        Button(width=15, height=4, text="7", relief="flat", bg="#FFFFFF", command=lambda: self.show(7)).place(x=0, y=266)
        Button(width=15, height=4, text="8", relief="flat", bg="#FFFFFF", command=lambda: self.show(8)).place(x=90, y=266)
        Button(width=15, height=4, text="9", relief="flat", bg="#FFFFFF", command=lambda: self.show(9)).place(x=178, y=266)
        Button(width=15, height=4, text="0", relief="flat", bg="#FFFFFF", command=lambda: self.show(0)).place(x=90, y=338)
        Button(width=15, height=4, text=".", relief="flat", bg="#FFFFFF", command=lambda: self.show(".")).place(x=178, y=338)
        Button(width=15, height=4, text="%", relief="flat", bg="#FFFFFF", command=lambda: self.show("%")).place(x=0, y=338)
        Button(width=10, height=4, text="+", relief="flat", bg="#FFFFFF", command=lambda: self.show("+")).place(x=290, y=50)
        Button(width=10, height=4, text="-", relief="flat", bg="#FFFFFF", command=lambda: self.show("-")).place(x=290, y=122)
        Button(width=10, height=4, text="x", relief="flat", bg="#FFFFFF", command=lambda: self.show("*")).place(x=290, y=194)
        Button(width=10, height=4, text="/", relief="flat", bg="#FFFFFF", command=lambda: self.show("/")).place(x=290, y=266)
        Button(width=10, height=4, text="=", relief="flat", bg="red", command=lambda: self.solve()).place(x=290, y=338)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ""
        self.equation.set(self.entry_value)

    def solve(self):
        result = eval(self.entry_value)
        self.equation.set(result)


root = Tk()
obj = Calculator(root)
root.mainloop()
