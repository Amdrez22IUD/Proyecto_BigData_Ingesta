# Proyecto Integrador Big Data — EA1 (Ingestión) y EA2 (Preprocesamiento)

## 1. Descripción de la Solución

Este proyecto implementa las etapas de **Ingesta de Datos** y **Preprocesamiento y Limpieza** en un entorno que simula una plataforma de Big Data en la nube.

La solución automatiza el siguiente flujo:
* **Fase 1 (Ingesta):** Extracción de información desde una API externa y su almacenamiento en una base de datos analítica SQLite (simulando el entorno cloud).
* **Fase 2 (Limpieza):** Análisis exploratorio, eliminación de duplicados, manejo de valores nulos, corrección de tipos de datos y estandarización utilizando Pandas.
* **Fase 3 (Evidencias):** Generación de archivos de auditoría y muestras en Excel para garantizar la trazabilidad de los datos limpios.

---

## 2. Estructura del Proyecto

El repositorio sigue la siguiente estructura jerárquica:

```text
[PROYECTO_BIGDATA]
├── .github/workflows/
│   └── bigdata.yml             # Configuración de automatización (GitHub Actions)
├── src/
│   ├── ingestion.py            # Script EA1: conexión, extracción y carga
│   ├── cleaning.py             # Script EA2: preprocesamiento y limpieza
│   ├── db/
│   │   └── ingestion.db        # Base de datos SQLite (Simulación Nube)
│   ├── static/auditoria/
│   │   ├── ingestion.txt       # Reporte de auditoría de ingesta
│   │   └── cleaning_report.txt # Reporte de impacto de la limpieza
│   └── xlsx/
│       ├── ingestion.xlsx      # Muestra de registros de ingesta
│       └── cleaned_data.xlsx   # Muestra representativa de datos limpios
├── setup.py                    # Gestión de dependencias
└── README.md                   # Trazabilidad y documentación del proceso
```

---

## 3. Instrucciones de Ejecución

Para clonar e instalar las dependencias necesarias del proyecto localmente:

### Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/tu-repositorio.git
```

### Instalar dependencias

```bash
pip install -e .
```

### Ejecutar el script de ingesta

```bash
python src/ingestion.py
```

---

## 4. Automatización (GitHub Actions)

Se ha configurado un *workflow* en GitHub Actions para ejecutar automáticamente el proceso de ingesta.
El flujo realiza las siguientes acciones:

* Instala Python y las dependencias necesarias (`requests`, `pandas`, `openpyxl`).
* Ejecuta el script de lectura del API y actualiza la base de datos SQLite.
* Genera el archivo de muestra (`.xlsx`) y el reporte de auditoría (`.txt`).
* Guarda los archivos generados como evidencia en el repositorio para facilitar su revisión.

---

## 5. Trazabilidad y Auditoría

El archivo de auditoría `ingestion.txt` realiza una comparación directa entre:

* Los registros obtenidos del API.
* Los registros almacenados en la base de datos SQLite.

Este reporte detalla el número de registros extraídos y confirma la integridad de los datos, validando que la sincronización fue exitosa.
