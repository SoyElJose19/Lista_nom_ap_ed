import csv
def validar_nombre_apellido(texto):
    if len(texto) < 3:
        print(f"ERROR: {texto.capitalize()} debe tener al menos 3 caracteres")
        return False
    return True

def validar_edad(texto):
    try:
        edad = int(texto)
        if edad < 0:
            print("ERROR: La edad debe ser un número entero positivo")
            return False
        return True
    except ValueError:
        print("ERROR: La edad debe ser un número entero")
        return False

def datos_persona():
    while True:
        nombre = input("Ingrese Nombre: ")
        if validar_nombre_apellido(nombre):
            break

    while True:
        apellido = input("Ingrese Apellido: ")
        if validar_nombre_apellido(apellido):
            break

    while True:
        edad = input("Ingrese Edad: ")
        if validar_edad(edad):
            break

    return [nombre, apellido, edad]

def nom_ap_ed_csv(p_lista_datos):
    archivo = "Lista_nom_ap_ed.csv"
    with open(archivo, "w", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(p_lista_datos)
def eliminar_persona_menos_caracteres():
    archivo = "Lista_nom_ap_ed.csv"
    with open(archivo, "r", newline="") as archivo_csv:
        lector = csv.reader(archivo_csv)
        lista_personas = list(lector)
    
    if len(lista_personas) > 0:
        persona_menos_caracteres = min(lista_personas, key=lambda x: len(x[0]) + len(x[1]))
        lista_personas.remove(persona_menos_caracteres)
        
        with open(archivo, "w", newline="") as archivo_csv:
            escritor = csv.writer(archivo_csv)
            escritor.writerows(lista_personas)
        print(f"Se ha eliminado a {persona_menos_caracteres[0]} {persona_menos_caracteres[1]} del archivo CSV.")
