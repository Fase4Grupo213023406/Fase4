# IMPORTACIONES: Módulos funcionales desarrollados para el equipo
from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada

# --- NOTA ----
# Falta importar el módulo reserva y logger para la integración final.
# Ejemplo: from logger import registrar_log

# LISTAS INTERNAS: Almacenamiento volátil obligatorio
lista_clientes = []
lista_reservas = []

def registrar_usuario():
    """Captura datos de cliente. Aquí solicitamos los datos personales """
    try:
        print("\n ___REGISTRO DE CLIENTE___")
        # Capturamos todos los datos.
        id_c = int(input("Ingrese ID (Solo números): "))
        nom = input("Ingrese nombre completo: ")
        correo = input("Ingrese correo electrónico: ")
        tel = input("Ingrese número de teléfono: ")

        # Creamos el objeto con datos reales. Esto dispara las validaciones en cliente.py 
        nuevo_c = Cliente(id_c, nom, correo, tel)
        lista_clientes.append(nuevo_c)
        print(f"¡Registro exitoso! Bienvenido {nom}.")
        return nuevo_c

# si el ususario  dijita una informacion o formanto int o srt  mal, se guarda el reporte y no deja avanzar.
    except ValueError as e:
        #excepciones .
        print(f"Error detectado en los datos: {e}")
        return None

def adquirir_servicio():
    # Muestra las opciones de servicios funcionales disponibles 
    print("\n **SERVICIOS DISPONIBLES** ")
    # PUEDES AJUSTAR ESTA PARTE, ES SOLO UN EJEMPLO PARA QUE EL MUNU FUNCIONE
    print("1. Sala ($100/h) | 2. Equipo ($50/h) | 3. Asesoría ($200/h)")
    op = input("Seleccione una opción: ")
    
    # Se retornan objetos de las clases especializadas.
    if op == "1": return ReservaSala("Sala Juntas", 100)
    elif op == "2": return AlquilerEquipo("Laptop Pro", 50)
    elif op == "3": return AsesoriaEspecializada("Asesoría IT", 200)
    return None

def menu_principal():
    # Mantiene el sistema activo mediante un bucle While True
    while True:
        try:
            print("\n- MENÚ DE GESTIÓN SOFTWARE FJ -")
            print("1. Adquirir Servicio")
            print("2. Ver mi Información")
            print("3. Salir")
             # importante, en esta seccion deben de completar la seccion de reserva, servicios, y el menu y ajustarlo para que en la seccion de " ver mi informcion"
            # puedoa mostrar los servicios adquiridos, y costos.
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                servicio = adquirir_servicio()
                if servicio:
                    print(f"Seleccionaste: {servicio.nombre}. (Compañeros: Falta calcular costo)")
                else:
                    print("Servicio no válido.")
            
            elif opcion == "2":
                # Muestra los datos capturados en el registro
                print("\n INFORMACIÓN DE CUENTA ")
                for c in lista_clientes: print(c)

            elif opcion == "3":
                print("Saliendo del sistema...")
                break # Rompe el ciclo y finaliza.
            
            else:
                print("Opción fuera de rango.")

        except Exception as e:
            # Garantiza que el programa siga funcionando ante errores.
            print(f"Ocurrió un problema: {e}")
        finally:
            # Bloque obligatorio para flujo constante.
            print("Operación finalizada.")

if __name__ == "__main__":
    print("Sistema Software FJ Iniciado.")

    # Capturar los datos del usuario primero.
    cliente_actual = registrar_usuario()
    
    #  el usuario se registró bien, llamamos al menú
    if cliente_actual:
        menu_principal()
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