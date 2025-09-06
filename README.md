# WhatsApp Image Renamer 🖼️✨

Un **script en Python** para renombrar automáticamente imágenes de WhatsApp en un directorio, con nombres uniformes como `image-1.jpg`, `image-2.png`, etc. Perfecto para organizar tus fotos de manera profesional.

![WhatsApp Images](docs/preview.png)

---

## 🚀 Funcionalidades

* Detecta archivos que comienzan con `WhatsApp Image`
* Renombra automáticamente con formato `image-N` manteniendo la extensión original
* Permite ingresar el directorio dinámicamente o usar la carpeta actual
* Compatible con `.jpg`, `.jpeg`, `.png` y `.gif`
* Muestra en consola las rutas antes y después del renombrado

---

## ⚙️ Requisitos

* Python 3.x
* Windows / macOS / Linux

---

## 📝 Uso

1. Clonar el repositorio:

```bash
git clone https://github.com/NicoButter/filerenamer.git
cd whatsapp-image-renamer
```

2. Ejecutar el script:

```bash
python rename_images.py
```

3. Ingresar la ruta de la carpeta con las imágenes o presionar **Enter** para usar la carpeta actual:

```
Ingresa el path de la carpeta (Enter para usar la carpeta actual):
```

4. El script renombrará las imágenes y mostrará los cambios en consola:

```
Renombrando: WhatsApp Image 2025-09-06 at 10.12.34.jpg -> image-1.jpg
Renombrando: WhatsApp Image 2025-09-06 at 10.15.47.png -> image-2.png
...
Renombrado completado ✅
```

---

## 🔧 Personalización

* Cambiar prefijo de los nombres:

```python
nuevo_nombre = f"miFoto-{i}{extension}"
```

* Agregar más extensiones:

```python
patron = re.compile(r'^WhatsApp Image.*\.(jpg|jpeg|png|gif|heic)$', re.IGNORECASE)
```

---

## 📂 Estructura del Repo

```
whatsapp-image-renamer/
├── rename_images.py      # Script principal
├── README.md            # Este archivo
└── docs/
    └── preview.png      # Imagen de ejemplo
```

---

## 🛡️ Licencia

MIT License - ¡Usalo y modificalo libremente!

---

## 📬 Contacto

Desarrollado por Nicolás Butterfield
📧 [nicobutter@gmail.com](mailto:nicobutter@gmail.com)

¡Se aceptan ideas, sugerencias, mejoras o memes!

💡 **Tip:** Ideal para limpiar carpetas de fotos de WhatsApp antes de subirlas a tu galería, repositorios o proyectos.
