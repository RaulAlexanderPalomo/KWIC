from Modelo.kwic_model import KWICModel
from Vista.kwic_view import KWICView
from Controlador.kwic_controller import KWICController

if __name__ == "__main__":
    # Crear el modelo
    model = KWICModel()

    # Crear el controlador sin vista (la vista se asigna adelantr)
    controller = KWICController(model, None)

    # Crear la vista y pasar el controlador
    view = KWICView(controller)

    # Asignar la vista al controlador
    controller.view = view

    # Iniciar la interfaz gráfica
    view.mainloop()
