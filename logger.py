from datetime import datetime


def registrar_log(mensaje):

    try:

        with open("errores.log", "a", encoding="utf-8") as archivo:

            fecha = datetime.now()

            archivo.write(f"[{fecha}] {mensaje}\n")

    except Exception as e:

        print("Error al escribir en el archivo log:", e)