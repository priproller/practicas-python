# =============================================================
# Tema 03 · Listas y ciclo for · EJERCICIOS
# python-adso · SENA ADSO
#
# INSTRUCCIONES
#   1. Copia este archivo a tu repositorio practicas-python como:
#        tema-03.py
#   2. Resuelve cada ejercicio debajo de su enunciado.
#   3. Van de fácil a difícil: bronce, plata y oro. Avanza a tu ritmo.
#   4. Súbelo a GitHub con el commit:
#        feat: ejercicios del tema 03
#
# Nombre completo:
# Mi app se llama:
# =============================================================


# =============================================================
# 🥉 BRONCE
# =============================================================

# -------------------------------------------------------------
# EJERCICIO 1 · Lista de invitados
# -------------------------------------------------------------
# Crea una lista con 5 nombres de compañeros de clase.
#   - Muestra el primero y el último (usa las posiciones).
#   - Con un for, saluda a cada persona.
#   - Al final, muestra cuántas personas hay con len().
#
# Así debe verse:
#   Primero: Ana   Último: Sara
#   Hola, Ana. Te damos la bienvenida
#   ...
#   Total de invitados: 5

# Tu código aquí:

# invitados = ["Matías", "Carlos", "Laura", "Andrés", "Sara"]

# print("Primero:", invitados[0], "Último:", invitados[-1])

# for persona in invitados:
#     print(f"Hola, {persona}. Te damos la bienvenida")

# print("Total de invitados:", len(invitados))

# -------------------------------------------------------------
# EJERCICIO 2 · La tabla de multiplicar
# -------------------------------------------------------------
# Pregunta un número con input() y muestra su tabla del 1 al 10
# usando for y range().
#
# Así debe verse (si escribe 7):
#   7 x 1 = 7
#   7 x 2 = 14
#   ...
#   7 x 10 = 70
#
# Pista: range(1, 11) va del 1 al 10.

# Tu código aquí:

# numero = int(input("¿Qué tabla de multiplicar quieres consultar? "))

# for i in range(1, 11):
#     resultado = numero * i
#     print(f"{numero} x {i} = {resultado}")

# =============================================================
# 🥈 PLATA
# =============================================================

# -------------------------------------------------------------
# EJERCICIO 3 · Las notas del trimestre
# -------------------------------------------------------------
# notas = [4.2, 2.9, 3.5, 4.8, 2.5, 3.0]
#   - Con un for, muestra cada nota y si aprobó (>= 3.0) o no.
#   - Cuenta cuántas aprobaron.
#   - Calcula el promedio:  sum(notas) / len(notas)
#
# Así debe verse:
#   4.2 -> aprobó
#   2.9 -> no aprobó
#   ...
#   Aprobaron 4 de 6. Promedio: 3.48

# Tu código aquí:

# notas = [4.2, 2.9, 3.5, 4.8, 2.5, 3.0]
# aprobadas = 0

# for nota in notas:
#     if nota >= 3.0:
#         print(f"{nota} -> aprobó")
#         aprobadas += 1
#     else:
#         print(f"{nota} -> no aprobó")

# promedio = sum(notas) / len(notas)

# print(f"Aprobaron {aprobadas} de {len(notas)}. Promedio: {promedio:.2f}")

# -------------------------------------------------------------
# EJERCICIO 4 · Encuentra el error (1)
# -------------------------------------------------------------
# Este código tiene 3 errores. Corrígelos y explica en un
# comentario qué estaba mal en cada uno.
#
#   colores = ["rojo", "verde", "azul"]
#   print(colores[3])
#   for color in colores
#   print(color)

# Tu código corregido aquí:

colores = ["rojo", "verde", "azul"]

print(colores[2])

for color in colores:
    print(color)

# Error 1: colores[3] no existe; los índices van de 0 a 2.
# Error 2: faltaban los dos puntos (:) al final del for.
# Error 3: print(color) necesitaba sangría para estar dentro del ciclo.

# -------------------------------------------------------------
# EJERCICIO 5 · Encuentra el error (2)
# -------------------------------------------------------------
# Este código debería sumar los precios y mostrar 15000, pero
# muestra 5000. Tiene UN error. Encuéntralo y explica por qué pasa.
#
#   precios = [5000, 5000, 5000]
#   for precio in precios:
#       total = 0
#       total = total + precio
#   print(total)

# Tu código corregido aquí:
# precios = [5000, 5000, 5000]
# total = 0

# for precio in precios:
#     total = total + precio

# print(total)

# ¿Qué pasaba?: total = 0 estaba dentro del for y se reiniciaba
# en cada repetición. Al moverlo antes del ciclo, se acumulan
# correctamente los tres precios.




# =============================================================
# 🥇 ORO
# =============================================================

# -------------------------------------------------------------
# EJERCICIO 6 · La mini tienda
# -------------------------------------------------------------
# Haz un menú con while (como el del tema 02) que guarde
# productos en una lista:
#   1. Agregar producto (pregunta el precio y haz append a la lista)
#   2. Ver productos (muestra cada precio con un for)
#   3. Ver total con IVA (el 19 %)
#   4. Salir
#
# Reto extra: en la opción 3, crea la lista de precios con IVA
# en UNA sola línea con list comprehension.
#
# Pista: crea precios = [] (lista vacía) ANTES del while.

# Tu código aquí:

precios = []
opcion = ""

while opcion != "4":
    print("\n--- MINI TIENDA ---")
    print("1. Agregar producto")
    print("2. Ver productos")
    print("3. Ver total con IVA")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        precio = float(input("Ingresa el precio del producto: "))
        if precio >= 0:
            precios.append(precio)
            print("Producto agregado.")
        else:
            print("El precio no puede ser negativo.")

    elif opcion == "2":
        if len(precios) == 0:
            print("Todavía no hay productos.")
        else:
            for precio in precios:
                print(f"${precio:.2f}")

    elif opcion == "3":
        precios_con_iva = [precio * 1.19 for precio in precios]
        total = sum(precios_con_iva)
        print(f"Total con IVA: ${total:.2f}")

    elif opcion == "4":
        print("Hasta pronto.")

    else:
        print("Opción no válida.")

# =============================================================
# EJERCICIO 7 · LLÉVALO A TU APP  (va en src/app.py de tu app, no aquí)
# =============================================================
# Tu app ya tiene un menú (tema 02). Hoy aprende a GUARDAR
# varios registros mientras está abierta:
#   1. Crea una lista vacía antes del menú. Ejemplos: citas = [],
#      productos = [], metas = [], tareas = [].
#   2. Agrega la opción "Agregar ...": pregunta el dato y haz append.
#   3. Agrega la opción "Ver ...": muéstralos con un for, numerados.
#      Si la lista está vacía, muestra "Todavía no hay registros".
#   4. Muestra cuántos registros hay con len().
#
# Ejemplo para una app de citas de barbería:
#   1. Agendar cita
#   2. Ver citas
#   3. Salir
#   Opción: 2
#   1. Carlos - 10:00
#   2. Valentina - 11:30
#   Total de citas: 2
#
# Pista para numerar: for i in range(len(citas)):
#                         print(f"{i + 1}. {citas[i]}")
#
# OJO: cuando cierras la app, la lista se borra. Guardar en un
# archivo es un tema más adelante.
# =============================================================
