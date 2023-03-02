# Description: Main file for the calculator
import tkinter as tk
import math
# create window
class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # create display widget
        self.display = tk.Entry(master, width=30, justify="right", font=("Arial", 16))
        self.display.grid(row=0, column=0, columnspan=6, padx=5, pady=5)

        # create buttons
        self.create_button("(", 1, 0)
        self.create_button(")", 1, 1)
        self.create_button("^", 1, 2)
        self.create_button("sin", 1, 3)
        self.create_button("cos", 1, 4)
        self.create_button("tan", 1, 5)

        self.create_button("7", 2, 0)
        self.create_button("8", 2, 1)
        self.create_button("9", 2, 2)
        self.create_button("/", 2, 3)
        self.create_button("del", 2, 4)
        self.create_button("C", 2, 5)

        self.create_button("4", 3, 0)
        self.create_button("5", 3, 1)
        self.create_button("6", 3, 2)
        self.create_button("*", 3, 3)
        self.create_button("(", 3, 4)
        self.create_button(")", 3, 5)

        self.create_button("1", 4, 0)
        self.create_button("2", 4, 1)
        self.create_button("3", 4, 2)
        self.create_button("-", 4, 3)
        self.create_button("pi", 4, 4)
        self.create_button("e", 4, 5)

        self.create_button("0", 5, 0)
        self.create_button(".", 5, 1)
        self.create_button("=", 5, 2, columnspan=4)
        self.create_button("+", 5, 3)
    # create button widget
    def create_button(self, text, row, column, columnspan=1):
        button = tk.Button(self.master, text=text, width=5, height=2, font=("Arial", 12), command=lambda:self.button_click(text))
        button.grid(row=row, column=column, columnspan=columnspan, padx=5, pady=5)
        button.bind("<Button-1>", self.button_click)
    # create button click event
    def button_click(self, text):
        if text == "C":
            self.display.delete(0, tk.END)
        elif text == "del":
            current = self.display.get()
            self.display.delete(len(current)-1, tk.END)
        elif text == "pi":
            self.display.insert(tk.END, math.pi)
        elif text == "e":
            self.display.insert(tk.END, math.e)
        elif text == "=":
            #error handling
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except ZeroDivisionError:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Infinity")
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error: Invalid input")
        elif text in ["sin", "cos", "tan"]:
            try:
                angle = math.radians(eval(self.display.get()))
                if text == "sin":
                    result = math.sin(angle)
                elif text == "cos":
                    result = math.cos(angle)
                elif text == "tan":
                    result = math.tan(angle)
                self.display.set(str(result))
            except Exception as e:
                self.display.set("Error")
            try:
                result = math.sin(eval(self.display.get()))
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Invalid input")
        elif text == "cos":
            try:
                result = math.cos(eval(self.display.get()))
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Invalid input")
        elif text == "tan":
            try:
                result = math.tan(eval(self.display.get()))
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Invalid input")
        elif text == "^":
            try:
                result = eval(self.display.get())
                if isinstance(result, (int, float)):
                    result = math.pow(result, 2)
                    self.display.delete(0, tk.END)
                    self.display.insert(0, str(result))
                else:
                    raise TypeError
            except TypeError:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Invalid input")    
            else:
                self.display.insert(tk.END, text)
        elif text == "tan":
            try:
                result = math.tan(eval(self.display.get()))
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except ValueError:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Invalid input")
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
            else:
                self.display.insert(tk.END, text)
# create main window
root = tk.Tk()
calc = Calculator(root)
root.mainloop()
