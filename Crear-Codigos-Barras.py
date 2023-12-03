import tkinter as tk
from barcode import EAN13
from barcode.writer import ImageWriter
import random

def generate_barcode():
    product_name = product_name_entry.get()
    
    if product_name:
        # Genera un número de 13 dígitos aleatorio
        random_number = str(random.randint(10**12, 10**13 - 1))
        
        barcode_data = random_number
        barcode = EAN13(barcode_data, writer=ImageWriter())
        barcode_filename = f"{product_name}_barcode"
        barcode.save(barcode_filename)
        
        # Agregar el código y el nombre al archivo codigos.txt
        with open("codigos.txt", "a") as file:
            file.write(f"Nombre del Producto: {product_name}, Código de Barras: {barcode_data}\n")
        
        result_label.config(text=f"¡Código de barras generado como {barcode_filename}.png!")
    else:
        result_label.config(text="Por favor, ingrese el nombre del producto.")

# Función para limpiar la entrada y el resultado
def clear_input_and_result():
    product_name_entry.delete(0, tk.END)
    result_label.config(text="")

# Crear una ventana tkinter
window = tk.Tk()
window.title("Generador de Códigos de Barras")

# Etiqueta y campo de entrada para el nombre del producto
product_name_label = tk.Label(window, text="Nombre del Producto:")
product_name_label.pack()
product_name_entry = tk.Entry(window)
product_name_entry.pack()

generate_button = tk.Button(window, text="Generar Código de Barras", command=generate_barcode)
generate_button.pack()

clear_button = tk.Button(window, text="Limpiar", command=clear_input_and_result)
clear_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
