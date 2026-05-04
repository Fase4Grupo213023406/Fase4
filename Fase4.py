# main.py

"""
Sistema Software FJ
Punto de entrada principal del sistema
"""

def ejecutar_sistema():
    print("===================================")
    print("  SISTEMA SOFTWARE FJ INICIADO")
    print("===================================")

    try:
        # Aquí luego se integrarán clientes, servicios y reservas
        print("Sistema ejecutándose correctamente...")

    except Exception as e:
        print("Error en la ejecución:", e)

    finally:
        print("===================================")
        print("  SISTEMA FINALIZADO")
        print("===================================")


# Punto de entrada del programa
if __name__ == "__main__":
    ejecutar_sistema()