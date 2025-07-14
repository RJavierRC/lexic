#!/bin/bash
# Script de inicio para macOS
# Analizador Léxico para Brazo Robótico

echo "🤖 Iniciando Analizador Léxico para Brazo Robótico en macOS..."
echo "📁 Directorio: $(pwd)"

# Verificar que estemos en el directorio correcto
if [ ! -f "main.py" ]; then
    echo "❌ Error: No se encontró main.py"
    echo "   Asegúrate de estar en el directorio del proyecto"
    exit 1
fi

# Verificar entorno virtual
if [ ! -d ".venv" ]; then
    echo "⚠️  No se encontró entorno virtual (.venv)"
    echo "   Creando entorno virtual..."
    python3 -m venv .venv
    echo "✅ Entorno virtual creado"
fi

# Activar entorno virtual
echo "🔄 Activando entorno virtual..."
source .venv/bin/activate

# Verificar Python
echo "� Versión de Python: $(python --version)"

# Mostrar funcionalidades por sistema
echo ""
echo "🍎 MODO macOS DETECTADO:"
echo "   ✅ Análisis léxico, sintáctico y semántico completo"
echo "   ✅ Generación de código intermedio (cuádruplos)" 
echo "   ✅ Generación de código ensamblador (.asm)"
echo "   ✅ Interfaz gráfica optimizada para macOS"
echo "   ⚠️  Compilación .EXE no disponible (requiere Windows/Linux)"
echo "   💡 Usa el botón 'Ver ASM' para generar código ensamblador"
echo ""

# Ejecutar aplicación
echo "🚀 Iniciando aplicación..."
echo "   Nota: La interfaz está optimizada para macOS"
echo ""

# Silenciar warning de Tkinter y ejecutar
export TK_SILENCE_DEPRECATION=1
python main.py

echo ""
echo "👋 Analizador cerrado. ¡Hasta luego!"
