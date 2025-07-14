#!/bin/bash
# Script de inicio para Linux
# Analizador Léxico para Brazo Robótico

echo "🤖 Iniciando Analizador Léxico para Brazo Robótico en Linux..."
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
echo "🐍 Versión de Python: $(python --version)"

# Mostrar funcionalidades para Linux
echo ""
echo "🐧 MODO LINUX DETECTADO:"
echo "   ✅ Análisis léxico, sintáctico y semántico completo"
echo "   ✅ Generación de código intermedio (cuádruplos)" 
echo "   ✅ Generación de código ensamblador (.asm)"
echo "   ✅ Compilación a ejecutable .EXE (via DOSBox + TASM)"
echo "   ✅ Todas las funcionalidades disponibles"
echo "   💡 Usa 'Compilar' para generar archivos .exe"
echo ""

# Verificar DOSBox (opcional)
if [ -d "DOSBox2" ]; then
    echo "✅ DOSBox encontrado - Compilación .EXE disponible"
else
    echo "⚠️  DOSBox no encontrado - Solo generación ASM disponible"
    echo "   Para compilación completa, asegúrate que DOSBox2/ esté presente"
fi

# Ejecutar aplicación
echo "🚀 Iniciando aplicación..."
echo ""

python main.py

echo ""
echo "👋 Analizador cerrado. ¡Hasta luego!"
