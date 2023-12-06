import tkinter as tk
from barcode import EAN13
from barcode.writer import ImageWriter
from PIL import Image, ImageDraw, ImageFont
import random
import os

def generate_barcode():
    product_name = product_name_entry.get()
    expiration_date = expiration_date_entry.get()
    quantity = quantity_entry.get()
    unit = unit_variable.get()

    if product_name and expiration_date and quantity:
        # Genera un número de 13 dígitos aleatorio para el código de barras
        random_number = str(random.randint(10**12, 10**13 - 1))
        
        barcode_data = random_number
        barcode = EAN13(barcode_data, writer=ImageWriter())
        barcode_filename = f"{product_name}_barcode"
        barcode.save(barcode_filename)
        
        # Crear una imagen con la información
        img = Image.new('RGB', (300, 200), color = (255, 255, 255))
        d = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial.ttf", 12)
        font2 = ImageFont.truetype("arial_bold.ttf", 16)

        d.text((15, 10), f"Mascotienda San Josecito", fill=(0, 0, 0), font=font2)
        d.text((15, 40), f"Producto: {product_name}", fill=(0, 0, 0), font=font)
        d.text((15, 60), f"Cantidad: {quantity} {unit}", fill=(0, 0, 0), font=font)
        d.text((15, 80), f"Fecha de Vencimiento: {expiration_date}", fill=(0, 0, 0), font=font)

        barcode_filepath = "/Users/cecilia/Desktop/Codigos-Barras/"
        barcode_img = Image.open(barcode_filepath + barcode_filename + ".png")
        barcode_img = barcode_img.resize((250,80))
        img.paste(barcode_img, (20, 110))

        img.save(f"{product_name}_etiqueta.png")
        os.remove(barcode_filepath + barcode_filename + ".png")

        with open ("1 codigos.txt", "a") as file:
            file.write(f"Nombre del Producto: {product_name}, Cantidad: {quantity} {unit}, Código de barras: {barcode_data}, Fecha de Vencimiento: {expiration_date} . \n \n")
            
        result_label.config(text=f"¡Etiqueta generada como {product_name}_etiqueta.png!")
    else:
        result_label.config(text="Por favor, complete todos los campos.")

# Función para limpiar la entrada y el resultado
def clear_input_and_result():
    product_name_entry.delete(0, tk.END)
    expiration_date_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)
    result_label.config(text="")

# Crear una ventana tkinter
window = tk.Tk()
window.title("Generador de Etiquetas")

# Etiqueta y campo de entrada para el nombre del producto
product_name_label = tk.Label(window, text="Nombre del Producto:")
product_name_label.pack()
product_name_entry = tk.Entry(window)
product_name_entry.pack()

# Etiqueta y campo de entrada para la fecha de vencimiento
expiration_date_label = tk.Label(window, text="Fecha de Vencimiento:")
expiration_date_label.pack()
expiration_date_entry = tk.Entry(window)
expiration_date_entry.pack()

# Etiqueta y campo de entrada para la cantidad
quantity_label = tk.Label(window, text="Cantidad:")
quantity_label.pack()
quantity_entry = tk.Entry(window)
quantity_entry.pack()

# Opción para elegir gramos o mililitros
unit_variable = tk.StringVar(window)
unit_variable.set("gramos")  # Valor predeterminado
unit_option = tk.OptionMenu(window, unit_variable, "gramos", "kilogramos", "mililitros", "litros")
unit_option.pack()

generate_button = tk.Button(window, text="Generar Etiqueta", command=generate_barcode)
generate_button.pack()

clear_button = tk.Button(window, text="Limpiar", command=clear_input_and_result)
clear_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
