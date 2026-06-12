# IPUC Colombia — Directorio de Congregaciones

Página web moderna y responsiva que muestra el directorio de congregaciones de la Iglesia Pentecostal Unida de Colombia por departamento, con mapas interactivos y conteos dinámicos actualizados automáticamente.

## Características

✨ **Directorio interactivo**
- 34 departamentos con mapas embebidos de Google My Maps
- Búsqueda y filtrado en tiempo real
- Diseño responsivo (móvil, tablet, escritorio)
- Banner de datos actualizados

📊 **Conteos dinámicos**
- Total de congregaciones en tiempo real
- Conteo por departamento visible en el sidebar
- Excluye "Sedes distritales, CAN y fundaciones" del total
- Actualización semanal automática vía GitHub Actions

📥 **Exportación de datos**
- CSV con lista completa de congregaciones (nombre, coords, departamento)
- Disponible en `congregations.csv`

## Publicación en GitHub Pages

### Requisitos previos
- Repositorio en GitHub (público recomendado)
- Git instalado localmente

### Paso a paso (⏱️ 5 minutos)

#### 1️⃣ Subir el proyecto a GitHub

Si tu repo ya está sincronizado:
```bash
cd /ruta/a/tu/proyecto
git add .
git commit -m "Initial commit: directorio de congregaciones IPUC"
git push origin main
```

Si es la primera vez:
```bash
# Crear repo en GitHub.com primero (nombre sugerido: congregaciones-ipuc)
# Luego clonar o asociar:
git remote add origin https://github.com/tuusuario/congregaciones-ipuc.git
git branch -M main
git push -u origin main
```

#### 2️⃣ Activar GitHub Pages

1. Ve a tu repo en GitHub.com
2. Menú superior → **Settings** → **Pages** (lado izq)
3. **Source**: selecciona `Deploy from a branch`
4. **Branch**: selecciona `main` y `/root` (la raíz del proyecto)
5. Haz clic en **Save**
6. Espera ~1 minuto. Aparecerá un enlace tipo `https://tuusuario.github.io/congregaciones-ipuc`

#### 3️⃣ Verificar que el Workflow funciona

1. Ve a tu repo en GitHub
2. Menú superior → **Actions**
3. Verás el workflow "Update congregation counts"
4. El workflow corre **cada lunes a las 06:00 UTC** (ajustable en `.github/workflows/update-counts.yml`)
5. Cuando corra, commitea automáticamente los cambios en `department-counts.json` y `congregations.csv`

#### 4️⃣ (Opcional) Personalizar horario del workflow

Edita `.github/workflows/update-counts.yml` línea ~7:
```yaml
- cron: '0 6 * * 1'   # Lunes 06:00 UTC
# Cambiar a:
- cron: '0 3 * * 0'   # Domingo 03:00 UTC (otro ejemplo)
# Herramienta: https://crontab.guru/
```

Luego commitea y pushea el cambio:
```bash
git add .github/workflows/update-counts.yml
git commit -m "chore: cambiar horario del workflow a domingo 03:00 UTC"
git push
```

---

## Uso local

### Ejecutar el script de actualización manualmente
```bash
python3 process-kmz.py
```
- Descarga conteos de los 34 mapas (toma ~2 minutos)
- Actualiza `department-counts.json` y `congregations.csv`
- Excluye las sedes del total automáticamente

### Inspeccionar/depurar un departamento
```bash
python3 debug_fetch.py "Antioquia"
```
- Muestra URL remota, cantidad de placemarks y primeros 30 nombres/coords
- Útil para verificar si los cambios en My Maps se reflejaron

### Ver la página localmente
```bash
python3 -m http.server 8000
# Abre http://localhost:8000/index.html
```

---

## Archivos principales

| Archivo | Descripción |
|---------|------------|
| `index.html` | Estructura HTML con sidebar sticky, mapas, stats |
| `styles.css` | Tema oscuro, diseño responsivo, CSS custom properties |
| `script.js` | Lógica de navegación, carga de conteos, búsqueda |
| `process-kmz.py` | Script que descarga datos de KMZ remoto (Google My Maps) |
| `congregations.csv` | Lista de todas las congregaciones (auto-generado) |
| `department-counts.json` | Conteos por departamento en JSON (auto-generado) |
| `.github/workflows/update-counts.yml` | Workflow semanal que ejecuta el script y commitea |
| `update_counts.sh` | Script helper para ejecución local/cron con opción de push |
| `debug_fetch.py` | Diagnóstico para inspeccionar KMZ remoto |

---

## Solución de problemas

### Los conteos siguen sin reflejarse después de cambios en My Maps
**Causa probable**: El KML remoto no se actualizó en Google.

**Solución**:
1. Abre el mapa en Google My Maps
2. Asegúrate de que la marca fue **realmente eliminada** (no oculta)
3. Guarda el mapa y ciérralo
4. Espera 1-5 minutos
5. Ejecuta: `python3 debug_fetch.py "Nombre departamento"` para verificar

Si el conteo remoto sigue igual, revisa los permisos de compartir del mapa en Google My Maps.

### El workflow no se ejecuta en GitHub Actions
- Verifica que `.github/workflows/update-counts.yml` esté en el branch `main`
- Revisa la pestaña **Actions** en GitHub para ver errores
- Asegúrate de que Python 3 está disponible (lo está por defecto en runners ubuntu-latest)

### La página no aparece en GitHub Pages
1. Verifica que GitHub Pages esté activado en Settings → Pages
2. Espera ~2 minutos después de activarlo
3. El URL es `https://tuusuario.github.io/nombredelrepo/`

---

## Datos

**Último conteo**: 2.983 congregaciones (excluyendo 15 sedes)
- Departamento mayor: Antioquia (426)
- Departamento menor: Vaupés (1)
- Sedes distritales, CAN y fundaciones: 15 (no incluidas en total)

---

## Licencia

Proyecto comunitario para la Iglesia Pentecostal Unida de Colombia.

---

## Contacto & Contribuciones

Para reportar errores en los datos o sugerir mejoras, abre un issue en GitHub o contacta al administrador del repo.

**Nota de privacidad**: Los datos de congregaciones son públicos (extraídos de Google My Maps). Respeta la política de privacidad y términos de servicio de Google.
