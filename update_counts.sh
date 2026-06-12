#!/usr/bin/env bash
# Script helper para ejecutar process-kmz.py y opcionalmente commitear los resultados.
set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR"

echo "Ejecutando process-kmz.py..."
python3 process-kmz.py

if [ "$?" -ne 0 ]; then
  echo "El script devolvió error. Abortando commit."
  exit 1
fi

# Si se exportó un CSV y estamos en un repo git, opcionalmente commitear
if command -v git >/dev/null 2>&1 && [ "${AUTO_PUSH:-0}" = "1" ]; then
  if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    git add department-counts.json congregations.csv || true
    git commit -m "chore: actualizar conteos de congregaciones (automático)" || true
    git push || true
    echo "Cambios empujados al remoto (si había cambios)."
  fi
fi

echo "Hecho."
