# Análisis Exploratorio de Datos - Proyecto Bancario
[notebook](notebooks/EDA_bank_customers.ipynb)

## 1. Importación de librerías y carga de datos

- Importación de pandas, numpy, matplotlib y seaborn.
- Implementación de funciones de carga en [data_loader.py](src/data/data_loader.py):
  - `load_customer_data()`: Carga datos de clientes desde Excel
  - `load_bank_data()`: Carga datos bancarios desde CSV. 
  - `get_basic_info()`: Obtiene información básica del DataFrame

El parámetro index_col=0 indica que la primera columna del CSV se utilizará como índice del DataFrame, si no, el csv se carga de forma errónea

#### Dataset de Clientes (customer-details.xlsx):
- Tamaño del dataset: 20,115 filas × 7 columnas
- Columnas disponibles:
  - Income (ingresos)
  - Kidhome (número de niños)
  - Teenhome (número de adolescentes)
  - Dt_Customer (fecha de registro)
  - NumWebVisitsMonth (visitas web mensuales)
  - ID (identificador único)

#### Datos Bancarios (bank-additional.csv):
- Tamaño del dataset: 43,000 filas x 23 columnas
- Columnas disponibles:
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

## 2. Transformación y limpieza de los datos

### 2.1 Estandarización de nombres de columnas
[notebook](notebooks/EDA_bank_customers.ipynb)

El primer paso es la estandarización de los nombres de las columnas en ambos datasets. Esta estandarización se realiza con el objetivo de:
- Mejorar la legibilidad y comprensión del significado de cada variable
- Mantener consistencia en el formato con Pascal_Snake_Case
- Facilitar la interpretación de los resultados en las fases posteriores del análisis

### 2.2 Análisis de valores nulos
[notebook](notebooks/EDA_bank_customers.ipynb)

#### Dataset de Clientes (customer-details.xlsx):
- Tipos de datos:
  - 5 columnas numéricas (int64)
  - 1 columna de fecha (datetime64[ns])
  - 1 columna de texto (object - Customer_ID)
- No hay valores nulos en ninguna columna

### Datos Bancarios:
- Tipos de datos:
  - 7 columnas numéricas (float64)
  - 4 columnas enteras (int64)
  - 12 columnas de texto (object)
- Valores nulos encontrados:
  - Age: 5,120 valores nulos
  - Job: 345 valores nulos
  - Marital_Status: 85 valores nulos
  - Education_Level: 1,807 valores nulos
  - Credit_Default: 8,981 valores nulos
  - Mortgage_Loan: 1,026 valores nulos
  - Personal_Loan: 1,026 valores nulos
  - Consumer_Price_Index: 471 valores nulos
  - Euribor_3M_Rate: 9,256 valores nulos
  - Date: 248 valores nulos


-----------------------------------------------------------------
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