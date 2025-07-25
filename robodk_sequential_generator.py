#!/usr/bin/env python3
"""
Generador secuencial de archivos .mod para RoboDK
Convierte sintaxis robótica a movimientos RAPID secuenciales
"""

import os
import re
from datetime import datetime
from robot_lexical_analyzer import RobotLexicalAnalyzer

class RoboDKSequentialGenerator:
    """Generador secuencial de archivos .mod que sigue el orden del código Robot"""
    
    def __init__(self):
        self.analyzer = RobotLexicalAnalyzer()
        self.robot_name = "r1"
        self.current_state = {
            'base': 0.0,
            'hombro': 0.0,
            'codo': 0.0,
            'muneca': 0.0,
            'garra': 90.0,  # Garra abierta por defecto
            'velocidad': 1
        }
        self.movement_sequence = []
        
    def analyze_robot_code(self, code):
        """Analiza el código y extrae la secuencia de movimientos"""
        # Limpiar código de comentarios
        lines = code.split('\n')
        clean_lines = []
        
        for line in lines:
            line = line.strip()
            if line and not line.startswith('#') and not line.startswith('//'):
                clean_lines.append(line)
        
        clean_code = '\n'.join(clean_lines)
        
        # Analizar con el analizador léxico
        tokens, errors = self.analyzer.analyze(clean_code)
        
        # Extraer nombre del robot
        for i, token in enumerate(tokens):
            if hasattr(token, 'type') and hasattr(token, 'value'):
                if token.type == 'KEYWORD' and token.value.lower() == 'robot':
                    if i + 1 < len(tokens):
                        next_token = tokens[i + 1]
                        if hasattr(next_token, 'value'):
                            self.robot_name = next_token.value
                            break
        
        # Procesar secuencialmente las instrucciones
        self._process_sequential_instructions(clean_code)
        
        return tokens, errors
    
    def _process_sequential_instructions(self, code):
        """Procesa las instrucciones en orden secuencial"""
        lines = code.split('\n')
        
        for line in lines:
            line = line.strip()
            if not line or line.startswith('#') or line.startswith('//'):
                continue
                
            # Buscar patrón: robot.componente = valor
            pattern = r'(\w+)\.(\w+)\s*=\s*(\w+)'
            match = re.match(pattern, line)
            
            if match:
                robot_name, component, value = match.groups()
                
                if robot_name == self.robot_name:
                    # Convertir valor
                    if component == 'velocidad':
                        self.current_state[component] = int(value)
                    elif component == 'espera':
                        # Agregar movimiento de espera
                        self.movement_sequence.append({
                            'type': 'wait',
                            'time': float(value)
                        })
                    elif component in ['base', 'hombro', 'codo', 'muneca', 'garra']:
                        # Actualizar estado y agregar movimiento
                        old_value = self.current_state[component]
                        new_value = float(value)
                        self.current_state[component] = new_value
                        
                        # Agregar movimiento
                        self.movement_sequence.append({
                            'type': 'move',
                            'component': component,
                            'from': old_value,
                            'to': new_value,
                            'velocity': self.current_state['velocidad'],
                            'state': self.current_state.copy()
                        })
    
    def generate_mod_file(self, code, output_filename="robot_program.mod"):
        """Genera archivo .mod secuencial para RoboDK"""
        
        # Analizar código
        tokens, errors = self.analyze_robot_code(code)
        
        # Generar timestamp
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        # Crear contenido del archivo .mod
        mod_content = f"""%%%
  VERSION:1
  LANGUAGE:ENGLISH
%%%
MODULE MOD_MainProgram

    ! -------------------------------
    ! Programa generado automáticamente desde sintaxis robótica
    ! Robot: {self.robot_name}
    ! Fecha: {timestamp}
    ! Movimientos secuenciales: {len(self.movement_sequence)} pasos
    ! -------------------------------

    ! Tool variables: 
    PERS tooldata RobotiQ2F85Gripper(FullyClosed) := [TRUE,[[0.000,0.000,130.000],[1.00000000,0.00000000,0.00000000,0.00000000]],[1,[0,0,20],[1,0,0,0],0,0,0.005]];

    ! Reference variables:
    PERS wobjdata Frame2 := [FALSE, TRUE, "", [[0,0,0],[1,0,0,0]],[[-140.437,-738.971,5.234],[1.00000000,0.00000000,0.00000000,0.00000000]]];

"""
        
        # Generar procedimiento Main con movimientos secuenciales
        mod_content += self._generate_main_procedure()
        
        # Cerrar módulo
        mod_content += "\nENDMODULE\n"
        
        # Guardar archivo
        output_path = os.path.join(os.getcwd(), output_filename)
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(mod_content)
            
            return True, f"✅ Archivo .mod secuencial generado exitosamente:\n📁 {output_path}\n🤖 Robot: {self.robot_name}\n📊 Movimientos secuenciales: {len(self.movement_sequence)} pasos\n🎯 Listo para importar en RoboDK"
            
        except Exception as e:
            return False, f"❌ Error al generar archivo .mod: {str(e)}"
    
    def _generate_main_procedure(self):
        """Genera el procedimiento Main con movimientos secuenciales"""
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        main_proc = f"""    PROC Main()
        ConfJ \\On;
        ConfL \\Off;
        
        ! Program generated from Robot syntax on {timestamp}
        ! Robot: {self.robot_name}
        ! Secuencia de {len(self.movement_sequence)} movimientos
        
        ! === INICIO DE SECUENCIA DE MOVIMIENTOS ===
        
"""
        
        step = 1
        for movement in self.movement_sequence:
            if movement['type'] == 'move':
                # Generar movimiento MoveAbsJ
                state = movement['state']
                velocity = self._get_velocity_string(movement['velocity'])
                component = movement['component']
                
                main_proc += f"        ! Paso {step}: Mover {component} de {movement['from']}° a {movement['to']}°\n"
                
                # Determinar gripper basado en garra
                gripper_state = "RobotiQ2F85Gripper(FullyClosed)" if state['garra'] < 50 else "RobotiQ2F85Gripper(FullyClosed)"
                
                # Generar MoveAbsJ con estado completo
                main_proc += f"        MoveAbsJ [[{state['base']:.6f},{state['hombro']:.6f},{state['codo']:.6f},{state['muneca']:.6f},{self._get_gripper_angle(state['garra'])},-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],{velocity},z1,{gripper_state} \\WObj:=Frame2;\n"
                
                step += 1
                
            elif movement['type'] == 'wait':
                # Generar espera
                main_proc += f"        ! Paso {step}: Esperar {movement['time']} segundos\n"
                main_proc += f"        WaitTime {movement['time']};\n"
                step += 1
            
            main_proc += "\n"
        
        main_proc += f"""        ! === FIN DE SECUENCIA ===
        ! Total de pasos ejecutados: {step - 1}
        
    ENDPROC"""
        
        return main_proc
    
    def _get_velocity_string(self, velocity):
        """Convierte velocidad numérica a string RAPID"""
        velocity_map = {
            1: "v50",   # Muy lenta
            2: "v100",  # Lenta
            3: "v200",  # Media
            4: "v500",  # Rápida
            5: "v1000"  # Muy rápida
        }
        return velocity_map.get(velocity, f"v{velocity * 50}")
    
    def _get_gripper_angle(self, garra_value):
        """Convierte valor de garra a ángulo de quinta articulación"""
        # Si garra es baja (cerrada), usar ángulo negativo
        # Si garra es alta (abierta), usar ángulo positivo
        if garra_value < 50:
            return f"{-abs(garra_value):.6f}"  # Cerrada
        else:
            return f"{garra_value:.6f}"        # Abierta
    
    def get_movement_summary(self):
        """Obtiene resumen de los movimientos"""
        if not self.movement_sequence:
            return "No hay movimientos procesados"
        
        summary = f"Secuencia de {len(self.movement_sequence)} movimientos:\n\n"
        
        for i, movement in enumerate(self.movement_sequence, 1):
            if movement['type'] == 'move':
                summary += f"{i}. Mover {movement['component']}: {movement['from']}° → {movement['to']}° (v={movement['velocity']})\n"
            elif movement['type'] == 'wait':
                summary += f"{i}. Esperar: {movement['time']} segundos\n"
        
        return summary

def test_sequential_generator():
    """Función de prueba para el generador secuencial"""
    
    # Código de prueba completo
    test_code = """Robot r1                          
                 
# === POSICIÓN INICIAL DE APROXIMACIÓN ===
r1.velocidad = 1       
r1.base = 0            
r1.hombro = 90         
r1.codo = 90           
r1.garra = 90          
r1.espera = 2          

# === IR A POSICIÓN DEL OBJETO ===
r1.velocidad = 2       
r1.base = 45           
r1.hombro = 120        
r1.codo = 90           
r1.espera = 1          

# === BAJAR Y AGARRAR OBJETO ===
r1.velocidad = 1       
r1.codo = 45           
r1.espera = 1          

r1.garra = 20          
r1.espera = 1          

# === LEVANTAR OBJETO ===
r1.codo = 90           
r1.hombro = 90         
r1.espera = 1          

# === MOVER A POSICIÓN DE DESTINO ===
r1.velocidad = 3       
r1.base = 180          
r1.hombro = 100        
r1.espera = 2          

# === COLOCAR OBJETO ===
r1.velocidad = 1       
r1.codo = 60           
r1.espera = 1          

r1.garra = 90          
r1.espera = 1          

# === ALEJARSE DEL OBJETO ===
r1.codo = 90           
r1.hombro = 90         
r1.espera = 1          

# === REGRESAR A POSICIÓN ORIGINAL ===
r1.velocidad = 4       
r1.base = 0            
r1.hombro = 90         
r1.codo = 90           
r1.espera = 2"""
    
    generator = RoboDKSequentialGenerator()
    success, message = generator.generate_mod_file(test_code, "pick_place_sequence.mod")
    
    print("=== GENERADOR SECUENCIAL .MOD PARA ROBODK ===")
    print(f"Resultado: {message}")
    
    print("\n=== RESUMEN DE MOVIMIENTOS ===")
    print(generator.get_movement_summary())
    
    if success:
        print("\n=== ARCHIVO .MOD GENERADO (PRIMERAS LÍNEAS) ===")
        try:
            with open("pick_place_sequence.mod", 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.split('\n')
                for i, line in enumerate(lines[:50]):  # Mostrar primeras 50 líneas
                    print(f"{i+1:2d}: {line}")
                if len(lines) > 50:
                    print(f"... y {len(lines) - 50} líneas más")
        except:
            print("No se pudo leer el archivo generado")

if __name__ == "__main__":
    test_sequential_generator()