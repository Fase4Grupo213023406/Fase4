# Pedir todos los datos al cliente.
class Cliente:

    # Clase que representa a un cliente.
    def __init__(self, id_cliente, nombre, correo, telefono):

        # La asignación llama a los setters
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    # ---------------- ID CLIENTE ----------------

    @property
    def id_cliente(self):
        return self._id_cliente

    @id_cliente.setter
    def id_cliente(self, valor):

        # Validar ID positivo
        if not isinstance(valor, int) or valor <= 0:

            raise ValueError(
                "El ID debe ser un número entero positivo."
            )

        self._id_cliente = valor

    # ---------------- NOMBRE ----------------

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):

        # No permitir nombres vacíos
        if not valor or valor.strip() == "":

            raise ValueError(
                "El nombre no puede estar vacío."
            )

        self._nombre = valor

    # ---------------- CORREO ----------------

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, valor):

        # Validar correo
        if "@" not in valor or "." not in valor:

            raise ValueError(
                "El correo electrónico no es válido."
            )

        self._correo = valor

    # ---------------- TELÉFONO ----------------

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):

        # Validar longitud del teléfono
        if len(valor) < 7:

            raise ValueError(
                "El número de teléfono no es válido."
            )

        self._telefono = valor

    # ---------------- MOSTRAR INFORMACIÓN ----------------

    def __str__(self):

        return (
            f"Cliente: {self.nombre} "
            f"(ID: {self.id_cliente})"
        )