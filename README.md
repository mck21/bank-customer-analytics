# Proyecto de Análisis Exploratorio de Datos (EDA)

Este proyecto realiza un análisis exploratorio de datos utilizando Python, enfocado en el análisis de datos bancarios y detalles de clientes.

## Estructura del Proyecto

```
├── data/                   # Carpeta con los datos originales
├── notebooks/             # Jupyter notebooks para el análisis
├── src/                   # Código fuente Python
│   ├── data/             # Scripts para procesamiento de datos
│   └── visualization/    # Scripts para visualización
├── results/              # Resultados del análisis
│   ├── figures/         # Gráficos generados
│   └── reports/         # Reportes generados
└── requirements.txt      # Dependencias del proyecto
```

## Datos

El proyecto utiliza dos conjuntos de datos:
1. `customer-details.xlsx`: Detalles de clientes
2. `bank-additional.csv`: Datos bancarios adicionales

## Requisitos

- Python 3.8+
- Dependencias listadas en `requirements.txt`

## Instalación

1. Clonar el repositorio
2. Crear un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```
3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ``` 