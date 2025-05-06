# Proyecto de Análisis Exploratorio de Datos (EDA)

Este proyecto realiza un análisis exploratorio de datos utilizando Python, de datos bancarios y detalles de clientes.

## Estructura del Proyecto

```
├── data/                      # Carpeta con los datos originales
│   ├── customer-details.xlsx  # Datos originales de clientes
│   └── bank-additional.csv    # Datos bancarios originales
├── src/                      # Código fuente Python
│   └── data/                 # Scripts para procesamiento de datos
│       └── data_loader.py    # Funciones de carga y análisis básico
├── results/                  # Resultados del análisis
│   ├── customers_clean.csv   # Dataset de clientes procesado
│   └── bank_clean.csv        # Dataset bancario procesado
├── requirements.txt          # Dependencias del proyecto
├── README.md                 # Documentación principal
└── ANALYSIS.md              # Metodología y resultados del análisis
```

## Datos

El proyecto utiliza dos conjuntos de datos:
1. `customer-details.xlsx`: Detalles de clientes
2. `bank-additional.csv`: Datos bancarios adicionales

> [!IMPORTANT]
> Para ver el detalle completo del análisis exploratorio de datos, incluyendo los pasos seguidos, metodología y resultados, consulta el archivo [ANALYSIS.md](ANALYSIS.md).

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

### ¿Por qué usar un entorno virtual?

El uso de un entorno virtual (`venv`) permite aislar las dependencias del proyecto, evitando conflictos con otras versiones de librerías instaladas en el sistema. Esto garantiza que el código funcione de manera consistente en diferentes entornos y facilita la instalación de dependencias específicas sin afectar otros proyectos.  

Al activar el entorno virtual, cualquier paquete instalado con `pip` se almacenará dentro del directorio `venv`, en lugar de instalarse globalmente en el sistema.  
