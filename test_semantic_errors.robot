# Prueba de validaciones semánticas

# ===== CASO 1: ROBOTS VÁLIDOS =====
Robot r1
r1.base = 90
r1.hombro = 45
r1.codo = 60
r1.garra = 30

# ===== CASO 2: DECLARACIÓN DUPLICADA =====
Robot r2
r2.base = 120

Robot r2  # Error: declaración duplicada

# ===== CASO 3: ASIGNACIONES DUPLICADAS =====
Robot r3
r3.base = 50
r3.hombro = 90
r3.base = 100  # Error: asignación duplicada

# ===== CASO 4: VALORES FUERA DE RANGO =====
Robot r4
r4.base = 500    # Error: base debe estar entre 0-360
r4.hombro = 200  # Error: hombro debe estar entre 0-180
r4.codo = -50    # Error: codo debe estar entre 0-180
r4.garra = 150   # Error: garra debe estar entre 0-90

# ===== CASO 5: ROBOT NO DECLARADO =====
r5.base = 90     # Error: r5 no fue declarado
