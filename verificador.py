import json
from datetime import datetime

def obtener_tareas_vencidas():
    """
    Lee el archivo de tareas y retorna una lista de las tareas que han expirado.
    Tambien actualiza el estado de estas tareas en el archivo JSON.
    """
    tareas_file = "tareas.json"
    
    try:
        with open(tareas_file, "r+", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            tareas_vencidas = []
            for tarea in datos.get("Tareas", []):
                # Usamos .get() para evitar errores si la clave no existe
                estado_actual = tarea.get("estado", "activa")
                fecha_vencimiento_str = tarea.get("Vencimiento")
                # Procesa solo las tareas activas con una fecha de vencimiento
                if estado_actual == "activa" and fecha_vencimiento_str:
                    try:
                        fecha_vencimiento = datetime.fromisoformat(fecha_vencimiento_str)
                        if datetime.now() > fecha_vencimiento:
                            # Marca la tarea como vencida
                            tarea["estado"] = "vencida"
                            tarea["prioridad"] = "10"
                            datos["Tareas"].sort(key=lambda tarea:  tarea["prioridad"])
                            tareas_vencidas.append(tarea)
                            print(f"Tarea vencida encontrada: {tarea['Nombre']}")
                    except ValueError as e:
                        print(f"Error de formato de fecha en la tarea {tarea.get('ID')}: {e}")
            # Si se encontraron tareas vencidas, sobrescribe el archivo
            if tareas_vencidas:
                archivo.seek(0)
                json.dump(datos, archivo, indent=4, ensure_ascii=False)
            return tareas_vencidas
    except FileNotFoundError:
        print("El archivo 'tareas.json' no se encontro.")
        return []
    except Exception as e:
        print(f"Ocurrio un error inesperado: {e}")
        return []

if __name__ == "__main__":
    vencidas = obtener_tareas_vencidas()
    if vencidas:
        print("Se encontraron las siguientes tareas vencidas:")
        for t in vencidas:
            print(f"- {t['Nombre']} (ID: {t['ID']})")
    else:
        print("No hay tareas vencidas en este momento.")