import os
import json

class KWICModel:
    def __init__(self):
        """Inicializa el modelo KWIC y configura el directorio de almacenamiento."""
        self.indexed_lines = []
        self.storage_path = os.path.join("KWIC", "kwic_data.json")

    def generate_kwic(self, text, rotation_strategy):
        """Genera el índice KWIC utilizando la estrategia proporcionada y retorna la lista de rotaciones."""
        self.indexed_lines.clear()
        lines = text.strip().split('\n')
        for line in lines:
            words = line.split()
            for i in range(len(words)):
                rotated_line = rotation_strategy.rotate(words, i)
                self.indexed_lines.append(rotated_line)
        return sorted(self.indexed_lines)

    def save_to_json(self, input_text, kwic_result):
        """Guarda el texto original y el resultado KWIC en un archivo JSON."""
        if not os.path.exists("KWIC"):
            os.makedirs("KWIC")  # Crear el directorio si no existe

        data = {
            "input_text": input_text,
            "kwic_result": kwic_result
        }

        with open(self.storage_path, 'a') as json_file:
            json.dump(data, json_file, indent=4)
            json_file.write("\n")

        return self.storage_path

# Estrategias para rotar las palabras
class DefaultRotationStrategy:
    def rotate(self, words, index):
        """Estrategia por defecto: Rota las palabras de la lista."""
        return ' '.join(words[index:] + words[:index])

class ReverseRotationStrategy:
    def rotate(self, words, index):
        """Estrategia de rotación inversa."""
        return ' '.join(reversed(words[index:] + words[:index]))
