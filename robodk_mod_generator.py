#!/usr/bin/env python3
"""
Generador de archivos .mod para RoboDK
Convierte sintaxis robótica a formato RAPID compatible con RoboDK
"""

import os
from datetime import datetime
from robot_lexical_analyzer import RobotLexicalAnalyzer

class RoboDKModGenerator:
    """Generador de archivos .mod para RoboDK desde sintaxis robótica"""
    
    def __init__(self):
        self.analyzer = RobotLexicalAnalyzer()
        self.robot_name = "r1"
        self.motor_values = {
            'base': 0.0,
            'hombro': 0.0,
            'codo': 0.0,
            'muneca': 0.0,
            'garra': 0.0,
            'velocidad': 'v500'
        }
        self.procedures = []
        self.main_calls = []
        
    def analyze_robot_code(self, code):
        """Analiza el código robótico y extrae valores"""
        tokens, errors = self.analyzer.analyze(code)
        
        if errors:
            print(f"⚠️ Advertencias encontradas: {len(errors)}")
            for error in errors[:3]:  # Mostrar solo primeros 3
                print(f"  - {error}")
        
        # Extraer nombre del robot
        for i, token in enumerate(tokens):
            if hasattr(token, 'type') and hasattr(token, 'value'):
                if token.type == 'KEYWORD' and token.value.lower() == 'robot':
                    if i + 1 < len(tokens):
                        next_token = tokens[i + 1]
                        if hasattr(next_token, 'value'):
                            self.robot_name = next_token.value
                            break
        
        # Extraer valores de componentes
        i = 0
        while i < len(tokens) - 2:
            token = tokens[i]
            if hasattr(token, 'type') and hasattr(token, 'value'):
                # Buscar patrón: identificador.componente = valor
                if (token.type == 'IDENTIFIER' and 
                    i + 1 < len(tokens) and hasattr(tokens[i + 1], 'type') and
                    tokens[i + 1].type == 'DOT' and
                    i + 2 < len(tokens) and hasattr(tokens[i + 2], 'value')):
                    
                    component = tokens[i + 2].value.lower()
                    
                    # Buscar el valor después del '='
                    j = i + 3
                    while j < len(tokens) and hasattr(tokens[j], 'type'):
                        if tokens[j].type in ['ASSIGN', 'ASSIGN_OP']:
                            if j + 1 < len(tokens) and hasattr(tokens[j + 1], 'value'):
                                value = tokens[j + 1].value
                                if component in self.motor_values:
                                    if component == 'velocidad':
                                        # Mapear velocidad
                                        if str(value).lower() in ['rapida', 'rapid', 'fast']:
                                            self.motor_values[component] = 'v500'
                                        elif str(value).lower() in ['lenta', 'slow']:
                                            self.motor_values[component] = 'v50'
                                        else:
                                            self.motor_values[component] = f'v{value}'
                                    else:
                                        self.motor_values[component] = float(value)
                                break
                        j += 1
            i += 1
        
        return tokens, errors
    
    def generate_mod_file(self, code, output_filename="robot_program.mod"):
        """Genera archivo .mod completo para RoboDK"""
        
        # Analizar código
        tokens, errors = self.analyze_robot_code(code)
        
        # Generar timestamp
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        # Crear contenido del archivo .mod
        mod_content = f"""%%%
  VERSION:1
  LANGUAGE:ENGLISH
%%%
MODULE MOD_{self.robot_name.upper()}Program

    ! -------------------------------
    ! Programa generado automáticamente desde sintaxis robótica
    ! Robot: {self.robot_name}
    ! Fecha: {timestamp}
    ! -------------------------------

    ! Tool variables: 
    PERS tooldata RobotiQ2F85Gripper(FullyClosed) := [TRUE,[[0.000,0.000,130.000],[1.00000000,0.00000000,0.00000000,0.00000000]],[1,[0,0,20],[1,0,0,0],0,0,0.005]];

    ! Reference variables:
    PERS wobjdata Frame2 := [FALSE, TRUE, "", [[0,0,0],[1,0,0,0]],[[-140.437,-738.971,5.234],[1.00000000,0.00000000,0.00000000,0.00000000]]];

"""
        
        # Generar procedimientos basados en los valores extraídos
        self._generate_procedures(mod_content)
        
        # Agregar procedimientos generados
        for proc in self.procedures:
            mod_content += proc + "\n"
        
        # Generar procedimiento Main
        mod_content += self._generate_main_procedure()
        
        # Cerrar módulo
        mod_content += "\nENDMODULE\n"
        
        # Guardar archivo
        output_path = os.path.join(os.getcwd(), output_filename)
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(mod_content)
            
            return True, f"✅ Archivo .mod generado exitosamente:\n📁 {output_path}\n🤖 Robot: {self.robot_name}\n📊 Valores extraídos: {self.motor_values}"
            
        except Exception as e:
            return False, f"❌ Error al generar archivo .mod: {str(e)}"
    
    def _generate_procedures(self, mod_content):
        """Genera procedimientos específicos basados en valores del código"""
        
        # Procedimiento para BASE
        if self.motor_values['base'] != 0.0:
            base_angle = self.motor_values['base']
            velocity = self.motor_values['velocidad']
            
            proc_base = f"""    PROC base()
        ConfJ \\On;
        ConfL \\Off;
        MoveAbsJ [[0.000000,0.000000,0.000000,0.000000,0.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],{velocity},z1,RobotiQ2F85Gripper(FullyClosed) \\WObj:=Frame2;
        MoveAbsJ [[{base_angle:.6f},0.000000,0.000000,0.000000,0.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],{velocity},z1,RobotiQ2F85Gripper(FullyClosed) \\WObj:=Frame2;
        MoveAbsJ [[{-base_angle:.6f},0.000000,0.000000,0.000000,0.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],{velocity},z1,RobotiQ2F85Gripper(FullyClosed) \\WObj:=Frame2;
        MoveAbsJ [[0.000000,0.000000,0.000000,0.000000,0.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],{velocity},z1,RobotiQ2F85Gripper(FullyClosed) \\WObj:=Frame2;
    ENDPROC"""
            
            self.procedures.append(proc_base)
            self.main_calls.append("base;")
        
        # Procedimiento para HOMBRO (brazo)
        if self.motor_values['hombro'] != 0.0:
            hombro_angle = self.motor_values['hombro']
            velocity = self.motor_values['velocidad']
            
            proc_hombro = f"""    PROC hombro()
        ConfJ \\On;
        ConfL \\Off;
        MoveAbsJ [[0.000000,0.000000,0.000000,0.000000,0.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],{velocity},z1,RobotiQ2F85Gripper(FullyClosed) \\WObj:=Frame2;
        MoveAbsJ [[0.000000,{hombro_angle:.6f},0.000000,0.000000,0.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],{velocity},z1,RobotiQ2F85Gripper(FullyClosed) \\WObj:=Frame2;
        MoveAbsJ [[0.000000,{-hombro_angle:.6f},0.000000,0.000000,0.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],{velocity},z1,RobotiQ2F85Gripper(FullyClosed) \\WObj:=Frame2;
        MoveAbsJ [[0.000000,0.000000,0.000000,0.000000,0.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],{velocity},z1,RobotiQ2F85Gripper(FullyClosed) \\WObj:=Frame2;
    ENDPROC"""
            
            self.procedures.append(proc_hombro)
            self.main_calls.append("hombro;")
        
        # Procedimiento para CODO
        if self.motor_values['codo'] != 0.0:
            codo_angle = self.motor_values['codo']
            velocity = self.motor_values['velocidad']
            
            proc_codo = f"""    PROC codo()
        ConfJ \\On;
        ConfL \\Off;
        MoveAbsJ [[0.000000,0.000000,0.000000,0.000000,0.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],{velocity},z1,RobotiQ2F85Gripper(FullyClosed) \\WObj:=Frame2;
        MoveAbsJ [[0.000000,0.000000,{codo_angle:.6f},0.000000,0.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],{velocity},z1,RobotiQ2F85Gripper(FullyClosed) \\WObj:=Frame2;
        MoveAbsJ [[0.000000,0.000000,{-codo_angle:.6f},0.000000,0.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],{velocity},z1,RobotiQ2F85Gripper(FullyClosed) \\WObj:=Frame2;
        MoveAbsJ [[0.000000,0.000000,0.000000,0.000000,0.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],{velocity},z1,RobotiQ2F85Gripper(FullyClosed) \\WObj:=Frame2;
    ENDPROC"""
            
            self.procedures.append(proc_codo)
            self.main_calls.append("codo;")
        
        # Procedimiento para MUÑECA
        if self.motor_values['muneca'] != 0.0:
            muneca_angle = self.motor_values['muneca']
            velocity = self.motor_values['velocidad']
            
            proc_muneca = f"""    PROC muneca()
        ConfJ \\On;
        ConfL \\Off;
        MoveAbsJ [[0.000000,0.000000,0.000000,0.000000,0.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],{velocity},z1,RobotiQ2F85Gripper(FullyClosed) \\WObj:=Frame2;
        MoveAbsJ [[0.000000,0.000000,0.000000,{muneca_angle:.6f},0.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],{velocity},z1,RobotiQ2F85Gripper(FullyClosed) \\WObj:=Frame2;
        MoveAbsJ [[0.000000,0.000000,0.000000,{-muneca_angle:.6f},0.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],{velocity},z1,RobotiQ2F85Gripper(FullyClosed) \\WObj:=Frame2;
        MoveAbsJ [[0.000000,0.000000,0.000000,0.000000,0.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],{velocity},z1,RobotiQ2F85Gripper(FullyClosed) \\WObj:=Frame2;
    ENDPROC"""
            
            self.procedures.append(proc_muneca)
            self.main_calls.append("muneca;")
        
        # Procedimiento para GARRA
        if self.motor_values['garra'] != 0.0:
            garra_angle = self.motor_values['garra']
            velocity = self.motor_values['velocidad']
            
            proc_garra = f"""    PROC garra()
        ConfJ \\On;
        ConfL \\Off;
        MoveAbsJ [[0.000000,0.000000,0.000000,0.000000,0.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],{velocity},z1,RobotiQ2F85Gripper(FullyClosed) \\WObj:=Frame2;
        MoveAbsJ [[0.000000,0.000000,0.000000,0.000000,{garra_angle:.6f},-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],{velocity},z1,RobotiQ2F85Gripper(FullyClosed) \\WObj:=Frame2;
        MoveAbsJ [[0.000000,0.000000,0.000000,0.000000,{-garra_angle:.6f},-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],{velocity},z1,RobotiQ2F85Gripper(FullyClosed) \\WObj:=Frame2;
        MoveAbsJ [[0.000000,0.000000,0.000000,0.000000,0.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],{velocity},z1,RobotiQ2F85Gripper(FullyClosed) \\WObj:=Frame2;
    ENDPROC"""
            
            self.procedures.append(proc_garra)
            self.main_calls.append("garra;")
    
    def _generate_main_procedure(self):
        """Genera el procedimiento Main que llama a todos los procedimientos"""
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        main_proc = f"""    PROC Main()
        ConfJ \\On;
        ConfL \\Off;
        ! Program generated from Robot syntax on {timestamp}
        ! Robot: {self.robot_name}
        ! Extracted values: base={self.motor_values['base']}°, hombro={self.motor_values['hombro']}°, codo={self.motor_values['codo']}°, muneca={self.motor_values['muneca']}°, garra={self.motor_values['garra']}°
        
"""
        
        # Agregar llamadas a procedimientos
        for call in self.main_calls:
            main_proc += f"        {call}\n"
        
        main_proc += "    ENDPROC"
        
        return main_proc

def test_mod_generator():
    """Función de prueba para el generador .mod"""
    
    # Código de prueba
    test_code = """Robot brazo_industrial
brazo_industrial.base = 90
brazo_industrial.hombro = 45
brazo_industrial.codo = 60
brazo_industrial.muneca = 30
brazo_industrial.garra = 15
brazo_industrial.velocidad = rapida
"""
    
    generator = RoboDKModGenerator()
    success, message = generator.generate_mod_file(test_code, "test_robot.mod")
    
    print("=== GENERADOR DE ARCHIVOS .MOD PARA ROBODK ===")
    print(f"Resultado: {message}")
    
    if success:
        print("\n=== ARCHIVO .MOD GENERADO ===")
        try:
            with open("test_robot.mod", 'r', encoding='utf-8') as f:
                content = f.read()
                print(content[:1000] + "..." if len(content) > 1000 else content)
        except:
            print("No se pudo leer el archivo generado")

if __name__ == "__main__":
    test_mod_generator()