# Prueba de validaciones semánticas - Caso correcto

# Robots correctamente declarados y configurados
Robot brazo_principal
brazo_principal.base = 180
brazo_principal.hombro = 90
brazo_principal.codo = 45
brazo_principal.garra = 60

Robot brazo_secundario
brazo_secundario.base = 270
brazo_secundario.hombro = 120
brazo_secundario.codo = 90
brazo_secundario.garra = 30

# Valores en los límites (debe generar advertencias)
Robot brazo_limites
brazo_limites.base = 0      # Límite inferior
brazo_limites.hombro = 180  # Límite superior
brazo_limites.codo = 0      # Límite inferior
brazo_limites.garra = 90    # Límite superior
