from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reserva
from logger import registrar_log
from excepciones import ClienteError, ServicioError, ReservaError


# LISTAS INTERNAS: Almacenamiento volátil obligatorio
lista_clientes = []
lista_reservas = []


def registrar_usuario():
    """Captura datos de cliente. Aquí solicitamos los datos personales"""

    try:

        print("\n ___REGISTRO DE CLIENTE___")

        # Capturamos todos los datos.
        id_c = int(input("Ingrese ID (Solo números): "))
        nom = input("Ingrese nombre completo: ")
        correo = input("Ingrese correo electrónico: ")
        tel = input("Ingrese número de teléfono: ")

        # Creamos el objeto con datos reales.
        # Esto dispara las validaciones en cliente.py
        nuevo_c = Cliente(id_c, nom, correo, tel)

        # Guardar cliente
        lista_clientes.append(nuevo_c)

        print(f"¡Registro exitoso! Bienvenido {nom}.")

        return nuevo_c

    # si el usuario dijita una informacion o formato int o str mal,
    # se guarda el reporte y no deja avanzar.
    except ValueError as e:

        registrar_log(str(e))  # se guarda el error en el archivo

        print(f"Error detectado en los datos: {e}")

        return None


def adquirir_servicio():

    # Muestra las opciones de servicios funcionales disponibles
    print("\n **SERVICIOS DISPONIBLES** ")

    # PUEDES AJUSTAR ESTA PARTE,
    # ES SOLO UN EJEMPLO PARA QUE EL MENU FUNCIONE
    print("1. Sala ($100/h)")
    print("2. Equipo ($50/h)")
    print("3. Asesoría ($200/h)")

    op = input("Seleccione una opción: ")

    # Se retornan objetos de las clases especializadas.
    if op == "1":

        return ReservaSala("Sala Juntas", 100)

    elif op == "2":

        return AlquilerEquipo("Laptop Pro", 50)

    elif op == "3":

        return AsesoriaEspecializada("Asesoría IT", 200)

    return None


def menu_principal(cliente_actual):

    # Mantiene el sistema activo mediante un bucle While True
    while True:

        try:

            print("\n- MENÚ DE GESTIÓN SOFTWARE FJ -")
            print("1. Adquirir Servicio")
            print("2. Ver mi Información")
            print("3. Salir")

            # importante, en esta seccion deben de completar
            # la seccion de reserva, servicios, y el menu
            # y ajustarlo para que en la seccion de
            # "ver mi informacion"
            # pueda mostrar los servicios adquiridos y costos.

            opcion = input("Seleccione una opción: ")

            # ---------------------------------------------------
            # OPCIÓN 1  ADQUIRIR SERVICIO
            # ---------------------------------------------------

            if opcion == "1":

                servicio = adquirir_servicio()

                if servicio:

                    # Pedir duración de la reserva
                    duracion = int(
                        input("Ingrese duración en horas: ")
                    )

                    # Crear reserva
                    reserva = Reserva(
                        cliente_actual,
                        servicio,
                        duracion
                    )

                    # Guardar reserva en lista
                    lista_reservas.append(reserva)

                    # Mostrar información de la reserva
                    print("\nRESERVA REALIZADA")
                    print(reserva)

                else:

                    print("Servicio no válido.")

            # ---------------------------------------------------
            # OPCIÓN 2  VER INFORMACIÓN
            # ---------------------------------------------------

            elif opcion == "2":

                print("\n INFORMACIÓN DE CUENTA ")

                # Mostrar cliente
                for c in lista_clientes:

                    print(c)

                print("\n RESERVAS REALIZADAS ")

                # Mostrar reservas
                if len(lista_reservas) == 0:

                    print("No hay reservas registradas.")

                else:

                    for r in lista_reservas:

                        print(r)

            # ---------------------------------------------------
            # OPCIÓN 3  SALIR
            # ---------------------------------------------------

            elif opcion == "3":

                print("Saliendo del sistema...")

                break  # Rompe el ciclo y finaliza.

            else:

                print("Opción fuera de rango.")

        except Exception as e:

            # Garantiza que el programa siga funcionando
            # ante errores.
            registrar_log(str(e))

            print(f"Ocurrió un problema: {e}")

        finally:

            # Bloque obligatorio para flujo constante.
            print("Operación finalizada.")


# ---------------------------------------------------
# PRUEBAS AUTOMÁTICAS
# ---------------------------------------------------

def pruebas_automaticas():

    print("\n===== PRUEBAS AUTOMÁTICAS =====")

    pruebas = [

        # PRUEBAS CORRECTAS
        (1, "Elizabeth", "elizabeth@gmail.com", "1234567", "sala", 2),
        (2, "Luis", "luis@gmail.com", "7654321", "equipo", 3),
        (3, "Alejandro", "alejo16@gmail.com", "3457623", "asesoria", 1),
        (4, "Thomas", "thomas@gmail.com", "9873253", "sala", 4),
        (5, "Marta", "marta@gmail.com", "8345092", "equipo", 2),

        # PRUEBAS INCORRECTAS
        (-1, "Pedro", "pedrogmail.com", "12", "sala", 2),
        (0, "", "correo", "1", "equipo", 3),
        (-5, "Juan", "juan@", "abc", "asesoria", 1),
        ("a", "Karen", "kare.com", "", "sala", 2),
        (10, "", "", "", "equipo", 5)
    ]

    for dato in pruebas:

        try:

            id_c, nombre, correo, telefono, tipo, horas = dato

            # Crear cliente
            cliente = Cliente(
                id_c,
                nombre,
                correo,
                telefono
            )

            # Crear servicio
            if tipo == "sala":

                servicio = ReservaSala(
                    "Sala Juntas",
                    100
                )

            elif tipo == "equipo":

                servicio = AlquilerEquipo(
                    "Laptop",
                    50
                )

            else:

                servicio = AsesoriaEspecializada(
                    "Asesoría IT",
                    200
                )

            # Crear reserva
            reserva = Reserva(
                cliente,
                servicio,
                horas
            )

            print("\nReserva exitosa:")
            print(reserva)

        except Exception as e:

            registrar_log(str(e))

            print(f"\nError detectado: {e}")


# ---------------------------------------------------
# INICIO DEL SISTEMA
# ---------------------------------------------------

if __name__ == "__main__":

    print("Sistema Software FJ Iniciado.")

    # Capturar los datos del usuario primero.
    cliente_actual = registrar_usuario()

    # el usuario se registró bien, llamamos al menú
    if cliente_actual:

        menu_principal(cliente_actual)

    # Ejecutar pruebas automáticas
    pruebas_automaticas()
#--------------------------------------------------------------------------------

# #### ###############------------IMPORTANTE---------------------- 
# --- PLAN DE ACCIÓN PARA EL GRUPO (Sugerencias) ---
    # 1. COMPAÑERO DE RESERVA: Debe crear 'reserva.py' con una clase que reciba 
    #    un objeto Cliente y un objeto Servicio, y gestione el 'estado' (Pendiente/Confirmada) [5, 7].
    
    # 2. COMPAÑERO DE LOGGER: Debe crear 'logger.py' que use 'with open' para 
    #    escribir cada excepción capturada en un archivo 'errores.log' [3, 11].
    
    # 3. COMPAÑERO DE INTEGRACIÓN: Debe crear el bucle 'while True' con el menú 
    #    principal (Venta, Consulta, Reporte) similar al ejemplo dado [8, 10, 12].
    
    # 4. REQUISITO FINAL: No olviden programar la función que ejecute las 
    #    '10 operaciones automáticas' (éxitos y fallos) para la nota final [7].

    # Prueba de captura funcional:

    #DEBEN ASEGURARSE QUE DESPUES DE DIGITAR LOS DATOS, SALGA UN MENU EN DONDE SE PUEDE SELECCIONAR:
   # 1. Informacion personal : pense que aca seria mostrar la informacion del cleinte, los datos y que compro y su valor, que compro
   #2. servivios: lista de servicios que muestre el precicio (se puede en str al lado) que al seleccionr guarde el dato en el usuiaro.
   # 3. Reservas: lo mismo que los servicios.
   # SI HAY ALGUNA MODIFICACION, ALGO, ASEGUREN QUE TODo SE CUMPLA BAJO LA ESTA ESTRUCTIRA O MEJORARLA PARA QUE SEA MAS SIMPLE PERO CUMPLIENDO
   # CON LA GUIA Y TENIENDO EN CUENTA EL TIEMPO DE entrega.