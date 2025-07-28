Robot r1

# === PRUEBA SIMPLE DE DETECCIÓN DE CAMBIOS ===

# Posición inicial
r1.velocidad = 50
r1.base = 0
r1.hombro = 0
r1.espera = 1

# Cambio 1: Solo base
r1.base = 45
r1.espera = 2

# Cambio 2: Cambiar velocidad y hombro
r1.velocidad = 150
r1.hombro = 60
r1.espera = 2

# Cambio 3: Múltiples ejes
r1.base = 90
r1.hombro = 30
r1.codo = -45
r1.espera = 2

# Cambio 4: Repetición
r1.repetir = 3
r1.base = 0
r1.hombro = 0
r1.codo = 0
r1.espera = 1