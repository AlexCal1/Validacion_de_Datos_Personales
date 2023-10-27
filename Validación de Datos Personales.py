import csv

# Solicitar información personal
cedula = input("Ingrese su cédula: ")
nombre = input("Ingrese su nombre: ")
fechaNac = int(input("Ingrese su fecha de nacimiento: "))
pais = input("Ingrese su país: ")
titulo = input("Ingrese su título: ")
notasG = float(input("Ingrese su nota de grado: "))

# Validar las reglas
regla1 = len(cedula) == 10 and cedula.isdigit()
regla2 = nombre.strip().isalpha()
edad = 2023 - fechaNac
regla3 = pais.lower() in ["colombia", "ecuador", "peru", "argentina", "brasil", "chile", "bolivia", "uruguay", "paraguay", "venezuela"]
regla4 = titulo.lower() in ["ingenieria", "licenciado", "maestria", "doctorado", "otro"]
regla5 = 0 <= notasG <= 10

if not regla1:
    print("Cédula incorrecta")
elif edad >= 40:
    print("No cumple con la edad requerida")
elif not regla3:
    print("País incorrecto")
elif not regla4:
    print("Título incorrecto")
elif not regla5:
    print("La nota de grado debe estar entre 0 y 10")
else:
    # Mostrar todos los datos ingresados por el usuario
    print(f"Cédula: {cedula}")
    print(f"Nombre: {nombre}")
    print(f"Fecha de Nacimiento: {fechaNac}")
    print(f"País: {pais}")
    print(f"Título: {titulo}")
    print(f"Nota de Grado: {notasG}")

    # Guardar los datos en un archivo CSV
    with open('datos_personales.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Cédula", "Nombre", "Fecha de Nacimiento", "País", "Título", "Nota de Grado"])
        writer.writerow([cedula, nombre, fechaNac, pais, titulo, notasG])
        print("Los datos se han guardado en 'datos_personales.csv'")
