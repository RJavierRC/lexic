# Definición de tokens para Lenguaje de Brazo Robótico
import re

# Palabras clave del lenguaje robótico
ROBOT_KEYWORDS = {
    # Declaración de robot
    'Robot', 'robot',
    
    # Componentes del brazo
    'base', 'hombro', 'codo', 'garra', 'muneca', 'velocidad',
    
    # Comandos de movimiento (sintaxis antigua - mantenida para compatibilidad)
    'girai', 'giraf', 'abre', 'cierra', 'mueve', 'rotara', 'posicion',
    'parar', 'continuar',
    
    # Nuevos comandos para rutinas y control temporal
    'espera', 'inicio', 'fin', 'repetir', 'veces',
    
    # Direcciones y posiciones
    'arriba', 'abajo', 'izquierda', 'derecha', 'adelante', 'atras',
    'centro', 'home', 'inicial',
    
    # Estados y condiciones
    'si', 'entonces', 'sino', 'mientras', 'cuando', 'hasta',
    'verdadero', 'falso', 'activado', 'desactivado',
    
    # Sensores y actuadores
    'sensor', 'motor', 'servomotor', 'encoder', 'limite',
    
    # Unidades
    'grados', 'radianes', 'mm', 'cm', 'segundos', 'milisegundos',
    'rpm', 'velocidad_max', 'velocidad_min'
}

# Componentes válidos del brazo robótico
VALID_COMPONENTS = {'base', 'hombro', 'codo', 'garra', 'muneca', 'velocidad', 'repetir', 'inicio', 'fin', 'espera'}

# Definición de patrones de tokens usando expresiones regulares
TOKEN_PATTERNS = [
    # Comentarios
    ('COMMENT_MULTI', r'/\*[\s\S]*?\*/'),
    ('COMMENT_SINGLE', r'//.*'),
    ('COMMENT_HASH', r'#.*'),
    
    # Literales numéricos
    ('FLOAT_LITERAL', r'-?\d+\.\d+'),
    ('INTEGER_LITERAL', r'-?\d+'),
    
    # Literales booleanos
    ('BOOLEAN_LITERAL', r'\b(verdadero|falso|activado|desactivado)\b'),
    
    # Identificadores (debe ir después de las palabras clave)
    ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),
    
    # Operadores de comparación
    ('COMPARISON_OP', r'(==|!=|<=|>=|<|>)'),
    
    # Operadores de asignación
    ('ASSIGN_OP', r'='),
    
    # Operadores aritméticos
    ('ARITHMETIC_OP', r'[\+\-\*/%]'),
    
    # Operadores lógicos
    ('LOGICAL_OP', r'(&&|\|\||y|o|no|!)'),
    
    # Delimitadores estructurales
    ('LBRACE', r'\{'),
    ('RBRACE', r'\}'),
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('LBRACKET', r'\['),
    ('RBRACKET', r'\]'),
    
    # Separadores
    ('SEMICOLON', r';'),
    ('COMMA', r','),
    ('DOT', r'\.'),
    ('COLON', r':'),
    
    # Espacios en blanco
    ('WHITESPACE', r'[ \t]+'),
    ('NEWLINE', r'\n'),
    
    # Caracteres no reconocidos
    ('UNKNOWN', r'.')
]

def get_token_type(token_value):
    """Determina el tipo de token basado en su valor"""
    if token_value in ROBOT_KEYWORDS or token_value.lower() in ROBOT_KEYWORDS:
        return 'KEYWORD'
    return None

# Información adicional sobre el lenguaje
LANGUAGE_INFO = {
    'name': 'RobotArm Language',
    'version': '1.0',
    'description': 'Lenguaje de programación para control de brazo robótico',
    'file_extensions': ['.robot', '.arm', '.rb', '.txt'],
    'components': [
        'base - Componente base del brazo robótico',
        'hombro - Articulación del hombro',
        'codo - Articulación del codo',
        'garra - Efector final (pinza)',
        'muneca - Articulación de la muñeca'
    ],
    'commands': [
        'girai - Girar a la izquierda (grados)',
        'giraf - Girar a la derecha (grados)',
        'abre - Abrir garra (grados)',
        'cierra - Cerrar garra (grados)',
        'mueve - Mover a posición específica',
        'espera - Pausar ejecución (tiempo)',
        'inicio - Marcar inicio de secuencia',
        'fin - Marcar fin de secuencia'
    ]
}
