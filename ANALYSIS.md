# Análisis Exploratorio de Datos - Proyecto Bancario

## 1. Carga de datos
- Implementación de funciones de carga en [data_loader.py](src/data/data_loader.py):
  - `load_customer_data()`: Carga datos de clientes desde Excel
  - `load_bank_data()`: Carga datos bancarios desde CSV
  - `get_basic_info()`: Obtiene información básica del DataFrame
  
- Verificar la estructura con .info(), .head(), .shape().

## 2. Limpieza de datos
- Identificar y manejar valores nulos (.isnull().sum()).
- Eliminar duplicados (.duplicated().sum(), .drop_duplicates()).
- Revisar tipos de datos y convertir si es necesario (.astype()).

## 3. Análisis estadístico
- Resumen estadístico (.describe()).
- Distribución de valores en columnas categóricas (.value_counts()).
- Identificar outliers con boxplots (seaborn.boxplot()).

## 4. Análisis de correlaciones
- Matriz de correlación (df.corr()).
- Mapa de calor con seaborn.heatmap().

## 5. Visualización de datos
- Histogramas (df.hist()).
- Gráficos de barras y dispersión con matplotlib y seaborn.
- Distribución de variables numéricas (sns.kdeplot()).

## 6. Detección de patrones y segmentación
- Análisis de tendencias en el tiempo si hay fechas.
- Agrupación de clientes por características (groupby()).

## 7. Conclusiones y preparación para modelado
- Identificar insights clave.
- Preparar datos limpios para análisis predictivo o machine learning. 