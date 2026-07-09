planes = {
'F001': ['Plan Básico', 'mensual', 1, False, False, 'libre'],
'F002': ['Plan Full', 'mensual', 1, True, True, 'libre'],
'F003': ['Plan Estudiante', 'trimestral', 3, False, True, 'tarde'],
'F004': ['Plan Senior', 'trimestral', 3, True, False, 'mañana'],
'F005': ['Plan Anual Pro', 'anual', 12, True, True, 'libre'],
'F006': ['Plan Nocturno', 'mensual', 1, False, True, 'noche'],
}
inscripciones = {
'F001': [14990, 30],
'F002': [22990, 10],
'F003': [39990, 0],
'F004': [35990, 6],
'F005': [159990, 2],
'F006': [18990, 15],}

def mostrar_menu():
    print("""
========== MENÚ PRINCIPAL ==========
1. Cupos por tipo de plan
2. Búsqueda de planes por rango de precio
3. Actualizar precio de plan
4. Agregar plan
5. Eliminar plan
6. Salir
=====================================
""")
    
def opcion_menu():
    while True:
        try:
            opmenu = int(input("Ingrese la opción del menú (entre 1 y 6): "))
            if 1 <= opmenu <= 6:
                return opmenu
            else:
                print("Opción inválida. la opción debe ser entre 1 y 6.")

        except ValueError:
            print("Error. Datos ingresados incorrectamente.")

def cupos_tipo(tipo):
    total = 0
    for codigo in planes:
        if planes[codigo][0] == tipo:
            total += inscripciones[codigo][1]
            print(f"La cantidad de cupos para el tipo {tipo} es de: {total}.")
            return True   
        else:
            print("No hay ni una inscripción con el tipo solicitado.")
            return False  

def busqueda_precio(p_min, p_max):

    lista = []
    encontrado = False

    for codigo in inscripciones:
        if p_min <= inscripciones[codigo][0] <= p_max and inscripciones[codigo][1] != 0:
            encontrado == True
            lista.append(f"{planes[codigo][0]}-{codigo}")
        else:
            print("No hay planes en ese rango de precios. ")

    print("Lista de planes encontrados en el rango de precio: ")

    lista.sort()
    for planes in lista:
        print(lista)




def buscar_codigo (codigo): ####################

    for codigo in inscripciones:

        if inscripciones[codigo][0] == codigo:
            return True
        
        else:
            return False

def actualizar_precio(codigo, nuevo_precio):

    buscar_codigo(codigo)

    if codigo == True:
        inscripciones[codigo][0] == nuevo_precio
        print("Precio actualizado correctamente.")
        return True

    else:
        return False
    
def validar_codigo(codigo):

    if codigo == "":
        return False
    else:
        return True
    
def validar_nombre(nombre):

    if nombre == "":
        return False
    else:
        return True
def validar_tipo(tipo):

    if tipo in ("mensual", "trimestral", "anual"):
        return True
    
    else:
        return False
    
def validar_duracion(duracion):

    if duracion < 0:
        return False
    
    else:
        return True
    
def validar_acceso_piscina(acceso_piscina):

    if acceso_piscina == "s" or "n":
        return True
    else:
        return False
    
def validar_incluye_clases(incluye_clases):

    if incluye_clases == "s" or "n":
        return True
    else:
        return False
    
def validar_horario(horario):

    if horario == "":
        return False
    else:
        return True
    
def validar_precio(precio):

    if precio < 0:
        return False
    
    else:
        return True
        

def validar_cupos(cupos):

    if cupos < 0:
        return False
    
    else: 
        return True
    
def agregar_plan(codigo, nombre, tipo, duracion, acceso_piscina, incluye_clases, horario, precio, cupos):

    planes = {
        codigo,
        nombre,
        tipo,
        duracion,
        acceso_piscina,
        incluye_clases,
        horario,
    }

    inscripciones = {
        precio,
        cupos,
    }

def eliminar_plan(codigo):

    buscar_codigo(codigo)

    if codigo in planes:

        del planes[codigo]
        
        if codigo in inscripciones:

            del inscripciones[codigo]
            return True
        
    else:
        return False
    

############# MAIN ###############

while True:

    mostrar_menu()
    opmenu = opcion_menu()

    if opmenu == 1:
        
        tipo = input("Ingrese el tipo de plan: ").strip()

        cupos_tipo(tipo)


    elif opmenu == 2:

        while True:

            try:

                p_min = int(input("Ingrese el precio mínimo: "))

                p_max = int(input("Ingrese el precio máximo: "))

                if p_min < 0 or p_max < 0 or p_max < p_min:
                    print("Valores ingresados incorrectamente, el precio mínimo no puede ser menor a 0, " \
                          "el precio máximo no puede ser menor que 0, el precio máximo no puede ser menor al precio mínimo.")

                busqueda_precio(p_min, p_max)

            except ValueError():
                print("Datos ingresados incorrectamente, debe ingresar valores enteros.")

    elif opmenu == 3:

        while True:
            try:
        
                codigo = input("Ingrese el código a buscar: ").strip().lower()

                nuevo_precio = int(input("Ingrese el precio a actualizar: "))
                
                actualizar_precio(codigo, nuevo_precio)

                

                repetir = input("Desea actualizar otro precio (s/n)?: ").strip().lower()

                if repetir == "s":
                    continue
                else:
                    break

            except ValueError:
                print("Datos ingresados incorrectamente.")

    elif opmenu == 4:

        codigo = input("Ingrese el código: ").strip().lower()
        validar_codigo(codigo)
        if validar_codigo(codigo) == True:
            continue
        else:
            print("El código no puede estar vacío.")

        nombre = input("Ingrese el nombre: ").strip().lower()
        validar_nombre(nombre)
        if nombre == True: 
         
        else:
            print("Error. El nombre no puede estar vacío ni ser sólo espacios en blanco.")

        tipo = input("Ingrese el tipo: ").strip().lower()
        validar_tipo(tipo)
        if validar_tipo(tipo) == True:
            c
        else:
            print("Error. Debe ser exactamente 'mensual', 'Trimestral', 'anual'.")

        try:
            duracion = int(input("Ingrese la duración: "))
            validar_duracion(duracion)
            if duracion == True:
                continue
            else:
                print("Error Debe ser un número entero mayor que 0.")
        
        except ValueError:
            print("Datos ingresados incorrectamente.")
            continue

        acceso_piscina = input("¿Tiene acceso a la piscina (s/n)? ").strip().lower()
        validar_acceso_piscina(acceso_piscina)
        
        if acceso_piscina == "s":
            acceso_piscina == True
            continue
        elif acceso_piscina == "n":
            acceso_piscina == False
            continue
        else:
            print("Datos ingresados incorrectamente, debe ser únicamente 's/n'.")

        incluye_clases = input("¿Incluye clases (s/n)? ").strip().lower()
        validar_incluye_clases(incluye_clases)
        if incluye_clases == "s":
            incluye_clases == True
            continue
        elif incluye_clases == "n":
            incluye_clases == False
            continue
        else:
            print("Datos ingresados incorrectamente, debe ser únicamente 's/n'.")
           

        horario = input("Ingrese el horario: ").strip().lower()
        validar_horario(horario)
        if horario == True:
            continue  
        try:
            precio = int(input("Ingrese el precio (número entero mayor que 0)"))
            validar_precio(precio)
            if precio == True:
                continue
            else:
                print("El precio no puede ser menor que 0.")

            cupos = int(input("Ingrese los cupos (número entero mayor o igual a 0): "))
            validar_cupos(cupos)
            if cupos == True:
                continue
            else:
                print("Error. Los cupos debe ser un número entero mayor o igual a 0.")

        except ValueError:
            print("Error. Datos ingresados incorrectamente.")


        agregar_plan(codigo, nombre, tipo, duracion, acceso_piscina, incluye_clases, horario, precio, cupos)
        
        if agregar_plan == True:
            print("Plan agregado.")

        else:
            print("El código ya existe.")

    elif opmenu == 5:

        codigo = input("Ingrese el código a buscar: ").strip().lower()
        eliminar_plan(codigo)
        if codigo == True:
            print("Plan eliminado.")
        
        else:
            print("Error. El código no existe")

    elif opmenu == 6:

        print("Programa finalizado.")
        break 





    


    
     





    
        



        




