import json

with open("servidor/datos/catalogo.json", encoding="utf-8") as f:
    datos = json.load(f)

articulos = datos["articulos"]
print("Artículos en el catálogo:", len(articulos))