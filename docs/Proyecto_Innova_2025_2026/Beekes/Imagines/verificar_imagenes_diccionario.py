
import os
from PIL import Image

# Configuración
CARPETA = "paginas"
PREFIJO = "pagina_"
SUFIJO = ".jpg"
ALTURA_MIN = 1400
ALTURA_MAX = 2200
PESO_MAX_KB = 500

def es_nombre_valido(nombre):
    return nombre.startswith(PREFIJO) and nombre.endswith(SUFIJO) and nombre[len(PREFIJO):-len(SUFIJO)].isdigit()

def verificar_imagenes():
    archivos = os.listdir(CARPETA)
    jpgs = [f for f in archivos if f.lower().endswith('.jpg')]
    nombres_invalidos = []
    duplicados = set()
    nombres_vistos = set()
    errores_resolucion = []
    errores_peso = []

    for nombre in sorted(jpgs):
        if not es_nombre_valido(nombre):
            nombres_invalidos.append(nombre)
        else:
            if nombre in nombres_vistos:
                duplicados.add(nombre)
            else:
                nombres_vistos.add(nombre)

        ruta = os.path.join(CARPETA, nombre)
        try:
            with Image.open(ruta) as img:
                w, h = img.size
                if h < ALTURA_MIN or h > ALTURA_MAX:
                    errores_resolucion.append((nombre, w, h))
            peso_kb = os.path.getsize(ruta) / 1024
            if peso_kb > PESO_MAX_KB:
                errores_peso.append((nombre, round(peso_kb, 1)))
        except Exception as e:
            print(f"⚠️ No se pudo abrir la imagen {nombre}: {e}")

    print("\n📋 Informe de verificación de imágenes:")
    if nombres_invalidos:
        print(f"❌ Nombres inválidos: {nombres_invalidos}")
    if duplicados:
        print(f"❌ Duplicados: {duplicados}")
    if errores_resolucion:
        print("\n❌ Imágenes con resolución fuera de rango:")
        for nombre, w, h in errores_resolucion:
            print(f"  - {nombre}: {w}x{h}px")
    if errores_peso:
        print("\n❌ Imágenes que superan los {PESO_MAX_KB} KB:")
        for nombre, peso in errores_peso:
            print(f"  - {nombre}: {peso} KB")

    if not (nombres_invalidos or duplicados or errores_resolucion or errores_peso):
        print("✅ Todas las imágenes son válidas.")

if __name__ == "__main__":
    verificar_imagenes()
