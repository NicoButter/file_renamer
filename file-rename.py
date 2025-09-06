import os
import re

# Pedir al usuario el directorio, con valor por defecto
directorio = input("Ingresa el path de la carpeta (Enter para usar la carpeta actual): ").strip()
if not directorio:
    directorio = os.getcwd()  # usa la carpeta actual si no se ingresa nada

# Verificar que exista
if not os.path.isdir(directorio):
    print("❌ El path ingresado no existe.")
    exit(1)

# Expresión regular para detectar archivos que empiezan con "WhatsApp Image"
patron = re.compile(r'^WhatsApp Image.*\.(jpg|jpeg|png|gif)$', re.IGNORECASE)

# Listar y filtrar archivos
archivos = [f for f in os.listdir(directorio) if patron.match(f)]
archivos.sort()

# Renombrar
for i, archivo in enumerate(archivos, start=1):
    extension = os.path.splitext(archivo)[1]
    nuevo_nombre = f"image-{i}{extension}"
    ruta_vieja = os.path.join(directorio, archivo)
    ruta_nueva = os.path.join(directorio, nuevo_nombre)
    
    print(f'Renombrando: {ruta_vieja} -> {ruta_nueva}')
    os.rename(ruta_vieja, ruta_nueva)

print("Renombrado completado ✅")
