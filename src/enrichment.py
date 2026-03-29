import pandas as pd
import os
import json

# Rutas de entrada y salida
CLEANED_DATA_PATH = 'src/xlsx/cleaned_data.xlsx'
ENRICHED_DATA_PATH = 'src/xlsx/enriched_data.xlsx'
AUDITORIA_PATH = 'src/static/auditoria/enriched_report.txt'

def generar_fuentes_adicionales():
    """Genera archivos de prueba en distintos formatos para la integración"""
    os.makedirs('src/data', exist_ok=True)
    
    # 1. Crear archivo JSON (Nombres de usuario y correos)
    users_data = [{"userId": i, "userName": f"Usuario_{i}", "email": f"user{i}@iudigital.edu.co"} for i in range(1, 15)]
    with open('src/data/users.json', 'w') as f:
        json.dump(users_data, f)
        
    # 2. Crear archivo CSV (Ubicaciones)
    csv_data = "userId,country\n" + "\n".join([f"{i},Colombia" if i%2==0 else f"{i},Mexico" for i in range(1, 15)])
    with open('src/data/locations.csv', 'w') as f:
        f.write(csv_data)
        
    # 3. Crear archivo TXT (Prioridad de la tarea usando separador '|')
    txt_data = "id|priority\n" + "\n".join([f"{i}|Alta" if i%5==0 else f"{i}|Media" for i in range(1, 201)])
    with open('src/data/priorities.txt', 'w') as f:
        f.write(txt_data)
        
    print("Archivos adicionales generados en src/data/ (JSON, CSV, TXT).")

def enriquecer_datos():
    print("Cargando dataset base limpio...")
    # Leemos el Excel que generamos en la EA2
    df_base = pd.read_excel(CLEANED_DATA_PATH)
    registros_iniciales = len(df_base)
    
    print("Cargando fuentes adicionales...")
    df_json = pd.read_json('src/data/users.json')
    df_csv = pd.read_csv('src/data/locations.csv')
    df_txt = pd.read_csv('src/data/priorities.txt', sep='|')
    
    print("Iniciando cruce de datos (Merge/Join)...")
    # Unimos la información basándonos en columnas comunes [cite: 372-373]
    # Cruzamos por userId
    df_enriched = df_base.merge(df_json, on='userId', how='left')
    df_enriched = df_enriched.merge(df_csv, on='userId', how='left')
    # Cruzamos por el id de la tarea
    df_enriched = df_enriched.merge(df_txt, on='id', how='left')
    
    # Llenamos posibles nulos generados en el cruce
    df_enriched = df_enriched.fillna("No asignado")
    registros_finales = len(df_enriched)
    
    # Guardar resultados [cite: 376-377]
    df_enriched.to_excel(ENRICHED_DATA_PATH, index=False)
    
    # Generar reporte de auditoría [cite: 386-387]
    with open(AUDITORIA_PATH, 'w', encoding='utf-8') as f:
        f.write("=== REPORTE DE AUDITORÍA DE ENRIQUECIMIENTO ===\n")
        f.write(f"Registros en dataset base: {registros_iniciales}\n")
        f.write(f"Registros en dataset enriquecido: {registros_finales}\n\n")
        f.write("Operaciones de cruce e integración realizadas:\n")
        f.write("- Left Join con users.json usando 'userId' (Nuevas columnas: userName, email)\n")
        f.write("- Left Join con locations.csv usando 'userId' (Nueva columna: country)\n")
        f.write("- Left Join con priorities.txt usando 'id' (Nueva columna: priority)\n")
        f.write("\nObservaciones: La integración se realizó exitosamente agregando 4 columnas nuevas de 3 formatos distintos, sin pérdida de registros base.\n")
        
    print(f"Proceso completado. Datos guardados en {ENRICHED_DATA_PATH}")
    print(f"Reporte de auditoría guardado en {AUDITORIA_PATH}")

if __name__ == '__main__':
    generar_fuentes_adicionales()
    enriquecer_datos()