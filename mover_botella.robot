Robot brazo_industrial

# ===== RUTINA COMPLETA: MOVER BOTELLA =====
# Escenario: Robot toma una botella de la mesa A y la lleva a la mesa B

# === POSICIÓN INICIAL SEGURA ===
brazo_industrial.velocidad = 2
brazo_industrial.base = 0
brazo_industrial.hombro = 20
brazo_industrial.codo = 45
brazo_industrial.muneca = 0
brazo_industrial.garra = 90
brazo_industrial.espera = 2

# === APROXIMARSE A LA BOTELLA (Mesa A) ===
# Cambiar a velocidad lenta para precisión
brazo_industrial.velocidad = 1
brazo_industrial.base = 45
brazo_industrial.espera = 3

# Posicionar brazo sobre la botella
brazo_industrial.hombro = 40
brazo_industrial.espera = 2

brazo_industrial.codo = 70
brazo_industrial.espera = 2

# === BAJAR PARA AGARRAR LA BOTELLA ===
# Bajar muy lentamente para no tirar la botella
brazo_industrial.hombro = 60
brazo_industrial.espera = 1

brazo_industrial.codo = 90
brazo_industrial.espera = 1

# === CERRAR LA GARRA - AGARRAR BOTELLA ===
brazo_industrial.garra = 25
brazo_industrial.espera = 2

# === LEVANTAR LA BOTELLA ===
# Subir lentamente con la botella
brazo_industrial.codo = 70
brazo_industrial.espera = 1

brazo_industrial.hombro = 40
brazo_industrial.espera = 1

# === TRANSPORTAR A MESA B ===
# Cambiar a velocidad rápida para transporte
brazo_industrial.velocidad = 4

# Girar hacia mesa B (lado opuesto)
brazo_industrial.base = -60
brazo_industrial.espera = 1

# Ajustar altura para mesa B
brazo_industrial.hombro = 50
brazo_industrial.espera = 1

# === POSICIONAR SOBRE MESA B ===
# Cambiar a velocidad media para colocación precisa
brazo_industrial.velocidad = 3

brazo_industrial.muneca = 45
brazo_industrial.espera = 1

# === BAJAR LA BOTELLA ===
# Bajar lentamente para colocar
brazo_industrial.velocidad = 1

brazo_industrial.hombro = 65
brazo_industrial.espera = 1

brazo_industrial.codo = 85
brazo_industrial.espera = 1

# === SOLTAR LA BOTELLA ===
brazo_industrial.garra = 90
brazo_industrial.espera = 2

# === ALEJARSE DE LA BOTELLA ===
brazo_industrial.velocidad = 2

brazo_industrial.codo = 70
brazo_industrial.espera = 1

brazo_industrial.hombro = 50
brazo_industrial.espera = 1

# === REGRESAR A POSICIÓN INICIAL ===
# Velocidad rápida para regreso
brazo_industrial.velocidad = 4

brazo_industrial.base = 0
brazo_industrial.hombro = 20
brazo_industrial.codo = 45
brazo_industrial.muneca = 0
brazo_industrial.garra = 90
brazo_industrial.espera = 3

# === MISIÓN COMPLETADA ===