# Análisis Exploratorio de Datos - Proyecto Bancario

## 1. Carga de datos
- Implementación de funciones de carga en [data_loader.py](src/data/data_loader.py):
  - `load_customer_data()`: Carga datos de clientes desde Excel
  - `load_bank_data()`: Carga datos bancarios desde CSV. El parámetro index_col=0 indica que la primera columna del CSV se utilizará como índice del DataFrame, si no, el csv se carga de forma errónea
  - `get_basic_info()`: Obtiene información básica del DataFrame

#### Datos de Clientes (customer-details.xlsx):
- Tamaño del dataset: 20,115 filas × 7 columnas
- Columnas disponibles:
  - Unnamed: 0 (índice)
  - Income (ingresos)
  - Kidhome (número de niños)
  - Teenhome (número de adolescentes)
  - Dt_Customer (fecha de registro)
  - NumWebVisitsMonth (visitas web mensuales)
  - ID (identificador único)

#### Datos Bancarios (bank-additional.csv):
- Tamaño del dataset: 43,000 filas x 23 columnas
- Estado actual: Los datos están concatenados en una sola columna con comas como separador
- Necesita procesarse para separar en las siguientes 23 columnas:
  - age (edad)
  - job (trabajo)
  - marital (estado civil)
  - education (educación)
  - default (incumplimiento)
  - housing (vivienda)
  - loan (préstamo)
  - contact (tipo de contacto)
  - duration (duración)
  - campaign (campaña)
  - pdays (días desde último contacto)
  - previous (contactos previos)
  - poutcome (resultado previo)
  - emp.var.rate (tasa de variación del empleo)
  - cons.price.idx (índice de precios al consumo)
  - cons.conf.idx (índice de confianza del consumidor)
  - euribor3m (tipo de interés Euribor 3 meses)
  - nr.employed (número de empleados)
  - y (variable objetivo)
  - date (fecha)
  - latitude (latitud)
  - longitude (longitud)
  - id_ (identificador)

## 2. Análisis Inicial

### Datos de Clientes:
- No hay valores nulos en ninguna columna
- Tipos de datos:
  - 5 columnas numéricas (int64)
  - 1 columna de fecha (datetime64[ns])
  - 1 columna de texto (object - ID)
- Estadísticas descriptivas:
  - Income: Media de 93,087.21, rango de 5,852 a 180,791
  - Kidhome: Media de 1.00, máximo 2
  - Teenhome: Media de 1.00, máximo 2
  - NumWebVisitsMonth: Media de 16.54, rango de 1 a 32

### Datos Bancarios:
- Los datos están en formato concatenado y necesitan ser procesados
- No hay valores nulos aparentes
- Requiere separación de columnas para análisis detallado

## Próximos Pasos
1. Procesar y separar las columnas del dataset bancario
2. Realizar análisis estadístico detallado
3. Crear visualizaciones para entender mejor la distribución de los datos
4. Identificar patrones y correlaciones entre variables
5. Realizar segmentación de clientes
6. Generar conclusiones y recomendaciones

## 3. Limpieza de datos
- Identificar y manejar valores nulos (.isnull().sum()).
- Eliminar duplicados (.duplicated().sum(), .drop_duplicates()).
- Revisar tipos de datos y convertir si es necesario (.astype()).

## 4. Análisis estadístico
- Resumen estadístico (.describe()).
- Distribución de valores en columnas categóricas (.value_counts()).
- Identificar outliers con boxplots (seaborn.boxplot()).

## 5. Análisis de correlaciones
- Matriz de correlación (df.corr()).
- Mapa de calor con seaborn.heatmap().

## 6. Visualización de datos
- Histogramas (df.hist()).
- Gráficos de barras y dispersión con matplotlib y seaborn.
- Distribución de variables numéricas (sns.kdeplot()).

## 7. Detección de patrones y segmentación
- Análisis de tendencias en el tiempo si hay fechas.
- Agrupación de clientes por características (groupby()).

## 8. Conclusiones y preparación para modelado
- Identificar insights clave.
- Preparar datos limpios para análisis predictivo o machine learning. 