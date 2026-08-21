"""
Santander Open Academy — Cursor con Python: desarrollo inteligente con IA
Módulo práctico — automatización del sistema de archivos.

Clasifica Descargas por extensión (Imagenes, Documentos, Videos, Musica, Otros).
Práctica con Cursor: preguntar pathlib (suffix, iterdir, rename, mkdir).
La IA recuerda la API; tú decides la carpeta y pruebas antes en datos de ejemplo.

Cuidado: mueve archivos reales. No ejecutar a ciegas en carpetas importantes.
"""

from pathlib import Path

carpeta_objetivo = Path.home() / "Downloads"

categorias = {
    "Imagenes": [".png", ".jpg", ".jpeg", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Musica": [".mp3", ".wav"],
}

categoria_predeterminada = "Otros"

# Dict invertido: ".pdf" -> "Documentos" (búsqueda directa).
extension_a_categoria = {}

for categoria, extensiones in categorias.items():
    for extension in extensiones:
        extension_a_categoria[extension.lower()] = categoria

archivos = [archivo for archivo in carpeta_objetivo.iterdir() if archivo.is_file()]

for archivo in archivos:
    extension = archivo.suffix.lower()
    categoria = extension_a_categoria.get(extension, categoria_predeterminada)

    destino_dir = carpeta_objetivo / categoria
    destino_dir.mkdir(exist_ok=True)

    destino = destino_dir / archivo.name
    archivo.rename(destino)

    print(f"Movido: {archivo.name} → {categoria}")
