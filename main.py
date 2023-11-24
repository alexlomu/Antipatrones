import tkinter as tk
from tkinter import messagebox
import csv

def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        raise ValueError("No se puede dividir entre cero.")

def factorial(num1, num2):
    return num1 ** num2
def calcular():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operacion = selected_operation.get()

        if operacion == '+':
            resultado = suma(num1, num2)
        elif operacion == '-':
            resultado = resta(num1, num2)
        elif operacion == 'x':
            resultado = multiplicacion(num1, num2)
        elif operacion == '/':
            resultado = division(num1, num2)
        elif operacion == '^':
            resultado = factorial(num1,num2)
        else:
            raise ValueError("Operación no soportada")

        label_resultado.config(text=f"Resultado: {resultado}", foreground="green")

        guardar_en_csv(num1,num2,operacion,resultado)
    except ValueError as ve:
        messagebox.showerror("Error de entrada", str(ve))
    except Exception as e:
        messagebox.showerror("Error", str(e))
        label_resultado.config(text="Resultado:", foreground="black")

def guardar_en_csv(num1, num2, operacion, resultado):
    with open('operaciones.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([num1, num2, operacion, resultado])
def set_operation(op):
    selected_operation.set(op)

    # Cambiar el color de fondo del botón seleccionado
    for btn in operation_buttons:
        if btn["text"] == op:
            btn.config(bg="#4caf50")
        else:
            btn.config(bg="#f0f0f0")

# Interfaz gráfica
app = tk.Tk()
app.title("Calculadora")
app.geometry("400x300")
app.resizable(False, False)
app.configure(bg="#f0f0f0")

label_num1 = tk.Label(app, text="Número 1:")
label_num1.grid(row=0, column=0, padx=10, pady=10)

entry_num1 = tk.Entry(app)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

label_num2 = tk.Label(app, text="Número 2:")
label_num2.grid(row=1, column=0, padx=10, pady=10)

entry_num2 = tk.Entry(app)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

# Usar botones para seleccionar la operación
operation_buttons = []

button_suma = tk.Button(app, text="+", command=lambda: set_operation('+'))
button_suma.grid(row=2, column=0, padx=5, pady=10) 
operation_buttons.append(button_suma)

button_resta = tk.Button(app, text="-", command=lambda: set_operation('-'))
button_resta.grid(row=2, column=1, padx=5, pady=10)
operation_buttons.append(button_resta)

button_multiplicacion = tk.Button(app, text="x", command=lambda: set_operation('x'))
button_multiplicacion.grid(row=2, column=3, padx=5, pady=10)
operation_buttons.append(button_multiplicacion)

button_division = tk.Button(app, text="/", command=lambda: set_operation('/'))
button_division.grid(row=3, column=0, padx=5, pady=10)
operation_buttons.append(button_division)

button_division = tk.Button(app, text="^", command=lambda: set_operation('^'))
button_division.grid(row=3, column=1, padx=5, pady=10)
operation_buttons.append(button_division)

button_calcular = tk.Button(app, text="Calcular", command=calcular)
button_calcular.grid(row=4, column=1, columnspan=5, pady=10)

label_resultado = tk.Label(app, text="Resultado:", font=("Helvetica", 14, "bold"))
label_resultado.grid(row=5, column=1, columnspan=5, pady=10)

# Variable para rastrear la operación seleccionada
selected_operation = tk.StringVar()
selected_operation.set('+')

app.mainloop()
