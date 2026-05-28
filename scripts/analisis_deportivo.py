import pandas as pd
import matplotlib.pyplot as plt

# Leer datos
df = pd.read_csv("../datos/partidos.csv")

# Equipos
equipos = pd.concat([
    df["equipo_local"],
    df["equipo_visitante"]
]).unique()

# Tabla
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

    # Victoria local
    if gl > gv:
        tabla[local]["Puntos"] += 3
        tabla[local]["Ganados"] += 1

    # Victoria visitante
    elif gv > gl:
        tabla[visitante]["Puntos"] += 3
        tabla[visitante]["Ganados"] += 1

    # Empate
    else:
        tabla[local]["Puntos"] += 1
        tabla[visitante]["Puntos"] += 1

# Convertir a DataFrame
tabla_df = pd.DataFrame(tabla).T

# Ordenar por puntos
tabla_df = tabla_df.sort_values(by="Puntos", ascending=False)

# Guardar tabla
tabla_df.to_csv("../resultados/tabla_posiciones.csv")

# Promedio goles
promedio_goles = (
    df["goles_local"].sum() +
    df["goles_visitante"].sum()
) / len(df)

print("Promedio de goles:", round(promedio_goles, 2))

# Gráfico
tabla_df["Puntos"].plot(kind="bar")

plt.title("Puntos por equipo")
plt.ylabel("Puntos")

plt.tight_layout()

plt.savefig("../resultados/grafico_puntos.png")

print("Análisis completado.")