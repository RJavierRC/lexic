# Prueba completa: robots válidos, tokens desconocidos y errores

# ===== ROBOTS VÁLIDOS =====
Robot r1
r1.base = 50
r1.hombro = 45
r1.codo = 30

Robot r2
r2.base = 120
r2.garra = 10
r2.muneca = 180

# ===== TOKENS DESCONOCIDOS =====
Robot r3
r3.base = 90@      # Símbolo @ no válido
r3.hombro = 60$    # Símbolo $ no válido
r3.codo* = 45      # Símbolo * no válido

# ===== ERRORES SINTÁCTICOS =====
Robot             # Falta nombre del robot
r4.base = 100     # r4 no fue declarado

# ===== MÁS TOKENS DESCONOCIDOS =====
~comando_invalido
¡Robot r5!        # Símbolos ¡ ! no válidos
r5.base = 75¿     # Símbolo ¿ no válido
r5.garra& = 20    # Símbolo & no válido

# ===== VALORES EXTREMOS (ADVERTENCIAS) =====
Robot r6
r6.base = 500     # Valor > 360 grados
r6.hombro = -400  # Valor < -360 grados

# ===== CARACTERES UNICODE NO VÁLIDOS =====
Robot r7€         # Símbolo € no válido
r7.base = 90¤     # Símbolo ¤ no válido
r7.codo¥ = 45     # Símbolo ¥ no válido
