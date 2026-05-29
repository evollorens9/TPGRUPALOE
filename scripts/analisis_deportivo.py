import pandas as pd
import matplotlib.pyplot as plt

# Leer dataset
df = pd.read_csv("datos/partidos.csv")

# Renombrar columnas importantes
df = df.rename(columns={
    "HomeTeam": "local",
    "AwayTeam": "visitante",
    "FTHG": "goles_local",
    "FTAG": "goles_visitante"
})

# Obtener equipos
equipos = pd.concat([
    df["equipo_local"],
    df["equipo_visitante"]
]).unique()

# Crear tabla
tabla = {
    equipo: {
        "Puntos": 0,
        "Ganados": 0,
        "GF": 0,
        "GC": 0
    }
    for equipo in equipos
}

# Procesar partidos
for _, fila in df.iterrows():

    local = fila["equipo_local"]
    visitante = fila["equipo_visitante"]

    gl = fila["goles_local"]
    gv = fila["goles_visitante"]

    tabla[local]["GF"] += gl
    tabla[local]["GC"] += gv

    tabla[visitante]["GF"] += gv
    tabla[visitante]["GC"] += gl

    if gl > gv:
        tabla[local]["Puntos"] += 3
        tabla[local]["Ganados"] += 1

    elif gv > gl:
        tabla[visitante]["Puntos"] += 3
        tabla[visitante]["Ganados"] += 1

    else:
        tabla[local]["Puntos"] += 1
        tabla[visitante]["Puntos"] += 1

# DataFrame final
tabla_df = pd.DataFrame(tabla).T

# Diferencia de gol
tabla_df["DG"] = tabla_df["GF"] - tabla_df["GC"]

# Ordenar
tabla_df = tabla_df.sort_values(
    by=["Puntos", "DG"],
    ascending=False
)

# Guardar resultados
tabla_df.to_csv("resultados/tabla_posiciones.csv")

# Promedio de goles
promedio = (
    df["goles_local"].sum() +
    df["goles_visitante"].sum()
) / len(df)

print(f"Promedio de goles: {promedio:.2f}")

# Gráfico
tabla_df["Puntos"].plot(kind="bar")

plt.title("Puntos por equipo")
plt.ylabel("Puntos")

plt.tight_layout()

plt.savefig("resultados/grafico_puntos.png")

print("Proceso finalizado.")