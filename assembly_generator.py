#!/usr/bin/env python3
"""
Generador de código ensamblador para brazo robótico
Convierte cuádruplos a código ensamblador x86 para TASM
"""

import os
import subprocess
import tempfile
import glob
from datetime import datetime

class AssemblyGenerator:
    """Generador de código ensamblador desde cuádruplos"""
    
    def __init__(self):
        self.variables = {}  # Variables declaradas
        self.labels = {}     # Etiquetas
        self.counters = {}   # Contadores
        self.temp_vars = {}  # Variables temporales
        self.code_lines = []
        self.data_lines = []
        self.ports = {
            'base': 'PORTA',
            'hombro': 'PORTB', 
            'codo': 'PORTC',
            'garra': 'PORTD',
            'muneca': 'PORTE',
            'velocidad': 'PORTF'
        }
        
    def generate_assembly(self, cuadruplos, program_name="robot_program"):
        """Genera código ensamblador completo desde cuádruplos"""
        self.reset()
        
        # Procesar cuádruplos
        for i, cuadruplo in enumerate(cuadruplos):
            self.process_cuadruplo(cuadruplo, i)
        
        # Generar código completo
        assembly_code = self.generate_complete_program(program_name)
        return assembly_code
    
    def reset(self):
        """Reinicia el generador"""
        self.variables.clear()
        self.labels.clear()
        self.counters.clear()
        self.temp_vars.clear()
        self.code_lines.clear()
        self.data_lines.clear()
    
    def process_cuadruplo(self, cuadruplo, index):
        """Procesa un cuádruplo individual"""
        op = cuadruplo.operacion
        arg1 = cuadruplo.arg1
        arg2 = cuadruplo.arg2
        result = cuadruplo.resultado
        
        if op == 'DECLARAR':
            self.process_declarar(arg1, result)
        elif op == 'ASIG':
            self.process_asignacion(arg1, result)
        elif op == 'CALL':
            self.process_call(arg1, arg2, result)
        elif op == 'COMPARAR':
            self.process_comparar(arg1, arg2, result)
        elif op == 'SALTO_CONDICIONAL':
            self.process_salto_condicional(arg1, result)
        elif op == 'SALTO_INCONDICIONAL':
            self.process_salto_incondicional(result)
        elif op == 'DECREMENTO':
            self.process_decremento(arg1, result)
        elif op == 'DECLARAR_ETIQUETA':
            self.process_declarar_etiqueta(result)
        elif op == 'FIN':
            self.process_fin(result)
    
    def process_declarar(self, tipo, robot_name):
        """Procesa declaración de robot"""
        if tipo == 'robot':
            self.code_lines.append(f"; === DECLARACIÓN DEL ROBOT {robot_name.upper()} ===")
            self.data_lines.append(f"{robot_name.upper()}_STATUS DB 0  ; Estado del robot")
    
    def process_asignacion(self, valor, variable):
        """Procesa asignación de valor a variable"""
        if variable.startswith('CX'):
            # Contador
            self.counters[variable] = valor
            self.data_lines.append(f"{variable} DW {valor}  ; Contador")
            self.code_lines.append(f"    MOV {variable}, {valor}  ; Inicializar contador")
        elif variable.startswith('T'):
            # Variable temporal
            self.temp_vars[variable] = valor
            self.data_lines.append(f"{variable} DW {valor}  ; Variable temporal")
        elif variable in self.ports:
            # Componente del robot
            self.variables[variable] = valor
            port = self.ports[variable]
            self.code_lines.append(f"    MOV AL, {valor}  ; Valor para {variable}")
            self.code_lines.append(f"    MOV DX, {port}  ; Puerto del {variable}")
            self.code_lines.append(f"    OUT DX, AL  ; Enviar valor al {variable}")
    
    def process_call(self, component, value, robot):
        """Procesa llamada a movimiento"""
        if component in self.ports:
            port = self.ports[component]
            self.code_lines.append(f"    ; === MOVER {component.upper()} DEL ROBOT {robot.upper()} ===")
            
            if component == 'espera':
                # Comando de espera
                delay_value = int(float(value) * 10000)  # Convertir a ciclos
                self.code_lines.append(f"    MOV CX, {delay_value}  ; Esperar {value} segundos")
                self.code_lines.append("DELAY_LOOP:")
                self.code_lines.append("    LOOP DELAY_LOOP")
            else:
                # Movimiento de motor
                motor_pattern = self.get_motor_pattern(component, value)
                self.code_lines.append(f"    MOV AL, {motor_pattern}  ; Patrón para {component}")
                self.code_lines.append(f"    MOV DX, {port}  ; Puerto del {component}")
                self.code_lines.append(f"    OUT DX, AL  ; Mover {component} a {value}°")
                
                # Agregar delay entre movimientos
                self.code_lines.append("    MOV CX, 0FFFFH  ; Delay entre movimientos")
                self.code_lines.append("MOVE_DELAY:")
                self.code_lines.append("    LOOP MOVE_DELAY")
    
    def process_comparar(self, var1, var2, result):
        """Procesa comparación"""
        self.code_lines.append(f"    ; === COMPARAR {var1} CON {var2} ===")
        self.code_lines.append(f"    CMP {var1}, {var2}  ; Comparar {var1} con {var2}")
        self.code_lines.append(f"    MOV {result}, 0  ; Asumir falso")
        self.code_lines.append(f"    JNE COMP_END_{result}  ; Si no son iguales, saltar")
        self.code_lines.append(f"    MOV {result}, 1  ; Son iguales, verdadero")
        self.code_lines.append(f"COMP_END_{result}:")
    
    def process_salto_condicional(self, condition, label):
        """Procesa salto condicional"""
        self.code_lines.append(f"    ; === SALTO CONDICIONAL ===")
        self.code_lines.append(f"    CMP {condition}, 1  ; Verificar condición")
        self.code_lines.append(f"    JE {label}  ; Saltar si es verdadero")
    
    def process_salto_incondicional(self, label):
        """Procesa salto incondicional"""
        self.code_lines.append(f"    JMP {label}  ; Salto incondicional")
    
    def process_decremento(self, variable, result):
        """Procesa decremento"""
        self.code_lines.append(f"    DEC {variable}  ; Decrementar {variable}")
        if result != variable:
            self.code_lines.append(f"    MOV {result}, {variable}  ; Guardar resultado")
    
    def process_declarar_etiqueta(self, label):
        """Procesa declaración de etiqueta"""
        self.labels[label] = len(self.code_lines)
        self.code_lines.append(f"{label}:")
    
    def process_fin(self, label):
        """Procesa fin de bloque"""
        self.code_lines.append(f"{label}:")
        self.code_lines.append(f"    ; === FIN DEL BLOQUE ===")
    
    def get_motor_pattern(self, component, value):
        """Obtiene el patrón de bits para mover un motor"""
        # Convertir valor a patrón de bits para motor paso a paso
        angle = int(float(value))
        
        # Mapear ángulo a patrón de 8 bits
        # Esto es una simplificación, en la práctica dependería del motor específico
        patterns = {
            'base': f"{(angle % 256):08b}B",
            'hombro': f"{(angle % 256):08b}B", 
            'codo': f"{(angle % 256):08b}B",
            'garra': f"{(angle % 256):08b}B",
            'muneca': f"{(angle % 256):08b}B"
        }
        
        return patterns.get(component, f"{(angle % 256):08b}B")
    
    def generate_complete_program(self, program_name):
        """Genera el programa ensamblador completo"""
        header = f"""
; =====================================================
; CÓDIGO ENSAMBLADOR GENERADO AUTOMÁTICAMENTE
; Programa: {program_name}
; Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
; Generado desde cuádruplos del analizador robótico
; =====================================================

.MODEL SMALL

.STACK 100H

.DATA
    ; === CONFIGURACIÓN DE PUERTOS ===
    PORTA  EQU 00H    ; Puerto para motor BASE
    PORTB  EQU 02H    ; Puerto para motor HOMBRO
    PORTC  EQU 04H    ; Puerto para motor CODO
    PORTD  EQU 06H    ; Puerto para motor GARRA
    PORTE  EQU 08H    ; Puerto para motor MUÑECA
    PORTF  EQU 0AH    ; Puerto para VELOCIDAD
    CONFIG EQU 0CH    ; Puerto de configuración
    
    ; === VARIABLES DEL PROGRAMA ===
"""
        
        # Agregar variables de datos
        for data_line in self.data_lines:
            header += f"    {data_line}\n"
        
        # Agregar variables temporales y contadores que no se declararon
        for var, value in self.temp_vars.items():
            if not any(var in line for line in self.data_lines):
                header += f"    {var} DW {value}  ; Variable temporal\n"
        
        for var, value in self.counters.items():
            if not any(var in line for line in self.data_lines):
                header += f"    {var} DW {value}  ; Contador\n"
        
        code_section = """
.CODE
MAIN PROC
    ; === INICIALIZACIÓN ===
    MOV AX, @DATA
    MOV DS, AX
    
    ; Configurar puertos como salidas
    MOV DX, CONFIG
    MOV AL, 10000000B  ; Todos los puertos como salidas
    OUT DX, AL
    
    ; === INICIO DEL PROGRAMA PRINCIPAL ===
"""
        
        # Agregar código generado
        for code_line in self.code_lines:
            code_section += f"    {code_line}\n"
        
        footer = """
    ; === FIN DEL PROGRAMA ===
    MOV AH, 4CH  ; Función de terminación
    MOV AL, 0    ; Código de salida
    INT 21H      ; Llamada al sistema
    
MAIN ENDP
END MAIN
"""
        
        return header + code_section + footer

class DOSBoxController:
    """Controlador para automatizar DOSBox y TASM - Optimizado para Windows"""
    
    def __init__(self, dosbox_path=None):
        # Detectar automáticamente la ruta para Windows
        if dosbox_path is None:
            current_dir = os.getcwd()
            dosbox_path = os.path.join(current_dir, "DOSBox2")
        
        self.dosbox_path = dosbox_path
        self.tasm_path = os.path.join(dosbox_path, "Tasm")
        self.dosbox_exe = os.path.join(dosbox_path, "dosbox.exe")
    
    def compile_assembly(self, asm_code, output_name="robot_program"):
        """Compila código ensamblador usando DOSBox y TASM - Versión Windows Optimizada"""
        try:
            # Verificar que estamos en Windows
            if os.name != 'nt':
                return False, "⚠️ Esta versión está optimizada para Windows."
            
            # Verificar DOSBox
            if not os.path.exists(self.dosbox_exe):
                return False, f"❌ DOSBox no encontrado en: {self.dosbox_exe}"
            
            # Crear archivo .asm
            asm_file = os.path.join(self.tasm_path, f"{output_name}.asm")
            with open(asm_file, 'w', encoding='utf-8') as f:
                f.write(asm_code)
            
            # Script de compilación optimizado para Windows
            batch_script = f"""@echo off
echo ================================================
echo ANALIZADOR LEXICO - COMPILACION WINDOWS
echo ================================================
echo Programa: {output_name.upper()}.EXE
echo ================================================
cd Tasm
echo [1/3] Ejecutando TASM...
TASM {output_name}.asm
if errorlevel 1 goto error
echo [2/3] Ejecutando TLINK...
TLINK {output_name}.obj
if errorlevel 1 goto error
echo [3/3] Verificando resultado...
if exist "{output_name}.exe" (
    echo ✓ {output_name}.exe creado exitosamente
    goto success
) else (
    goto error
)

:success
echo ================================================
echo          COMPILACION EXITOSA
echo ================================================
goto end

:error
echo ================================================
echo         ERROR DE COMPILACION
echo ================================================

:end
timeout /t 2 /nobreak >nul
"""
            
            batch_file = os.path.join(self.dosbox_path, "compile_windows.bat")
            with open(batch_file, 'w', encoding='utf-8') as f:
                f.write(batch_script)
            
            # Ejecutar DOSBox con configuración optimizada para Windows
            cmd = [self.dosbox_exe, "-c", "mount c .", "-c", "c:", "-c", "compile_windows.bat", "-c", "exit"]
            
            print(f"🔧 Ejecutando compilación: {output_name}.exe")
            result = subprocess.run(cmd, cwd=self.dosbox_path, capture_output=True, text=True, timeout=30)
            
            # Verificar si se generó el ejecutable
            exe_file = os.path.join(self.tasm_path, f"{output_name}.exe")
            if os.path.exists(exe_file):
                return True, f"✅ Ejecutable {output_name}.exe generado exitosamente\n📁 Ubicación: DOSBox2/Tasm/{output_name}.exe"
            else:
                error_msg = "❌ Error en la compilación Windows.\n"
                if result.stderr:
                    error_msg += f"Error: {result.stderr}\n"
                if result.stdout:
                    error_msg += f"Output: {result.stdout}\n"
                return False, error_msg
                
        except subprocess.TimeoutExpired:
            return False, "⏱️ Timeout: La compilación tardó demasiado (>30s)"
        except Exception as e:
            return False, f"❌ Error al compilar: {str(e)}"
    
    def get_generated_files(self):
        """Obtiene lista de archivos generados en Windows"""
        files = []
        for ext in ['.asm', '.obj', '.exe', '.map']:
            pattern = os.path.join(self.tasm_path, f"*{ext}")
            files.extend(glob.glob(pattern))
        return files
    
    def verify_windows_setup(self):
        """Verifica que la configuración de Windows esté completa"""
        required_files = {
            "DOSBox": self.dosbox_exe,
            "TASM": os.path.join(self.tasm_path, "TASM.EXE"),
            "TLINK": os.path.join(self.tasm_path, "TLINK.EXE")
        }
        
        missing = []
        for name, path in required_files.items():
            if not os.path.exists(path):
                missing.append(f"{name}: {path}")
        
        if missing:
            return False, "Archivos faltantes:\n" + "\n".join(missing)
        return True, "✅ Configuración Windows verificada"

def test_assembly_generator():
    """Función de prueba para el generador"""
    from robot_lexical_analyzer import RobotLexicalAnalyzer
    
    # Código de prueba
    code = """
Robot r1
r1.repetir = 2
r1.inicio
r1.base = 90
r1.hombro = 45
r1.espera = 1
r1.fin
"""
    
    # Analizar código
    analyzer = RobotLexicalAnalyzer()
    tokens, errors = analyzer.analyze(code)
    
    if not errors and analyzer.intermediate_code_generator:
        # Generar ensamblador
        generator = AssemblyGenerator()
        asm_code = generator.generate_assembly(analyzer.intermediate_code_generator.cuadruplos)
        
        print("=== CÓDIGO ENSAMBLADOR GENERADO ===")
        print(asm_code)
        
        # Compilar (comentado para pruebas)
        # controller = DOSBoxController()
        # success, message = controller.compile_assembly(asm_code, "test_robot")
        # print(f"Compilación: {message}")
        
        return asm_code
    else:
        print(f"Errores en el análisis: {errors}")
        return None

if __name__ == "__main__":
    test_assembly_generator()
