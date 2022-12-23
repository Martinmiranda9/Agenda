print("-------- AGENDA --------")

def menu():
    print("¿Que operacion desea realizar?\n 1- Buscar contacto.\n 2- Agregar contacto.\n "
          "3- Borrar contacto.\n 4- Modificar contacto.\n 5- Salir.\n")

menu()
operacion = int(input("Ingrese un numero de operacion: "))
print("----------------------------------------------------------------")


agenda = {"Jeremias": ["Jeremias", "Gonzalez", 3512264907, "jeremias148@gmail.com", "Arcor"],
          "Agustin": ["Agustin", "Morales", 3512654789, "agustinmorales10@gmail.com", "Epec"]}


while operacion != 5:
    if operacion == 1:
        print("Buscar por:\n1-Nombre.\n2-Apellido.\n3-Empresa.")
        numero = int(input("Ingrese un numero de operacion: "))
        if numero == 1:
            nombre_buscar = input("Ingrese el nombre para buscar el contacto: ")
            if nombre_buscar in agenda:
                print("--------------------------------")
                print("Nombre:",agenda[nombre_buscar][0])
                print("Apellido:", agenda[nombre_buscar][1])
                print("Telefono:", agenda[nombre_buscar][2])
                print("Email:", agenda[nombre_buscar][3])
                print("Empresa:", agenda[nombre_buscar][4])
                print("--------------------------------")
                break
            else:
                nombre_buscar = input("El contacto no existe en la agenda. Ingrese nuevamente el nombre: ")
            menu()
            operacion = int(input("Ingrese un numero de operacion: "))

        if numero == 2:
            apellido_buscar = input("Ingrese el apellido para buscar: ")
            for apellido in agenda.values():
                if apellido[1] == apellido_buscar:
                    print("--------------------------------")
                    print("Nombre:", apellido[0])
                    print("Apellido:", apellido[1])
                    print("Telefono:", apellido[2])
                    print("Email:", apellido[3])
                    print("Empresa:", apellido[4])
                    print("--------------------------------")
                    break
                else:
                    apellido_buscar = input("El apellido no existe en la agenda")
        if numero == 3:
            empresa_buscar = input("Ingrese el nombre de la empresa para buscar: ")
            for empresa in agenda.values():
                if empresa[4] == empresa_buscar:
                    print("--------------------------------")
                    print("Nombre:", empresa[0])
                    print("Apellido:", empresa[1])
                    print("Telefono:", empresa[2])
                    print("Email:", empresa[3])
                    print("Empresa:", empresa[4])
                    print("--------------------------------")
                    break
                else:
                    empresa_buscar = input("La empresa no existe en la agenda.")
                menu()
                operacion = int(input("Ingrese un numero de operacion: "))


    elif operacion == 2:
        nombre1 = input("Ingrese el nombre para agendar: ")
        datos = []
        datos.append(input("Ingrese el nombre del contacto: "))
        datos.append(input("Ingrese el apellido del contacto: "))
        datos.append(input("Ingrese el telefono del contacto: "))
        datos.append(input("Ingrese el email del contacto: "))
        datos.append(input("Ingrese la empresa del contacto: "))

        agenda[nombre1] = [datos]
        print("El contacto se agrego correctamente. Por favor, revise los datos")
        print("--------------------------------")
        print("Nombre:", datos[0])
        print("Apellido:", datos[1])
        print("Telefono:", datos[2])
        print("Email:", datos[3])
        print("Empresa:", datos[4])
        print("--------------------------------")
        menu()
        operacion = int(input("Ingrese un numero de operacion: "))


    elif operacion == 3:
        borrar_contacto = input("Ingrese el nombre del contacto para eliminar: ")

        while borrar_contacto not in agenda.keys():
            print("El contacto ingresado no existe.")
            borrar_contacto = input("Ingrese de nuevo el nombre del contacto para eliminar: ")
        else:
            del agenda[borrar_contacto]
        print("Contacto eliminado")
        print("----------------------------------------------------------------")
        menu()
        operacion = int(input("Ingrese un numero de operacion: "))

    elif operacion == 4:
        print("----------------------------------------------------------------")
        print("¿Que dato desea modificar?\n1- Nombre.\n2- Apellido.\n3- Numero de telefono.\n4- E-mail\n"
              "5- Empresa")
        numero_modificacion = int(input("Ingrese el numero de dato para modificar: "))
        print("----------------------------------------------------------------")
        nombre_modificacion = input("Ingrese el nombre del contacto para modificar: ")
        print("----------------------------------------------------------------")

        if nombre_modificacion in agenda:
            if numero_modificacion == 1:
                agenda[nombre_modificacion][0] = input("Ingrese el nuevo nombre del contacto: ")
                print("Contacto Modificado", "-----", agenda[nombre_modificacion])
            elif numero_modificacion == 2:
                agenda[nombre_modificacion][1] = input("Ingrese el nuevo apellido del contacto: ")
                print("Contacto Modificado", "-----", agenda[nombre_modificacion])
            elif numero_modificacion == 3:
                agenda[nombre_modificacion][2] = int(input("Ingrese el nuevo numero de telefono del contacto: "))
                print("Contacto Modificado", "-----", agenda[nombre_modificacion])
            elif numero_modificacion == 4:
                agenda[nombre_modificacion][3] = input("Ingrese el nuevo e-mail del contacto: ")
                print("Contacto Modificado", "-----", agenda[nombre_modificacion])
            else:
                agenda[nombre_modificacion][4] = input("Ingrese el nuevo nombre de la empresa del contacto: ")
                print("Contacto Modificado", "-----", agenda[nombre_modificacion])
            break
        else:
            print("El contacto no existe en la agenda")
        print("----------------------------------------------------------------")
        menu()
        operacion = int(input("Ingrese un numero de operacion: "))
else:
    print("Cerrando Agenda...")
    print("¡Muchas gracias!")
