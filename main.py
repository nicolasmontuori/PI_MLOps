from fastapi import FastAPI
import pandas as pd

# Creo la App
app = FastAPI()

@app.get("/")
def index ():
    return ("Bienvenido a la Api de consulta de películas")

# Consulta 1: Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN.
@app.get("/get_max_duration/{year}/{platform}/{duration_type}")
def get_max_duration(year: int, platform: str, duration_type: str):
    df = pd.read_csv ("C:/Users/Administrador/Desktop/Henry/Labs/Proyectosindividuales/PrimerPI/Datasets/plat_score.csv")
    filtro_year = df.loc[ df["release_year"] == year ] # Aplico filtro por año
    filtro_plataforma = filtro_year.loc[ filtro_year["plataforma"] == platform ] # Aplico filtro por plataforma
    filtro_tipo_duracion = filtro_plataforma.loc[ filtro_plataforma["duration_type"] == duration_type ] # Aplico filtro tipo de duracion

    max_duracion = filtro_tipo_duracion.loc[ filtro_tipo_duracion["duration_int"] == filtro_tipo_duracion["duration_int"].max() ]
    
    movie_max_duracion = max_duracion["title"]

    return movie_max_duracion

# Consulta 2 : Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año
@app.get("/get_score_count/{platform}/{scored}/{year}")
def get_score_count(platform:str, scored:float, year:int):
    df = pd.read_csv ("C:/Users/Administrador/Desktop/Henry/Labs/Proyectosindividuales/PrimerPI/Datasets/plat_score.csv")
    df_filtro = df[(df["score"] > scored ) & (df["release_year"] == year)]  # Aplico filtro por score y año
    if platform == "netflix":
        df_gsc = df_filtro[(df_filtro["type"] == "movie") & (df_filtro["id"].str.findall("n"))]  # Aplico filtros por type y id.
    elif platform == "amazon":
        df_gsc = df_filtro[(df_filtro["type"] == "movie") & (df_filtro["id"].str.findall("a"))]
    elif platform == "hulu":
        df_gsc = df_filtro[(df_filtro["type"] == "movie") & (df_filtro["id"].str.findall("h"))]
    elif platform == "disney":
        df_gsc = df_filtro[(df_filtro["type"] == "movie") & (df_filtro["id"].str.findall("d"))]
    else:
        print("Try again")

    return f'Peliculas de {platform} del año {year} con puntaje {scored}: {df_gsc.shape[0]}'


# Consulta 3: Cantidad de películas por plataforma con filtro de PLATAFORMA. 
@app.get("/get_count_platform/{platform}")
def get_count_platform(platform: str):
      df = pd.read_csv ("C:/Users/Administrador/Desktop/Henry/Labs/Proyectosindividuales/PrimerPI/Datasets/plat_score.csv")
      filtro = df ["plataforma"] == platform # Aplico filtro por plataformas
      count_platform = df [filtro] ["type"].value_counts() # Cuento la cantidad de películas por plataformas

      return {"plataforma": platform,
              "Movies": str (count_platform[0])}


# Consulta 4: Actor que más se repite según plataforma y año.
@app.get("/get_actor/{platform}/{year}")
def get_actor(platform: str, year: int):
    df = pd.read_csv ("C:/Users/Administrador/Desktop/Henry/Labs/Proyectosindividuales/PrimerPI/Datasets/plat_score.csv")
    filtro = (df["plataforma"] == platform) & (df["release_year"] == year) # Aplico filtro por plataforma y por año
    df_filtrado = df.loc[filtro]
    
    actores = df_filtrado["cast"].str.split(",").explode() # Separo la columna "cast" de actores en filas distintas a partir de la coma ","
    
    count_actores = actores.value_counts() # cuento la cantidad de actores
    
    actor_mas_comun = count_actores.index[0] # retorno el actor que mas se repite
    return actor_mas_comun