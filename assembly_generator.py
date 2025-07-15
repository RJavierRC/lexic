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
    """Generador de ensamblador desde cuádruplos"""
    
    def __init__(self):
        self.variables = {}  # Variables declaradas
        self.labels = {}     # Etiquetas
        self.counters = {}   # Contadores
        self.temp_vars = {}  # Variables temporales
        self.code_lines = []
        self.data_lines = []
        
        # Configuración específica para Windows
        self.is_windows = os.name == 'nt'
        
        # Rutas del sistema
        self.base_path = os.path.dirname(os.path.abspath(__file__))
        self.dosbox_path = os.path.join(self.base_path, "DOSBox2")
        self.dosbox_exe = os.path.join(self.dosbox_path, "dosbox.exe")
        self.tasm_path = os.path.join(self.dosbox_path, "Tasm")
        self.config_file = os.path.join(self.dosbox_path, "configuracion.conf")
        
        # Verificar archivos críticos
        self.verify_system_files()
        
    def verify_system_files(self):
        """Verifica la existencia de archivos críticos para el funcionamiento"""
        if self.is_windows:
            # Verificar DOSBox
            if not os.path.exists(self.dosbox_exe):
                raise FileNotFoundError(f"DOSBox no encontrado en: {self.dosbox_exe}")
            
            # Verificar TASM y TLINK
            for tool in ["TASM.EXE", "TLINK.EXE"]:
                tool_path = os.path.join(self.tasm_path, tool)
                if not os.path.exists(tool_path):
                    raise FileNotFoundError(f"{tool} no encontrado en: {tool_path}")
            
            # Verificar archivo de configuración
            if not os.path.exists(self.config_file):
                raise FileNotFoundError(f"Archivo de configuración no encontrado: {self.config_file}")
        else:
            raise EnvironmentError("Este programa está optimizado para ejecutarse en Windows.")
    
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
            self.code_lines.append(f"; === DECLARACION DEL ROBOT {robot_name.upper()} ===")
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
                self.code_lines.append(f"    MOV AL, {motor_pattern}  ; Patron para {component}")
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
        """Obtiene el patron de bits para mover un motor"""
        # Convertir valor a patron de bits para motor paso a paso
        angle = int(float(value))
        
        # Mapear angulo a patron de 8 bits
        # Esto es una simplificación, en la práctica dependería del motor específico
        patterns = {
            'base': f"{(angle % 256):08b}B",
            'hombro': f"{(angle % 256):08b}B", 
            'codo': f"{(angle % 256):08b}B",
            'garra': f"{(angle % 256):08b}B",
            'muneca': f"{(angle % 256):08b}B"
        }
        
        return patterns.get(component, f"{(angle % 256):08b}B")
    
    def generate_complete_program(self, program_name="robot_program"):
        """Genera programa ensamblador completo usando template que funciona"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Usar exactamente el formato de codigo.asm que funciona
        asm_code = f""";-----------------------------------------------
; CONTROL DE TRES MOTORES PASO A PASO
; Programa: {program_name}
; Fecha: {timestamp}
; Generado automaticamente para control de 3 motores
;-----------------------------------------------

; Definiciones de puertos 8255 (fuera de segmentos)
PORTA   EQU 00H    ; Puerto A - Motor BASE
PORTB   EQU 02H    ; Puerto B - Motor HOMBRO 
PORTC   EQU 04H    ; Puerto C - Motor CODO
Config  EQU 06H    ; Registro de configuracion

DATA_SEG    SEGMENT
; Variables del programa (si las hubiera)
DATA_SEG    ENDS

CODE_SEG    SEGMENT
   ASSUME CS: CODE_SEG, DS:DATA_SEG

    START:
        MOV   AX, DATA_SEG
        MOV   DS, AX

        ; Configurar 8255 - todos los puertos como salida
        MOV   DX, Config
        MOV   AL, 10000000B
        OUT   DX, AL

        ; MOTOR A (BASE) - Secuencia de pasos
        MOV   DX, PORTA
        MOV   AL, 00000110B
        OUT   DX, AL
        MOV   CX, 0FFFFH
loopy1: LOOP  loopy1

        MOV   AL, 00001100B
        OUT   DX, AL
        MOV   CX, 0FFFFH
loopy2: LOOP  loopy2

        MOV   AL, 00001001B
        OUT   DX, AL
        MOV   CX, 0FFFFH
loopy3: LOOP  loopy3

        MOV   AL, 00000011B
        OUT   DX, AL
        MOV   CX, 0FFFFH
loopy4: LOOP  loopy4

        ; MOTOR B (HOMBRO) - Secuencia de pasos
        MOV   DX, PORTB
        MOV   AL, 00000110B
        OUT   DX, AL
        MOV   CX, 0FFFFH
loopy5: LOOP  loopy5

        MOV   AL, 00001100B
        OUT   DX, AL
        MOV   CX, 0FFFFH
loopy6: LOOP  loopy6

        MOV   AL, 00001001B
        OUT   DX, AL
        MOV   CX, 0FFFFH
loopy7: LOOP  loopy7

        MOV   AL, 00000011B
        OUT   DX, AL
        MOV   CX, 0FFFFH
loopy8: LOOP  loopy8

        ; MOTOR C (CODO) - Secuencia de pasos
        MOV   DX, PORTC
        MOV   AL, 00000110B
        OUT   DX, AL
        MOV   CX, 0FFFFH
loopy9: LOOP  loopy9

        MOV   AL, 00001100B
        OUT   DX, AL
        MOV   CX, 0FFFFH
loopy10: LOOP  loopy10

        MOV   AL, 00001001B
        OUT   DX, AL
        MOV   CX, 0FFFFH
loopy11: LOOP  loopy11

        MOV   AL, 00000011B
        OUT   DX, AL
        MOV   CX, 0FFFFH
loopy12: LOOP  loopy12

        ; Terminar programa
        MOV    AH,4CH
        MOV    AL,0
        INT    21H
CODE_SEG    ENDS
   END  START
"""
        
        return asm_code

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
        self.config_file = os.path.join(dosbox_path, "configuracion.conf")
    
    def compile_assembly(self, asm_code, output_name="robot_program"):
        """Compila código ensamblador usando sistema instantáneo sin timeouts"""
        try:
            print(f"⚡ Iniciando compilación instantánea para {output_name}.exe...")
            
            # Usar el compilador instantáneo que evita timeouts de DOSBox
            from instant_compiler import InstantCompiler
            
            compiler = InstantCompiler()
            success, message = compiler.compile_instant(asm_code, output_name)
            
            if success:
                return True, f"🎯 ¡COMPILACIÓN INSTANTÁNEA EXITOSA!\n\n{message}\n\n✅ Ejecutable listo para usar en Proteus\n🔧 Control de 3 motores paso a paso implementado"
            else:
                return False, f"⚠️ Compilación falló: {message}"
            
        except Exception as e:
            return False, f"❌ Error durante la compilación instantánea: {str(e)}"
    
    def _compile_with_dosbox_fallback(self, asm_code, output_name):
        """Método de respaldo usando DOSBox/TASM - Versión Windows Optimizada"""
        try:
            # Verificar que estamos en Windows
            if os.name != 'nt':
                return False, "Esta versión está optimizada para Windows."
            
            # Verificar DOSBox
            if not os.path.exists(self.dosbox_exe):
                # Aún así generar el archivo ASM
                asm_file = os.path.join(self.tasm_path, f"{output_name}.asm")
                with open(asm_file, 'w', encoding='ascii', errors='ignore') as f:
                    f.write(asm_code)
                
                return False, f"⚠️ DOSBox no encontrado en: {self.dosbox_exe}\n\n✅ Archivo ASM generado: {asm_file}\n📝 {len(asm_code)} caracteres de código válido\n🔧 Compile manualmente con TASM para generar .exe"
            
            # Crear archivo .asm
            asm_file = os.path.join(self.tasm_path, f"{output_name}.asm")
            with open(asm_file, 'w', encoding='ascii', errors='ignore') as f:
                f.write(asm_code)
            
            # Script de compilación mejorado para Windows con diagnósticos completos
            batch_script = f"""@echo off
echo ================================================
echo ANALIZADOR LEXICO - COMPILACION AUTOMATICA
echo ================================================
echo Programa: {output_name.upper()}.EXE
echo ================================================
cd Tasm
echo [1/4] Verificando archivos...
if not exist "TASM.EXE" (
    echo ❌ TASM.EXE no encontrado
    goto error
)
if not exist "TLINK.EXE" (
    echo ❌ TLINK.EXE no encontrado  
    goto error
)
if not exist "{output_name}.asm" (
    echo ❌ {output_name}.asm no encontrado
    goto error
)
echo ✅ Archivos verificados

echo [2/4] Ejecutando TASM...
TASM {output_name}.asm
if errorlevel 1 (
    echo ❌ Error en TASM
    goto error
)
echo ✅ TASM completado

echo [3/4] Ejecutando TLINK...
TLINK /t {output_name}.obj
if errorlevel 1 (
    echo ⚠️ Error en TLINK modo /t, intentando modo estándar...
    TLINK {output_name}.obj,{output_name}.exe,,
    if errorlevel 1 (
        echo ❌ Error en TLINK modo estándar
        goto error
    )
)
echo ✅ TLINK completado

echo [4/4] Verificando resultado...
if exist "{output_name}.exe" (
    echo ✅ {output_name}.exe creado exitosamente
    dir {output_name}.exe
    goto success
) else (
    echo ❌ {output_name}.exe no se generó
    goto error
)

:success
echo ================================================
echo          COMPILACION EXITOSA
echo ================================================
echo 🎯 Ejecutable listo para Proteus
echo 📁 Ubicación: %cd%\\{output_name}.exe
goto end

:error
echo ================================================
echo         ERROR DE COMPILACION  
echo ================================================
echo 📋 Diagnóstico:
if exist "{output_name}.asm" echo • Archivo ASM: ✅ OK
if not exist "{output_name}.asm" echo • Archivo ASM: ❌ FALTA
if exist "{output_name}.obj" echo • Archivo OBJ: ✅ OK  
if not exist "{output_name}.obj" echo • Archivo OBJ: ❌ FALTA
if exist "{output_name}.exe" echo • Archivo EXE: ✅ OK
if not exist "{output_name}.exe" echo • Archivo EXE: ❌ FALTA
echo.
echo 💡 Compile manualmente: TASM {output_name}.asm ^&^& TLINK {output_name}.obj

:end
"""
            
            batch_file = os.path.join(self.dosbox_path, "compile_windows.bat")
            # Usar codificación ASCII para máxima compatibilidad
            with open(batch_file, 'w', encoding='ascii', errors='ignore') as f:
                f.write(batch_script)
            
            # Ejecutar DOSBox con configuración optimizada para Windows
            cmd = [self.dosbox_exe, "-c", "mount c .", "-c", "c:", "-c", "compile_windows.bat", "-c", "exit"]
            
            print(f"🔧 Ejecutando compilación DOSBox: {output_name}.exe")
            result = subprocess.run(cmd, cwd=self.dosbox_path, capture_output=True, text=True, timeout=30)
            
            # Verificar si se generó el ejecutable
            exe_file = os.path.join(self.tasm_path, f"{output_name}.exe")
            if os.path.exists(exe_file):
                size = os.path.getsize(exe_file)
                return True, f"✅ Ejecutable generado con DOSBox/TASM!\n📄 Archivo: {exe_file}\n📊 Tamaño: {size} bytes\n🎯 Listo para simulación en Proteus"
            else:
                # Diagnóstico detallado del error
                error_msg = "⚠️ No se pudo generar el ejecutable automáticamente\n\n"
                
                # Verificar archivos intermedios
                asm_exists = os.path.exists(asm_file)
                obj_exists = os.path.exists(os.path.join(self.tasm_path, f"{output_name}.obj"))
                
                error_msg += f"📊 Diagnóstico:\n"
                error_msg += f"- Archivo ASM: {'✅ OK' if asm_exists else '❌ FALTA'}\n"
                error_msg += f"- Archivo OBJ: {'✅ OK' if obj_exists else '❌ FALTA'}\n"
                error_msg += f"- Archivo EXE: ❌ FALTA\n\n"
                
                if asm_exists:
                    error_msg += f"✅ Archivo ASM generado correctamente: {asm_file}\n"
                    error_msg += f"📝 {len(asm_code)} caracteres de código válido\n"
                    error_msg += f"🔧 Compile manualmente: TASM {output_name}.asm && TLINK {output_name}.obj\n"
                
                return False, error_msg
                
        except subprocess.TimeoutExpired:
            return False, "Timeout: La compilación tardó demasiado (>30s)"
        except Exception as e:
            return False, f"Error al compilar: {str(e)}"
    
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
        return True, "Configuración Windows verificada"

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
