import os
import re

# Carpeta actual
carpeta = "."

renombrados = 0

for archivo in os.listdir(carpeta):
    if archivo.lower().endswith(".jpg"):
        nombre_sin_ext, ext = os.path.splitext(archivo)
        # Buscar los últimos 4 dígitos antes del .jpg
        match = re.search(r'(\d{4})$', nombre_sin_ext)
        if match:
            numero = match.group(1)
            nuevo_nombre = f"pagina_{numero}.jpg"
            if archivo != nuevo_nombre:
                os.rename(archivo, nuevo_nombre)
                print(f"✅ Renombrado: {archivo} → {nuevo_nombre}")
                renombrados += 1

if renombrados == 0:
    print("⚠️ No se encontró ningún archivo para renombrar.")
