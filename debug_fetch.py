#!/usr/bin/env python3
"""Script de diagnóstico: descarga el KMZ remoto de un departamento y lista algunos placemarks.
Uso: python3 debug_fetch.py "Antioquia"
"""
import sys
from pathlib import Path
import zipfile, xml.etree.ElementTree as ET, urllib.request

if len(sys.argv) < 2:
    print('Uso: debug_fetch.py "Nombre departamento"')
    sys.exit(1)

department = sys.argv[1]
repo = Path(__file__).parent
# Buscar el archivo kmz por mapeo simple
# Hacemos una búsqueda por nombre de archivo que contenga el nombre del departamento
kmz_dir = repo / 'Departamentos'
matches = [p for p in kmz_dir.iterdir() if p.is_file() and p.suffix.lower() == '.kmz' and department.lower() in p.name.lower()]
if not matches:
    print('No se encontró KMZ para', department)
    sys.exit(1)
kmz_path = matches[0]
print('Usando KMZ:', kmz_path.name)

# Extraer la URL
with zipfile.ZipFile(kmz_path,'r') as kmz:
    kml = kmz.read('doc.kml').decode('utf-8')
root = ET.fromstring(kml)
ns={'kml':'http://www.opengis.net/kml/2.2'}
href = root.find('.//kml:NetworkLink/kml:Link/kml:href',ns)
if href is None:
    href = root.find('.//NetworkLink/Link/href')
if href is None or not href.text:
    print('No hay NetworkLink en el KMZ local.')
    sys.exit(1)
url = href.text
print('NetworkLink URL:', url)

# Descargar remoto
req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=20) as r:
    data = r.read()

import io
kmz_remote = zipfile.ZipFile(io.BytesIO(data))
name=None
for n in kmz_remote.namelist():
    if n.endswith('.kml'):
        name=n; break
print('Remote KML:', name)

kml2 = kmz_remote.read(name).decode('utf-8')
root2 = ET.fromstring(kml2)
pe = root2.findall('.//{http://www.opengis.net/kml/2.2}Placemark')
if not pe:
    pe = root2.findall('.//Placemark')
print('Total placemarks remotos:', len(pe))

print('\nPrimeros 30 placemarks (nombre, coords):')
for pm in pe[:30]:
    nm = pm.find('{http://www.opengis.net/kml/2.2}name') or pm.find('name')
    coord = pm.find('.//{http://www.opengis.net/kml/2.2}coordinates') or pm.find('.//coordinates')
    nm_text = nm.text.strip() if nm is not None and nm.text else ''
    coord_text = coord.text.strip() if coord is not None and coord.text else ''
    print('-', nm_text[:80], coord_text)

print('\nSi esperabas otro conteo, revisa en Google My Maps que los cambios se hayan guardado y publicado (compartir/privado).')
