<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

# Analizador Léxico para Brazo Robótico - Instrucciones para Copilot

Este es un proyecto de analizador léxico desarrollado en Python con interfaz gráfica usando tkinter, especializado para lenguaje de control de brazo robótico.

## Características del proyecto:
- Analizador léxico para lenguaje de brazo robótico personalizado
- Interfaz gráfica con tkinter
- Editor de texto con contador de líneas
- Botones para abrir, guardar, analizar y limpiar
- Pantalla de salida para resultados y mensajes
- Validaciones específicas para componentes robóticos

## Estructura:
- `main.py`: Archivo principal con la interfaz gráfica
- `robot_lexical_analyzer.py`: Lógica del analizador léxico robótico
- `robot_tokens.py`: Definición de tokens robóticos
- `test_robot_code.robot`: Archivo de prueba robótico
- `lexical_analyzer.py`: Analizador léxico original (Java) - backup
- `java_tokens.py`: Definición de tokens de Java - backup
- `test_code.java`: Archivo de prueba Java - backup

## Lenguaje robótico soportado:
- Componentes: base, hombro, codo, garra, muneca
- Comandos: girai, giraf, abre, cierra, mueve, espera, inicio, fin, home
- Sintaxis: componente { comando valor }
- Comentarios: //, /* */, #
- Valores numéricos: enteros y decimales (incluyendo negativos)
- Estructuras: if/then/else, while, secuencias
