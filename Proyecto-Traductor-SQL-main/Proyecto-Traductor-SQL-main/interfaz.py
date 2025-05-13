import tkinter as tk
from tkinter import messagebox
from main import traducir  # Importa la función traducir del archivo main.py

def procesar():
    consulta = entry.get().upper()  # Tomar la entrada y convertir a mayúsculas
    if consulta:
        try:
            consulta_sql = traducir(consulta)
            actualizar_resultado(consulta_sql)  # Actualizar el texto en result_text
        except Exception as e:
            messagebox.showerror("Error", f"Error al procesar la consulta: {e}")
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingresa una consulta válida.")

# Crear la ventana principal
root = tk.Tk()
root.title("Traductor SQL")
root.geometry("600x400")
root.config(bg="#f0f0f0")  # Fondo de color gris claro

# Instrucciones en la interfaz
instructions = tk.Label(
    root,
    text="Escribe tu consulta en letras mayusculas",
    font=("Arial", 14),
    bg="#f0f0f0",
    fg="#333333",
    width=50,  # Ancho ajustado para centrar el texto
    height=2   # Alto ajustado para centrar el texto
)
instructions.config(anchor="center")  # Centrar el texto dentro del Label
instructions.pack(pady=20)

exampletxt = tk.Label(
    root,
    text="Ejemplo:\n' MOSTRAR PRODUCTOS CON PRECIO MAYOR A 1000 '",
    font=("Arial", 12),
    bg="#f0f0f0",
    fg="#333333",
    width=50,  # Ancho ajustado para centrar el texto
    height=2   # Alto ajustado para centrar el texto
)
exampletxt.config(anchor="center")  # Centrar el texto dentro del Label
exampletxt.pack(pady=0)

# Campo de entrada
entry = tk.Entry(root, width=50, font=("Arial", 14), bd=2, relief="solid", highlightthickness=2, highlightcolor="#4CAF50")
entry.config(justify="center")  # Centrar el texto en el campo de entrada
entry.pack(pady=10)

# Botón para procesar la entrada
process_button = tk.Button(
    root,
    text="Traducir a SQL",
    command=procesar,
    font=("Arial", 14, "bold"),
    bg="#4CAF50",
    fg="white",
    activebackground="#45a049",  # Color cuando se hace clic
    activeforeground="white",
    relief="flat",
    width=20,
    height=2
)
process_button.pack(pady=20)

# Etiqueta para mostrar el resultado
result_label = tk.Label(
    root,
    text="Consulta SQL:",
    font=("Arial", 12),
    bg="#f0f0f0",
    fg="#333333",
    justify=tk.LEFT
)
result_label.pack(pady=20)

# Cuadro de texto para mostrar la consulta traducida (más grande para facilitar la lectura)
result_text = tk.Label(
    root,
    text="",
    font=("Courier New", 12),
    bg="#f0f0f0",
    fg="#000000",
    height=6,
    width=50,
    relief="solid",
    anchor="nw",
    justify="left",  # Asegurar que el texto en result_text se alinee correctamente
    padx=10,
    pady=10
)
result_text.config(anchor="center")  # Centrar el texto dentro del Label
result_text.pack(pady=10)

# Función que actualiza el texto generado en la consulta
def actualizar_resultado(texto):
    result_text.config(text=texto)

# Ejecutar la interfaz
root.mainloop()
