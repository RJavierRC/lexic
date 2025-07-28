#!/usr/bin/env python3
"""
Generador CORREGIDO de archivos .mod para RoboDK
Mapeo correcto de articulaciones ABB IRB140
"""

import os
import re
from datetime import datetime
from robot_lexical_analyzer import RobotLexicalAnalyzer

class RoboDKFixedGenerator:
    """Generador corregido con mapeo correcto de articulaciones"""
    
    def __init__(self):
        self.analyzer = RobotLexicalAnalyzer()
        self.robot_name = "r1"
        self.current_state = {
            'base': 0.0,      # Eje 1: Rotación base
            'hombro': 0.0,    # Eje 2: Brazo inferior  
            'codo': 0.0,      # Eje 3: Codo
            'muneca': 0.0,    # Eje 4: Rotación antebrazo
            'garra': 0.0,     # Eje 6: Garra (NO eje 5)
            'velocidad': 1
        }
        self.movement_sequence = []
        
    def analyze_robot_code(self, code):
        """Analiza el código y extrae la secuencia de movimientos"""
        lines = code.split('\n')
        clean_lines = []
        
        for line in lines:
            line = line.strip()
            if line and not line.startswith('#') and not line.startswith('//'):
                clean_lines.append(line)
        
        clean_code = '\n'.join(clean_lines)
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
        
        # Procesar tokens secuencialmente
        i = 0
        while i < len(tokens):
            token = tokens[i]
            
            if hasattr(token, 'type') and hasattr(token, 'value'):
                if token.type == 'IDENTIFIER' and '.' in token.value:
                    robot_component = token.value.split('.')
                    if len(robot_component) == 2:
                        robot_var, component = robot_component
                        
                        # Buscar el valor asignado
                        if i + 2 < len(tokens):
                            equals_token = tokens[i + 1]
                            value_token = tokens[i + 2]
                            
                            if (hasattr(equals_token, 'type') and equals_token.type == 'ASSIGN' and
                                hasattr(value_token, 'type') and value_token.type == 'NUMBER'):
                                
                                old_value = self.current_state.get(component, 0.0)
                                new_value = float(value_token.value)
                                
                                # Solo agregar si el valor cambió
                                if abs(old_value - new_value) > 0.001:
                                    if component == 'espera':
                                        # Agregar espera
                                        self.movement_sequence.append({
                                            'type': 'wait',
                                            'time': new_value
                                        })
                                    elif component in self.current_state:
                                        # Agregar movimiento
                                        self.movement_sequence.append({
                                            'type': 'move',
                                            'component': component,
                                            'from': old_value,
                                            'to': new_value,
                                            'velocity': self.current_state['velocidad'],
                                            'state': self.current_state.copy()
                                        })
                                        
                                        # Actualizar estado
                                        self.current_state[component] = new_value
            i += 1
            
        return tokens, errors
    
    def generate_mod_file(self, code, output_filename="robot_fixed.mod"):
        """Genera archivo .mod CORREGIDO para RoboDK"""
        
        # Analizar código
        tokens, errors = self.analyze_robot_code(code)
        
        # Generar timestamp
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        # Crear contenido del archivo .mod
        mod_content = f"""%%%
  VERSION:1
  LANGUAGE:ENGLISH
%%%
MODULE MOD_FixedProgram

    ! -------------------------------
    ! Programa CORREGIDO - Mapeo correcto de articulaciones
    ! Robot: {self.robot_name}
    ! Fecha: {timestamp}
    ! Movimientos: {len(self.movement_sequence)} pasos
    ! -------------------------------

    ! Tool variables: 
    PERS tooldata RobotiQ2F85Gripper := [TRUE,[[0.000,0.000,130.000],[1.00000000,0.00000000,0.00000000,0.00000000]],[1,[0,0,20],[1,0,0,0],0,0,0.005]];

    ! Reference variables:
    PERS wobjdata Frame2 := [FALSE, TRUE, "", [[0,0,0],[1,0,0,0]],[[-140.437,-738.971,5.234],[1.00000000,0.00000000,0.00000000,0.00000000]]];

"""
        
        # Generar procedimiento Main corregido
        mod_content += self._generate_main_procedure_fixed()
        
        # Cerrar módulo
        mod_content += "\nENDMODULE\n"
        
        # Guardar archivo
        output_path = os.path.join(os.getcwd(), output_filename)
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(mod_content)
            
            return True, f"✅ Archivo .mod CORREGIDO generado:\n📁 {output_path}\n🤖 Robot: {self.robot_name}\n📊 Movimientos: {len(self.movement_sequence)} pasos\n🎯 Mapeo de articulaciones CORREGIDO"
            
        except Exception as e:
            return False, f"❌ Error: {str(e)}"
    
    def _generate_main_procedure_fixed(self):
        """Genera procedimiento Main con mapeo CORRECTO de articulaciones"""
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        main_proc = f"""    PROC Main()
        ConfJ \\On;
        ConfL \\Off;
        
        ! Programa generado {timestamp}
        ! Robot: {self.robot_name}
        ! MAPEO CORRECTO:
        ! base → Eje 1 (rotación horizontal)
        ! hombro → Eje 2 (brazo inferior arriba/abajo)  
        ! codo → Eje 3 (codo arriba/abajo)
        ! muneca → Eje 4 (rotación antebrazo)
        ! garra → Eje 6 (apertura/cierre gripper)
        
        ! Posición inicial
        MoveAbsJ [[0,0,0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v50,z1,RobotiQ2F85Gripper \\WObj:=Frame2;
        
"""
        
        step = 1
        for movement in self.movement_sequence:
            if movement['type'] == 'move':
                # Obtener estado actualizado
                state = movement['state'].copy()
                state[movement['component']] = movement['to']  # Actualizar componente cambiado
                
                velocity = self._get_velocity_string(movement['velocity'])
                component = movement['component']
                
                main_proc += f"        ! Paso {step}: {component} de {movement['from']:.1f}° a {movement['to']:.1f}° (velocidad {movement['velocity']})\n"
                
                # MAPEO CORRECTO DE ARTICULACIONES ABB IRB140:
                # Eje 1: base (rotación horizontal)
                # Eje 2: hombro (brazo inferior)  
                # Eje 3: codo (codo)
                # Eje 4: muñeca (rotación antebrazo)
                # Eje 5: 0 (no usado directamente)
                # Eje 6: garra (apertura/cierre)
                
                eje1 = state['base']     # Base horizontal
                eje2 = state['hombro']   # Hombro arriba/abajo
                eje3 = state['codo']     # Codo arriba/abajo  
                eje4 = state['muneca']   # Rotación muñeca
                eje5 = 0.0               # No usado
                eje6 = self._convert_garra_to_eje6(state['garra'])  # Garra
                
                main_proc += f"        MoveAbsJ [[{eje1:.1f},{eje2:.1f},{eje3:.1f},{eje4:.1f},{eje5:.1f},{eje6:.1f}],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],{velocity},z1,RobotiQ2F85Gripper \\WObj:=Frame2;\n"
                
                step += 1
                
            elif movement['type'] == 'wait':
                main_proc += f"        ! Paso {step}: Esperar {movement['time']} segundos\n"
                main_proc += f"        WaitTime {movement['time']};\n"
                step += 1
            
            main_proc += "\n"
        
        main_proc += f"""        ! === PROGRAMA TERMINADO ===
        ! Total pasos: {step - 1}
        
    ENDPROC"""
        
        return main_proc
    
    def _get_velocity_string(self, velocity):
        """Convierte velocidad a string RAPID"""
        velocity_map = {
            1: "v50",   # Muy lenta
            2: "v100",  # Lenta  
            3: "v200",  # Media
            4: "v500",  # Rápida
        }
        return velocity_map.get(velocity, f"v{velocity * 50}")
    
    def _convert_garra_to_eje6(self, garra_value):
        """Convierte valor de garra a ángulo correcto del eje 6"""
        # Mapeo lógico:
        # garra = 90 → eje6 = 0 (abierta)
        # garra = 20 → eje6 = -70 (cerrada)
        
        if garra_value >= 90:
            return 0.0      # Garra abierta
        elif garra_value <= 20:
            return -70.0    # Garra cerrada
        else:
            # Interpolación lineal
            return -(90 - garra_value) * 70 / 70
    
    def get_movement_summary(self):
        """Resumen de movimientos"""
        if not self.movement_sequence:
            return "No hay movimientos"
        
        summary = f"SECUENCIA CORREGIDA - {len(self.movement_sequence)} movimientos:\n\n"
        
        for i, movement in enumerate(self.movement_sequence, 1):
            if movement['type'] == 'move':
                summary += f"{i}. {movement['component']}: {movement['from']:.1f}° → {movement['to']:.1f}° (v={movement['velocity']})\n"
            elif movement['type'] == 'wait':
                summary += f"{i}. Esperar: {movement['time']} segundos\n"
        
        return summary

def test_fixed_generator():
    """Prueba del generador corregido"""
    
    # Código simple para probar
    test_code = """Robot r1

# Movimiento simple para probar velocidades
r1.velocidad = 1
r1.base = 30
r1.espera = 2

r1.velocidad = 2  
r1.hombro = 45
r1.espera = 1

r1.velocidad = 3
r1.codo = 60
r1.espera = 1

r1.velocidad = 4
r1.base = 0
r1.hombro = 0
r1.codo = 0
"""
    
    print("=== GENERADOR CORREGIDO .MOD PARA ROBODK ===")
    
    generator = RoboDKFixedGenerator()
    success, message = generator.generate_mod_file(test_code, "demo_velocidades_fixed.mod")
    
    print("Resultado:", "✅" if success else "❌", message)
    
    if success:
        print("\n=== RESUMEN DE MOVIMIENTOS ===")
        print(generator.get_movement_summary())
        print("\n🎯 Archivo generado: demo_velocidades_fixed.mod")
        print("🤖 Importar en RoboDK con opción 2: 'Como programa (posiciones de articulación)'")

if __name__ == "__main__":
    test_fixed_generator()