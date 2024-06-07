
from funcion_lista import *
personas = []

while True:
    persona = datos_persona()
    personas.append(persona)

    respuesta = input("Desea continuar? (si/no): ").lower()
    if respuesta == 'no':
        break
    elif respuesta != 'si':
        print("Respuesta no válida. Por favor, responda 'si' o 'no'.")

nom_ap_ed_csv(personas)
eliminar_persona_menos_caracteres()
print("Datos guardados exitosamente...")
