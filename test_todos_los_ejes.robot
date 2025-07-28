Robot r1

# === PRUEBA CORTA DE TODOS LOS EJES ===

# Configurar velocidad y precisión
r1.velocidad = 100
r1.precision = 3

# Mover cada eje individualmente
r1.base = 90
r1.espera = 1

r1.hombro = 60
r1.espera = 1

r1.codo = -45
r1.espera = 1

r1.muneca = 180
r1.espera = 1

r1.inclinacion = -30
r1.espera = 1

r1.garra = 270
r1.espera = 1

# Regreso a posición inicial
r1.base = 0
r1.hombro = 0
r1.codo = 0
r1.muneca = 0
r1.inclinacion = 0
r1.garra = 0
r1.espera = 2