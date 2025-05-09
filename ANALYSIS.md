<p align="center">
  <img src="https://github.com/mck21/bank-customer-analytics/blob/main/img/informehead.png?raw=true" alt="Header Image" />
</p>

# Análisis Exploratorio de Datos - Proyecto Bancario. 
El código se encuentra en diferentes notebooks, en la carpeta [notebooks](notebooks).
- [01TransformacionyLimpieza.ipynb](notebooks/01TransformacionYLimpieza.ipynb): Carga inicial + transformación y limpieza de datos
- [02AnalisisDescriptivo.ipynb](notebooks/02AnalisisDescriptivo.ipynb): Análisis estadístico descriptivo
- [03Visualizacion.ipynb](notebooks/03Visualizacion.ipynb): Visualizaciones y gráficos

## Índice
1. [Importación de librerías y carga de datos](#1-importación-de-librerías-y-carga-de-datos)
2. [Transformación y limpieza de los datos](#2-transformación-y-limpieza-de-los-datos) 
3. [Análisis estadístico descriptivo](#3-análisis-estadístico-descriptivo)
4. [Visualización de datos](#4-visualización-de-datos)
5. [Conclusiones](#5-conclusiones)
6. [Recomendaciones](#6-recomendaciones)

<br/>
<br/>
<p align="center">
  <img src="https://github.com/mck21/bank-customer-analytics/blob/main/img/cargadedatos.png?raw=true"/>
</p>

## 1. Importación de librerías y carga de datos

- Importación de pandas, numpy, matplotlib y seaborn.
- Implementación de funciones de carga en [data_loader.py](src/data/data_loader.py):
  - `load_customer_data()`: Carga datos de clientes desde Excel.
  - `load_bank_data()`: Carga datos bancarios desde CSV. 
  - `load_clean_data()`: Carga datos limpios resultantes de la limpieza de los datos, desde CSV.
  - `get_basic_info()`: Obtiene información básica del DataFrame.

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

<br/>
<p align="center">
  <img src="https://github.com/mck21/bank-customer-analytics/blob/main/img/transformacionylimpieza.png?raw=true" />
</p>

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
    'Kidhome': 'Number_of_Kids',
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
    'date': 'Contacted_Date',
    'latitude': 'Latitude',
    'longitude': 'Longitude',
    'id_': 'Customer_ID'
}
```

### 2.2 Corrección de formato y trasformación de columnas

La corrección del tipado de los datos además de crear tablas a partir de las disponibles para esclarecer los datos pasa por realizar las siguientes transformaciones:

En el dataset de clientes:

- Reformatear la columna Registration_Date para que tenga un formato dd/mm/yyyy. Y mantener el formato con la fecha del dataset de datos bancarios.
- Hacer una columna categorica Frequency a partir de las visitas mensuales de cada cliente.

En el dataset de datos bancarios:
- Pasar los valores de Age a integer.
- A primera vista, parece que Credit_Default solo tenga valores 0.0 o nulos, por lo que se hace una búsqueda de valores distintos de 0.0 y se comprueba que sí hay valores 1.0, por lo que no se descarta la columna.
- Pasar a booleanos los valores de las columnas Credit_Default, Mortgage_Loan, y Personal_Loan, en lugar de usar 1.0 y 0.0.
- Reformatear la columna Contacted_Date para que tenga un formato dd/mm/yyyy.
- Latitude y Longitude tienen algunos valores decimales y otros string, por lo que se convierten a float ambas columnas.
- Agrupar Latitude y Longitude en una nueva columna Coordinates.
- Categorizar la columna Days_Since_Last_Contact en una columna booleana Contacted, dependiendo si el valor es menor de 999 o no.
- Categorizar la columna Call_Duration en "Very short", "Short", "Medium", "Long" y "Very long" dependiendo del valor en una nueva columna llamada Call_Duration_Categ.
- En el caso de columnas decimales, en Google Sheets aparecen muchos valores a la izquierda de la celda (en principio string), pero al hacer una comprobacion del tipo de dato, se observa que toda la columna es float. 

### 2.3 Análisis de valores nulos

#### Dataset de Clientes:
- Tipos de datos:
  - 5 columnas numéricas (int64).
  - 1 columna de fecha (datetime64[ns]).
  - 1 columna de texto (object - Customer_ID).
- No hay valores nulos en ninguna columna.

#### Dataset de Datos Bancarios:
- Tipos de datos:
  - 7 columnas numéricas (float64).
  - 4 columnas enteras (int64).
  - 12 columnas de texto (object).
- Valores nulos encontrados:
  - Age: 5,120 valores nulos.
  - Job: 345 valores nulos.
  - Marital_Status: 85 valores nulos.
  - Education_Level: 1,807 valores nulos.
  - Credit_Default: 8,981 valores nulos.
  - Mortgage_Loan: 1,026 valores nulos.
  - Personal_Loan: 1,026 valores nulos.
  - Consumer_Price_Index: 471 valores nulos.
  - Euribor_3M_Rate: 9,256 valores nulos.
  - Date: 248 valores nulos.

### 2.4 Tratado de los nulos

#### Estrategia para el manejo de los nulos

- Variables categóricas (strings) → reemplazar por "unknown".

- Variables numéricas (floats/ints) → reemplazar por la media de la columna.

- Fechas → reemplazar por la media de la columna y formatear a dd/mm/yyyy.

Al no contar con un volumen demasiado alto de nulos, no se ha descartado ninguna columna para el análisis.

### 2.5 Eliminación de duplicados

En caso de existir duplicados, se eliminan de ambos datasets. Pero no se han encontrado.

### 2.6 Agrupación de dataframes

Se agrupan ambos dataframes por Customer_ID en un nuevo dataframe: df_completo.

### 2.7 Exportación del dataset limpio

Exportar el dataframe df_completo en la carpeta de /results como csv.


<br/>
<p align="center">
  <img src="https://github.com/mck21/bank-customer-analytics/blob/main/img/analisisestadisticodescriptivo.png?raw=true" alt="Header Image" />
</p>

## 3. Análisis estadístico descriptivo

### 3.1 Análisis de variables numéricas

#### Estadísticas descriptivas principales:
- **Income (Ingresos)**:
  - Media: 93,071.66.
  - Mediana: 92,973.50.
  - Desviación estándar: 50,615.70.
  - Rango: [5,852 - 180,791].

- **Age (Edad)**:
  - Media: 39.89 años.
  - Mediana: 40 años.
  - Desviación estándar: 8.76 años.
  - Rango: [19 - 61] años.

- **Call_Duration (Duración de llamadas)**:
  - Media: 260.71 segundos.
  - Mediana: 180 segundos.
  - Desviación estándar: 262.29 segundos.
  - Rango: [0 - 3,643] segundos.
  - Presenta outliers: 1,490 casos (7.44%).

- **Campaign_Contacts (Contactos de campaña)**:
  - Media: 2.91 contactos.
  - Mediana: 2 contactos.
  - Desviación estándar: 3.39 contactos.
  - Rango: [1 - 56] contactos.
  - Presenta outliers: 1,556 casos (7.77%).

- **Monthly_Web_Visits (Visitas web mensuales)**:
  - Media: 16.54 visitas.
  - Mediana: 16 visitas.
  - Desviación estándar: 9.23 visitas.
  - Rango: [1 - 32] visitas.

- **Number_of_Kids (Número de niños)**:
  - Media: 1.00 niños.
  - Mediana: 1 niño.
  - Desviación estándar: 0.82 niños.
  - Rango: [0 - 2] niños.

- **Number_of_Teenagers (Número de adolescentes)**:
  - Media: 1.00 adolescentes.
  - Mediana: 1 adolescente.
  - Desviación estándar: 0.82 adolescentes.
  - Rango: [0 - 2] adolescentes.

### 3.2 Análisis de variables categóricas

#### Distribución de empleos (Job):
- Blue-collar: 27.48% (trabajadores manuales o físicos en sectores como construcción, producción industrial, transporte, minería, etc.).
- Administrativo: 22.77% (trabajadores de oficina, secretarías, contabilidad, etc.).
- Técnico: 15.03% (trabajadores técnicos en sectores como IT, ingeniería, etc.).
- Servicios: 11.09% (trabajadores de servicios como limpieza, jardinería, etc.).
- Gestión: 6.25% (trabajadores de gestión en sectores como dirección, administración, etc.).
- Otros (emprendedor, autónomo, etc.): 17.38%.

#### Estado civil (Marital_Status):
- Casado: 63.28%.
- Soltero: 24.70%.
- Divorciado: 11.85%.
- Desconocido: 0.16%.

#### Nivel educativo (Education_Level):
- Educación secundaria: 24.18%.
- Grado universitario: 23.36%.
- Educación básica 9 años: 16.99%.
- Curso profesional: 12.00%.
- Educación básica 4 años: 11.90%.
- Educación básica 6 años: 6.75%.
- Desconocido: 4.78%.
- Analfabeto: 0.03%.

#### Frecuencia de visitas web (Frequency):
- Muy alta: 25.21%.
- Media: 25.13%.
- Baja: 24.91%.
- Alta: 24.75%.

#### Tipo de contacto (Contact_Type):
- Teléfono fijo: 65.19%.
- Teléfono móvil: 34.81%.

#### Duración de llamadas (Call_Duration_Categ):
- Corta: 46.88%.
- Muy corta: 40.81%.
- Media: 10.95%.
- Larga: 1.21%.
- Muy larga: 0.15%.

#### Préstamos y créditos:
- **Mortgage_Loan (Préstamo hipotecario)**:
  - Sin préstamo: 49.45%.
  - Con préstamo: 47.95%.
  - Desconocido: 2.60%.

- **Personal_Loan (Préstamo personal)**:
  - Sin préstamo: 82.37%.
  - Con préstamo: 15.03%.
  - Desconocido: 2.60%.

#### Distribución de fechas de contacto (Contacted_Date):
- **Campaña masiva**: 
  - El 17 de junio de 2017 se realizó una campaña masiva de contactos.
  - Representa el 61.95% de todos los contactos (12,401 clientes).
  - Esta fecha destaca significativamente sobre el resto de contactos.

- **Otros contactos**:
  - El segundo día con más contactos (08/04/2017) solo representa el 0.11% (22 clientes).
  - La mayoría de las fechas tienen menos de 20 contactos.
  - Hay 721 fechas diferentes de contacto en total.
  - Muchas fechas tienen solo 3-4 contactos (0.01-0.02%).

Esta distribución sugiere que la estrategia de contacto se centró principalmente en una campaña masiva, con contactos esporádicos en otras fechas.

### 3.3 Análisis de correlaciones

#### Correlaciones significativas:
1. **Correlación negativa fuerte**:
   - Consumer_Confidence_Index y Employment_Variation_Rate: -0.858.
   - Esta fuerte correlación negativa sugiere que cuando la tasa de variación del empleo aumenta, el índice de confianza del consumidor tiende a disminuir. Esto indica que la confianza del consumidor no depende únicamente del empleo, lo que puede afectar las decisiones de inversión y la efectividad de las campañas bancarias.

#### Correlaciones débiles:
1. **Call_Duration y Campaign_Contacts**: -0.072.
   - Correlación negativa débil que sugiere que las llamadas más largas tienden a tener menos contactos de campaña. Por lo que las llamadas más largas no son efectivas para generar más contactos de campaña.

2. **Consumer_Price_Index y Employment_Variation_Rate**: 0.124.
   - Correlación positiva débil entre el índice de precios al consumo y la tasa de variación del empleo. Cuando el precio de los bienes y servicios aumenta, la demanda de empleo disminuye.

3. **Consumer_Confidence_Index y Campaign_Contacts**: -0.123.
   - Correlación negativa débil que sugiere que las campañas bancarias que se centran en la confianza del consumidor pueden ser más efectivas.

### 3.4 Análisis de outliers

#### Método de cálculo de outliers
Los outliers se han calculado utilizando el método del rango intercuartílico (IQR - Interquartile Range), que es un método robusto para detectar valores atípicos. El proceso es el siguiente:

1. **Cálculo de cuartiles**:
   - Q1 (Primer cuartil): 25% de los datos.
   - Q3 (Tercer cuartil): 75% de los datos.
   - IQR = Q3 - Q1 (Rango intercuartílico).

2. **Definición de límites**:
   - Límite inferior = Q1 - 1.5 * IQR.
   - Límite superior = Q3 + 1.5 * IQR.

3. **Identificación de outliers**:
   - Se consideran outliers los valores que están por debajo del límite inferior o por encima del límite superior.

Este método es particularmente útil porque:
- Es resistente a la presencia de valores extremos.
- No depende de la media ni de la desviación estándar.
- Es adecuado para distribuciones no normales.

Se detectaron outliers significativos en las siguientes variables:

1. **Call_Duration**:
   - 1,490 casos (7.44%).
   - Rango de outliers: [646.00 - 3,643.00] segundos.

2. **Campaign_Contacts**:
   - 1,556 casos (7.77%).
   - Rango de outliers: [7 - 56] contactos.

3. **Consumer_Price_Index**:
   - 5,806 casos (29.00%).
   - Rango de outliers: [93.44 - 94.47].

4. **Euribor_3M_Rate**:
   - 4,127 casos (20.62%).
   - Rango de outliers: [3.62 - 3.62].

### 3.5 Conclusiones del análisis estadístico

1. **Distribución demográfica**:
   - La mayoría de los clientes son casados (63.28%), seguido de solteros (24.70%) y divorciados (11.85%).
   - El rango de edad está concentrado entre 33 y 46 años, con una media de 40.91 años y una desviación estándar de 10.6 años. La edad mínima es de 19 años y la máxima de 61 años.
   - Predominan los trabajadores blue-collar (27.5%) y administrativos (22.8%), seguidos por técnicos (15.0%).
   - El nivel educativo predominante es educación secundaria (24.18%), seguido de grado universitario (23.36%) y educación básica 9 años (16.99%).

2. **Análisis de correlaciones**:
   - Existe una correlación negativa débil (-0.072) entre la duración de llamadas y contactos de campaña, sugiriendo que las llamadas más largas no son efectivas para generar más contactos.
   - Hay una correlación positiva débil (0.124) entre el índice de precios al consumo y la tasa de variación del empleo, por lo que cuando el precio de los bienes y servicios aumenta, la demanda de empleo disminuye.
   - La correlación negativa débil (-0.123) entre el índice de confianza del consumidor y contactos de campaña sugiere que las campañas enfocadas en la confianza del consumidor pueden ser más efectivas.

3. **Análisis de outliers**:
   - Call_Duration: 7.44% de casos atípicos (1,490 casos), con valores entre 646 y 3,643 segundos.
   - Campaign_Contacts: 7.77% de outliers (1,556 casos), entre 7 y 56 contactos.
   - Consumer_Price_Index: 29% de valores atípicos (5,806 casos), rango de 93.44 a 94.47.
   - Euribor_3M_Rate: 20.62% de casos atípicos (4,127 casos) concentrados en 3.62%.

4. **Comportamiento financiero**:
   - La mayoría (82.37%) no tiene préstamos personales.
   - En préstamos hipotecarios: 47.95% tienen préstamo, 49.45% no tienen.
   - Alta variabilidad en ingresos con una media de 93,071.66€ y desviación estándar de 50,615.70€.
   - Los ingresos varían entre 5,852€ y 180,791€.

5. **Patrones de contacto**:
   - Predominan las llamadas cortas (87.69% entre muy cortas y cortas).
   - Duración media de llamadas de 260.71 segundos.
   - Media de 2.91 contactos por campaña por cliente.
   - 65.19% de contactos por teléfono fijo y 34.81% por móvil.

<br/>
<p align="center">
  <img src="https://github.com/mck21/bank-customer-analytics/blob/main/img/visualizacion.png?raw=true"/>
</p>

## 4. Visualización de datos

Para la visualización de datos se utilizaron diferentes tipos de gráficos mediante las librerías seaborn y matplotlib, incluyendo gráficos de barras para relaciones entre variables categóricas y numéricas, gráficos circulares para proporciones, gráficos de dispersión y mapas de calor para correlaciones entre variables.

<br/>
<p align="center">
  <img src="https://github.com/mck21/bank-customer-analytics/blob/main/img/output01.png?raw=true"/>
</p>
<br/>
<p align="center">
  <img src="https://github.com/mck21/bank-customer-analytics/blob/main/img/output02.png?raw=true"/>
</p>
<br/>
<p align="center">
  <img src="https://github.com/mck21/bank-customer-analytics/blob/main/img/output03.png?raw=true"/>
</p>
<br/>
<p align="center">
  <img src="https://github.com/mck21/bank-customer-analytics/blob/main/img/output04.png?raw=true"/>
</p>
<br/>
<p align="center">
  <img src="https://github.com/mck21/bank-customer-analytics/blob/main/img/output05.png?raw=true"/>
</p>

## 4.1 Interpretaciones de los gráficos

a. Distribución de Estado Civil  
- La mayoría de los clientes están casados, seguidos por solteros y divorciados; el estado "unknown" es despreciable.

b. Distribución de Edad  
- La edad se concentra entre 35 y 45 años, con un pico alrededor de los 40 años (por la media asignada a los nulos), pero la tendencia es ascendente hasta los 30-35 años (en ese rango se mantiene constante) y descendente hasta los 60 años, habiendo un pico real entorno a los 30-35 años.

c. Nivel Educativo  
- Los niveles más frecuentes son "high-school", "university-degree" y "basic-9y"; los niveles más bajos y "unknown" son minoritarios, e "illiterate" es despreciable.

d. Distribución de Tipo de Empleo  
- Predominan los empleos "blue-collar", "admin." y "technician", seguidos de "services".

e. Ingresos por Nivel Educativo  
- Los ingresos son similares para niveles medios y altos, salvo "illiterate" y "unknown" que son minoritarios en cuanto a la media.

f. Ingresos por Tipo de Empleo  
- Los ingresos más altos corresponden a "unknown", seguido de "technician" y "admin.", los más bajos a "student" y "entrepreneur".

g. Préstamos Personales (True) por Nivel Educativo  
- Los niveles con más préstamos personales son "high-school" y "university-degree".

h. Préstamos Hipotecarios (True) por Estado Civil  
- La mayoría de las hipotecas son solicitadas por personas casadas.

i. Ingresos Promedio por Estado Civil  
- Los ingresos son similares entre casados, solteros y divorciados, estando estos ligeramente por encima; y "unknown" presenta gran varianza.

j. Distribución de Ingresos por Grupos de Edad  
- La distribución de ingresos es similar entre todos los grupos de edad, con medianas constantes alrededor de $90000, sugiriendo que la edad no influye significativamente en el nivel de ingresos en esta población. 
Apreciamos un outlier de un estudiante de 19 años con 170000 de ingresos, que no es representativo de la población general.

k. Proporción de Llamadas por Tipo de Contacto  
- El canal más usado es el teléfono fijo (65.2 %), seguido del celular (34.8 %).

l. Relación entre Duración de Llamada y Número de Contactos  
- Existe una ligera relación negativa entre duración de llamadas y número de contactos. Demostrando que las llamadas más largas no son efectivas para generar más contactos.

m. Distribución de Préstamos Personales  
- El 82.4 % no tiene préstamos personales, el 15 % sí, y el 2.6 % está en "Desconocido".

n. Tasa de Morosidad  
- El 29.3 % de los clientes presenta impagos, mientras que el 70.7 % no.

o. Mapa de Calor de Correlaciones entre Variables Numéricas  
- Se observa alta correlación entre edad y grupo de edad (0.99) (normal, ya que una columna deriva de la otra) y una fuerte correlación negativa entre empleo y confianza del consumidor.

<br/>
<p align="center">
  <img src="https://github.com/mck21/bank-customer-analytics/blob/main/img/conclusiones.png?raw=true"/>
</p>

## 5. Conclusiones

- El perfil medio del cliente es una persona casada (63.28%), en edad laboral madura (35-45 años), con educación secundaria o universitaria (47.54%), y empleada principalmente en sectores manuales (27.48%) o administrativos (22.77%).

- Los ingresos muestran una distribución homogénea entre estados civiles, pero con desviaciones significativas por categoría laboral, siendo más altos en perfiles técnicos y administrativos, y más bajos en estudiantes y emprendedores.

- La mayoría de clientes no tiene préstamos: solo 15.03% tiene préstamos personales y 47.95% hipotecarios. Entre quienes los tienen, destacan perfiles con educación media/alta y estado civil casado.

- El canal telefónico fijo domina con 65.19% de uso, aunque el móvil (34.81%) muestra una tendencia creciente.

- Las llamadas tienden a ser cortas (87.69% entre muy cortas y cortas), observándose menor efectividad en llamadas largas.

- Tasa de morosidad preocupante del 29.3%, especialmente considerando que la mayoría de clientes no tiene préstamos activos.

- La frecuencia de visitas web muestra una distribución equilibrada entre las categorías (aprox. 25% cada una), sugiriendo un uso consistente de canales digitales.

- La campaña masiva del 17/06/2017 alcanzó al 61.95% de clientes, evidenciando una estrategia de contacto concentrada.

- La fuerte correlación negativa entre empleo y confianza del consumidor (-0.858) sugiere que a mayor tasa de empleo, menor es la confianza del consumidor, lo que podría indicar precaución o pesimismo en períodos de alta empleabilidad. Este hallazgo es relevante para anticipar comportamientos financieros de los clientes.

- Los outliers significativos en duración de llamadas (7.44%) y contactos de campaña (7.77%) sugieren casos que requieren atención especial.

Estas conclusiones proporcionan una base sólida para optimizar estrategias comerciales, gestión de riesgos y segmentación de clientes.

<br/>
<p align="center">
  <img src="https://github.com/mck21/bank-customer-analytics/blob/main/img/recomendaciones.png?raw=true"/>
</p>

## 6. Recomendaciones

1. **Optimización de campañas**:
   - Priorizar el uso del teléfono fijo (65.19% de efectividad) mientras se desarrolla la estrategia móvil.
   - Mantener llamadas cortas, ya que el 87.69% de las llamadas efectivas son breves.
   - Evitar concentrar campañas masivas en un solo día como la del 17/06/2017.

2. **Segmentación y targeting**:
   - Enfocar esfuerzos en el perfil mayoritario: personas casadas (63.28%), 35-45 años, con educación media/superior.
   - Adaptar ofertas según sector laboral, considerando mayores ingresos en perfiles técnicos y administrativos.
   - Desarrollar productos específicos para el 85% de clientes sin préstamos personales.

3. **Gestión de riesgos**:
   - Implementar sistema de alerta temprana para la alta tasa de morosidad (29.3%).
   - Monitorear especialmente clientes sin préstamos activos que muestran señales de riesgo.
   - Considerar la correlación negativa empleo-confianza del consumidor para anticipar comportamientos.






