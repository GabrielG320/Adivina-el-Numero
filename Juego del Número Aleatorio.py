# ============================================================
# PROYECTO: JUEGO DEL NÚMERO ALEATORIO
# AUTOR: GabrielG320
# ============================================================
# DESCRIPCIÓN: El programa genera un número y el usuario intenta adivinarlo.
#
# LO QUE APRENDÍ Y DESAFÍOS:
# 1. Tuve problemas al principio con el 'input', se me olvidaban los paréntesis ().
# 2. El mayor reto fue el bucle infinito: me quedaba atrapado diciendo 
#    "te quedan X intentos" sin dejar que el usuario escribiera nada.
# 3. Aprendí que para comparar números el código necesita '==' y no solo '='.
#
# TIEMPO DE DESARROLLO: Unas 2 horas de pelearme con los errores hasta que funcionó.
# ============================================================

import random 
while True:
    clave_real = random.randint(1,100)
    print( "pensé un nuevo numero del 1 al 100")
    while True:
        intento=int(input("escribe el numero: "))
        if intento==clave_real:
            print("muy bien lo adivinaste")
            break
        elif intento < clave_real:
            print("el numero es mas grande")
        elif intento > clave_real:
            print("el numero es mas pequeño")
    respuesta = input("Quieres jugar de nuevo? (si/no): ")
    if respuesta=="no":
        break