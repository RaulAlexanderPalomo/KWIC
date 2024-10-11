from Modelo.kwic_model import DefaultRotationStrategy, ReverseRotationStrategy

class RotationFactory:
    @staticmethod
    def get_strategy(strategy_type):
        """Devuelve la estrategia de rotación basada en el tipo seleccionado."""
        if strategy_type == "default":
            return DefaultRotationStrategy()
        elif strategy_type == "reverse":
            return ReverseRotationStrategy()
        else:
            raise ValueError(f"Estrategia desconocida: {strategy_type}")
