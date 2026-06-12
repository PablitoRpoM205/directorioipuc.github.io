#!/usr/bin/env python3
import os
import json
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path
import urllib.request
import urllib.error
import time
import io

# Paths
department_dir = Path(__file__).parent / 'Departamentos'
output_file = Path(__file__).parent / 'department-counts.json'

# Mapping de archivos KMZ a nombres de departamento
department_mapping = {
    'Amazonas.kmz': 'Amazonas',
    'Antioquia.kmz': 'Antioquia',
    'Arauca.kmz': 'Arauca',
    'Atlántico.kmz': 'Atlántico',
    'Bogotá D.C.kmz': 'Bogotá D.C.',
    'Bolívar.kmz': 'Bolívar',
    'Boyacá.kmz': 'Boyacá',
    'Caldas.kmz': 'Caldas',
    'Caquetá.kmz': 'Caquetá',
    'Casanare.kmz': 'Casanare',
    'Cauca.kmz': 'Cauca',
    'Cesar.kmz': 'Cesar',
    'Chocó.kmz': 'Chocó',
    'Córdoba.kmz': 'Córdoba',
    'Cundinamarca.kmz': 'Cundinamarca',
    'Guainía.kmz': 'Guainía',
    'Guaviare.kmz': 'Guaviare',
    'Huila.kmz': 'Huila',
    'La Guajira.kmz': 'La Guajira',
    'Magdalena.kmz': 'Magdalena',
    'Meta.kmz': 'Meta',
    'Nariño.kmz': 'Nariño',
    'Norte de Santander.kmz': 'Norte de Santander',
    'Putumayo.kmz': 'Putumayo',
    'Quindío.kmz': 'Quindío',
    'Risaralda.kmz': 'Risaralda',
    'San Andrés y Providencia.kmz': 'San Andrés y Providencia',
    'Santander.kmz': 'Santander',
    'Sedes distritales y Centro Administrativo Nacional (CAN).kmz': 'Sedes distritales, CAN y fundaciones',
    'Sucre.kmz': 'Sucre',
    'Tolima.kmz': 'Tolima',
    'Valle del Cauca.kmz': 'Valle del Cauca',
    'Vaupés.kmz': 'Vaupés',
    'Vichada.kmz': 'Vichada'
}

# Departamentos que no se consideran congregaciones (no sumar en total)
EXCLUDE_FROM_TOTAL = {
    'Sedes distritales, CAN y fundaciones'
}


def extract_network_link(kmz_path):
    """Extrae la URL del NetworkLink desde el KML dentro del KMZ"""
    try:
        with zipfile.ZipFile(kmz_path, 'r') as kmz:
            # leer doc.kml si existe
            names = kmz.namelist()
            kml_name = None
            for n in names:
                if n.endswith('doc.kml') or n.endswith('.kml'):
                    kml_name = n
                    break
            if not kml_name:
                return None
            kml_content = kmz.read(kml_name).decode('utf-8')

        root = ET.fromstring(kml_content)
        namespaces = {'kml': 'http://www.opengis.net/kml/2.2'}

        # Buscar el href del NetworkLink
        href = root.find('.//kml:NetworkLink/kml:Link/kml:href', namespaces)
        if href is None:
            href = root.find('.//NetworkLink/Link/href')

        if href is not None and href.text:
            return href.text
        return None
    except Exception:
        return None


def download_and_count_placemarks(url, dept_name):
    """Descarga el KMZ remoto, extrae el KML, cuenta los placemarks y devuelve lista de placemarks."""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        req = urllib.request.Request(url, headers=headers)

        print(f'⬇ Descargando datos de {dept_name}...', end=' ', flush=True)
        with urllib.request.urlopen(req, timeout=20) as response:
            data = response.read()

        # Manejar ZIP (KMZ) en memoria
        kmz_file = io.BytesIO(data)
        with zipfile.ZipFile(kmz_file, 'r') as kmz:
            kml_name = None
            for name in kmz.namelist():
                if name.endswith('.kml'):
                    kml_name = name
                    break
            if not kml_name:
                print('✗ No se encontró KML en KMZ remoto')
                return None, []
            kml_content = kmz.read(kml_name).decode('utf-8')

        root = ET.fromstring(kml_content)
        namespaces = {'kml': 'http://www.opengis.net/kml/2.2'}

        placemark_elems = root.findall('.//kml:Placemark', namespaces)
        if not placemark_elems:
            placemark_elems = root.findall('.//Placemark')

        placemarks = []
        for pm in placemark_elems:
            name_el = pm.find('kml:name', namespaces) or pm.find('name')
            desc_el = pm.find('kml:description', namespaces) or pm.find('description')
            coord_el = pm.find('.//kml:Point/kml:coordinates', namespaces) or pm.find('.//coordinates')
            name = name_el.text.strip() if name_el is not None and name_el.text else ''
            desc = desc_el.text.strip() if desc_el is not None and desc_el.text else ''
            lat = None
            lon = None
            if coord_el is not None and coord_el.text:
                parts = coord_el.text.strip().split(',')
                if len(parts) >= 2:
                    lon = parts[0].strip()
                    lat = parts[1].strip()
            placemarks.append({
                'name': name,
                'description': desc,
                'latitude': lat,
                'longitude': lon,
                'source': url
            })

        count = len(placemarks)
        print(f'✓ {count} congregaciones')
        return count, placemarks

    except urllib.error.URLError:
        print('✗ Error de conexión')
        return None, []
    except Exception as e:
        print(f'✗ Error: {type(e).__name__}')
        return None, []


def process_kmz(filename):
    kmz_path = department_dir / filename
    dept_name = department_mapping.get(filename, filename.replace('.kmz', ''))

    print(f'\nProcesando: {dept_name}')

    url = extract_network_link(kmz_path)
    if not url:
        print('✗ No se encontró NetworkLink')
        return dept_name, None, []

    count, placemarks = download_and_count_placemarks(url, dept_name)

    time.sleep(0.25)
    return dept_name, count, placemarks


def main():
    counts = {}
    total = 0
    all_congregations = []

    files = sorted([f for f in os.listdir(department_dir) if f.endswith('.kmz')])
    print(f'Descargando datos de {len(files)} mapas...\n')
    print('=' * 60)

    for filename in files:
        dept_name, count, placemarks = process_kmz(filename)
        if count is not None:
            counts[dept_name] = count
            if dept_name not in EXCLUDE_FROM_TOTAL:
                total += count
        else:
            counts[dept_name] = None

        for p in placemarks:
            r = p.copy()
            r['department'] = dept_name
            all_congregations.append(r)

    output = {
        'total': total,
        'departments': counts,
        'dynamic': True
    }

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    # Export CSV
    if all_congregations:
        import csv
        csv_file = Path(__file__).parent / 'congregations.csv'
        with open(csv_file, 'w', newline='', encoding='utf-8') as cf:
            writer = csv.writer(cf)
            writer.writerow(['department', 'name', 'description', 'latitude', 'longitude', 'source'])
            for r in all_congregations:
                writer.writerow([r.get('department'), r.get('name'), r.get('description'), r.get('latitude'), r.get('longitude'), r.get('source')])
        print(f'✓ CSV exportado en: {csv_file.name}')

    print('\n' + '=' * 60)
    print(f'\n✓ Total de congregaciones (excluyendo sedes): {total}')
    print(f'✓ Datos guardados en: {output_file.name}')
    print('\nLos conteos se actualizarán cada vez que ejecutes este script.')


if __name__ == '__main__':
    main()
