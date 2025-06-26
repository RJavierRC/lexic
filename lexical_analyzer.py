import re
from java_tokens import TOKEN_PATTERNS, JAVA_KEYWORDS, get_token_type

class Token:
    """Clase para representar un token"""
    def __init__(self, type_, value, line, column):
        self.type = type_
        self.value = value
        self.line = line
        self.column = column
    
    def __str__(self):
        return f"Token({self.type}, '{self.value}', {self.line}:{self.column})"
    
    def __repr__(self):
        return self.__str__()

class LexicalAnalyzer:
    """Analizador léxico para Java"""
    
    def __init__(self):
        self.tokens = []
        self.errors = []
        self.current_line = 1
        self.current_column = 1
        
    def analyze(self, source_code):
        """Analiza el código fuente y genera tokens"""
        self.tokens = []
        self.errors = []
        self.current_line = 1
        self.current_column = 1
        
        # Combinar todos los patrones en una expresión regular
        combined_pattern = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_PATTERNS)
        regex = re.compile(combined_pattern)
        
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
                
                # Crear token
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
        
        return self.tokens, self.errors
    
    def get_token_statistics(self):
        """Genera estadísticas de los tokens encontrados"""
        stats = {}
        for token in self.tokens:
            if token.type in stats:
                stats[token.type] += 1
            else:
                stats[token.type] = 1
        return stats
    
    def get_formatted_output(self):
        """Genera salida formateada de los tokens"""
        output = []
        
        if self.errors:
            output.append("=== ERRORES LÉXICOS ===")
            for error in self.errors:
                output.append(error)
            output.append("")
        
        if self.tokens:
            output.append("=== TOKENS ENCONTRADOS ===")
            output.append(f"{'Tipo':<20} {'Valor':<20} {'Línea':<8} {'Columna':<8}")
            output.append("-" * 60)
            
            for token in self.tokens:
                output.append(f"{token.type:<20} {repr(token.value):<20} {token.line:<8} {token.column:<8}")
            
            output.append("")
            output.append("=== ESTADÍSTICAS ===")
            stats = self.get_token_statistics()
            total_tokens = sum(stats.values())
            output.append(f"Total de tokens: {total_tokens}")
            
            for token_type, count in sorted(stats.items()):
                percentage = (count / total_tokens) * 100
                output.append(f"{token_type}: {count} ({percentage:.1f}%)")
        
        return "\n".join(output)
