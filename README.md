![HenryLogo](https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png)

# **PROYECTO INDIVIDUAL N° 1: MACHINE LEARNING OPERATIONS (MLOps)**
# **ALUMNO: Montuori Nicolás I.**
## **Propuesta de Trabajo**
Elaborar un mvp de un sistema de recomendación de peliculas. Para ello se nos brindaron un conjunto de datasets sobre los cuales tuve que realizar las `transformaciones` indicadas. El paso siguiente consistío en disponibilizar los datos a traves de una `Api`. Una vez limpiados los datos y levantada la Api, procedí a efectuar un `análisis exploratorio (EDA)`, para finalmente terminar con el `modelo de machine learning` (consistente en un sistema de recomendación de películas).  

# **TRANSFORMACIONES - ETL**
Se nos brindaron 4 datasets de plataformas y 8 de rating. Sobre los primeros 4, realicé las siguientes transformaciones: 
1) Generé un campo id compuesto de la primera letra del nombre de la plataforma, seguido del show_id ya presente en los datasets (ejemplo para títulos de Amazon = as123).
2) Generé un campo plataforma (amazon, disney, netflix, hulu), para luego poder trabajar de manera mas fácil con las funciones.
3) Remplacé los valores nulos del campo rating  por el string “G”.
4) Cambié el formato de las fechas al siguiente: AAAA-mm-dd.
5) Cambié todos los campos de texto a minúsculas. 
6) Convertí el campo duration en dos campos: duration_int y duration_type. El primero es un integer y el segundo un string e indica  la unidad de medición de duración: min (minutos) o season (temporadas).
7) Remplacé la palabra "seasons" por "season".
8) Unifiqué los cuatro datasets correspondientes a plataformas. 

Sobre los 8 datasets restantes, realicé las siguientes: 
1) Unifiqué los 8 en uno nuevo. 
2) Cambié el nombre de la columna rating por score. 
3) Modifiqué el formato de la columna "timestamp" a AAAA,mm,dd.

Una vez efectuado el proceso de ETL, unifiqué los datasets correspondientes a plataformas y rating (utilizando merge) y lo exporté (completo.csv). Este dataset  es el que voy a utilizar posteriormente para el EDA y modelo de ML.

De la misma manera unifiqué los datasets de las plataformas con el de score promedio y también lo exporté (plat_score.csv). Este dataset es el que voy a utilizar para las consultas de la Api

Para resumir, del proceso de transformación de datos, obtuve dos datasets. Uno para el modelo de ML (`completo.csv`), y otro para la Api (`plat_score.csv`).   

# **DESARROLLO API**
Aquí lo primero que hice fue desarrollar el código de las consultas en el archivo `funciones.ipynb`. Para el mismo, utilicé el dataset ya limpio plat_score.csv. Posteriormente creo la Api e incluyo las consultas  en el archivo `main.py`. Se solicitaron las siguientes consultas: 
- Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN. (la función se llama get_max_duration(year, platform, duration_type))

- Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año (la función se llama get_score_count(platform, scored, year))

- Cantidad de películas por plataforma con filtro de PLATAFORMA. (La función se llama get_count_platform(platform))

- Actor que más se repite según plataforma y año. (La función se llama get_actor(platform, year)) 

# **EDA - MODELO DE MACHINE LEARNING**
Para el armado del sistema de recomendación, he decido utilizar el filtro colaborativo. El mismo basa su recomendación teniendo en cuenta las similitudes existentes entre los usuarios. Es por este motivo que trabajaré unicamente con los campos "userId", "score" y "id" del dataset ya limpio, llamado "completo.csv". Ver archivos `EDA.ipynb` y `Modelo_ML.ipynb`.

# **DATA UTILIZADA**
En el siguiente link de google drive se encuentran ordenados los csv con los que trabajé. https://drive.google.com/drive/folders/1VKiLGQcDWSIoOnIaQ_sCouSNpfpx4ouw?usp=sharing