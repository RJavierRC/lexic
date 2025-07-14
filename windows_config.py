# Configuración para Windows - Analizador Léxico
# Este archivo contiene las rutas y configuraciones específicas para Windows

import os
import platform

# Verificar que estamos en Windows
if platform.system() != "Windows":
    raise RuntimeError("Este proyecto está optimizado para Windows. Usa la versión multiplataforma para otros sistemas.")

# Configuración de rutas
PROJECT_DIR = os.getcwd()
DOSBOX_DIR = os.path.join(PROJECT_DIR, "DOSBox2")
TASM_DIR = os.path.join(DOSBOX_DIR, "Tasm")
DOSBOX_EXE = os.path.join(DOSBOX_DIR, "dosbox.exe")

# Archivos necesarios
REQUIRED_FILES = {
    "DOSBox": DOSBOX_EXE,
    "TASM": os.path.join(TASM_DIR, "TASM.EXE"),
    "TLINK": os.path.join(TASM_DIR, "TLINK.EXE")
}

# Configuración de compilación
COMPILATION_CONFIG = {
    "timeout_seconds": 30,
    "show_dosbox_window": False,
    "keep_intermediate_files": True,
    "output_directory": TASM_DIR
}

# Tipos de archivos soportados
SUPPORTED_EXTENSIONS = {
    "robot": "Archivos Robot (*.robot)",
    "asm": "Archivos Ensamblador (*.asm)",
    "exe": "Archivos Ejecutables (*.exe)"
}

def verify_windows_setup():
    """Verifica que la configuración de Windows esté completa"""
    missing_files = []
    
    for name, path in REQUIRED_FILES.items():
        if not os.path.exists(path):
            missing_files.append(f"{name}: {path}")
    
    if missing_files:
        error_msg = "Archivos faltantes para la compilación:\n\n"
        error_msg += "\n".join(f"• {file}" for file in missing_files)
        error_msg += "\n\nAsegúrate de que la carpeta DOSBox2 esté completa."
        return False, error_msg
    
    return True, "Configuración de Windows verificada correctamente"

def get_output_path(program_name):
    """Obtiene la ruta completa del archivo .exe generado"""
    return os.path.join(TASM_DIR, f"{program_name}.exe")

def get_dosbox_command(batch_file):
    """Genera el comando para ejecutar DOSBox"""
    return [
        DOSBOX_EXE,
        "-c", "mount c .",
        "-c", "c:",
        "-c", batch_file,
        "-c", "exit"
    ]

# Información del sistema
SYSTEM_INFO = {
    "name": "Windows Edition",
    "version": "5.0",
    "platform": platform.system(),
    "architecture": platform.architecture()[0],
    "python_version": platform.python_version(),
    "compilation_available": True
}

print("🪟 Configuración Windows cargada exitosamente")
