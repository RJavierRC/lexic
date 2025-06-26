# Definición de tokens para Java
import re

# Palabras clave de Java
JAVA_KEYWORDS = {
    'abstract', 'assert', 'boolean', 'break', 'byte', 'case', 'catch', 'char',
    'class', 'const', 'continue', 'default', 'do', 'double', 'else', 'enum',
    'extends', 'final', 'finally', 'float', 'for', 'goto', 'if', 'implements',
    'import', 'instanceof', 'int', 'interface', 'long', 'native', 'new', 'package',
    'private', 'protected', 'public', 'return', 'short', 'static', 'strictfp',
    'super', 'switch', 'synchronized', 'this', 'throw', 'throws', 'transient',
    'try', 'void', 'volatile', 'while', 'true', 'false', 'null'
}

# Definición de patrones de tokens usando expresiones regulares
TOKEN_PATTERNS = [
    # Comentarios
    ('COMMENT_MULTI', r'/\*[\s\S]*?\*/'),
    ('COMMENT_SINGLE', r'//.*'),
    
    # Literales
    ('STRING_LITERAL', r'"([^"\\]|\\.)*"'),
    ('CHAR_LITERAL', r"'([^'\\]|\\.)'"),
    ('FLOAT_LITERAL', r'\d+\.\d+[fF]?'),
    ('DOUBLE_LITERAL', r'\d+\.\d+[dD]?'),
    ('LONG_LITERAL', r'\d+[lL]'),
    ('INTEGER_LITERAL', r'\d+'),
    ('BOOLEAN_LITERAL', r'\b(true|false)\b'),
    ('NULL_LITERAL', r'\bnull\b'),
    
    # Identificadores (debe ir después de las palabras clave)
    ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),
    
    # Operadores de asignación
    ('ASSIGN_OP', r'(\+=|-=|\*=|/=|%=|&=|\|=|\^=|<<=|>>=|>>>=|=)'),
    
    # Operadores de comparación
    ('RELATIONAL_OP', r'(==|!=|<=|>=|<|>)'),
    
    # Operadores lógicos
    ('LOGICAL_OP', r'(&&|\|\||!)'),
    
    # Operadores aritméticos
    ('ARITHMETIC_OP', r'(\+\+|--|[\+\-\*/%])'),
    
    # Operadores bit a bit
    ('BITWISE_OP', r'(<<|>>>|>>|&|\||\^|~)'),
    
    # Operador ternario
    ('TERNARY_OP', r'\?|:'),
    
    # Delimitadores
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('LBRACE', r'\{'),
    ('RBRACE', r'\}'),
    ('LBRACKET', r'\['),
    ('RBRACKET', r'\]'),
    ('SEMICOLON', r';'),
    ('COMMA', r','),
    ('DOT', r'\.'),
    
    # Espacios en blanco
    ('WHITESPACE', r'[ \t]+'),
    ('NEWLINE', r'\n'),
    
    # Caracteres no reconocidos
    ('UNKNOWN', r'.')
]

def get_token_type(token_value):
    """Determina el tipo de token basado en su valor"""
    if token_value in JAVA_KEYWORDS:
        return 'KEYWORD'
    return None
