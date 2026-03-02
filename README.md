# EA1: Ingestión de Datos desde un API — Proyecto Integrador Big Data

## 1. Descripción de la Solución

Este proyecto implementa la etapa de **ingesta de datos** del proyecto integrador de Big Data.

La solución automatiza:

* La extracción de información desde una API externa.
* Su almacenamiento en una base de datos analítica SQLite.
* La generación de evidencias de integridad para asegurar la calidad de las etapas posteriores de preprocesamiento y modelado.

---

## 2. Estructura del Proyecto

El repositorio sigue la siguiente estructura jerárquica:

```text
[PROYECTO_BIGDATA]
├── .github/workflows/
│   └── bigdata.yml       # Configuración de automatización (GitHub Actions)
├── src/
│   ├── ingestion.py      # Script de conexión, extracción y carga
│   ├── db/
│   │   └── ingestion.db  # Base de datos SQLite analítica
│   ├── static/
│   │   └── auditoria/
│   │       └── ingestion.txt # Reporte de auditoría de registros
│   └── xlsx/
│       └── ingestion.xlsx # Muestra de registros exportada con Pandas
├── setup.py              # Gestión de dependencias del proyecto
└── README.md             # Trazabilidad y documentación del proceso
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
