#script para analizar un archivo csv y crear un scatter plot


import pandas as pd
import matplotlib.pyplot as plt

ARCHIVO_CSV = "datos.csv"

df = pd.read_csv(ARCHIVO_CSV)

print(f"Análisis de: {ARCHIVO_CSV}\n")
print("Estadísticas por columna:")
print("-" * 50)

for columna in df.columns:
    media = df[columna].mean()
    mediana = df[columna].median()
    desviacion = df[columna].std()

    print(f"\n{columna}:")
    print(f"  Media:              {media:,.2f}")
    print(f"  Mediana:            {mediana:,.2f}")
    print(f"  Desviación estándar: {desviacion:,.2f}")

col1, col2 = df.columns[0], df.columns[1]

plt.figure(figsize=(8, 6))
plt.scatter(df[col1], df[col2], alpha=0.7, edgecolors="black", linewidths=0.5)
plt.xlabel(col1)
plt.ylabel(col2)
plt.title(f"Scatter plot: {col1} vs {col2}")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("scatter_plot.png", dpi=150)
plt.show()

print(f"\nGráfica guardada en: scatter_plot.png")
