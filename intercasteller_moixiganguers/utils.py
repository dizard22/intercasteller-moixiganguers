import reflex as rx


# Común
def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='cat'")


preview = "moixiganguers-igualada.png"

_meta = [
    {"name": "og:type", "content": "website"},
    {"name": "og:image", "content": preview},
    {"name": "twitter:card", "content": "summary_large_image"},
    {"name": "twitter:site", "content": "@moixiganguers"}
]

# Index
index_title = "Selecció morada | Presentació de l'equip casteller de futbol de la ciutat d'Igualada"
index_description = ("Els moixiganguers d'Igualada disputaran el XX Torneig Casteller de Futbol 2024 de Berga.")

index_meta = [
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_description},
]
index_meta.extend(_meta)
