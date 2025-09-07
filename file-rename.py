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

# Pedir el número de inicio para la secuencia
try:
    inicio = input("Ingresa el número de inicio para la secuencia (Enter para empezar desde 1): ").strip()
    inicio = int(inicio) if inicio else 1
except ValueError:
    print("❌ Entrada inválida. Se usará 1 como inicio.")
    inicio = 1

# Expresión regular para detectar archivos que empiezan con "WhatsApp Image"
patron = re.compile(r'^WhatsApp Image.*\.(jpg|jpeg|png|gif)$', re.IGNORECASE)

# Listar y filtrar archivos
archivos = [f for f in os.listdir(directorio) if patron.match(f)]
archivos.sort()  # Ordenar alfabéticamente para consistencia

if not archivos:
    print("⚠️  No se encontraron archivos que coincidan con el patrón 'WhatsApp Image'.")
    exit(0)

# Renombrar
print(f"\nRenombrando {len(archivos)} archivos, comenzando desde {inicio}...\n")

for i, archivo in enumerate(archivos, start=inicio):
    nombre, extension = os.path.splitext(archivo)
    nuevo_nombre = f"image-{i}{extension.lower()}"  # Normalizar extensión a minúsculas
    ruta_vieja = os.path.join(directorio, archivo)
    ruta_nueva = os.path.join(directorio, nuevo_nombre)
    
    # Evitar sobrescribir si ya existe un archivo con el nuevo nombre
    if os.path.exists(ruta_nueva):
        print(f"⚠️  {ruta_nueva} ya existe. Saltando {archivo}.")
        continue
    
    try:
        print(f'✅ Renombrando: {archivo} -> {nuevo_nombre}')
        os.rename(ruta_vieja, ruta_nueva)
    except OSError as e:
        print(f"❌ Error al renombrar {archivo}: {e}")

print("\n✨ Renombrado completado.")