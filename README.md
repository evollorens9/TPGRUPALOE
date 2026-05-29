# Análisis de Resultados Deportivos

## Descripción del Proyecto

Este proyecto tiene como objetivo analizar los resultados de un campeonato deportivo utilizando Python y pandas.

El sistema permite:

* importar resultados de partidos desde un archivo CSV
* calcular estadísticas básicas del torneo
* generar una tabla de posiciones
* calcular el promedio de goles
* generar gráficos comparativos entre equipos

---

## Estructura del Proyecto

```text
TP/
│
├── scripts/
│   └── analisis_deportivo.py
│
├── datos/
│   └── partidos.csv
│
├── resultados/
│   ├── tabla_posiciones.csv
│   └── grafico_puntos.png
│
├── README.md
│
└── .gitignore
```

---

## Librerías Utilizadas

* pandas
* matplotlib

---

## Cómo Ejecutar el Proyecto

1. Clonar el repositorio:

```bash
git clone URL_DEL_REPOSITORIO
```

2. Ingresar a la carpeta del proyecto:

```bash
cd TP
```

3. Ejecutar el script principal:

```bash
python scripts/analisis_deportivo.py
```

---

## Resultados Generados

El programa genera:

* una tabla de posiciones en formato CSV
* gráficos de rendimiento de equipos
* estadísticas generales del torneo

Todos los resultados se guardan dentro de la carpeta `/resultados`.

---

## Buenas Prácticas Implementadas

* Uso de rutas relativas
* Organización modular del proyecto
* Trazabilidad mediante Jira
* Uso de `.gitignore`
* Separación entre scripts, datos y resultados
