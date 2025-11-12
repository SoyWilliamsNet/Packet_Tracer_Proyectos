#!/usr/bin/env python3
"""
generar_readmes_extended.py

Lee videos.csv (formato extendido) y genera README.md en cada carpeta listada
si el README.md no existe (salta si existe, a menos que uses --force).

Uso:
  python generar_readmes_extended.py --csv videos.csv       # modo normal
  python generar_readmes_extended.py --csv videos.csv --dry # dry-run (no escribe)
  python generar_readmes_extended.py --csv videos.csv --force # sobrescribe READMEs

CSV esperado (encabezado, las columnas pueden estar en cualquier orden):
folder,video_id,title,description,obj1,obj2,obj3,obj4,Tecnologias utilizadas,Estructura del repositorio,pkt_file,image_file

Reglas para nombres de archivos:
- El nombre de la carpeta (column `folder`) se respeta tal cual.
- Si `pkt_file` o `image_file` están vacíos, se generan desde el nombre de la carpeta:
  espacios -> '_' ; eliminar '-' y '.' (puntos) del nombre generado.
"""
import argparse
import csv
from pathlib import Path
import sys

TEMPLATE = """# {title}

## 📘 Descripción del proyecto
{description}

🔗 **Video del laboratorio:**  
🎥 [{title}](https://youtu.be/{video_id})

---

## 🎯 Objetivos del proyecto

1. **{obj1}**

2. **{obj2}**

3. **{obj3}**

4. **{obj4}**

---

## 🧰 Tecnologías y herramientas utilizadas

{technologies}

---

## 📂 Estructura del repositorio
{folder}/

├── {pkt_file} ← Archivo del laboratorio (abrir con Packet Tracer)

├── {image_file} ← Imagen de la topología del proyecto

└── README.md ← Documentación del laboratorio


---

## 🚀 Cómo usarlo

1. Descarga el archivo `.pkt` desde esta carpeta.  
2. Ábrelo con **Cisco Packet Tracer 8.x o superior**.  
3. Revisa la topología y las configuraciones.  
4. Ejecuta pruebas (`ping`, `show ip route`, etc.) para validar la red.  

---

## 🌐 Topología visual

![Topología del laboratorio]({image_file})

---

## 📝 Notas adicionales

- Proyecto educativo del canal **El Networker TI**  
  🎬 [YouTube - El Networker TI](https://www.youtube.com/@ElNetworkerTI)  
- Más laboratorios disponibles en:  
  💼 [GitHub - Packet Tracer Projects](https://github.com/TU_USUARIO/TU_REPO)

---
"""

def sanitize_filename(name: str) -> str:
    # reglas: espacios -> '_', eliminar '-' y '.', conservar resto
    s = name.replace(' ', '_')
    s = s.replace('-', '')
    s = s.replace('.', '')
    return s

def read_csv(csv_path: Path):
    if not csv_path.exists():
        print(f"CSV no encontrado: {csv_path}")
        sys.exit(1)
    rows = []
    with csv_path.open(newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append({k.strip(): (v.strip() if v is not None else '') for k,v in r.items()})
    return rows

def get_field(row, key, default=''):
    # acepta variantes de nombre de columna
    if key in row and row[key]:
        return row[key]
    # intentos con mayúsculas iniciales
    alt = key.capitalize()
    if alt in row and row[alt]:
        return row[alt]
    return default

def generate_readme_text(fields):
    return TEMPLATE.format(**fields)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--csv', '-c', default='videos.csv', help='CSV con metadata')
    parser.add_argument('--root', '-r', default='.', help='Raíz donde están las carpetas')
    parser.add_argument('--force', '-f', action='store_true', help='Forzar sobrescritura de README')
    parser.add_argument('--dry', action='store_true', help='Simular sin escribir archivos')
    args = parser.parse_args()

    csv_path = Path(args.csv).resolve()
    root = Path(args.root).resolve()
    rows = read_csv(csv_path)

    for row in rows:
        folder_name = row.get('folder') or row.get('Folder') or ''
        if not folder_name:
            print("[WARN] fila sin 'folder' -> salto")
            continue

        folder_path = root / folder_name
        if not folder_path.exists() or not folder_path.is_dir():
            print(f"[SKIP] Carpeta no encontrada: {folder_path}")
            continue

        # campos básicos
        title = get_field(row, 'title', folder_name)
        video_id = get_field(row, 'video_id', 'XXXXX')
        description = get_field(row, 'description', f"Laboratorio práctico: {title}.")
        obj1 = get_field(row, 'obj1', f"Comprender los conceptos clave relacionados con {title}.")
        obj2 = get_field(row, 'obj2', "Configurar los dispositivos necesarios y aplicar comandos.")
        obj3 = get_field(row, 'obj3', "Verificar la conectividad entre dispositivos.")
        obj4 = get_field(row, 'obj4', "Probar variantes o extensiones del laboratorio.")
        technologies = get_field(row, 'Tecnologias utilizadas', get_field(row, 'technologies', "Cisco Packet Tracer; Routers; Switches; PCs; CLI"))

        # pkt e imagen: si estan en CSV, respetar; si no, generarlos desde folder_name
        pkt_file = get_field(row, 'pkt_file', '')
        image_file = get_field(row, 'image_file', '')

        if not pkt_file:
            pkt_file = sanitize_filename(folder_name) + '.pkt'
        if not image_file:
            image_file = sanitize_filename(folder_name) + '.jpg'

        # preparar campos para plantilla
        fields = {
            'title': title,
            'description': description,
            'video_id': video_id,
            'obj1': obj1,
            'obj2': obj2,
            'obj3': obj3,
            'obj4': obj4,
            'technologies': technologies,
            'folder': folder_name,
            'pkt_file': pkt_file,
            'image_file': image_file
        }

        readme_path = folder_path / 'README.md'
        if readme_path.exists() and not args.force:
            print(f"[SKIP] README ya existe en {folder_name}")
            continue

        content = generate_readme_text(fields)
        if args.dry:
            print("---- DRY RUN ----")
            print(f"Carpeta: {folder_name}")
            print(f"README path: {readme_path}")
            print("Contenido (primeras 10 líneas):")
            print('\n'.join(content.splitlines()[:10]))
            print("-----------------")
            continue

        readme_path.write_text(content, encoding='utf-8')
        print(f"[CREATED] {readme_path}")

if __name__ == '__main__':
    main()

