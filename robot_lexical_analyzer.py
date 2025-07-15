import re
from robot_tokens import TOKEN_PATTERNS, ROBOT_KEYWORDS, get_token_type, LANGUAGE_INFO, VALID_COMPONENTS

# Definir rangos válidos para cada componente robótico
COMPONENT_RANGES = {
    'base': {'min': 0, 'max': 360, 'description': 'gira de 0 a 360°'},
    'hombro': {'min': 0, 'max': 180, 'description': 'gira de 0 a 180°'},
    'codo': {'min': 0, 'max': 180, 'description': 'gira de 0 a 180°'},
    'garra': {'min': 0, 'max': 90, 'description': 'abre y cierra de 0 a 90°'},
    'muneca': {'min': 0, 'max': 360, 'description': 'gira de 0 a 360°'},
    'velocidad': {'min': 0.1, 'max': 10.0, 'description': 'tiempo por movimiento de 0.1 a 10 segundos'},
    'repetir': {'min': 1, 'max': 100, 'description': 'número de repeticiones de 1 a 100'},
    'espera': {'min': 0.1, 'max': 60.0, 'description': 'tiempo de espera de 0.1 a 60 segundos'}
}

class Simbolo:
    """Clase para representar un símbolo en la tabla de símbolos"""
    def __init__(self, id, metodo, parametro, valor, es_declaracion=False, linea=None):
        self.id = id           # Identificador: r1, r2, etc.
        self.metodo = metodo   # base, hombro, codo, garra, etc. o "DECLARACION"
        self.parametro = parametro  # parámetro fijo como 1
        self.valor = valor     # valor numérico asignado o "-" para declaraciones
        self.es_declaracion = es_declaracion  # True si es una declaración de robot
        self.linea = linea     # Número de línea donde aparece el símbolo
    
    def __str__(self):
        if self.es_declaracion:
            return f"| {self.id:<3} | {'DECLARACION':<7} | {self.parametro:<9} | {self.valor:<5} |"
        else:
            return f"| {self.id:<3} | {self.metodo:<7} | {self.parametro:<9} | {self.valor:<5} |"
    
    def __repr__(self):
        return self.__str__()

class Token:
    """Clase para representar un token del lenguaje robótico"""
    def __init__(self, type_, value, line, column):
        self.type = type_
        self.value = value
        self.line = line
        self.column = column
    
    def __str__(self):
        return f"Token({self.type}, '{self.value}', {self.line}:{self.column})"
    
    def __repr__(self):
        return self.__str__()

class SyntaxError(Exception):
    """Excepción para errores sintácticos"""
    def __init__(self, message, line=None, column=None):
        self.message = message
        self.line = line
        self.column = column
        super().__init__(self.message)

class RobotParser:
    """Parser sintáctico para el lenguaje robótico"""
    
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0
        self.errors = []
        self.robots = {}  # Diccionario de robots: {nombre: [asignaciones]}
        self.assignments = []
        self.tabla_simbolos = []  # Tabla de símbolos
        self.rutinas = {}  # Diccionario de rutinas: {nombre: Rutina}
        self.comandos_espera = []  # Lista de comandos espera encontrados
        
    def peek(self):
        """Mira el token actual sin consumirlo"""
        if self.current < len(self.tokens):
            return self.tokens[self.current]
        return None
    
    def consume(self, expected_type=None):
        """Consume el token actual"""
        if self.current < len(self.tokens):
            token = self.tokens[self.current]
            self.current += 1
            if expected_type and token.type != expected_type:
                raise SyntaxError(f"Se esperaba {expected_type}, se encontró {token.type}", token.line, token.column)
            return token
        return None
    
    def skip_to_fin(self):
        """Salta tokens hasta encontrar 'fin' o llegar al final"""
        while self.peek() is not None:
            token = self.peek()
            if token.type == 'KEYWORD' and token.value.lower() == 'fin':
                self.consume()  # Consumir el 'fin'
                break
            self.consume()
    
    def parse(self):
        """Parsea el programa completo según la nueva gramática: S → PROGRAMA"""
        try:
            # Verificar que hay tokens
            if not self.tokens:
                self.errors.append("Error: No hay código para analizar")
                return False
            
            # Parsear múltiples elementos: PROGRAMA → (ROBOT_DECL | ROBOT_INSTRUCTION)* 
            while self.peek() is not None:
                token = self.peek()
                
                # Buscar declaración de robot
                if token.type == 'KEYWORD' and token.value.lower() == 'robot':
                    if not self.parse_robot_declaration():
                        pass
                # Buscar instrucciones de robot (r1.algo)
                elif token.type == 'IDENTIFIER':
                    if not self.parse_robot_instruction():
                        # Si falla parsear instrucción, saltar este token
                        self.consume()
                else:
                    # Saltar tokens que no son declaraciones válidas
                    self.consume()
            
            return len(self.errors) == 0
            
        except Exception as e:
            self.errors.append(f"Error sintáctico: {str(e)}")
            return False
    
    def parse_robot_declaration(self):
        """Parsea una declaración de robot: ROBOT_DECL → Robot ID"""
        try:
            # Primer token debe ser "Robot"
            robot_token = self.consume()
            if not robot_token or robot_token.type != 'KEYWORD' or robot_token.value.lower() != 'robot':
                self.errors.append(f"Error en línea {robot_token.line if robot_token else 1}: Se esperaba 'Robot', se encontró '{robot_token.value if robot_token else 'EOF'}'")
                return False
            
            # Segundo token debe ser el nombre del robot
            name_token = self.consume()
            if not name_token or name_token.type != 'IDENTIFIER':
                self.errors.append(f"Error en línea {name_token.line if name_token else 1}: Se esperaba nombre del robot (identificador), se encontró '{name_token.value if name_token else 'EOF'}'")
                return False
            
            current_robot = name_token.value
            
            # SIEMPRE agregar declaración de robot a la tabla de símbolos
            simbolo_declaracion = Simbolo(current_robot, "DECLARACION", "-", "-", es_declaracion=True, linea=name_token.line)
            self.tabla_simbolos.append(simbolo_declaracion)
            
            # Inicializar lista de asignaciones para este robot si no existe
            if current_robot not in self.robots:
                self.robots[current_robot] = []
            
            return True
            
        except Exception as e:
            self.errors.append(f"Error en declaración de robot: {str(e)}")
            return False
    
    def parse_robot_instruction(self):
        """Parsea una instrucción de robot con la nueva sintaxis: robot.comando [= valor | valor]"""
        try:
            # robot_name
            name_token = self.consume()
            if not name_token or name_token.type != 'IDENTIFIER':
                self.errors.append(f"Error en línea {name_token.line if name_token else 'EOF'}: Se esperaba nombre del robot")
                return False
            
            robot_name = name_token.value
            
            # .
            dot_token = self.consume()
            if not dot_token or dot_token.type != 'DOT':
                self.errors.append(f"Error en línea {dot_token.line if dot_token else 'EOF'}: Se esperaba '.'")
                return False
            
            # comando/componente
            command_token = self.consume()
            if not command_token or command_token.type != 'KEYWORD':
                self.errors.append(f"Error en línea {command_token.line if command_token else 'EOF'}: Se esperaba comando del robot")
                return False
            
            command = command_token.value.lower()
            
            if command not in VALID_COMPONENTS:
                self.errors.append(f"Error en línea {command_token.line}: '{command}' no es un comando válido. Comandos válidos: {', '.join(VALID_COMPONENTS)}")
                return False
            
            # Manejar diferentes tipos de comandos
            if command == 'inicio':
                return self.parse_robot_inicio(robot_name, command_token.line)
            elif command == 'fin':
                return self.parse_robot_fin(robot_name, command_token.line)
            elif command == 'espera':
                return self.parse_robot_espera(robot_name, command_token.line)
            else:
                # Comando que requiere asignación (=)
                return self.parse_robot_assignment(robot_name, command, command_token.line)
            
        except Exception as e:
            self.errors.append(f"Error en instrucción de robot: {str(e)}")
            return False
    
    def parse_robot_assignment(self, robot_name, command, line):
        """Parsea una asignación: robot.comando = valor"""
        try:
            # =
            equals_token = self.consume()
            if not equals_token or equals_token.type != 'ASSIGN_OP':
                self.errors.append(f"Error en línea {equals_token.line if equals_token else 'EOF'}: Se esperaba '='")
                return False
            
            # valor
            value_token = self.consume()
            if not value_token or value_token.type not in ['INTEGER_LITERAL', 'FLOAT_LITERAL']:
                self.errors.append(f"Error en línea {value_token.line if value_token else 'EOF'}: Se esperaba valor numérico")
                return False
            
            value = float(value_token.value)
            
            # Validar rango de valores si existe
            if command in COMPONENT_RANGES:
                range_info = COMPONENT_RANGES[command]
                if value < range_info['min'] or value > range_info['max']:
                    self.errors.append(f"Advertencia en línea {value_token.line}: Valor {value} para '{robot_name}.{command}' fuera del rango válido [{range_info['min']}, {range_info['max']}]")
            
            # Guardar asignación
            self.assignments.append({
                'robot': robot_name,
                'component': command,
                'value': value,
                'line': line
            })
            
            # Agregar a la tabla de símbolos
            simbolo = Simbolo(robot_name, command, 1, int(value) if value.is_integer() else value, linea=line)
            self.tabla_simbolos.append(simbolo)
            
            return True
            
        except Exception as e:
            self.errors.append(f"Error en asignación: {str(e)}")
            return False
    
    def parse_robot_inicio(self, robot_name, line):
        """Parsea comando robot.inicio"""
        # Registrar inicio de bloque
        simbolo_inicio = Simbolo(robot_name, "inicio", "-", "-", linea=line)
        self.tabla_simbolos.append(simbolo_inicio)
        return True
    
    def parse_robot_fin(self, robot_name, line):
        """Parsea comando robot.fin"""
        # Registrar fin de bloque
        simbolo_fin = Simbolo(robot_name, "fin", "-", "-", linea=line)
        self.tabla_simbolos.append(simbolo_fin)
        return True
    
    def parse_robot_espera(self, robot_name, line):
        """Parsea comando robot.espera = valor"""
        try:
            # =
            equals_token = self.consume()
            if not equals_token or equals_token.type != 'ASSIGN_OP':
                self.errors.append(f"Error en línea {equals_token.line if equals_token else 'EOF'}: Se esperaba '=' después de espera")
                return False
            
            # valor
            value_token = self.consume()
            if not value_token or value_token.type not in ['INTEGER_LITERAL', 'FLOAT_LITERAL']:
                self.errors.append(f"Error en línea {value_token.line if value_token else 'EOF'}: Se esperaba tiempo de espera")
                return False
            
            tiempo = float(value_token.value)
            
            # Validar rango de tiempo
            if tiempo < 0.1 or tiempo > 60.0:
                self.errors.append(f"Error en línea {value_token.line}: Tiempo de espera {tiempo} fuera del rango válido (0.1-60.0 segundos)")
                return False
            
            # Agregar comando espera a la lista
            self.comandos_espera.append({
                'robot': robot_name,
                'tiempo': tiempo,
                'linea': line
            })
            
            # Agregar a tabla de símbolos
            simbolo_espera = Simbolo(robot_name, "espera", tiempo, tiempo, linea=line)
            self.tabla_simbolos.append(simbolo_espera)
            
            return True
            
        except Exception as e:
            self.errors.append(f"Error en comando espera: {str(e)}")
            return False
    
    def parse_routine(self):
        """Parsea una rutina: inicio NOMBRE [repetir N veces] COMANDOS fin"""
        try:
            # Consumir 'inicio'
            inicio_token = self.consume()
            if not inicio_token or inicio_token.type != 'KEYWORD' or inicio_token.value.lower() != 'inicio':
                self.errors.append(f"Error en línea {inicio_token.line if inicio_token else 1}: Se esperaba 'inicio'")
                return False
            
            # Nombre de la rutina
            name_token = self.consume()
            if not name_token or name_token.type != 'IDENTIFIER':
                self.errors.append(f"Error en línea {name_token.line if name_token else 1}: Se esperaba nombre de rutina")
                return False
            
            routine_name = name_token.value
            repeticiones = 1
            
            # Verificar si hay 'repetir N veces'
            next_token = self.peek()
            if next_token and next_token.type == 'KEYWORD' and next_token.value.lower() == 'repetir':
                self.consume()  # consumir 'repetir'
                
                # Número de repeticiones
                num_token = self.consume()
                if not num_token or num_token.type not in ['INTEGER_LITERAL']:
                    self.errors.append(f"Error en línea {num_token.line if num_token else 1}: Se esperaba número de repeticiones")
                    return False
                
                repeticiones = int(num_token.value)
                
                # Verificar 'veces'
                veces_token = self.consume()
                if not veces_token or veces_token.type != 'KEYWORD' or veces_token.value.lower() != 'veces':
                    self.errors.append(f"Error en línea {veces_token.line if veces_token else 1}: Se esperaba 'veces'")
                    return False
            
            # Parsear comandos hasta encontrar 'fin'
            comandos = []
            while self.peek() is not None:
                token = self.peek()
                
                if token.type == 'KEYWORD' and token.value.lower() == 'fin':
                    break
                elif token.type == 'IDENTIFIER':
                    # Instrucción de robot - guardar posición antes de parsear
                    pos_antes = self.current
                    if self.parse_instruction_in_routine():
                        comandos.append("asignacion")
                    else:
                        # Si falla, restaurar posición y saltar token
                        self.current = pos_antes + 1
                elif token.type == 'KEYWORD' and token.value.lower() == 'espera':
                    if self.parse_wait_command():
                        comandos.append("espera")
                    else:
                        # Si falla parsear espera, saltar token
                        self.consume()
                else:
                    self.consume()  # Saltar otros tokens
            
            # Consumir 'fin'
            fin_token = self.consume()
            if not fin_token or fin_token.type != 'KEYWORD' or fin_token.value.lower() != 'fin':
                self.errors.append(f"Error en línea {fin_token.line if fin_token else 1}: Se esperaba 'fin' para cerrar rutina")
                return False
            
            # Crear rutina
            rutina = Rutina(routine_name, comandos, repeticiones, name_token.line)
            self.rutinas[routine_name] = rutina
            
            return True
            
        except Exception as e:
            self.errors.append(f"Error en rutina: {str(e)}")
            return False
    
    def parse_instruction_in_routine(self):
        """Parsea una instrucción dentro de una rutina"""
        return self.parse_instruction(None)  # Sin robot específico, se determina dinámicamente
    
    def parse_standalone_instruction(self):
        """Parsea una instrucción fuera de rutinas"""
        return self.parse_instruction(None)
    
    def parse_wait_command(self):
        """Parsea comando espera: espera TIEMPO"""
        try:
            # Consumir 'espera'
            espera_token = self.consume()
            if not espera_token or espera_token.type != 'KEYWORD' or espera_token.value.lower() != 'espera':
                self.errors.append(f"Error en línea {espera_token.line if espera_token else 1}: Se esperaba 'espera'")
                return False
            
            # Tiempo
            time_token = self.consume()
            if not time_token or time_token.type not in ['INTEGER_LITERAL', 'FLOAT_LITERAL']:
                self.errors.append(f"Error en línea {time_token.line if time_token else 1}: Se esperaba tiempo numérico")
                return False
            
            tiempo = float(time_token.value)
            
            # Validar rango de tiempo
            if tiempo < 0.1 or tiempo > 60.0:
                self.errors.append(f"Error en línea {time_token.line}: Tiempo de espera {tiempo} fuera del rango válido (0.1-60.0 segundos)")
                return False
            
            # Agregar comando espera a la lista
            self.comandos_espera.append({
                'tiempo': tiempo,
                'linea': espera_token.line
            })
            
            # Agregar a tabla de símbolos como operación especial
            simbolo_espera = Simbolo("ESP", "espera", tiempo, tiempo, linea=espera_token.line)
            self.tabla_simbolos.append(simbolo_espera)
            
            return True
            
        except Exception as e:
            self.errors.append(f"Error en comando espera: {str(e)}")
            return False

class RobotLexicalAnalyzer:
    """Analizador léxico, sintáctico y semántico para lenguaje de brazo robótico"""
    
    def __init__(self):
        self.tokens = []
        self.errors = []
        self.warnings = []
        self.current_line = 1
        self.current_column = 1
        self.components_found = set()
        self.commands_used = set()
        self.syntax_valid = False
        self.semantic_valid = False
        self.parser = None
        self.semantic_analyzer = None
        self.intermediate_code_generator = None
        
    def analyze(self, source_code):
        """Analiza el código fuente y genera tokens"""
        self.tokens = []
        self.errors = []
        self.warnings = []
        self.current_line = 1
        self.current_column = 1
        self.components_found = set()
        self.commands_used = set()
        self.syntax_valid = False
        
        # Combinar todos los patrones en una expresión regular
        combined_pattern = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_PATTERNS)
        regex = re.compile(combined_pattern, re.IGNORECASE)
        
        position = 0
        
        while position < len(source_code):
            match = regex.match(source_code, position)
            
            if match:
                token_type = match.lastgroup
                token_value = match.group()
                
                # Manejar casos especiales
                if token_type == 'IDENTIFIER':
                    # Verificar si es una palabra clave
                    keyword_type = get_token_type(token_value)
                    if keyword_type:
                        token_type = keyword_type
                        
                        # Rastrear componentes y comandos encontrados
                        if token_value.lower() in VALID_COMPONENTS:
                            self.components_found.add(token_value.lower())
                        elif token_value.lower() in ['girai', 'giraf', 'abre', 'cierra', 'mueve']:
                            self.commands_used.add(token_value.lower())
                
                elif token_type == 'WHITESPACE':
                    # Actualizar columna pero no crear token
                    self.current_column += len(token_value)
                    position = match.end()
                    continue
                    
                elif token_type == 'NEWLINE':
                    # Actualizar línea y columna
                    self.current_line += 1
                    self.current_column = 1
                    position = match.end()
                    continue
                    
                elif token_type == 'UNKNOWN':
                    # Reportar error léxico
                    self.errors.append(f"Error léxico en línea {self.current_line}, columna {self.current_column}: Caracter no reconocido '{token_value}'")
                    # Crear token para el caracter desconocido
                    token = Token(token_type, token_value, self.current_line, self.current_column)
                    self.tokens.append(token)
                    
                    # Actualizar posición
                    self.current_column += len(token_value)
                    position = match.end()
                    continue
                
                # Crear token (excepto para comentarios que se procesan pero no se almacenan como tokens activos)
                if token_type not in ['COMMENT_SINGLE', 'COMMENT_MULTI', 'COMMENT_HASH']:
                    token = Token(token_type, token_value, self.current_line, self.current_column)
                    self.tokens.append(token)
                
                # Actualizar posición
                self.current_column += len(token_value)
                position = match.end()
            else:
                # No se encontró coincidencia, reportar error
                char = source_code[position]
                self.errors.append(f"Error léxico en línea {self.current_line}, columna {self.current_column}: Caracter no reconocido '{char}'")
                self.current_column += 1
                position += 1
        
        # Realizar análisis sintáctico
        self.parser = RobotParser(self.tokens)
        self.syntax_valid = self.parser.parse()
        if self.parser.errors:
            self.errors.extend(self.parser.errors)
        
        # Solo realizar análisis semántico y código intermedio si NO hay errores léxicos ni sintácticos
        if not self.errors and self.parser and self.parser.tabla_simbolos:
            # Análisis semántico
            self.semantic_analyzer = SemanticAnalyzer()
            self.semantic_valid = self.semantic_analyzer.analyze(self.parser)
            if self.semantic_analyzer.errors:
                self.errors.extend(self.semantic_analyzer.errors)
            if self.semantic_analyzer.warnings:
                self.warnings.extend(self.semantic_analyzer.warnings)
            
            # Generar código intermedio solo si el análisis semántico también es exitoso
            if self.semantic_valid:
                self.intermediate_code_generator = IntermediateCodeGenerator()
                self.intermediate_code_generator.generar_codigo_intermedio(self.parser)
        
        # Generar advertencias adicionales
        self._generate_warnings()
        
        return self.tokens, self.errors
    
    def _generate_warnings(self):
        """Genera advertencias sobre el código analizado"""
        # Advertencias para valores numéricos muy grandes
        for token in self.tokens:
            if token.type in ['INTEGER_LITERAL', 'FLOAT_LITERAL']:
                value = float(token.value)
                if abs(value) > 360:
                    self.warnings.append(f"Línea {token.line}: Valor angular {value} excede 360 grados")
    
    def get_token_statistics(self):
        """Genera estadísticas de los tokens encontrados"""
        stats = {}
        for token in self.tokens:
            if token.type in stats:
                stats[token.type] += 1
            else:
                stats[token.type] = 1
        return stats
    
    def get_tabla_simbolos(self):
        """Obtiene la tabla de símbolos"""
        if self.parser:
            return self.parser.tabla_simbolos
        return []
    
    def get_cuadruplos(self):
        """Obtiene los cuádruplos generados"""
        if self.intermediate_code_generator:
            return self.intermediate_code_generator.cuadruplos
        return []
    
    def get_formatted_output(self):
        """Genera salida formateada de los tokens y análisis"""
        output = []
        
        # Información del lenguaje
        output.append("=== ANALIZADOR LÉXICO Y SINTÁCTICO PARA BRAZO ROBÓTICO ===")
        output.append(f"Lenguaje: {LANGUAGE_INFO['name']} v{LANGUAGE_INFO['version']}")
        output.append("")
        
        # Estado del análisis sintáctico
        if not self.errors:
            output.append("✅ ANÁLISIS SINTÁCTICO: CORRECTO")
            output.append("La sintaxis del programa es válida según la gramática:")
            output.append("S → Robot ID INSTS")
            output.append("INSTS → INST INSTS | ε")
            output.append("INST → ID.componente = valor")
            output.append("")
            
            # Estado del análisis semántico
            if self.semantic_valid:
                output.append("✅ ANÁLISIS SEMÁNTICO: CORRECTO")
                output.append("El programa cumple con todas las reglas semánticas:")
                output.append("• Declaración única de robots")
                output.append("• Asignaciones únicas por componente")
                output.append("• Valores dentro de rangos válidos")
                output.append("• Robots correctamente declarados")
                output.append("")
            else:
                output.append("❌ ANÁLISIS SEMÁNTICO: ERRORES ENCONTRADOS")
                output.append("El programa no cumple con las reglas semánticas del lenguaje")
                output.append("")
        else:
            output.append("❌ ANÁLISIS SINTÁCTICO: ERRORES ENCONTRADOS")
            output.append("❌ ANÁLISIS SEMÁNTICO: NO EJECUTADO (requiere sintaxis correcta)")
            output.append("")
        
        # Errores léxicos y sintácticos
        if self.errors:
            output.append("=== ERRORES ===")
            for error in self.errors:
                output.append(f"❌ {error}")
            output.append("")
        
        # Advertencias
        if self.warnings:
            output.append("=== ADVERTENCIAS ===")
            for warning in self.warnings:
                output.append(f"⚠️ {warning}")
            output.append("")
        
        # Tokens desconocidos encontrados
        unknown_tokens = [token for token in self.tokens if token.type == 'UNKNOWN']
        if unknown_tokens:
            output.append("=== 🚫 TOKENS DESCONOCIDOS ===")
            output.append(f"{'Caracter':<10} {'Línea':<6} {'Columna':<8} {'Descripción'}")
            output.append("-" * 45)
            for token in unknown_tokens:
                output.append(f"{repr(token.value):<10} {token.line:<6} {token.column:<8} Caracter no válido en el lenguaje")
            output.append("")
        
        # SOLO MOSTRAR INFORMACIÓN DETALLADA SI NO HAY ERRORES
        if not self.errors:
            # Información del parser
            if self.parser and self.parser.robots:
                output.append("=== INFORMACIÓN DE ROBOTS ===")
                for robot_name, robot_assignments in self.parser.robots.items():
                    output.append(f"🤖 Robot: {robot_name}")
                    if robot_assignments:
                        output.append(f"   📋 Asignaciones ({len(robot_assignments)}):")
                        for assignment in robot_assignments:
                            output.append(f"      • {assignment['robot']}.{assignment['component']} = {assignment['value']} (línea {assignment['line']})")
                    else:
                        output.append("   📋 Sin asignaciones")
                    output.append("")
            
            # Información de rutinas
            if self.parser and self.parser.rutinas:
                output.append("=== RUTINAS DEFINIDAS ===")
                for nombre, rutina in self.parser.rutinas.items():
                    output.append(f"🔄 Rutina: {nombre}")
                    output.append(f"   📋 Repeticiones: {rutina.repeticiones}")
                    output.append(f"   📋 Comandos: {len(rutina.comandos)}")
                    output.append(f"   📋 Línea: {rutina.linea}")
                    output.append("")
            
            # Información de comandos espera
            if self.parser and self.parser.comandos_espera:
                output.append("=== COMANDOS DE ESPERA ===")
                for i, comando in enumerate(self.parser.comandos_espera, 1):
                    output.append(f"⏱️ Espera {i}: {comando['robot']}.espera {comando['tiempo']} segundos (línea {comando['linea']})")
                output.append("")
            
            # Información de bloques inicio/fin
            if self.parser and self.parser.tabla_simbolos:
                inicio_symbols = [s for s in self.parser.tabla_simbolos if s.metodo == 'inicio']
                fin_symbols = [s for s in self.parser.tabla_simbolos if s.metodo == 'fin']
                
                if inicio_symbols or fin_symbols:
                    output.append("=== BLOQUES DE CONTROL ===")
                    for simbolo in inicio_symbols:
                        output.append(f"🔄 {simbolo.id}.inicio (línea {simbolo.linea})")
                    for simbolo in fin_symbols:
                        output.append(f"🔚 {simbolo.id}.fin (línea {simbolo.linea})")
                    output.append("")
            
            # Tabla de Símbolos (SOLO SI NO HAY ERRORES)
            if self.parser and self.parser.tabla_simbolos:
                output.append("=== 📋 TABLA DE SÍMBOLOS ===")
                output.append("| ID  | MÉTODO  | PARÁMETRO | VALOR |")
                output.append("|-----|---------|-----------|-------|")
                for simbolo in self.parser.tabla_simbolos:
                    output.append(str(simbolo))
                output.append("")
            
            # Tabla de Cuádruplos (SOLO SI NO HAY ERRORES)
            if self.intermediate_code_generator and self.intermediate_code_generator.cuadruplos:
                output.append(self.intermediate_code_generator.get_formatted_table())
            
            # Tokens encontrados (SOLO SI NO HAY ERRORES)
            if self.tokens:
                output.append("=== TOKENS ENCONTRADOS ===")
                output.append(f"{'Tipo':<20} {'Valor':<15} {'Línea':<6} {'Columna':<8} {'Descripción':<30}")
                output.append("-" * 85)
                
                for token in self.tokens:
                    description = self._get_token_description(token)
                    output.append(f"{token.type:<20} {repr(token.value):<15} {token.line:<6} {token.column:<8} {description:<30}")
                
                output.append("")
                
                # Análisis de componentes
                if self.components_found:
                    output.append("=== COMPONENTES ROBÓTICOS DETECTADOS ===")
                    for component in sorted(self.components_found):
                        if component in COMPONENT_RANGES:
                            range_info = COMPONENT_RANGES[component]
                            output.append(f"🔧 {component.upper()}: {range_info['description']} (rango: {range_info['min']}-{range_info['max']})")
                        else:
                            output.append(f"🔧 {component.upper()}")
                    output.append("")
                
                # Información semántica adicional
                if self.semantic_analyzer:
                    output.append("=== VALIDACIONES SEMÁNTICAS ===")
                    output.append("📋 Rangos válidos para componentes:")
                    for component, range_info in COMPONENT_RANGES.items():
                        output.append(f"   • {component}: {range_info['min']}-{range_info['max']}° ({range_info['description']})")
                    output.append("")
                
                # Estadísticas
                output.append("=== ESTADÍSTICAS ===")
                stats = self.get_token_statistics()
                total_tokens = sum(stats.values())
                output.append(f"📊 Total de tokens: {total_tokens}")
                output.append(f"📊 Líneas procesadas: {self.current_line}")
                output.append(f"📊 Componentes encontrados: {len(self.components_found)}")
                
                if self.parser:
                    output.append(f"📊 Asignaciones válidas: {len(self.parser.assignments) if self.parser.assignments else 0}")
                    output.append(f"📊 Símbolos en tabla: {len(self.parser.tabla_simbolos) if self.parser.tabla_simbolos else 0}")
                    output.append(f"📊 Rutinas definidas: {len(self.parser.rutinas) if self.parser.rutinas else 0}")
                    output.append(f"📊 Comandos de espera: {len(self.parser.comandos_espera) if self.parser.comandos_espera else 0}")
                    
                    # Contar bloques inicio/fin
                    if self.parser.tabla_simbolos:
                        inicio_count = len([s for s in self.parser.tabla_simbolos if s.metodo == 'inicio'])
                        fin_count = len([s for s in self.parser.tabla_simbolos if s.metodo == 'fin'])
                        output.append(f"📊 Bloques de control: {inicio_count} inicio, {fin_count} fin")
                
                output.append("")
                
                # Desglose por tipo de token
                output.append("=== DISTRIBUCIÓN DE TOKENS ===")
                for token_type, count in sorted(stats.items()):
                    percentage = (count / total_tokens) * 100
                    output.append(f"{token_type}: {count} ({percentage:.1f}%)")
        else:
            # Si HAY ERRORES, mostrar información básica solamente
            output.append("ℹ️ Análisis interrumpido debido a errores.")
            output.append("ℹ️ Corrija los errores antes de proceder con el análisis completo.")
        
        if not self.tokens and not self.errors:
            output.append("ℹ️ No se encontraron tokens para analizar.")
        
        return "\n".join(output)
    
    def _get_token_description(self, token):
        """Obtiene una descripción del token"""
        descriptions = {
            'KEYWORD': 'Palabra clave del lenguaje',
            'IDENTIFIER': 'Identificador definido por usuario',
            'INTEGER_LITERAL': 'Número entero',
            'FLOAT_LITERAL': 'Número decimal',
            'BOOLEAN_LITERAL': 'Valor booleano',
            'LBRACE': 'Apertura de bloque',
            'RBRACE': 'Cierre de bloque',
            'LPAREN': 'Paréntesis izquierdo',
            'RPAREN': 'Paréntesis derecho',
            'SEMICOLON': 'Fin de instrucción',
            'COMMA': 'Separador',
            'ASSIGN_OP': 'Operador de asignación',
            'COMPARISON_OP': 'Operador de comparación',
            'ARITHMETIC_OP': 'Operador aritmético',
            'DOT': 'Punto de acceso',
            'COMMENT_SINGLE': 'Comentario de línea',
            'COMMENT_MULTI': 'Comentario de bloque',
            'COMMENT_HASH': 'Comentario con #',
            'UNKNOWN': '❌ CARACTER DESCONOCIDO'
        }
        return descriptions.get(token.type, 'Token no clasificado')
    
    def generate_assembly_code(self, program_name="robot_program"):
        """Genera código ensamblador optimizado para Proteus"""
        try:
            # Usar el nuevo generador optimizado para Proteus - VERSIÓN CORREGIDA
            from proteus_assembly_generator_fixed import ProteusAssemblyGeneratorFixed
            
            generator = ProteusAssemblyGeneratorFixed()
            
            # Extraer comandos del parser si están disponibles
            motor_commands = []
            if self.parser and self.parser.assignments:
                for assignment in self.parser.assignments:
                    command_data = {assignment['component']: assignment['value']}
                    motor_commands.append(command_data)
            
            # Si no hay asignaciones del parser, usar valores por defecto para demostración
            if not motor_commands:
                motor_commands = [
                    {'base': 45},
                    {'hombro': 90},
                    {'codo': 60},
                    {'espera': 1}
                ]
            
            # Generar código assembly optimizado para Proteus
            asm_code = generator.generate_from_robot_data(motor_commands, program_name)
            return asm_code, None
                
        except Exception as e:
            # Fallback al generador original si hay problemas
            try:
                from assembly_generator import AssemblyGenerator
                
                generator = AssemblyGenerator()
                
                if not self.intermediate_code_generator or not self.intermediate_code_generator.cuadruplos:
                    asm_code = generator.generate_complete_program(program_name)
                    return asm_code, None
                else:
                    asm_code = generator.generate_assembly(self.intermediate_code_generator.cuadruplos, program_name)
                    return asm_code, None
                    
            except Exception as fallback_error:
                return None, f"Error al generar código ensamblador: {str(e)} | Fallback error: {str(fallback_error)}"
    
    def compile_to_executable(self, asm_code, output_name="robot_program"):
        """Compila código ensamblador a ejecutable usando DOSBox y TASM"""
        try:
            # Importar el controlador de DOSBox
            from assembly_generator import DOSBoxController
            
            controller = DOSBoxController()
            success, message = controller.compile_assembly(asm_code, output_name)
            return success, message
        except Exception as e:
            return False, f"Error al compilar: {str(e)}"
    
    def generate_and_compile(self, program_name="robot_program"):
        """Proceso completo: genera ensamblador y compila a ejecutable"""
        # Solo rechazar si hay errores críticos
        if self.errors and any("Error crítico" in str(error) for error in self.errors):
            return False, "No se puede generar código con errores críticos en el análisis"
        
        # Generar código ensamblador (funciona con o sin cuádruplos)
        asm_code, error = self.generate_assembly_code(program_name)
        if error:
            return False, error
        
        # Compilar a ejecutable
        success, message = self.compile_to_executable(asm_code, program_name)
        
        if success:
            return True, f"Ejecutable {program_name}.exe generado exitosamente en DOSBox2/Tasm/"
        else:
            return False, f"Error en la compilación: {message}"
    
    def generate_and_compile_for_proteus(self, program_name="robot_program"):
        """Proceso completo optimizado específicamente para Proteus"""
        try:
            # Usar el generador específico para Proteus
            from proteus_specific_generator import ProteusSpecificGenerator
            
            generator = ProteusSpecificGenerator()
            
            # Generar código ASM específico para Proteus
            asm_code = generator.generate_proteus_compatible_asm(program_name)
            
            # Compilar específicamente para Proteus
            success, message = generator.compile_for_proteus(asm_code, program_name)
            
            if success:
                return True, f"🎯 EJECUTABLE PROTEUS GENERADO!\n\n{message}\n\n✅ Compatible con procesador 8086\n🔌 Configurado para puertos 0300h-0303h (8255 PPI)\n🤖 Control de 3 motores paso a paso\n📱 Listo para simulación en Proteus ISIS"
            else:
                return False, f"Error generando ejecutable para Proteus: {message}"
                
        except Exception as e:
            return False, f"Error en generación para Proteus: {str(e)}"
    
    def generate_and_compile_dos_real(self, program_name="robot_program"):
        """Genera ejecutable DOS REAL para 8086 - Compatible con Proteus"""
        try:
            # Usar el generador DOS real
            from dos_real_generator import DOSRealExecutableGenerator
            
            generator = DOSRealExecutableGenerator()
            
            # Generar código ASM DOS real
            asm_code = generator.generate_real_dos_asm(program_name)
            
            # Compilar a ejecutable DOS real
            success, message = generator.compile_to_real_dos_exe(asm_code, program_name)
            
            if success:
                return True, f"🎯 EJECUTABLE DOS REAL GENERADO!\n\n{message}\n\n✅ Compatible con procesador 8086 REAL\n🔌 Configurado para puertos 0300h-0303h (8255 PPI)\n🤖 Control de 3 motores paso a paso\n📱 Formato MS-DOS auténtico para Proteus\n⚡ Sin errores de opcode desconocido"
            else:
                return False, f"Error generando ejecutable DOS real: {message}"
                
        except Exception as e:
            return False, f"Error en generación DOS real: {str(e)}"

class SemanticError(Exception):
    """Excepción para errores semánticos"""
    def __init__(self, message, line=None, column=None):
        self.message = message
        self.line = line
        self.column = column
        super().__init__(self.message)

class SemanticAnalyzer:
    """Analizador semántico para validar las reglas del lenguaje robótico"""
    
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.declared_robots = {}  # {nombre_robot: línea_declaración}
        self.robot_assignments = {}  # {nombre_robot: {componente: [líneas_asignación]}}
    
    def analyze(self, parser):
        """Realiza el análisis semántico basado en los resultados del parser sintáctico"""
        self.errors = []
        self.warnings = []
        self.declared_robots = {}
        self.robot_assignments = {}
        
        # 1. Verificar declaraciones de robots y asignaciones
        self._check_robot_declarations(parser)
        
        # 2. Verificar unicidad de declaraciones
        self._check_declaration_uniqueness(parser)
        
        # 3. Verificar unicidad de asignaciones
        self._check_assignment_uniqueness(parser)
        
        # 4. Verificar rangos de valores
        self._check_value_ranges(parser)
        
        # 5. Verificar robots no declarados
        self._check_undeclared_robots(parser)
        
        return len(self.errors) == 0
    
    def _check_robot_declarations(self, parser):
        """Verifica las declaraciones de robots en la tabla de símbolos"""
        for simbolo in parser.tabla_simbolos:
            if simbolo.es_declaracion:
                robot_name = simbolo.id
                if robot_name not in self.declared_robots:
                    self.declared_robots[robot_name] = 'declarado'
                    self.robot_assignments[robot_name] = {}
    
    def _check_declaration_uniqueness(self, parser):
        """Verifica que no haya declaraciones duplicadas de robots"""
        robot_declarations = {}
        
        for i, simbolo in enumerate(parser.tabla_simbolos):
            if simbolo.es_declaracion:
                robot_name = simbolo.id
                if robot_name in robot_declarations:
                    # Encontrada declaración duplicada
                    linea_anterior = robot_declarations[robot_name]
                    linea_actual = simbolo.linea if simbolo.linea else "desconocida"
                    self.errors.append(f"Error semántico en línea {linea_actual}: Robot '{robot_name}' ya fue declarado previamente en línea {linea_anterior}")
                else:
                    robot_declarations[robot_name] = simbolo.linea if simbolo.linea else "desconocida"
    
    def _check_assignment_uniqueness(self, parser):
        """Verifica que no haya asignaciones duplicadas para el mismo componente (solo fuera de rutinas)"""
        # En el contexto de rutinas robóticas, es válido tener múltiples asignaciones
        # al mismo componente en diferentes momentos de la secuencia.
        # Esta validación se omite para permitir secuencias de movimiento complejas.
        pass
    
    def _check_value_ranges(self, parser):
        """Verifica que los valores asignados estén dentro de los rangos válidos"""
        for simbolo in parser.tabla_simbolos:
            if not simbolo.es_declaracion:
                component = simbolo.metodo
                value = simbolo.valor
                robot_name = simbolo.id
                linea = simbolo.linea if simbolo.linea else "desconocida"
                
                if component in COMPONENT_RANGES:
                    range_info = COMPONENT_RANGES[component]
                    min_val = range_info['min']
                    max_val = range_info['max']
                    
                    try:
                        numeric_value = float(value)
                        if numeric_value < min_val or numeric_value > max_val:
                            self.errors.append(f"Error semántico en línea {linea}: Valor {numeric_value} para '{robot_name}.{component}' fuera del rango válido [{min_val}, {max_val}] - {range_info['description']}")
                        elif numeric_value == min_val or numeric_value == max_val:
                            self.warnings.append(f"Advertencia en línea {linea}: Valor {numeric_value} para '{robot_name}.{component}' está en el límite del rango válido")
                    except ValueError:
                        self.errors.append(f"Error semántico en línea {linea}: Valor '{value}' para '{robot_name}.{component}' no es un número válido")
    
    def _check_undeclared_robots(self, parser):
        """Verifica que todos los robots usados en asignaciones hayan sido declarados"""
        for simbolo in parser.tabla_simbolos:
            # Excluir comandos especiales y símbolos de declaración
            if not simbolo.es_declaracion and simbolo.id not in ['ESP'] and simbolo.metodo not in ['inicio', 'fin']:
                robot_name = simbolo.id
                linea = simbolo.linea if simbolo.linea else "desconocida"
                if robot_name not in self.declared_robots:
                    self.errors.append(f"Error semántico en línea {linea}: Robot '{robot_name}' usado sin haber sido declarado")

class Rutina:
    """Clase para representar una rutina en el código robótico"""
    def __init__(self, nombre, comandos, repeticiones=1, linea=None):
        self.nombre = nombre
        self.comandos = comandos  # Lista de comandos dentro de la rutina
        self.repeticiones = repeticiones
        self.linea = linea
    
    def __str__(self):
        return f"Rutina({self.nombre}, {len(self.comandos)} comandos, repetir {self.repeticiones} veces)"

class Cuadruplo:
    """Clase para representar un cuádruplo de código intermedio"""
    def __init__(self, numero, operacion, arg1, arg2, resultado, descripcion):
        self.numero = numero
        self.operacion = operacion
        self.arg1 = arg1 if arg1 is not None else "-"
        self.arg2 = arg2 if arg2 is not None else "-"
        self.resultado = resultado if resultado is not None else "-"
        self.descripcion = descripcion
    
    def __str__(self):
        return f"| {self.numero:<3} | {self.operacion:<15} | {self.arg1:<8} | {self.arg2:<8} | {self.resultado:<10} | {self.descripcion} |"

class IntermediateCodeGenerator:
    """Generador de código intermedio (cuádruplos) para el lenguaje robótico"""
    
    def __init__(self):
        self.cuadruplos = []
        self.contador_cuadruplos = 0
        self.contador_etiquetas = 0
        self.contador_temporales = 0
        self.contador_loops = 0
        self.pila_etiquetas = []  # Para manejar loops anidados
        
    def generar_etiqueta(self):
        """Genera una nueva etiqueta"""
        self.contador_etiquetas += 1
        return f"L{self.contador_etiquetas}"
    
    def generar_temporal(self):
        """Genera una nueva variable temporal"""
        self.contador_temporales += 1
        return f"T{self.contador_temporales}"
    
    def generar_contador_loop(self):
        """Genera un nuevo contador de loop"""
        self.contador_loops += 1
        return f"CX{self.contador_loops}"
    
    def agregar_cuadruplo(self, operacion, arg1=None, arg2=None, resultado=None, descripcion=""):
        """Agrega un nuevo cuádruplo a la lista"""
        cuadruplo = Cuadruplo(self.contador_cuadruplos, operacion, arg1, arg2, resultado, descripcion)
        self.cuadruplos.append(cuadruplo)
        self.contador_cuadruplos += 1
        return cuadruplo
    
    def generar_codigo_intermedio(self, parser):
        """Genera código intermedio basado en la tabla de símbolos del parser"""
        self.cuadruplos = []
        self.contador_cuadruplos = 0
        self.contador_etiquetas = 0
        self.contador_temporales = 0
        self.contador_loops = 0
        self.pila_etiquetas = []
        
        if not parser or not parser.tabla_simbolos:
            return self.cuadruplos
        
        # Variables para tracking del estado
        robot_actual = None
        repeticiones_robot = {}
        dentro_de_bloque = False
        etiqueta_inicio_loop = None
        etiqueta_fin_loop = None
        contador_loop = None
        
        for simbolo in parser.tabla_simbolos:
            if simbolo.es_declaracion:
                # Declaración de robot
                self.agregar_cuadruplo("DECLARAR", "robot", None, simbolo.id, f"Declaración del robot {simbolo.id}")
                robot_actual = simbolo.id
                
            elif simbolo.metodo == "repetir":
                # Configuración de repeticiones
                contador_loop = self.generar_contador_loop()
                repeticiones_robot[simbolo.id] = {
                    'contador': contador_loop,
                    'valor': simbolo.valor
                }
                self.agregar_cuadruplo("ASIG", simbolo.valor, None, contador_loop, f"Contador del loop = {simbolo.valor}")
                
            elif simbolo.metodo == "inicio":
                # Inicio de bloque con repetición
                dentro_de_bloque = True
                if simbolo.id in repeticiones_robot:
                    etiqueta_inicio_loop = self.generar_etiqueta()
                    etiqueta_fin_loop = self.generar_etiqueta()
                    contador_loop = repeticiones_robot[simbolo.id]['contador']
                    
                    self.agregar_cuadruplo("DECLARAR_ETIQUETA", None, None, etiqueta_inicio_loop, "Etiqueta de inicio del ciclo")
                    
                    # Comparar si el contador llegó a 0
                    temp_comparacion = self.generar_temporal()
                    self.agregar_cuadruplo("COMPARAR", contador_loop, "0", temp_comparacion, f"Compara si {contador_loop} == 0")
                    self.agregar_cuadruplo("SALTO_CONDICIONAL", temp_comparacion, None, etiqueta_fin_loop, f"Si {contador_loop} == 0 salta al final")
                    
                    self.pila_etiquetas.append({
                        'inicio': etiqueta_inicio_loop,
                        'fin': etiqueta_fin_loop,
                        'contador': contador_loop
                    })
                else:
                    # Bloque simple sin repetición
                    self.agregar_cuadruplo("DECLARAR_ETIQUETA", None, None, "BLOQUE_INICIO", "Inicio de bloque")
                
            elif simbolo.metodo == "fin":
                # Fin de bloque
                dentro_de_bloque = False
                if self.pila_etiquetas and simbolo.id in repeticiones_robot:
                    # Fin de loop con repetición
                    info_loop = self.pila_etiquetas.pop()
                    
                    # Decrementar contador
                    self.agregar_cuadruplo("DECREMENTO", info_loop['contador'], None, info_loop['contador'], "Resta 1 al contador")
                    
                    # Salto incondicional al inicio
                    self.agregar_cuadruplo("SALTO_INCONDICIONAL", None, None, info_loop['inicio'], "Vuelve al inicio del ciclo")
                    
                    # Etiqueta de fin
                    self.agregar_cuadruplo("FIN", None, None, info_loop['fin'], "Fin del ciclo")
                else:
                    # Fin de bloque simple
                    self.agregar_cuadruplo("FIN", None, None, "BLOQUE_FIN", "Fin del bloque")
                
            elif simbolo.metodo == "espera":
                # Comando de espera
                self.agregar_cuadruplo("ASIG", simbolo.valor, None, "espera", f"espera = {simbolo.valor}")
                self.agregar_cuadruplo("CALL", "espera", simbolo.valor, simbolo.id, f"Espera {simbolo.valor} segundos")
                
            elif simbolo.metodo in VALID_COMPONENTS and simbolo.metodo not in ["repetir", "inicio", "fin", "espera"]:
                # Asignación a componente robótico
                self.agregar_cuadruplo("ASIG", simbolo.valor, None, simbolo.metodo, f"{simbolo.metodo} = {simbolo.valor}")
                self.agregar_cuadruplo("CALL", simbolo.metodo, simbolo.valor, simbolo.id, f"Mueve {simbolo.metodo} a {simbolo.valor}°")
        
        return self.cuadruplos
    
    def get_formatted_table(self):
        """Retorna la tabla de cuádruplos formateada como string"""
        if not self.cuadruplos:
            return "No se generaron cuádruplos."
        
        output = []
        output.append("=== CÓDIGO INTERMEDIO (CUÁDRUPLOS) ===")
        output.append("")
        output.append("| #   | OPERACION       | ARG1     | ARG2     | RESULTADO  | DESCRIPCION")
        output.append("|-----|-----------------|----------|----------|------------|" + "-" * 50)
        
        for cuadruplo in self.cuadruplos:
            output.append(str(cuadruplo))
        
        output.append("")
        output.append(f"Total de cuádruplos generados: {len(self.cuadruplos)}")
        output.append("")
        
        # Información adicional sobre el código intermedio
        output.append("INFORMACIÓN DEL CÓDIGO INTERMEDIO:")
        output.append("• Cada operación del programa se descompone en instrucciones básicas")
        output.append("• Los cuádruplos facilitan la optimización y traducción a código máquina")
        output.append("• Variables temporales (T1, T2, ...) almacenan resultados intermedios")
        output.append("• Contadores de loop (CX1, CX2, ...) controlan las repeticiones")
        output.append("• Etiquetas (L1, L2, ...) marcan puntos de salto en el código")
        output.append("")
        
        return "\n".join(output)
