# Proyecto Integrador Big Data — EA1 (Ingestión) y EA2 (Preprocesamiento)

# Proyecto Integrador Big Data — Pipeline Completo (EA1, EA2 y EA3)

## 1. Descripción de la Solución
Este proyecto implementa un pipeline de datos completo simulando un entorno de Big Data en la nube. Automatiza el ciclo de vida del dato en tres fases:
1. **Fase 1 (Ingesta):** Extracción desde API externa a una base de datos SQLite.
2. **Fase 2 (Limpieza):** Preprocesamiento, manejo de nulos y estandarización con Pandas.
3. **Fase 3 (Enriquecimiento):** Integración (Merge/Join) del dataset limpio con múltiples fuentes adicionales de datos (JSON, CSV, TXT) para generar un dataset enriquecido de alto valor.

---

## 2. Estructura del Proyecto
El repositorio contiene la siguiente arquitectura:
```text
[PROYECTO_BIGDATA]
├── .github/workflows/
│   └── bigdata.yml             # Automatización CI/CD
├── src/
│   ├── ingestion.py            # Script EA1
│   ├── cleaning.py             # Script EA2
│   ├── enrichment.py           # Script EA3
│   ├── db/                     # Base de datos SQLite
│   ├── data/                   # Fuentes de datos crudas (JSON, CSV, TXT)
│   ├── static/auditoria/       # Reportes de calidad en cada fase
│   └── xlsx/                   # Datasets exportados en Excel
├── setup.py                    # Gestión de dependencias
└── README.md                   # Documentación principal
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
