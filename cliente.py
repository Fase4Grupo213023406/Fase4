# Pedir todos los datos al cliente. 
class Cliente:

    # Clase que representa a un cliente. .
    def __init__(self, id_cliente, nombre, correo, telefono):
        # La asignación llama a los setters para validar datos desde el inicio.
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    # @property para asegurar que los datos ingresados sean válidos
    @property
    def id_cliente(self):
        return self._id_cliente # Atributo privado protegido.

    @id_cliente.setter
    def id_cliente(self, valor):
        # Validación: El ID debe ser un número entero positivo.
        if not isinstance(valor, int) or valor <= 0:
            # SUGERENCIA PARA COMPAÑERO DE LOGGER:
            # Aquí se debe llamar a la función de registro de errores.
            raise ValueError("El ID debe ser un número entero positivo.")
        self._id_cliente = valor

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        # Validación: No permitir nombres vacíos.
        if not valor or valor.strip() == "":
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = valor

    # ---EQUIPO ----
    # Compañeros, podrían implementar validaciones adicionales aquí:
    # 1. Validar que el correo contenga un '@' y un '.'.
    # 2. Asegurar que el teléfono tenga una longitud mínima de dígitos.
    # si desean modifacar algo, cambiar la logica, mejorar, pueden hacerlo, pero que no afecte la estructura geneal del proyecto.

    def __str__(self):
        return f"Cliente: {self.nombre} (ID: {self.id_cliente})"