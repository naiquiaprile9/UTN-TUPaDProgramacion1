1
print("--- CAJA DEL KIOSCO ---")

cliente = input("Nombre del cliente: ")
while cliente == "" or not cliente.isalpha():
    print("Error: el nombre debe contener solo letras y no puede estar vacio.")
    cliente = input("Nombre del cliente: ")

cantidad = input("Cantidad de productos: ")
while not cantidad.isdigit() or int(cantidad) <= 0:
    print("Error: ingrese un numero entero positivo mayor que 0.")
    cantidad = input("Cantidad de productos: ")

cantidad = int(cantidad)
total_sin_descuentos = 0
total_con_descuentos = 0.0

for numero_producto in range(1, cantidad + 1):
    precio = input(f"Producto {numero_producto} - Precio: ")
    while not precio.isdigit():
        print("Error: ingrese un precio entero valido.")
        precio = input(f"Producto {numero_producto} - Precio: ")

    precio = int(precio)
    total_sin_descuentos += precio

    descuento = input("Descuento (S/N): ").lower()
    while descuento != "s" and descuento != "n":
        print("Error: ingrese S o N.")
        descuento = input("Descuento (S/N): ").lower()

    if descuento == "s":
        precio_final = precio * 0.90
    else:
        precio_final = precio

    total_con_descuentos += precio_final

ahorro = total_sin_descuentos - total_con_descuentos
promedio = total_con_descuentos / cantidad

print()
print(f"Cliente: {cliente}")
print(f"Total sin descuentos: ${total_sin_descuentos}")
print(f"Total con descuentos: ${total_con_descuentos:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")

#////////////////////////////////////#

2
USUARIO_CORRECTO = "alumno"
CLAVE_CORRECTA = "python123"

print("--- ACCESO AL CAMPUS ---")

intentos = 0
acceso_concedido = False
clave_actual = CLAVE_CORRECTA

while intentos < 3 and not acceso_concedido:
    intentos += 1
    usuario = input(f"Intento {intentos}/3 - Usuario: ")
    clave = input("Clave: ")

    if usuario == USUARIO_CORRECTO and clave == clave_actual:
        acceso_concedido = True
        print("Acceso concedido.")
    else:
        print("Error: credenciales invalidas.")

if not acceso_concedido:
    print("Cuenta bloqueada.")
else:
    salir = False

    while not salir:
        print()
        print("1) Estado 2) Cambiar clave 3) Mensaje 4) Salir")
        opcion = input("Opcion: ")

        while not opcion.isdigit():
            print("Error: ingrese un numero valido.")
            opcion = input("Opcion: ")

        opcion = int(opcion)

        while opcion < 1 or opcion > 4:
            print("Error: opcion fuera de rango.")
            opcion = input("Opcion: ")
            while not opcion.isdigit():
                print("Error: ingrese un numero valido.")
                opcion = input("Opcion: ")
            opcion = int(opcion)

        if opcion == 1:
            print("Inscripto")
        elif opcion == 2:
            nueva_clave = input("Nueva clave: ")
            if len(nueva_clave) < 6:
                print("Error: minimo 6 caracteres.")
            else:
                confirmacion = input("Confirmar clave: ")
                if nueva_clave == confirmacion:
                    clave_actual = nueva_clave
                    print("Clave cambiada correctamente.")
                else:
                    print("Error: las claves no coinciden.")
        elif opcion == 3:
            print("Cada practica te acerca a programar con mas confianza.")
        else:
            salir = True
            print("Sesion finalizada.")

#////////////////////////////////////

3
print("--- AGENDA DE TURNOS ---")

operador = input("Nombre del operador: ")
while operador == "" or not operador.isalpha():
    print("Error: el nombre debe contener solo letras.")
    operador = input("Nombre del operador: ")

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""

salir = False

while not salir:
    print()
    print("Operador:", operador)
    print("1) Reservar turno")
    print("2) Cancelar turno")
    print("3) Ver agenda del dia")
    print("4) Ver resumen general")
    print("5) Cerrar sistema")

    opcion = input("Opcion: ")
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 5:
        print("Error: ingrese un numero entre 1 y 5.")
        opcion = input("Opcion: ")

    opcion = int(opcion)

    if opcion >= 1 and opcion <= 3:
        dia = input("Dia (1=Lunes, 2=Martes): ")
        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            print("Error: ingrese 1 para Lunes o 2 para Martes.")
            dia = input("Dia (1=Lunes, 2=Martes): ")
        dia = int(dia)

    if opcion == 1:
        paciente = input("Nombre del paciente: ")
        while paciente == "" or not paciente.isalpha():
            print("Error: el nombre debe contener solo letras.")
            paciente = input("Nombre del paciente: ")

        if dia == 1:
            repetido = paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4
            if repetido:
                print("Error: el paciente ya tiene turno el lunes.")
            elif lunes1 == "":
                lunes1 = paciente
                print("Turno reservado en Lunes 1.")
            elif lunes2 == "":
                lunes2 = paciente
                print("Turno reservado en Lunes 2.")
            elif lunes3 == "":
                lunes3 = paciente
                print("Turno reservado en Lunes 3.")
            elif lunes4 == "":
                lunes4 = paciente
                print("Turno reservado en Lunes 4.")
            else:
                print("No hay turnos disponibles para Lunes.")
        else:
            repetido = paciente == martes1 or paciente == martes2 or paciente == martes3
            if repetido:
                print("Error: el paciente ya tiene turno el martes.")
            elif martes1 == "":
                martes1 = paciente
                print("Turno reservado en Martes 1.")
            elif martes2 == "":
                martes2 = paciente
                print("Turno reservado en Martes 2.")
            elif martes3 == "":
                martes3 = paciente
                print("Turno reservado en Martes 3.")
            else:
                print("No hay turnos disponibles para Martes.")

    elif opcion == 2:
        paciente = input("Nombre del paciente a cancelar: ")
        while paciente == "" or not paciente.isalpha():
            print("Error: el nombre debe contener solo letras.")
            paciente = input("Nombre del paciente a cancelar: ")

        cancelado = False

        if dia == 1:
            if paciente == lunes1:
                lunes1 = ""
                cancelado = True
            elif paciente == lunes2:
                lunes2 = ""
                cancelado = True
            elif paciente == lunes3:
                lunes3 = ""
                cancelado = True
            elif paciente == lunes4:
                lunes4 = ""
                cancelado = True
        else:
            if paciente == martes1:
                martes1 = ""
                cancelado = True
            elif paciente == martes2:
                martes2 = ""
                cancelado = True
            elif paciente == martes3:
                martes3 = ""
                cancelado = True

        if cancelado:
            print("Turno cancelado correctamente.")
        else:
            print("No se encontro un turno con ese nombre.")

    elif opcion == 3:
        if dia == 1:
            print("--- Agenda Lunes ---")
            print("Turno 1:", lunes1 if lunes1 != "" else "(libre)")
            print("Turno 2:", lunes2 if lunes2 != "" else "(libre)")
            print("Turno 3:", lunes3 if lunes3 != "" else "(libre)")
            print("Turno 4:", lunes4 if lunes4 != "" else "(libre)")
        else:
            print("--- Agenda Martes ---")
            print("Turno 1:", martes1 if martes1 != "" else "(libre)")
            print("Turno 2:", martes2 if martes2 != "" else "(libre)")
            print("Turno 3:", martes3 if martes3 != "" else "(libre)")

    elif opcion == 4:
        lunes_ocupados = 0
        martes_ocupados = 0

        if lunes1 != "":
            lunes_ocupados += 1
        if lunes2 != "":
            lunes_ocupados += 1
        if lunes3 != "":
            lunes_ocupados += 1
        if lunes4 != "":
            lunes_ocupados += 1

        if martes1 != "":
            martes_ocupados += 1
        if martes2 != "":
            martes_ocupados += 1
        if martes3 != "":
            martes_ocupados += 1

        lunes_disponibles = 4 - lunes_ocupados
        martes_disponibles = 3 - martes_ocupados

        print("--- Resumen general ---")
        print(f"Lunes: {lunes_ocupados} ocupados, {lunes_disponibles} disponibles.")
        print(f"Martes: {martes_ocupados} ocupados, {martes_disponibles} disponibles.")

        if lunes_ocupados > martes_ocupados:
            print("Dia con mas turnos: Lunes.")
        elif martes_ocupados > lunes_ocupados:
            print("Dia con mas turnos: Martes.")
        else:
            print("Dia con mas turnos: empate.")

    else:
        salir = True
        print("Sistema cerrado.")

#////////////////////////////////////

4
print("--- ESCAPE ROOM: LA BOVEDA ---")

agente = input("Nombre del agente: ")
while agente == "" or not agente.isalpha():
    print("Error: el nombre debe contener solo letras.")
    agente = input("Nombre del agente: ")

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_seguidas = 0
bloqueo = False

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not bloqueo:
    print()
    print(f"Agente: {agente}")
    print(f"Energia: {energia} | Tiempo: {tiempo} | Cerraduras abiertas: {cerraduras_abiertas}/3")
    print(f"Alarma: {'ON' if alarma else 'OFF'} | Codigo parcial: {codigo_parcial}")
    print("1) Forzar cerradura")
    print("2) Hackear panel")
    print("3) Descansar")

    opcion = input("Opcion: ")
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        print("Error: ingrese un numero entre 1 y 3.")
        opcion = input("Opcion: ")

    opcion = int(opcion)

    if opcion == 1:
        energia -= 20
        tiempo -= 2
        forzar_seguidas += 1

        if forzar_seguidas == 3:
            alarma = True
            print("La cerradura se trabo. Se activo la alarma y no se abrio ninguna cerradura.")
        else:
            if energia < 40:
                riesgo = input("Riesgo de alarma. Elija un numero entre 1 y 3: ")
                while not riesgo.isdigit() or int(riesgo) < 1 or int(riesgo) > 3:
                    print("Error: ingrese un numero entre 1 y 3.")
                    riesgo = input("Riesgo de alarma. Elija un numero entre 1 y 3: ")

                if int(riesgo) == 3:
                    alarma = True
                    print("Se activo la alarma.")

            if not alarma and cerraduras_abiertas < 3:
                cerraduras_abiertas += 1
                print("Cerradura abierta.")

    elif opcion == 2:
        energia -= 10
        tiempo -= 3
        forzar_seguidas = 0

        for paso in range(1, 5):
            codigo_parcial += "A"
            print(f"Hackeo paso {paso}/4 - Codigo: {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            codigo_parcial = ""
            print("El hackeo abrio una cerradura automaticamente.")

    else:
        energia += 15
        if energia > 100:
            energia = 100

        tiempo -= 1
        forzar_seguidas = 0

        if alarma:
            energia -= 10
            print("Descansaste con alarma activa y perdiste energia extra.")
        else:
            print("Descansaste y recuperaste energia.")

    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        bloqueo = True

print()
if cerraduras_abiertas == 3:
    print("VICTORIA: abriste la boveda.")
elif bloqueo:
    print("DERROTA: el sistema se bloqueo por alarma.")
elif energia <= 0 or tiempo <= 0:
    print("DERROTA: te quedaste sin energia o sin tiempo.")


#///////////////////////////////////

5
print("--- BIENVENIDO A LA ARENA ---")

nombre = input("Nombre del Gladiador: ")
while nombre == "" or not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ")

vida_gladiador = 100
vida_enemigo = 100
pociones = 3
danio_ataque_pesado = 15
danio_enemigo = 12
turno_gladiador = True
juego_activo = True

print("=== INICIO DEL COMBATE ===")

while juego_activo and vida_gladiador > 0 and vida_enemigo > 0:
    if turno_gladiador:
        print()
        print(f"{nombre} (HP: {vida_gladiador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
        print("Elige accion:")
        print("1. Ataque Pesado")
        print("2. Rafaga Veloz")
        print("3. Curar")

        opcion = input("Opcion: ")
        while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
            if not opcion.isdigit():
                print("Error: Ingrese un numero valido.")
            else:
                print("Error: opcion fuera de rango.")
            opcion = input("Opcion: ")

        opcion = int(opcion)

        if opcion == 1:
            danio_final = float(danio_ataque_pesado)
            if vida_enemigo < 20:
                danio_final = danio_ataque_pesado * 1.5
                print("Golpe Critico.")

            vida_enemigo -= danio_final
            print(f"Atacaste al enemigo por {danio_final:.1f} puntos de danio.")

        elif opcion == 2:
            print(">> Inicias una rafaga de golpes!")
            for golpe in range(3):
                vida_enemigo -= 5
                print("> Golpe conectado por 5 de danio")

        else:
            if pociones > 0:
                vida_gladiador += 30
                pociones -= 1
                print("Usaste una pocion y recuperaste 30 HP.")
            else:
                print("No quedan pociones!")

        turno_gladiador = False

    if not turno_gladiador and vida_enemigo > 0:
        vida_gladiador -= danio_enemigo
        print(f">> El enemigo contraataca por {danio_enemigo} puntos!")
        turno_gladiador = True

    if vida_gladiador <= 0 or vida_enemigo <= 0:
        juego_activo = False
    elif turno_gladiador:
        print("=== NUEVO TURNO ===")

print()
if vida_gladiador > 0:
    print(f"VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caido en combate.")