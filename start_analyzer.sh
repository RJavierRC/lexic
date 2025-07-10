#!/bin/bash

# Script de inicio para el Analizador Léxico Robótico
# Uso: ./start_analyzer.sh

echo "=== Analizador Léxico Robótico ==="
echo "Iniciando aplicación..."

# Verificar si estamos en el directorio correcto
if [ ! -f "main.py" ]; then
    echo "Error: No se encontró main.py"
    echo "Ejecuta este script desde el directorio del proyecto"
    exit 1
fi

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo "Error: Python3 no está instalado"
    exit 1
fi

# Verificar tkinter
if ! python3 -c "import tkinter" 2>/dev/null; then
    echo "Error: tkinter no está disponible"
    echo "Instala con: sudo apt install python3-tk"
    exit 1
fi

# Verificar DISPLAY para GUI
if [ -z "$DISPLAY" ]; then
    echo "Advertencia: DISPLAY no está configurado"
    echo "La GUI puede no funcionar correctamente"
fi

# Ejecutar la aplicación
echo "Ejecutando main.py..."
python3 main.py

echo "Aplicación terminada."
