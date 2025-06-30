import re
from robot_tokens import TOKEN_PATTERNS, ROBOT_KEYWORDS, get_token_type, LANGUAGE_INFO, VALID_COMPONENTS

# Definir rangos válidos para cada componente robótico
COMPONENT_RANGES = {
    'base': {'min': 0, 'max': 360, 'description': 'gira de 0 a 360°'},
    'hombro': {'min': 0, 'max': 180, 'description': 'gira de 0 a 180°'},
    'codo': {'min': 0, 'max': 180, 'description': 'gira de 0 a 180°'},
    'garra': {'min': 0, 'max': 90, 'description': 'abre y cierra de 0 a 90°'},
    'muneca': {'min': 0, 'max': 360, 'description': 'gira de 0 a 360°'}
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
    
    def parse(self):
        """Parsea el programa completo según la gramática: S → PROGRAMA"""
        try:
            # Verificar que hay tokens
            if not self.tokens:
                self.errors.append("Error: No hay código para analizar")
                return False
            
            # Parsear múltiples robots: PROGRAMA → ROBOT_DECL PROGRAMA | ε
            while self.peek() is not None:
                token = self.peek()
                
                # Buscar declaración de robot
                if token.type == 'KEYWORD' and token.value.lower() == 'robot':
                    if not self.parse_robot_declaration():
                        # Continuar aunque haya error en una declaración específica
                        pass
                else:
                    # Saltar tokens que no son declaraciones de robot ni instrucciones válidas
                    self.consume()
            
            return len(self.errors) == 0
            
        except Exception as e:
            self.errors.append(f"Error sintáctico: {str(e)}")
            return False
    
    def parse_robot_declaration(self):
        """Parsea una declaración de robot: ROBOT_DECL → Robot ID INSTS"""
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
            
            # Parsear instrucciones para este robot: INSTS → INST INSTS | ε
            while self.peek() is not None:
                next_token = self.peek()
                
                # Si encontramos otra declaración "Robot", terminar este robot
                if next_token.type == 'KEYWORD' and next_token.value.lower() == 'robot':
                    break
                
                # Si es una instrucción para algún robot, procesarla
                if next_token.type == 'IDENTIFIER':
                    # Verificar si el identificador es el nombre del robot actual
                    if next_token.value == current_robot:
                        # Es una instrucción para este robot
                        if not self.parse_instruction(current_robot):
                            # Continuar aunque haya error en la instrucción
                            pass
                    else:
                        # Es otro identificador, podría ser nombre de otro robot sin declarar
                        # Salir del bucle para que el parser principal lo maneje
                        break
                else:
                    # Otros tokens (comentarios, espacios, etc.) - saltarlos
                    self.consume()
            
            return True
            
        except Exception as e:
            self.errors.append(f"Error en declaración de robot: {str(e)}")
            return False
    
    def parse_instruction(self, expected_robot):
        """Parsea una instrucción: INST → robot_name.componente = valor"""
        try:
            # robot_name
            name_token = self.consume()
            if not name_token or name_token.type != 'IDENTIFIER':
                self.errors.append(f"Error en línea {name_token.line if name_token else 'EOF'}: Se esperaba nombre del robot")
                return False
            
            if name_token.value != expected_robot:
                self.errors.append(f"Error en línea {name_token.line}: Se esperaba '{expected_robot}', se encontró '{name_token.value}'")
                return False
            
            # .
            dot_token = self.consume()
            if not dot_token or dot_token.type != 'DOT':
                self.errors.append(f"Error en línea {dot_token.line if dot_token else 'EOF'}: Se esperaba '.'")
                return False
            
            # componente
            component_token = self.consume()
            if not component_token or component_token.type != 'KEYWORD':
                self.errors.append(f"Error en línea {component_token.line if component_token else 'EOF'}: Se esperaba componente del brazo")
                return False
            
            if component_token.value not in VALID_COMPONENTS:
                self.errors.append(f"Error en línea {component_token.line}: '{component_token.value}' no es un componente válido. Componentes válidos: {', '.join(VALID_COMPONENTS)}")
                return False
            
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
            
            # Validar rango de valores
            value = float(value_token.value)
            if value < 0 or value > 360:
                self.errors.append(f"Advertencia en línea {value_token.line}: Valor {value} fuera del rango típico (0-360 grados)")
            
            # Guardar asignación
            self.assignments.append({
                'robot': name_token.value,
                'component': component_token.value,
                'value': value,
                'line': name_token.line
            })
            
            # Agregar a la tabla de símbolos
            simbolo = Simbolo(name_token.value, component_token.value, 1, int(value), linea=name_token.line)
            self.tabla_simbolos.append(simbolo)
            
            return True
            
        except Exception as e:
            self.errors.append(f"Error en instrucción: {str(e)}")
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
        
        # Realizar análisis semántico SIEMPRE que tengamos tabla de símbolos
        if self.parser and self.parser.tabla_simbolos:
            self.semantic_analyzer = SemanticAnalyzer()
            self.semantic_valid = self.semantic_analyzer.analyze(self.parser)
            if self.semantic_analyzer.errors:
                self.errors.extend(self.semantic_analyzer.errors)
            if self.semantic_analyzer.warnings:
                self.warnings.extend(self.semantic_analyzer.warnings)
        
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
        
        # Tabla de Símbolos
        if self.parser and self.parser.tabla_simbolos:
            output.append("=== 📋 TABLA DE SÍMBOLOS ===")
            output.append("| ID  | MÉTODO  | PARÁMETRO | VALOR |")
            output.append("|-----|---------|-----------|-------|")
            for simbolo in self.parser.tabla_simbolos:
                output.append(str(simbolo))
            output.append("")
        
        # Tokens encontrados
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
            
            output.append("")
            
            # Desglose por tipo de token
            output.append("=== DISTRIBUCIÓN DE TOKENS ===")
            for token_type, count in sorted(stats.items()):
                percentage = (count / total_tokens) * 100
                output.append(f"{token_type}: {count} ({percentage:.1f}%)")
        
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
        """Verifica que no haya asignaciones duplicadas para el mismo componente"""
        for simbolo in parser.tabla_simbolos:
            if not simbolo.es_declaracion:
                robot_name = simbolo.id
                component = simbolo.metodo
                
                # Inicializar estructuras si no existen
                if robot_name not in self.robot_assignments:
                    self.robot_assignments[robot_name] = {}
                
                if component not in self.robot_assignments[robot_name]:
                    self.robot_assignments[robot_name][component] = []
                
                # Agregar esta asignación
                self.robot_assignments[robot_name][component].append(simbolo)
                
                # Verificar si hay duplicados
                if len(self.robot_assignments[robot_name][component]) > 1:
                    lineas = [str(s.linea) if s.linea else "?" for s in self.robot_assignments[robot_name][component]]
                    self.errors.append(f"Error semántico en líneas {', '.join(lineas)}: Asignación duplicada para '{robot_name}.{component}' - se encontraron múltiples asignaciones")
    
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
            if not simbolo.es_declaracion:
                robot_name = simbolo.id
                linea = simbolo.linea if simbolo.linea else "desconocida"
                if robot_name not in self.declared_robots:
                    self.errors.append(f"Error semántico en línea {linea}: Robot '{robot_name}' usado sin haber sido declarado")
