# UTN-TUPaDProgramacion1



este es un cambio



1

print("--- CAJA DEL KIOSCO ---")



cliente = input("Nombre del cliente: ")

while cliente == "" or not cliente.isalpha():

&#x20;   print("Error: el nombre debe contener solo letras y no puede estar vacio.")

&#x20;   cliente = input("Nombre del cliente: ")



cantidad = input("Cantidad de productos: ")

while not cantidad.isdigit() or int(cantidad) <= 0:

&#x20;   print("Error: ingrese un numero entero positivo mayor que 0.")

&#x20;   cantidad = input("Cantidad de productos: ")



cantidad = int(cantidad)

total\_sin\_descuentos = 0

total\_con\_descuentos = 0.0



for numero\_producto in range(1, cantidad + 1):

&#x20;   precio = input(f"Producto {numero\_producto} - Precio: ")

&#x20;   while not precio.isdigit():

&#x20;       print("Error: ingrese un precio entero valido.")

&#x20;       precio = input(f"Producto {numero\_producto} - Precio: ")



&#x20;   precio = int(precio)

&#x20;   total\_sin\_descuentos += precio



&#x20;   descuento = input("Descuento (S/N): ").lower()

&#x20;   while descuento != "s" and descuento != "n":

&#x20;       print("Error: ingrese S o N.")

&#x20;       descuento = input("Descuento (S/N): ").lower()



&#x20;   if descuento == "s":

&#x20;       precio\_final = precio \* 0.90

&#x20;   else:

&#x20;       precio\_final = precio



&#x20;   total\_con\_descuentos += precio\_final



ahorro = total\_sin\_descuentos - total\_con\_descuentos

promedio = total\_con\_descuentos / cantidad



print()

print(f"Cliente: {cliente}")

print(f"Total sin descuentos: ${total\_sin\_descuentos}")

print(f"Total con descuentos: ${total\_con\_descuentos:.2f}")

print(f"Ahorro: ${ahorro:.2f}")

print(f"Promedio por producto: ${promedio:.2f}")



\#////////////////////////////////////#



2

USUARIO\_CORRECTO = "alumno"

CLAVE\_CORRECTA = "python123"



print("--- ACCESO AL CAMPUS ---")



intentos = 0

acceso\_concedido = False

clave\_actual = CLAVE\_CORRECTA



while intentos < 3 and not acceso\_concedido:

&#x20;   intentos += 1

&#x20;   usuario = input(f"Intento {intentos}/3 - Usuario: ")

&#x20;   clave = input("Clave: ")



&#x20;   if usuario == USUARIO\_CORRECTO and clave == clave\_actual:

&#x20;       acceso\_concedido = True

&#x20;       print("Acceso concedido.")

&#x20;   else:

&#x20;       print("Error: credenciales invalidas.")



if not acceso\_concedido:

&#x20;   print("Cuenta bloqueada.")

else:

&#x20;   salir = False



&#x20;   while not salir:

&#x20;       print()

&#x20;       print("1) Estado 2) Cambiar clave 3) Mensaje 4) Salir")

&#x20;       opcion = input("Opcion: ")



&#x20;       while not opcion.isdigit():

&#x20;           print("Error: ingrese un numero valido.")

&#x20;           opcion = input("Opcion: ")



&#x20;       opcion = int(opcion)



&#x20;       while opcion < 1 or opcion > 4:

&#x20;           print("Error: opcion fuera de rango.")

&#x20;           opcion = input("Opcion: ")

&#x20;           while not opcion.isdigit():

&#x20;               print("Error: ingrese un numero valido.")

&#x20;               opcion = input("Opcion: ")

&#x20;           opcion = int(opcion)



&#x20;       if opcion == 1:

&#x20;           print("Inscripto")

&#x20;       elif opcion == 2:

&#x20;           nueva\_clave = input("Nueva clave: ")

&#x20;           if len(nueva\_clave) < 6:

&#x20;               print("Error: minimo 6 caracteres.")

&#x20;           else:

&#x20;               confirmacion = input("Confirmar clave: ")

&#x20;               if nueva\_clave == confirmacion:

&#x20;                   clave\_actual = nueva\_clave

&#x20;                   print("Clave cambiada correctamente.")

&#x20;               else:

&#x20;                   print("Error: las claves no coinciden.")

&#x20;       elif opcion == 3:

&#x20;           print("Cada practica te acerca a programar con mas confianza.")

&#x20;       else:

&#x20;           salir = True

&#x20;           print("Sesion finalizada.")



\#////////////////////////////////////



3

print("--- AGENDA DE TURNOS ---")



operador = input("Nombre del operador: ")

while operador == "" or not operador.isalpha():

&#x20;   print("Error: el nombre debe contener solo letras.")

&#x20;   operador = input("Nombre del operador: ")



lunes1 = ""

lunes2 = ""

lunes3 = ""

lunes4 = ""

martes1 = ""

martes2 = ""

martes3 = ""



salir = False



while not salir:

&#x20;   print()

&#x20;   print("Operador:", operador)

&#x20;   print("1) Reservar turno")

&#x20;   print("2) Cancelar turno")

&#x20;   print("3) Ver agenda del dia")

&#x20;   print("4) Ver resumen general")

&#x20;   print("5) Cerrar sistema")



&#x20;   opcion = input("Opcion: ")

&#x20;   while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 5:

&#x20;       print("Error: ingrese un numero entre 1 y 5.")

&#x20;       opcion = input("Opcion: ")



&#x20;   opcion = int(opcion)



&#x20;   if opcion >= 1 and opcion <= 3:

&#x20;       dia = input("Dia (1=Lunes, 2=Martes): ")

&#x20;       while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:

&#x20;           print("Error: ingrese 1 para Lunes o 2 para Martes.")

&#x20;           dia = input("Dia (1=Lunes, 2=Martes): ")

&#x20;       dia = int(dia)



&#x20;   if opcion == 1:

&#x20;       paciente = input("Nombre del paciente: ")

&#x20;       while paciente == "" or not paciente.isalpha():

&#x20;           print("Error: el nombre debe contener solo letras.")

&#x20;           paciente = input("Nombre del paciente: ")



&#x20;       if dia == 1:

&#x20;           repetido = paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4

&#x20;           if repetido:

&#x20;               print("Error: el paciente ya tiene turno el lunes.")

&#x20;           elif lunes1 == "":

&#x20;               lunes1 = paciente

&#x20;               print("Turno reservado en Lunes 1.")

&#x20;           elif lunes2 == "":

&#x20;               lunes2 = paciente

&#x20;               print("Turno reservado en Lunes 2.")

&#x20;           elif lunes3 == "":

&#x20;               lunes3 = paciente

&#x20;               print("Turno reservado en Lunes 3.")

&#x20;           elif lunes4 == "":

&#x20;               lunes4 = paciente

&#x20;               print("Turno reservado en Lunes 4.")

&#x20;           else:

&#x20;               print("No hay turnos disponibles para Lunes.")

&#x20;       else:

&#x20;           repetido = paciente == martes1 or paciente == martes2 or paciente == martes3

&#x20;           if repetido:

&#x20;               print("Error: el paciente ya tiene turno el martes.")

&#x20;           elif martes1 == "":

&#x20;               martes1 = paciente

&#x20;               print("Turno reservado en Martes 1.")

&#x20;           elif martes2 == "":

&#x20;               martes2 = paciente

&#x20;               print("Turno reservado en Martes 2.")

&#x20;           elif martes3 == "":

&#x20;               martes3 = paciente

&#x20;               print("Turno reservado en Martes 3.")

&#x20;           else:

&#x20;               print("No hay turnos disponibles para Martes.")



&#x20;   elif opcion == 2:

&#x20;       paciente = input("Nombre del paciente a cancelar: ")

&#x20;       while paciente == "" or not paciente.isalpha():

&#x20;           print("Error: el nombre debe contener solo letras.")

&#x20;           paciente = input("Nombre del paciente a cancelar: ")



&#x20;       cancelado = False



&#x20;       if dia == 1:

&#x20;           if paciente == lunes1:

&#x20;               lunes1 = ""

&#x20;               cancelado = True

&#x20;           elif paciente == lunes2:

&#x20;               lunes2 = ""

&#x20;               cancelado = True

&#x20;           elif paciente == lunes3:

&#x20;               lunes3 = ""

&#x20;               cancelado = True

&#x20;           elif paciente == lunes4:

&#x20;               lunes4 = ""

&#x20;               cancelado = True

&#x20;       else:

&#x20;           if paciente == martes1:

&#x20;               martes1 = ""

&#x20;               cancelado = True

&#x20;           elif paciente == martes2:

&#x20;               martes2 = ""

&#x20;               cancelado = True

&#x20;           elif paciente == martes3:

&#x20;               martes3 = ""

&#x20;               cancelado = True



&#x20;       if cancelado:

&#x20;           print("Turno cancelado correctamente.")

&#x20;       else:

&#x20;           print("No se encontro un turno con ese nombre.")



&#x20;   elif opcion == 3:

&#x20;       if dia == 1:

&#x20;           print("--- Agenda Lunes ---")

&#x20;           print("Turno 1:", lunes1 if lunes1 != "" else "(libre)")

&#x20;           print("Turno 2:", lunes2 if lunes2 != "" else "(libre)")

&#x20;           print("Turno 3:", lunes3 if lunes3 != "" else "(libre)")

&#x20;           print("Turno 4:", lunes4 if lunes4 != "" else "(libre)")

&#x20;       else:

&#x20;           print("--- Agenda Martes ---")

&#x20;           print("Turno 1:", martes1 if martes1 != "" else "(libre)")

&#x20;           print("Turno 2:", martes2 if martes2 != "" else "(libre)")

&#x20;           print("Turno 3:", martes3 if martes3 != "" else "(libre)")



&#x20;   elif opcion == 4:

&#x20;       lunes\_ocupados = 0

&#x20;       martes\_ocupados = 0



&#x20;       if lunes1 != "":

&#x20;           lunes\_ocupados += 1

&#x20;       if lunes2 != "":

&#x20;           lunes\_ocupados += 1

&#x20;       if lunes3 != "":

&#x20;           lunes\_ocupados += 1

&#x20;       if lunes4 != "":

&#x20;           lunes\_ocupados += 1



&#x20;       if martes1 != "":

&#x20;           martes\_ocupados += 1

&#x20;       if martes2 != "":

&#x20;           martes\_ocupados += 1

&#x20;       if martes3 != "":

&#x20;           martes\_ocupados += 1



&#x20;       lunes\_disponibles = 4 - lunes\_ocupados

&#x20;       martes\_disponibles = 3 - martes\_ocupados



&#x20;       print("--- Resumen general ---")

&#x20;       print(f"Lunes: {lunes\_ocupados} ocupados, {lunes\_disponibles} disponibles.")

&#x20;       print(f"Martes: {martes\_ocupados} ocupados, {martes\_disponibles} disponibles.")



&#x20;       if lunes\_ocupados > martes\_ocupados:

&#x20;           print("Dia con mas turnos: Lunes.")

&#x20;       elif martes\_ocupados > lunes\_ocupados:

&#x20;           print("Dia con mas turnos: Martes.")

&#x20;       else:

&#x20;           print("Dia con mas turnos: empate.")



&#x20;   else:

&#x20;       salir = True

&#x20;       print("Sistema cerrado.")



\#////////////////////////////////////



4

print("--- ESCAPE ROOM: LA BOVEDA ---")



agente = input("Nombre del agente: ")

while agente == "" or not agente.isalpha():

&#x20;   print("Error: el nombre debe contener solo letras.")

&#x20;   agente = input("Nombre del agente: ")



energia = 100

tiempo = 12

cerraduras\_abiertas = 0

alarma = False

codigo\_parcial = ""

forzar\_seguidas = 0

bloqueo = False



while energia > 0 and tiempo > 0 and cerraduras\_abiertas < 3 and not bloqueo:

&#x20;   print()

&#x20;   print(f"Agente: {agente}")

&#x20;   print(f"Energia: {energia} | Tiempo: {tiempo} | Cerraduras abiertas: {cerraduras\_abiertas}/3")

&#x20;   print(f"Alarma: {'ON' if alarma else 'OFF'} | Codigo parcial: {codigo\_parcial}")

&#x20;   print("1) Forzar cerradura")

&#x20;   print("2) Hackear panel")

&#x20;   print("3) Descansar")



&#x20;   opcion = input("Opcion: ")

&#x20;   while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:

&#x20;       print("Error: ingrese un numero entre 1 y 3.")

&#x20;       opcion = input("Opcion: ")



&#x20;   opcion = int(opcion)



&#x20;   if opcion == 1:

&#x20;       energia -= 20

&#x20;       tiempo -= 2

&#x20;       forzar\_seguidas += 1



&#x20;       if forzar\_seguidas == 3:

&#x20;           alarma = True

&#x20;           print("La cerradura se trabo. Se activo la alarma y no se abrio ninguna cerradura.")

&#x20;       else:

&#x20;           if energia < 40:

&#x20;               riesgo = input("Riesgo de alarma. Elija un numero entre 1 y 3: ")

&#x20;               while not riesgo.isdigit() or int(riesgo) < 1 or int(riesgo) > 3:

&#x20;                   print("Error: ingrese un numero entre 1 y 3.")

&#x20;                   riesgo = input("Riesgo de alarma. Elija un numero entre 1 y 3: ")



&#x20;               if int(riesgo) == 3:

&#x20;                   alarma = True

&#x20;                   print("Se activo la alarma.")



&#x20;           if not alarma and cerraduras\_abiertas < 3:

&#x20;               cerraduras\_abiertas += 1

&#x20;               print("Cerradura abierta.")



&#x20;   elif opcion == 2:

&#x20;       energia -= 10

&#x20;       tiempo -= 3

&#x20;       forzar\_seguidas = 0



&#x20;       for paso in range(1, 5):

&#x20;           codigo\_parcial += "A"

&#x20;           print(f"Hackeo paso {paso}/4 - Codigo: {codigo\_parcial}")



&#x20;       if len(codigo\_parcial) >= 8 and cerraduras\_abiertas < 3:

&#x20;           cerraduras\_abiertas += 1

&#x20;           codigo\_parcial = ""

&#x20;           print("El hackeo abrio una cerradura automaticamente.")



&#x20;   else:

&#x20;       energia += 15

&#x20;       if energia > 100:

&#x20;           energia = 100



&#x20;       tiempo -= 1

&#x20;       forzar\_seguidas = 0



&#x20;       if alarma:

&#x20;           energia -= 10

&#x20;           print("Descansaste con alarma activa y perdiste energia extra.")

&#x20;       else:

&#x20;           print("Descansaste y recuperaste energia.")



&#x20;   if alarma and tiempo <= 3 and cerraduras\_abiertas < 3:

&#x20;       bloqueo = True



print()

if cerraduras\_abiertas == 3:

&#x20;   print("VICTORIA: abriste la boveda.")

elif bloqueo:

&#x20;   print("DERROTA: el sistema se bloqueo por alarma.")

elif energia <= 0 or tiempo <= 0:

&#x20;   print("DERROTA: te quedaste sin energia o sin tiempo.")





\#///////////////////////////////////



5

print("--- BIENVENIDO A LA ARENA ---")



nombre = input("Nombre del Gladiador: ")

while nombre == "" or not nombre.isalpha():

&#x20;   print("Error: Solo se permiten letras.")

&#x20;   nombre = input("Nombre del Gladiador: ")



vida\_gladiador = 100

vida\_enemigo = 100

pociones = 3

danio\_ataque\_pesado = 15

danio\_enemigo = 12

turno\_gladiador = True

juego\_activo = True



print("=== INICIO DEL COMBATE ===")



while juego\_activo and vida\_gladiador > 0 and vida\_enemigo > 0:

&#x20;   if turno\_gladiador:

&#x20;       print()

&#x20;       print(f"{nombre} (HP: {vida\_gladiador}) vs Enemigo (HP: {vida\_enemigo}) | Pociones: {pociones}")

&#x20;       print("Elige accion:")

&#x20;       print("1. Ataque Pesado")

&#x20;       print("2. Rafaga Veloz")

&#x20;       print("3. Curar")



&#x20;       opcion = input("Opcion: ")

&#x20;       while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:

&#x20;           if not opcion.isdigit():

&#x20;               print("Error: Ingrese un numero valido.")

&#x20;           else:

&#x20;               print("Error: opcion fuera de rango.")

&#x20;           opcion = input("Opcion: ")



&#x20;       opcion = int(opcion)



&#x20;       if opcion == 1:

&#x20;           danio\_final = float(danio\_ataque\_pesado)

&#x20;           if vida\_enemigo < 20:

&#x20;               danio\_final = danio\_ataque\_pesado \* 1.5

&#x20;               print("Golpe Critico.")



&#x20;           vida\_enemigo -= danio\_final

&#x20;           print(f"Atacaste al enemigo por {danio\_final:.1f} puntos de danio.")



&#x20;       elif opcion == 2:

&#x20;           print(">> Inicias una rafaga de golpes!")

&#x20;           for golpe in range(3):

&#x20;               vida\_enemigo -= 5

&#x20;               print("> Golpe conectado por 5 de danio")



&#x20;       else:

&#x20;           if pociones > 0:

&#x20;               vida\_gladiador += 30

&#x20;               pociones -= 1

&#x20;               print("Usaste una pocion y recuperaste 30 HP.")

&#x20;           else:

&#x20;               print("No quedan pociones!")



&#x20;       turno\_gladiador = False



&#x20;   if not turno\_gladiador and vida\_enemigo > 0:

&#x20;       vida\_gladiador -= danio\_enemigo

&#x20;       print(f">> El enemigo contraataca por {danio\_enemigo} puntos!")

&#x20;       turno\_gladiador = True



&#x20;   if vida\_gladiador <= 0 or vida\_enemigo <= 0:

&#x20;       juego\_activo = False

&#x20;   elif turno\_gladiador:

&#x20;       print("=== NUEVO TURNO ===")



print()

if vida\_gladiador > 0:

&#x20;   print(f"VICTORIA! {nombre} ha ganado la batalla.")

else:

&#x20;   print("DERROTA. Has caido en combate.")

