# Análisis Exploratorio de Datos - Proyecto Bancario. 
[Ver análisis en el notebook](notebooks/EDA_bank_customers.ipynb)

## 1. Importación de librerías y carga de datos

- Importación de pandas, numpy, matplotlib y seaborn.
- Implementación de funciones de carga en [data_loader.py](src/data/data_loader.py):
  - `load_customer_data()`: Carga datos de clientes desde Excel
  - `load_bank_data()`: Carga datos bancarios desde CSV. 
  - `get_basic_info()`: Obtiene información básica del DataFrame

El parámetro index_col=0 indica que la primera columna del CSV se utilizará como índice del DataFrame, si no, el csv se carga de forma errónea

#### Info de Clientes (customer-details.xlsx):
- Tamaño del dataset: 20,115 filas × 7 columnas
- Columnas disponibles:
  - Income (ingresos)
  - Kidhome (número de niños)
  - Teenhome (número de adolescentes)
  - Dt_Customer (fecha de registro)
  - NumWebVisitsMonth (visitas web mensuales)
  - ID (identificador único)

#### Info de Datos Bancarios (bank-additional.csv):
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

El primer paso es la estandarización de los nombres de las columnas en ambos datasets. Esta estandarización se realiza con el objetivo de:
- Mejorar la legibilidad y comprensión del significado de cada variable
- Mantener consistencia en el formato con Pascal_Snake_Case
- Facilitar la interpretación de los resultados en las fases posteriores del análisis

De ahora en adelante, se utilizarán los siguientes nombres de columnas en el análisis:
```python
customer_columns_rename = {
    'Income': 'Income',
    'Kidhome': 'Number_of_Children',
    'Teenhome': 'Number_of_Teenagers',
    'Dt_Customer': 'Registration_Date',
    'NumWebVisitsMonth': 'Monthly_Web_Visits',
    'ID': 'Customer_ID'
}

bank_columns_rename = {
    'age': 'Age',
    'job': 'Job',
    'marital': 'Marital_Status',
    'education': 'Education_Level',
    'default': 'Credit_Default',
    'housing': 'Mortgage_Loan',
    'loan': 'Personal_Loan',
    'contact': 'Contact_Type',
    'duration': 'Call_Duration',
    'campaign': 'Campaign_Contacts',
    'pdays': 'Days_Since_Last_Contact',
    'previous': 'Previous_Contacts',
    'poutcome': 'Previous_Campaign_Outcome',
    'emp.var.rate': 'Employment_Variation_Rate',
    'cons.price.idx': 'Consumer_Price_Index',
    'cons.conf.idx': 'Consumer_Confidence_Index',
    'euribor3m': 'Euribor_3M_Rate',
    'nr.employed': 'Number_of_Employees',
    'y': 'Subscribed_to_Service',
    'date': 'Date',
    'latitude': 'Latitude',
    'longitude': 'Longitude',
    'id_': 'Customer_ID'
}
```

### 2.2 Corrección de formato y trasformación de columnas

La corrección del tipado de los datos además de crear tablas a partir de las disponibles para esclarecer los datos pasa por realizar las siguientes transformaciones:

En el dataset de clientes:

- Reformatear la columna date para que tenga un formato dd/mm/yyyy. Y mantener el formato con la fecha del dataset de datos bancarios.
- Hacer una columna categorica Frequency a partir de las visitas mensuales de cada cliente.

En el dataset de datos bancarios:
- Pasar los valores de Age de string a integer.
- Reemplazo de comas por puntos decimales en columnas numéricas con comas.
- A primera vista, parece que Credit_Default solo tenga valores 0.0 o nulos, por lo que se hace una busqueda de valores distintos de 0.0 y se comprueba que si hay valores 1.0, por lo que no se descarta la columna.
- Pasar a booleanos los valores de las columnas Credit_Default, Mortgage_Loan, y Personal_Loan, en lugar de usar 1.0 y 0.0.
- Reformatear la columna date para que tenga un formato dd/mm/yyyy.
- Latitude y Longitude tienen algunos valores decimales y otros string, por lo que se convierten a float ambas columnas.
- Agrupar Latitude y Longitude en una columna de Coordinates.
- Categorizar la columna Days_Since_Last_Contact en una columna booleana Contacted, dependiendo si el valor es menor de 999.
- Categorizar la columna Call_Duration en "Very short", "Short", "Medium", "Long" y "Very long" dependiendo del valor en una nueva columna llamada Call_Duration_Categ.


### 2.3 Análisis de valores nulos

#### Dataset de Clientes:
- Tipos de datos:
  - 5 columnas numéricas (int64)
  - 1 columna de fecha (datetime64[ns])
  - 1 columna de texto (object - Customer_ID)
- No hay valores nulos en ninguna columna

#### Dataset de Datos Bancarios:
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

### 2.4 Tratado de los nulos

#### Estrategia para el manejo de los nulos

- Variables categóricas (strings) → reemplazar por "unknown"

- Variables numéricas (floats/ints) → reemplazar por la media de la columna

- Fechas → reemplazar por la media de la columna y formatear a dd/mm/yyyy


### 2.5 Eliminación de duplicados

En caso de existir duplicados, se eliminan de ambos datasets. Pero no se han encontrado.







-----------------------------------------------------------------
TODO
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