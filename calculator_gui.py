import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Калькулятор")
        self.window.geometry("360x500")
        self.window.resizable(False, False)
        
        self.expression = ""
        
        self.input_field = tk.Entry(self.window, font=("Arial", 24), borderwidth=0, 
                                  relief="ridge", justify="right", bg="#f0f0f0")
        self.input_field.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipadx=8, ipady=20)
        
        buttons = [
            'C', '±', '%', '÷',
            '7', '8', '9', '×',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.', '='
        ]
        
        operator_color = "#ff9500"
        number_color = "#333333"
        special_color = "#a6a6a6"
        
        row = 1
        col = 0
        
        for button in buttons:
            if button == '0':
                btn = tk.Button(self.window, text=button, font=("Arial", 18, "bold"),
                              padx=20, pady=20, bg=number_color, fg="white",
                              command=lambda x=button: self.on_button_click(x))
                btn.grid(row=row, column=col, columnspan=2, sticky="nsew", padx=2, pady=2)
                col += 1
            else:
                if button in '÷×-+=':
                    color = operator_color
                    fg = "white"
                elif button in 'C±%':
                    color = special_color
                    fg = "black"
                else:
                    color = number_color
                    fg = "white"
                
                btn = tk.Button(self.window, text=button, font=("Arial", 18, "bold"),
                              padx=20, pady=20, bg=color, fg=fg,
                              command=lambda x=button: self.on_button_click(x))
                btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
            
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        for i in range(4):
            self.window.grid_columnconfigure(i, weight=1)
        for i in range(1, 6):
            self.window.grid_rowconfigure(i, weight=1)
        
        self.window.mainloop()
    
    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '±':
            if self.expression and self.expression != '0':
                if self.expression.startswith('-'):
                    self.expression = self.expression[1:]
                else:
                    self.expression = '-' + self.expression
        elif char == '=':
            try:
                result = self.expression.replace('×', '*').replace('÷', '/')
                answer = eval(result)
                self.expression = str(answer)
            except:
                messagebox.showerror("Ошибка", "Неверное выражение")
                self.expression = ""
        else:
            self.expression += char
        
        self.input_field.delete(0, tk.END)
        self.input_field.insert(0, self.expression)


if __name__ == "__main__":
    Calculator()