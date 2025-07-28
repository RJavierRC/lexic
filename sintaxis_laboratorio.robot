Robot asistente_lab

# ===== RUTINA DE LABORATORIO AUTOMATIZADO =====
# Robot maneja muestras, pipetas y equipos de laboratorio

# === CONFIGURACIÓN INICIAL DEL LABORATORIO ===
asistente_lab.velocidad = 125
asistente_lab.precision = 2
asistente_lab.base = 0
asistente_lab.hombro = 20
asistente_lab.codo = -30
asistente_lab.muneca = 0
asistente_lab.inclinacion = 0
asistente_lab.garra = 0
asistente_lab.espera = 3

# === PROCEDIMIENTO 1: TOMAR PIPETA ===
# Movimiento de alta precisión para equipo delicado
asistente_lab.velocidad = 75
asistente_lab.precision = 1

# Aproximarse a estación de pipetas
asistente_lab.base = 60
asistente_lab.hombro = 70
asistente_lab.espera = 2

# Descender con extrema precisión
asistente_lab.codo = -110
asistente_lab.muneca = 30
asistente_lab.inclinacion = -15
asistente_lab.espera = 2

# Agarrar pipeta con cuidado
asistente_lab.garra = -45
asistente_lab.espera = 1.5

# Levantar pipeta
asistente_lab.codo = -70
asistente_lab.hombro = 50
asistente_lab.espera = 2

# === PROCEDIMIENTO 2: PREPARAR MUESTRAS ===
# Velocidad media para eficiencia
asistente_lab.velocidad = 150
asistente_lab.precision = 3

# Moverse a bandeja de muestras (repetir para 6 muestras)
asistente_lab.repetir = 6

# Posicionarse sobre muestra
asistente_lab.base = -75
asistente_lab.hombro = 85
asistente_lab.codo = -130
asistente_lab.espera = 1

# Tomar muestra con pipeta
asistente_lab.inclinacion = -30
asistente_lab.muneca = -45
asistente_lab.espera = 0.8

# Transferir a placa de análisis
asistente_lab.base = 30
asistente_lab.hombro = 60
asistente_lab.codo = -90
asistente_lab.espera = 1

# Depositar muestra
asistente_lab.inclinacion = 30
asistente_lab.muneca = 45
asistente_lab.espera = 0.8

# Limpiar pipeta (movimiento de agitación)
asistente_lab.garra = 15
asistente_lab.espera = 0.3
asistente_lab.garra = -45
asistente_lab.espera = 0.3

# === PROCEDIMIENTO 3: ANÁLISIS ESPECTROSCÓPICO ===
# Velocidad rápida para traslado de equipos
asistente_lab.velocidad = 350
asistente_lab.precision = 7

# Soltar pipeta en estación de limpieza
asistente_lab.base = 90
asistente_lab.hombro = 40
asistente_lab.codo = -60
asistente_lab.espera = 1

asistente_lab.garra = 0
asistente_lab.espera = 1

# Moverse a espectrómetro
asistente_lab.base = -120
asistente_lab.hombro = 95
asistente_lab.codo = -150
asistente_lab.muneca = 90
asistente_lab.espera = 1.5

# Tomar placa de muestras
asistente_lab.inclinacion = -60
asistente_lab.garra = -80
asistente_lab.espera = 1

# Insertar en espectrómetro
asistente_lab.base = -90
asistente_lab.hombro = 110
asistente_lab.codo = -180
asistente_lab.muneca = 0
asistente_lab.espera = 2

# Soltar placa en equipo
asistente_lab.garra = 0
asistente_lab.espera = 1

# === PROCEDIMIENTO 4: TIEMPO DE ANÁLISIS ===
# Movimientos de espera y mantenimiento
asistente_lab.velocidad = 100
asistente_lab.precision = 4

# Alejarse del equipo durante análisis
asistente_lab.base = 0
asistente_lab.hombro = 30
asistente_lab.codo = -45
asistente_lab.muneca = 0
asistente_lab.inclinacion = 0
asistente_lab.espera = 5

# Rutina de calibración (repetir 3 veces)
asistente_lab.repetir = 3

# Movimiento de calibración de sensores
asistente_lab.base = 45
asistente_lab.inclinacion = 45
asistente_lab.espera = 1

asistente_lab.base = -45
asistente_lab.inclinacion = -45
asistente_lab.espera = 1

asistente_lab.base = 0
asistente_lab.inclinacion = 0
asistente_lab.espera = 1

# === PROCEDIMIENTO 5: RECOGER RESULTADOS ===
# Precisión máxima para manejo de resultados delicados
asistente_lab.velocidad = 60
asistente_lab.precision = 1

# Aproximarse nuevamente al espectrómetro
asistente_lab.base = -90
asistente_lab.hombro = 110
asistente_lab.codo = -180
asistente_lab.muneca = 0
asistente_lab.espera = 2

# Tomar placa procesada
asistente_lab.garra = -80
asistente_lab.espera = 2

# Mover a estación de almacenamiento
asistente_lab.base = 150
asistente_lab.hombro = 75
asistente_lab.codo = -100
asistente_lab.muneca = 60
asistente_lab.inclinacion = 30
asistente_lab.espera = 3

# Depositar en archivo de resultados
asistente_lab.garra = 0
asistente_lab.espera = 2

# === LIMPIEZA Y FINALIZACIÓN ===
# Velocidad media para rutina de limpieza
asistente_lab.velocidad = 200
asistente_lab.precision = 5

# Secuencia de limpieza de estación de trabajo
asistente_lab.base = 0
asistente_lab.hombro = 50
asistente_lab.codo = -80
asistente_lab.muneca = -90
asistente_lab.inclinacion = -45
asistente_lab.garra = 180
asistente_lab.espera = 2

# Movimiento de limpieza (repetir 5 veces)
asistente_lab.repetir = 5
asistente_lab.muneca = 90
asistente_lab.espera = 0.4
asistente_lab.muneca = -90
asistente_lab.espera = 0.4

# === POSICIÓN DE REPOSO ===
# Regreso a posición de standby
asistente_lab.velocidad = 150
asistente_lab.precision = 3

asistente_lab.base = 0
asistente_lab.hombro = 20
asistente_lab.codo = -30
asistente_lab.muneca = 0
asistente_lab.inclinacion = 0
asistente_lab.garra = 0
asistente_lab.espera = 3

# === PROCEDIMIENTO DE LABORATORIO COMPLETADO ===