Robot bailarin

# ===== RUTINA DE BAILE ROBÓTICO =====
# El robot ejecuta una coreografía completa con todos los ejes

# === PREPARACIÓN INICIAL ===
bailarin.velocidad = 200
bailarin.precision = 5
bailarin.base = 0
bailarin.hombro = 0
bailarin.codo = 0
bailarin.muneca = 0
bailarin.inclinacion = 0
bailarin.garra = 0
bailarin.espera = 2

# === MOVIMIENTO 1: "SALUDO AL PÚBLICO" ===
# Velocidad media con precisión normal
bailarin.velocidad = 150
bailarin.precision = 3

# Levantar brazo para saludar
bailarin.hombro = 80
bailarin.codo = -60
bailarin.muneca = 45
bailarin.espera = 1

# Movimiento de saludo (repetir 4 veces)
bailarin.repetir = 4
bailarin.garra = 180
bailarin.espera = 0.5
bailarin.garra = -180
bailarin.espera = 0.5

# === MOVIMIENTO 2: "GIRO ESPECTACULAR" ===
# Velocidad rápida con precisión relajada
bailarin.velocidad = 400
bailarin.precision = 8

# Giro completo de base mientras mueve otros ejes
bailarin.base = 180
bailarin.hombro = 45
bailarin.inclinacion = 90
bailarin.espera = 1

bailarin.base = -180
bailarin.muneca = -150
bailarin.garra = 360
bailarin.espera = 1

bailarin.base = 0
bailarin.hombro = 0
bailarin.espera = 1

# === MOVIMIENTO 3: "DANZA DE PRECISIÓN" ===
# Velocidad muy lenta con máxima precisión
bailarin.velocidad = 50
bailarin.precision = 1

# Secuencia coordinada de todos los ejes (repetir 2 veces)
bailarin.repetir = 2

# Fase 1: Elevación gradual
bailarin.base = 45
bailarin.hombro = 60
bailarin.espera = 1.5

bailarin.codo = -90
bailarin.muneca = 60
bailarin.espera = 1.5

bailarin.inclinacion = -45
bailarin.garra = 90
bailarin.espera = 1.5

# Fase 2: Descenso coordinado
bailarin.base = -45
bailarin.hombro = 30
bailarin.codo = -45
bailarin.espera = 1.5

bailarin.muneca = -60
bailarin.inclinacion = 45
bailarin.garra = -90
bailarin.espera = 1.5

# Regreso a centro
bailarin.base = 0
bailarin.hombro = 0
bailarin.codo = 0
bailarin.muneca = 0
bailarin.inclinacion = 0
bailarin.garra = 0
bailarin.espera = 2

# === MOVIMIENTO 4: "FINALE EXPLOSIVO" ===
# Velocidad máxima con movimientos extremos
bailarin.velocidad = 600
bailarin.precision = 10

# Movimiento caótico coordinado
bailarin.base = 135
bailarin.hombro = 90
bailarin.codo = -180
bailarin.muneca = 180
bailarin.inclinacion = -90
bailarin.garra = 300
bailarin.espera = 0.8

bailarin.base = -135
bailarin.hombro = -60
bailarin.codo = 30
bailarin.muneca = -180
bailarin.inclinacion = 90
bailarin.garra = -300
bailarin.espera = 0.8

# === REVERENCIA FINAL ===
# Velocidad lenta para reverencia elegante
bailarin.velocidad = 100
bailarin.precision = 2

bailarin.base = 0
bailarin.hombro = 70
bailarin.codo = -120
bailarin.muneca = 0
bailarin.inclinacion = -30
bailarin.garra = 0
bailarin.espera = 3

# Posición de descanso
bailarin.hombro = 0
bailarin.codo = 0
bailarin.inclinacion = 0
bailarin.espera = 2

# === FIN DE LA COREOGRAFÍA ===