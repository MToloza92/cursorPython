import json

from flask import Flask, request, redirect, render_template

app = Flask(__name__)

# Lista donde almacenaremos las tareas
tareas = []

# ID que tendrá la próxima tarea
siguiente_id = 1


def cargar_datos():
    global tareas, siguiente_id

    try:
        with open("tareas.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

            tareas = datos["tareas"]
            siguiente_id = datos["siguiente_id"]

    except FileNotFoundError:
        pass

def guardar_datos():
    with open("tareas.json", "w", encoding="utf-8") as archivo:
        json.dump(
            {
                "siguiente_id": siguiente_id,
                "tareas": tareas
            },
            archivo,
            ensure_ascii=False,
            indent=4
        )

def agregar_tarea(texto):
    global siguiente_id

    tareas.append({
        "id": siguiente_id,
        "texto": texto,
        "hecho": False
    })

    siguiente_id += 1
    guardar_datos()


def completar_tarea(id):
    for tarea in tareas:
        if tarea["id"] == id:
            tarea["hecho"] = True
            break

    guardar_datos()


@app.route("/")
def index():
    tareas_ordenadas = sorted(tareas, key=lambda t: t["hecho"])

    return render_template(
        "index.html",
        tareas=tareas_ordenadas
    )


@app.route("/agregar", methods=["POST"])
def agregar():
    texto_tarea = request.form.get("texto_tarea")

    if texto_tarea:
        agregar_tarea(texto_tarea)

    return redirect("/")


@app.route("/completar/<int:id>")
def completar(id):
    completar_tarea(id)

    return redirect("/")

cargar_datos()


if __name__ == "__main__":
    app.run(debug=True)