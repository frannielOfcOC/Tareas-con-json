from datetime import timedelta
from datetime import datetime
import json
import uuid

#primero creamos una funcion para pedirle al usuario que ingrese el nombre o descripcion de la tarea
#agregamos los datos y lo almacenamos en el archivo .json llamado tareas, como tipo biblioteca.

def crear_tarea(A, B, C, Z, prioridad, HORAS, MINUTOS): #A: nombre de la tarea, B: descripcion de esta, C: la fecha de vencimiento de esta, Z: el area o profesion, por ultimo agregamos 2 variables para obtener las horas y minutos.
  
        tareas = "tareas.json"
        name = A.strip() #strip lo usamos para eliminar los espacios.
        description = B.strip()
        date1 = datetime.now()
        date = date1 + timedelta(days= C, minutes= MINUTOS, hours= HORAS)
        area = Z.strip()
        random_id =str (uuid.uuid4()) #nos otorga un ID ramdon

        try:
         prioridad = int (prioridad.strip())
        except ValueError:
           print("solo numeros")
        
        try:
         with open(tareas, "r", encoding="utf-8") as f:
          datos = json.load(f)

        except FileNotFoundError:
         datos = {}

        if "Tareas" not in datos:
         datos["Tareas"] = []


    #creamos una variables biblioteca, que vamos a almacenar con nombres claves para usarla mas adelante
    
        biblioteca = {"ID": f"{random_id}",
                  "Nombre": f"{name}",
                    "Descripcion": f"{description}", 
                     "fecha actual": date1.isoformat(),
                      "Vencimiento": date.isoformat(),
                        "Area": f"{area}",
                         "prioridad": f"{prioridad}",
                           "estado": "activa"}
        
        datos["Tareas"].append(biblioteca)
        datos["Tareas"].sort(key=lambda tarea: tarea["prioridad"])

        for clave, valor in biblioteca.items():
          print(f"{clave}, {valor}")

    #ahora abrimos el archivo con un with W, para escribir arriba, y si no esta lo crea.
        with open (tareas, "w", encoding="utf-8") as archivo:
         json.dump(datos, archivo, indent=4, ensure_ascii=False) #indet para organizar, ensure para admitir letras como la enie
        
    
        return biblioteca

def imprimir_tareas():
  lista = []
  with open ("tareas.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)
    lista_de_tareas = datos.get("Tareas", [])
    for tarea in lista_de_tareas:
      print("---")
      for clave, valor in tarea.items():
         print (f"{clave}: {valor}")
    print("---")

  print("\n")
  #print(json.dumps(datos, indent=2))


def modificar_tareas (uid, clave, valor):

#primero tengo que abrir el archivo.
#segundo: buscar el uid unico en mi archivo, pero antes de, accedemos a tareas, ya despues dentro de esta:
#tercero, buscar la clave, y por ultimo, cambiar el valor dentro de esa clave.

  try:
      with open('tareas.json', 'r', encoding='utf-8') as archivo:
          datos = json.load(archivo) # load Para cargar desde un archivo
          lista_de_tareas = datos["Tareas"] #accedemos a tareas, lo dejamos asi porque python es inteligente XD
          for dato in lista_de_tareas: #ahora si, ya en tareas 
            if dato.get("ID") == uid: #buscamos el valor ID pero antes de, vamos a hacer varias cositas, como if para solo cambiar lo necesario.
             if clave == "ID":
                print("No se puede bro")
                return None
             elif clave == "prioridad":
                dato[clave] = valor
                datos["Tareas"].sort(key=lambda tarea:  tarea["prioridad"])
             elif clave == "Vencimiento":
                dato[clave] = valor
                dato["prioridad"] = "1"
                datos["Tareas"].sort(key=lambda tarea:  tarea["prioridad"])
                dato["estado"] = "activa"
             elif clave == "fecha actual":
                print("No se puede bro")
             else:
                dato [clave] = valor    

      with open('tareas.json', "w", encoding="utf-8") as archivo_salida:
            json.dump(datos, archivo_salida, indent=4, ensure_ascii=False)


  except IOError:
      print("Error al escribir en el archivo JSON.")
  
"""json.dumps() devuelve el objeto de Python serializado como una cadena JSON. Utiliza dump() 
 cuando necesites guardar datos en un archivo y dumps()
 cuando necesites una cadena para enviar por la red, 
 imprimir en la consola o manipular antes de escribirla"""


def verificar_vencimiento():
    """
    Verifica cada tarea en el archivo JSON y actualiza su estado si ha expirado.
    """
    tareas = "tareas.json"
    
    try:
        with open(tareas, "r+", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            for tarea in datos.get("Tareas", []):
                
                #Comprueba si la tarea ya esta vencida para no procesarla de nuevo
                if tarea.get("estado") == "vencida":
                    continue
                #Convierte la fecha de vencimiento del string a un objeto datetime
                vencimiento = datetime.fromisoformat(tarea["Vencimiento"])
                #Compara la fecha actual con la fecha de vencimiento
                if datetime.now() > vencimiento:
                    tarea["estado"] = "vencida"
                    tarea["prioridad"] = "10"
                    datos["Tareas"].sort(key=lambda tarea:  tarea["prioridad"])
                    print(f"La tarea: {tarea['Nombre']}' con ID: {tarea['ID']}, ha expirado. Estado actualizado.")
                    print("\n")
            
            #Mueve el cursor al inicio del archivo para sobrescribir los datos
            archivo.seek(0)
            
            #Escribe los datos actualizados de nuevo en el archivo JSON
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
            
    except FileNotFoundError:
        print("El archivo 'tareas.json' no existe.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

#Para probar la funcion, puedes llamarla directamente
if __name__ == "__main__":
    verificar_vencimiento()