Robot brazo_avanzado

# ===== EJEMPLO DE SINTAXIS COMPLETA =====
# Demuestra todos los 6 ejes + velocidades directas + zonas de precisión

# === CONFIGURACIÓN INICIAL ===
brazo_avanzado.velocidad = 150
brazo_avanzado.precision = 5
brazo_avanzado.base = 0
brazo_avanzado.hombro = 0
brazo_avanzado.codo = 0
brazo_avanzado.muneca = 0
brazo_avanzado.inclinacion = 0
brazo_avanzado.garra = 0
brazo_avanzado.espera = 2

# === DEMOSTRACIÓN EJE 1 - BASE (Rotación horizontal) ===
# Velocidad lenta para movimientos precisos
brazo_avanzado.velocidad = 75
brazo_avanzado.precision = 1
brazo_avanzado.base = 180
brazo_avanzado.espera = 3

brazo_avanzado.base = -180
brazo_avanzado.espera = 3

brazo_avanzado.base = 0
brazo_avanzado.espera = 2

# === DEMOSTRACIÓN EJE 2 - HOMBRO (Elevación) ===
brazo_avanzado.velocidad = 100
brazo_avanzado.precision = 3
brazo_avanzado.base = 46
brazo_avanzado.espera = 1

brazo_avanzado.hombro = 93
brazo_avanzado.espera = 2

brazo_avanzado.hombro = -83
brazo_avanzado.espera = 2

brazo_avanzado.hombro = 0
brazo_avanzado.base = 0
brazo_avanzado.espera = 2

# === DEMOSTRACIÓN EJE 3 - CODO (Articulación intermedia) ===
brazo_avanzado.velocidad = 50
brazo_avanzado.precision = 1
brazo_avanzado.base = -73
brazo_avanzado.espera = 1

# Codo a límites extremos (como en archivos originales)
brazo_avanzado.codo = -230
brazo_avanzado.espera = 3

brazo_avanzado.codo = 50
brazo_avanzado.espera = 3

brazo_avanzado.codo = 0
brazo_avanzado.base = 0
brazo_avanzado.espera = 2

# === DEMOSTRACIÓN EJE 4 - MUÑECA (Rotación antebrazo) ===
brazo_avanzado.velocidad = 125
brazo_avanzado.precision = 5
brazo_avanzado.base = 46
brazo_avanzado.espera = 1

brazo_avanzado.muneca = -200
brazo_avanzado.espera = 2

brazo_avanzado.muneca = 200
brazo_avanzado.espera = 2

brazo_avanzado.muneca = 0
brazo_avanzado.base = 0
brazo_avanzado.espera = 2

# === DEMOSTRACIÓN EJE 5 - INCLINACIÓN (Nuevo eje) ===
brazo_avanzado.velocidad = 75
brazo_avanzado.precision = 2
brazo_avanzado.base = 46
brazo_avanzado.espera = 1

# Inclinación de garra (como en garrabase.mod)
brazo_avanzado.inclinacion = -120
brazo_avanzado.espera = 2

brazo_avanzado.inclinacion = 120
brazo_avanzado.espera = 2

brazo_avanzado.inclinacion = 0
brazo_avanzado.base = 0
brazo_avanzado.espera = 2

# === DEMOSTRACIÓN EJE 6 - GARRA (Rotación final) ===
brazo_avanzado.velocidad = 200
brazo_avanzado.precision = 8
brazo_avanzado.base = -73
brazo_avanzado.espera = 1

# Garra con giro completo (como en garragiro.mod)
brazo_avanzado.garra = 400
brazo_avanzado.espera = 2

brazo_avanzado.garra = 10
brazo_avanzado.espera = 1

brazo_avanzado.garra = 0
brazo_avanzado.base = 0
brazo_avanzado.espera = 2

# === SECUENCIA COORDINADA ESPECTACULAR ===
# Velocidad rápida con precisión relajada
brazo_avanzado.velocidad = 400
brazo_avanzado.precision = 10

# Movimiento coordinado de TODOS los ejes
brazo_avanzado.base = 90
brazo_avanzado.hombro = 45
brazo_avanzado.codo = -120
brazo_avanzado.muneca = 90
brazo_avanzado.inclinacion = -60
brazo_avanzado.garra = 180
brazo_avanzado.espera = 2

# Movimiento opuesto coordinado
brazo_avanzado.base = -90
brazo_avanzado.hombro = -45
brazo_avanzado.codo = 45
brazo_avanzado.muneca = -90
brazo_avanzado.inclinacion = 60
brazo_avanzado.garra = -180
brazo_avanzado.espera = 2

# === REGRESO A POSICIÓN INICIAL ===
# Velocidad media con precisión normal
brazo_avanzado.velocidad = 200
brazo_avanzado.precision = 5

brazo_avanzado.base = 0
brazo_avanzado.hombro = 0
brazo_avanzado.codo = 0
brazo_avanzado.muneca = 0
brazo_avanzado.inclinacion = 0
brazo_avanzado.garra = 0
brazo_avanzado.espera = 3

# === DEMOSTRACIÓN TERMINADA ===