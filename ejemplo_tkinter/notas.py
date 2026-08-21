"""
Santander Open Academy — Cursor con Python: desarrollo inteligente con IA
Módulo práctico — GUI de escritorio con Tkinter.

Bloc de notas de escritorio: una ventana con texto multilínea y menú para
abrir, guardar y salir. El script busca demostrar que Python (y Cursor)
no sirven solo para consola o la web: también se puede armar una GUI con
Tkinter, que ya viene con el lenguaje.

El curso lo propone como ejemplo integrador porque una interfaz tiene
mucho código repetitivo (ventana, menú, diálogos de archivo). Ahí la IA
acelera, y tú practicas revisar el resultado: que el menú llame a las
funciones, que Abrir/Guardar lean y escriban el área de texto, y que los
errores de archivo se muestren al usuario. Además introduce un estilo
distinto al de un script lineal: la ventana se queda abierta esperando
clics (programación dirigida por eventos).
"""

import tkinter as tk
from tkinter import filedialog, messagebox


class EditorNotas(tk.Tk):
    """Ventana principal del bloc de notas (también es la app Tk)."""

    def __init__(self):
        # super() inicializa tk.Tk: título, geometría y el loop de eventos.
        super().__init__()

        self.title("Editor de Notas")
        self.geometry("600x400")

        # self. guarda el widget para usarlo en abrir_archivo / guardar_archivo.
        self.text_area = tk.Text(self)
        self.text_area.pack(expand=True, fill=tk.BOTH)

        self.crear_menu()

    def crear_menu(self):
        barra_menu = tk.Menu(self)
        # tearoff=0 evita el menú flotante con línea punteada.
        menu_archivo = tk.Menu(barra_menu, tearoff=0)

        # command=self.abrir_archivo enlaza el clic con el método de esta instancia.
        menu_archivo.add_command(
            label="Abrir",
            command=self.abrir_archivo
        )

        menu_archivo.add_command(
            label="Guardar",
            command=self.guardar_archivo
        )

        menu_archivo.add_separator()

        menu_archivo.add_command(
            label="Salir",
            command=self.quit
        )

        barra_menu.add_cascade(
            label="Archivo",
            menu=menu_archivo
        )

        self.config(menu=barra_menu)

    def abrir_archivo(self):
        filepath = filedialog.askopenfilename(
            filetypes=[
                ("Archivos de texto", "*.txt"),
                ("Todos los archivos", "*.*")
            ]
        )

        if not filepath:
            return

        try:
            with open(filepath, "r", encoding="utf-8") as file:
                contenido = file.read()

            # 1.0 = inicio del Text; tk.END = final.
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, contenido)

        except Exception as e:
            # Archivo binario o sin permiso: la IA suele olvidar este try/except.
            messagebox.showerror(
                "Error",
                f"No se pudo abrir el archivo:\n{e}"
            )

    def guardar_archivo(self):
        filepath = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[
                ("Archivos de texto", "*.txt"),
                ("Todos los archivos", "*.*")
            ]
        )

        if not filepath:
            return

        try:
            contenido = self.text_area.get(1.0, tk.END)

            with open(filepath, "w", encoding="utf-8") as file:
                file.write(contenido)

        except Exception as e:
            messagebox.showerror(
                "Error",
                f"No se pudo guardar el archivo:\n{e}"
            )


if __name__ == "__main__":
    # Solo arranca la GUI si ejecutas este archivo, no si lo importas.
    app = EditorNotas()
    app.mainloop()
