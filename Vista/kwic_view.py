import tkinter as tk
from tkinter import scrolledtext

class KWICView(tk.Tk):
    def __init__(self, controller):
        """Inicializa la ventana principal y los elementos de la interfaz gráfica."""
        super().__init__()
        self.controller = controller
        self.title("KWIC Generator")
        self.geometry("600x600")

        # Etiqueta de entrada
        self.label = tk.Label(self, text="Ingrese el texto:")
        self.label.pack(pady=10)

        # Campo de entrada de texto
        self.text_input = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=70, height=10)
        self.text_input.pack(pady=10)

        # Selector de estrategia
        self.strategy_label = tk.Label(self, text="Seleccione estrategia de rotación:")
        self.strategy_label.pack(pady=5)
        self.strategy_var = tk.StringVar(value="default")
        self.default_rb = tk.Radiobutton(self, text="Por defecto", variable=self.strategy_var, value="default")
        self.reverse_rb = tk.Radiobutton(self, text="Inversa", variable=self.strategy_var, value="reverse")
        self.default_rb.pack()
        self.reverse_rb.pack()

        # Botón para generar KWIC
        self.generate_button = tk.Button(self, text="Generar KWIC", command=self.controller.generate_kwic)
        self.generate_button.pack(pady=10)

        # Botón para guardar en JSON
        self.save_button = tk.Button(self, text="Guardar en JSON", command=self.controller.save_to_json)
        self.save_button.pack(pady=10)

        # Área de texto con desplazamiento para mostrar los resultados
        self.result_area = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=70, height=10)
        self.result_area.pack(pady=10)

    def get_text(self):
        """Obtiene el texto ingresado por el usuario."""
        return self.text_input.get("1.0", tk.END).strip()

    def get_selected_strategy(self):
        """Obtiene la estrategia de rotación seleccionada por el usuario."""
        return self.strategy_var.get()

    def display_result(self, result):
        """Muestra los resultados generados en el área de texto."""
        self.result_area.delete(1.0, tk.END)
        for line in result:
            self.result_area.insert(tk.END, line + '\n')

    def show_message(self, message):
        """Muestra un mensaje en la ventana (para notificaciones)."""
        self.result_area.insert(tk.END, message + '\n')
