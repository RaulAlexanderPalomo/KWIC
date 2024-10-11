from .rotation_factory import RotationFactory


class KWICController:
    def __init__(self, model, view):
        """Inicializa el controlador conectando el modelo con la vista."""
        self.model = model
        self.view = view

    def generate_kwic(self):
        """Genera KWIC utilizando la estrategia seleccionada y actualiza la vista con los resultados."""
        text = self.view.get_text()
        strategy_type = self.view.get_selected_strategy()
        strategy = RotationFactory.get_strategy(strategy_type)

        result = self.model.generate_kwic(text, strategy)
        self.view.display_result(result)

    def save_to_json(self):
        """Guarda el texto y los resultados KWIC en un archivo JSON."""
        input_text = self.view.get_text()
        kwic_result = self.model.indexed_lines

        if kwic_result:
            path = self.model.save_to_json(input_text, kwic_result)
            self.view.show_message(f"Datos guardados en {path}")
        else:
            self.view.show_message("Primero debe generar el KWIC antes de guardar.")
