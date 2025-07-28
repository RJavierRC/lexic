#!/usr/bin/env python3
"""
Generador seguro de archivos .mod para RoboDK
Usa límites seguros del robot ABB IRB140 y formato que funciona
"""

import os
import re
from datetime import datetime
from robot_lexical_analyzer import RobotLexicalAnalyzer

class RoboDKSafeGenerator:
    """Generador seguro que respeta límites del ABB IRB140"""
    
    def __init__(self):
        self.analyzer = RobotLexicalAnalyzer()
        self.robot_name = "r1"
        
        # Límites seguros para ABB IRB140-6/0.8 (en grados)
        self.safe_limits = {
            'base': {'min': -180, 'max': 180, 'safe_min': -170, 'safe_max': 170},      # J1
            'hombro': {'min': -90, 'max': 110, 'safe_min': -80, 'safe_max': 100},     # J2
            'codo': {'min': -230, 'max': 50, 'safe_min': -200, 'safe_max': 45},       # J3
            'muneca': {'min': -200, 'max': 200, 'safe_min': -180, 'safe_max': 180},   # J4
            'garra': {'min': -120, 'max': 120, 'safe_min': -100, 'safe_max': 100}     # J5
        }
        
        self.current_state = {
            'base': 0.0,
            'hombro': 0.0,
            'codo': 0.0,
            'muneca': 0.0,
            'garra': 0.0,
            'velocidad': 1
        }
        self.movement_sequence = []
        
    def limit_angle(self, component, angle):
        """Limita el ángulo a valores seguros para el robot"""
        if component not in self.safe_limits:
            return angle
            
        limits = self.safe_limits[component]
        safe_angle = max(limits['safe_min'], min(limits['safe_max'], angle))
        
        if safe_angle != angle:
            print(f"⚠️ Ángulo {component}={angle}° limitado a {safe_angle}° por seguridad")
            
        return safe_angle
    
    def analyze_robot_code(self, code):
        """Analiza el código y extrae la secuencia de movimientos seguros"""
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
        self._process_safe_instructions(clean_code)
        
        return tokens, errors
    
    def _process_safe_instructions(self, code):
        """Procesa las instrucciones aplicando límites seguros"""
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
                        # Aplicar límites seguros
                        raw_value = float(value)
                        safe_value = self.limit_angle(component, raw_value)
                        
                        # Actualizar estado y agregar movimiento
                        old_value = self.current_state[component]
                        self.current_state[component] = safe_value
                        
                        # Agregar movimiento
                        self.movement_sequence.append({
                            'type': 'move',
                            'component': component,
                            'from': old_value,
                            'to': safe_value,
                            'original': raw_value,
                            'velocity': self.current_state['velocidad'],
                            'state': self.current_state.copy()
                        })
    
    def generate_mod_file(self, code, output_filename="robot_safe.mod"):
        """Genera archivo .mod seguro para RoboDK"""
        
        # Analizar código
        tokens, errors = self.analyze_robot_code(code)
        
        # Generar timestamp
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        # Crear contenido del archivo .mod usando el formato que funciona
        mod_content = f"""%%%
  VERSION:1
  LANGUAGE:ENGLISH
%%%
MODULE MOD_{self.robot_name.upper()}Program
    ! -------------------------------
    ! Programa generado automáticamente desde sintaxis robótica
    ! Robot: {self.robot_name}
    ! Fecha: {timestamp}
    ! Movimientos seguros: {len(self.movement_sequence)} pasos
    ! Límites aplicados para ABB IRB140-6/0.8
    ! -------------------------------
    
    ! Tool variables: 
    PERS tooldata RobotiQ2F85Gripper(FullyClosed) := [TRUE,[[45,0,0,0,0,0]],[1,[0,0,20],[1,0,0,0],0,0,0.005]];
    
    ! Reference variables:
    PERS wobjdata Frame2 := [FALSE, TRUE, "", [[45,0,0,0,0,0]],[[45,0,0,0,0,0]]];
    
    PROC Main()
        ConfJ \\On;
        ConfL \\Off;
        ! Program generated from Robot syntax on {timestamp}
        ! Robot: {self.robot_name} - Secuencia segura de {len(self.movement_sequence)} movimientos
        
        ! === POSICIÓN INICIAL SEGURA ===
        MoveAbsJ [[0,0,0,0,0,0]],v50,z1,RobotiQ2F85Gripper(FullyClosed) \\WObj:=Frame2;
        
        ! === INICIO DE SECUENCIA DE MOVIMIENTOS SEGUROS ===
        
"""
        
        # Generar movimientos secuenciales seguros
        step = 1
        for movement in self.movement_sequence:
            if movement['type'] == 'move':
                # Generar movimiento MoveAbsJ seguro
                state = movement['state']
                velocity = self._get_safe_velocity_string(movement['velocity'])
                component = movement['component']
                
                # Comentario descriptivo
                if movement['original'] != movement['to']:
                    mod_content += f"        ! Paso {step}: Mover {component} de {movement['from']:.1f}° a {movement['to']:.1f}° (limitado desde {movement['original']:.1f}°)\n"
                else:
                    mod_content += f"        ! Paso {step}: Mover {component} de {movement['from']:.1f}° a {movement['to']:.1f}°\n"
                
                # Generar MoveAbsJ con estado seguro
                mod_content += f"        MoveAbsJ [[{state['base']:.1f},{state['hombro']:.1f},{state['codo']:.1f},{state['muneca']:.1f},{state['garra']:.1f},0]],{velocity},z1,RobotiQ2F85Gripper(FullyClosed) \\WObj:=Frame2;\n"
                
                step += 1
                
            elif movement['type'] == 'wait':
                # Generar espera
                mod_content += f"        ! Paso {step}: Esperar {movement['time']} segundos\n"
                mod_content += f"        WaitTime {movement['time']};\n"
                step += 1
            
            mod_content += "\n"
        
        # Regresar a posición inicial segura
        mod_content += f"""        ! === REGRESAR A POSICIÓN INICIAL SEGURA ===
        MoveAbsJ [[0,0,0,0,0,0]],v50,z1,RobotiQ2F85Gripper(FullyClosed) \\WObj:=Frame2;
        
        ! === FIN DE SECUENCIA SEGURA ===
        ! Total de pasos ejecutados: {step - 1}
        
    ENDPROC
ENDMODULE
"""
        
        # Guardar archivo
        output_path = os.path.join(os.getcwd(), output_filename)
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(mod_content)
            
            return True, f"✅ Archivo .mod SEGURO generado exitosamente:\n📁 {output_path}\n🤖 Robot: {self.robot_name}\n📊 Movimientos seguros: {len(self.movement_sequence)} pasos\n⚠️ Límites ABB IRB140 aplicados\n🎯 Listo para RoboDK sin errores de límites"
            
        except Exception as e:
            return False, f"❌ Error al generar archivo .mod seguro: {str(e)}"
    
    def _get_safe_velocity_string(self, velocity):
        """Convierte velocidad a string RAPID seguro"""
        velocity_map = {
            1: "v50",   # Muy lenta - segura
            2: "v100",  # Lenta - segura
            3: "v200",  # Media - segura
            4: "v500",  # Rápida - limitada para seguridad
            5: "v500"   # Muy rápida - limitada
        }
        return velocity_map.get(velocity, "v50")  # Por defecto, velocidad segura
    
    def get_safety_report(self):
        """Obtiene reporte de limitaciones aplicadas"""
        if not self.movement_sequence:
            return "No hay movimientos procesados"
        
        report = f"REPORTE DE SEGURIDAD - ABB IRB140-6/0.8\n{'='*50}\n\n"
        report += f"Movimientos analizados: {len(self.movement_sequence)}\n"
        
        limited_moves = 0
        for movement in self.movement_sequence:
            if movement['type'] == 'move' and movement['original'] != movement['to']:
                limited_moves += 1
        
        report += f"Movimientos limitados por seguridad: {limited_moves}\n\n"
        
        if limited_moves > 0:
            report += "LÍMITES APLICADOS:\n"
            for movement in self.movement_sequence:
                if movement['type'] == 'move' and movement['original'] != movement['to']:
                    component = movement['component']
                    original = movement['original']
                    limited = movement['to']
                    limits = self.safe_limits[component]
                    report += f"• {component}: {original}° → {limited}° (límite: {limits['safe_min']}° a {limits['safe_max']}°)\n"
        else:
            report += "✅ Todos los movimientos están dentro de límites seguros\n"
        
        report += f"\nLÍMITES SEGUROS CONFIGURADOS:\n"
        for component, limits in self.safe_limits.items():
            report += f"• {component}: {limits['safe_min']}° a {limits['safe_max']}°\n"
        
        return report

def test_safe_generator():
    """Función de prueba para el generador seguro"""
    
    # Código de prueba con valores potencialmente problemáticos
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
    
    generator = RoboDKSafeGenerator()
    success, message = generator.generate_mod_file(test_code, "safe_pick_place.mod")
    
    print("=== GENERADOR SEGURO .MOD PARA ROBODK ===")
    print(f"Resultado: {message}")
    
    print("\n=== REPORTE DE SEGURIDAD ===")
    print(generator.get_safety_report())
    
    if success:
        print("\n=== ARCHIVO .MOD SEGURO GENERADO (PRIMERAS LÍNEAS) ===")
        try:
            with open("safe_pick_place.mod", 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.split('\n')
                for i, line in enumerate(lines[:40]):  # Mostrar primeras 40 líneas
                    print(f"{i+1:2d}: {line}")
                if len(lines) > 40:
                    print(f"... y {len(lines) - 40} líneas más")
        except:
            print("No se pudo leer el archivo generado")

if __name__ == "__main__":
    test_safe_generator()