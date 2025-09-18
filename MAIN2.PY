from funciones import crear_tarea
from funciones import imprimir_tareas
from funciones import modificar_tareas
from datetime import timedelta
from datetime import datetime
from funciones import verificar_vencimiento

print("menu: 1, crear tarea, 2, leer(actualizar), 3, actualizar tarea, 4, salir")

while True:
    menu = input (": ")

    if menu == "1":

        nombre = input ("coloca el nombre de la tarea: ")
        descripcion = input ("coloca la descripcion de la tarea: ")

        dias = int (input ("coloca los dias: "))
        horas = int (input ("coloca las horas: "))
        minutos = int (input ("coloca los minutos: "))

        area = input ("coloca el area de la tarea: ")
        prioridad = input ("coloque la prioridad: ")
        print("\n")

        crear_tarea(A= nombre, B= descripcion, C= dias, HORAS= horas, MINUTOS= minutos, Z= area, prioridad= prioridad)
        print("\n")

    if menu == "2":
        print("\n")
        imprimir_tareas()
        verificar_vencimiento()

    if menu == "3":
        uid = input ("coloque el ID unico: ")
        clave = input ("coloque el dato que quiere cambiar: ")
        if clave == "Vencimiento":
            dias = int (input ("coloca los dias: "))
            horas = int (input ("coloca las horas: "))
            minutos = int (input ("coloca los minutos: "))
            feccha_actual = datetime.now()
            fecha_vencimiento = feccha_actual + timedelta(days=dias, hours=horas, minutes=minutos)
            valor = fecha_vencimiento.isoformat()

        else:
            valor = input("Coloque el nuevo valor: ")

        modificar_tareas(uid=uid, clave=clave, valor=valor)
    
    if menu == "4":
        break


