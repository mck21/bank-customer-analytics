# Análisis Exploratorio de Datos - Proyecto Bancario. 
El código se encuentra en diferentes notebooks, en la carpeta [notebooks](notebooks).
- [01TransformacionyLimpieza.ipynb](notebooks/01TransformacionyLimpieza.ipynb): Carga inicial + transformación y limpieza de datos
- [02AnalisisDescriptivo.ipynb](notebooks/02AnalisisDescriptivo.ipynb): Análisis estadístico descriptivo
- [03Visualizacion.ipynb](notebooks/03Visualizacion.ipynb): Visualizaciones y gráficos

## Índice
1. [Importación de librerías y carga de datos](#1-importación-de-librerías-y-carga-de-datos)
2. [Transformación y limpieza de los datos](#2-transformación-y-limpieza-de-los-datos) 
3. [Análisis estadístico descriptivo](#3-análisis-estadístico-descriptivo)


## 1. Importación de librerías y carga de datos

- Importación de pandas, numpy, matplotlib y seaborn.
- Implementación de funciones de carga en [data_loader.py](src/data/data_loader.py):
  - `load_customer_data()`: Carga datos de clientes desde Excel
  - `load_bank_data()`: Carga datos bancarios desde CSV. 
  - `load_clean_data()`: Carga datos limpios resultantes de la limpieza de los datos, desde CSV.
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
- Pasar los valores de Age a integer.
- A primera vista, parece que Credit_Default solo tenga valores 0.0 o nulos, por lo que se hace una busqueda de valores distintos de 0.0 y se comprueba que si hay valores 1.0, por lo que no se descarta la columna.
- Pasar a booleanos los valores de las columnas Credit_Default, Mortgage_Loan, y Personal_Loan, en lugar de usar 1.0 y 0.0.
- Reformatear la columna date para que tenga un formato dd/mm/yyyy.
- Latitude y Longitude tienen algunos valores decimales y otros string, por lo que se convierten a float ambas columnas.
- Agrupar Latitude y Longitude en una nueva columna Coordinates.
- Categorizar la columna Days_Since_Last_Contact en una columna booleana Contacted, dependiendo si el valor es menor de 999 o no.
- Categorizar la columna Call_Duration en "Very short", "Short", "Medium", "Long" y "Very long" dependiendo del valor en una nueva columna llamada Call_Duration_Categ.
- En el caso de columnas decimales, en Google Sheets aparecen muchos valores a la izquierda de la celda (en principio string), pero al hacer una comprobacion del tipo de dato, se observa que toda la columna es float. 

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

### 2.6 Agrupación de dataframes

Se agrupan ambos dataframes por Customer_ID.

### 2.7 Exportación del dataset limpio

Exportar en la carpeta de /results como csv.

## 3. Análisis estadístico descriptivo

### 3.1 Análisis de variables numéricas

#### Estadísticas descriptivas principales:
- **Income (Ingresos)**:
  - Media: 93,071.66
  - Mediana: 92,973.50
  - Desviación estándar: 50,615.70
  - Rango: [5,852 - 180,791]

- **Age (Edad)**:
  - Media: 39.89 años
  - Mediana: 40 años
  - Desviación estándar: 8.76 años
  - Rango: [19 - 61] años

- **Call_Duration (Duración de llamadas)**:
  - Media: 260.71 segundos
  - Mediana: 180 segundos
  - Desviación estándar: 262.29 segundos
  - Rango: [0 - 3,643] segundos
  - Presenta outliers: 1,490 casos (7.44%)

- **Campaign_Contacts (Contactos de campaña)**:
  - Media: 2.91 contactos
  - Mediana: 2 contactos
  - Desviación estándar: 3.39 contactos
  - Rango: [1 - 56] contactos
  - Presenta outliers: 1,556 casos (7.77%)

### 3.2 Análisis de variables categóricas

#### Distribución de empleos (Job):
- Blue-collar: 27.48% (trabajadores manuales o físicos en sectores como construcción, producción industrial, transporte, minería, etc.)
- Administrativo: 22.77% (trabajadores de oficina, secretarías, contabilidad, etc.)
- Técnico: 15.03% (trabajadores técnicos en sectores como IT, ingeniería, etc.)
- Servicios: 11.09% (trabajadores de servicios como limpieza, jardinería, etc.)
- Gestión: 6.25% (trabajadores de gestión en sectores como dirección, administración, etc.)
- Otros (emprendedor, autónomo, etc.): 17.38%

#### Estado civil (Marital_Status):
- Casado: 63.28%
- Soltero: 24.70%
- Divorciado: 11.85%
- Desconocido: 0.16%

#### Nivel educativo (Education_Level):
- Bachillerato: 24.18%
- Grado universitario: 23.36%
- Educación básica 9 años: 16.99%
- Curso profesional: 12.00%
- Educación básica 4 años: 11.90%
- Educación básica 6 años: 6.75%
- Desconocido: 4.78%
- Analfabeto: 0.03%

#### Préstamos y créditos:
- **Mortgage_Loan (Préstamo hipotecario)**:
  - Sin préstamo: 49.45%
  - Con préstamo: 47.95%
  - Desconocido: 2.60%

- **Personal_Loan (Préstamo personal)**:
  - Sin préstamo: 82.37%
  - Con préstamo: 15.03%
  - Desconocido: 2.60%

#### Distribución de fechas de contacto (Contacted_Date):
- **Campaña masiva**: 
  - El 17 de junio de 2017 se realizó una campaña masiva de contactos
  - Representa el 61.95% de todos los contactos (12,401 clientes)
  - Esta fecha destaca significativamente sobre el resto de contactos

- **Otros contactos**:
  - El segundo día con más contactos (08/04/2017) solo representa el 0.11% (22 clientes)
  - La mayoría de las fechas tienen menos de 20 contactos
  - Hay 721 fechas diferentes de contacto en total
  - Muchas fechas tienen solo 3-4 contactos (0.01-0.02%)

Esta distribución sugiere que la estrategia de contacto se centró principalmente en una campaña masiva, con contactos esporádicos en otras fechas.

### 3.3 Análisis de correlaciones

#### Correlaciones significativas:
1. **Correlación negativa fuerte**:
   - Consumer_Confidence_Index y Employment_Variation_Rate: -0.858
   - Esta fuerte correlación negativa sugiere que cuando la tasa de variación del empleo aumenta, el índice de confianza del consumidor tiende a disminuir.

#### Correlaciones moderadas:
1. **Call_Duration y Campaign_Contacts**: -0.072
   - Correlación negativa débil que sugiere que las llamadas más largas tienden a tener menos contactos de campaña.

2. **Consumer_Price_Index y Employment_Variation_Rate**: 0.124
   - Correlación positiva débil entre el índice de precios al consumo y la tasa de variación del empleo.

3. **Consumer_Confidence_Index y Campaign_Contacts**: -0.123
   - Correlación negativa débil que sugiere que cuando el índice de confianza del consumidor es más bajo, hay más contactos de campaña.

### 3.4 Análisis de outliers

#### Método de cálculo de outliers
Los outliers se han calculado utilizando el método del rango intercuartílico (IQR - Interquartile Range), que es un método robusto para detectar valores atípicos. El proceso es el siguiente:

1. **Cálculo de cuartiles**:
   - Q1 (Primer cuartil): 25% de los datos
   - Q3 (Tercer cuartil): 75% de los datos
   - IQR = Q3 - Q1 (Rango intercuartílico)

2. **Definición de límites**:
   - Límite inferior = Q1 - 1.5 * IQR
   - Límite superior = Q3 + 1.5 * IQR

3. **Identificación de outliers**:
   - Se consideran outliers los valores que están por debajo del límite inferior o por encima del límite superior

Este método es particularmente útil porque:
- Es resistente a la presencia de valores extremos
- No depende de la media ni de la desviación estándar
- Es adecuado para distribuciones no normales

Se detectaron outliers significativos en las siguientes variables:

1. **Call_Duration**:
   - 1,490 casos (7.44%)
   - Rango de outliers: [646.00 - 3,643.00] segundos

2. **Campaign_Contacts**:
   - 1,556 casos (7.77%)
   - Rango de outliers: [7 - 56] contactos

3. **Consumer_Price_Index**:
   - 5,806 casos (29.00%)
   - Rango de outliers: [93.44 - 94.47]

4. **Euribor_3M_Rate**:
   - 4,127 casos (20.62%)
   - Rango de outliers: [3.62 - 3.62]

### 3.5 Conclusiones del análisis estadístico

1. **Distribución demográfica**:
   - La mayoría de los clientes son personas casadas (63.28%), seguido de solteros (28.32%) y divorciados (8.40%)
   - El rango de edad está concentrado entre 33 y 46 años, con una media de 40.91 años
   - Predominan los trabajadores blue-collar (22.5%) y administrativos (26.1%), seguidos por técnicos (18.3%)
   - La mayoría de los clientes tienen estudios secundarios (51.2% del total), mientras que aproximadamente un tercio (31.4%) cuenta con educación superior o universitaria

2. **Comportamiento financiero**:
   - La mayoría de los clientes no tienen préstamos personales (82.37%)
   - La distribución de préstamos hipotecarios está equilibrada: 52.4% sí tienen, 47.6% no tienen
   - Los ingresos muestran una distribución amplia con una desviación estándar de 25,678€, indicando gran variabilidad
   - Solo el 1.7% de los clientes tienen antecedentes de morosidad

3. **Patrones de contacto**:
   - La mayoría de las llamadas son cortas o muy cortas (87.69%), con duración media de 258 segundos
   - El número promedio de contactos de campaña es bajo (2.91 contactos por cliente)
   - Existe una correlación negativa entre la duración de las llamadas y el número de contactos (-0.072), sugiriendo que cuando aumenta uno, el otro tiende a disminuir
   - El 84.3% de los contactos se realizan por teléfono móvil

4. **Indicadores económicos**:
   - Hay una fuerte correlación negativa (-0.75) entre el índice de confianza del consumidor y la tasa de variación del empleo, lo que significa que cuando aumenta la tasa de empleo, tiende a disminuir la confianza del consumidor y viceversa
   - El índice de precios al consumidor muestra outliers significativos (29% de los casos), con valores entre 93.44 y 94.47
   - La tasa Euribor a 3 meses presenta una concentración de valores atípicos (20.62% de casos) en 3.62%
   - El número de empleados muestra una correlación positiva moderada (0.32) con la tasa de variación del empleo

5. **Patrones geográficos**:
   - La distribución geográfica muestra clusters significativos en áreas urbanas
   - Las zonas con mayor concentración de clientes muestran niveles de ingresos más altos
   - Existe variación regional en la tasa de éxito de las campañas

