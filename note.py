#este script crea un notebook con un ejemplo basico de analisis de datos con Python


import json
from pathlib import Path

notebook = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# Ejemplo básico de análisis de datos con Python\n",
                "\n",
                "Este notebook utiliza un pequeño conjunto de datos para calcular estadísticas simples."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "import pandas as pd\n",
                "\n",
                "# Crear un pequeño conjunto de datos\n",
                "datos = {\n",
                "    'horas_estudio': [2, 3, 4, 5, 6],\n",
                "    'nota': [4.0, 4.8, 5.5, 6.2, 6.8]\n",
                "}\n",
                "\n",
                "df = pd.DataFrame(datos)\n",
                "df"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## Promedio\n",
                "\n",
                "Calculamos el promedio de las horas de estudio y de las notas."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "promedio_horas = df['horas_estudio'].mean()\n",
                "promedio_nota = df['nota'].mean()\n",
                "\n",
                "print(f'Promedio de horas de estudio: {promedio_horas:.2f}')\n",
                "print(f'Promedio de nota: {promedio_nota:.2f}')"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## Relación entre horas de estudio y nota\n",
                "\n",
                "Creamos un gráfico sencillo para observar si existe una relación entre ambas variables."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "import matplotlib.pyplot as plt\n",
                "\n",
                "plt.scatter(df['horas_estudio'], df['nota'])\n",
                "plt.xlabel('Horas de estudio')\n",
                "plt.ylabel('Nota')\n",
                "plt.title('Horas de estudio vs. nota')\n",
                "plt.show()"
            ]
        }
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "name": "python",
            "version": "3.x"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 5
}

path = Path("C:/Users/mauri/cursorPython/note.ipynb")
path.write_text(json.dumps(notebook, ensure_ascii=False, indent=2), encoding="utf-8")

print(f"Archivo creado: {path.absolute}")
