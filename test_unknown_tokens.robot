# Archivo de prueba con tokens desconocidos

Robot r1
r1.base = 50
r1.hombro = 45@
r1.codo = 30$

Robot r2
r2.base = 120%
r2.garra* = 10
r2.muneca = &180

# Varios tokens desconocidos
~invalid_command
r1.base = 90¿
¡error_here!
r2.codo = 45¥

# Caracteres especiales no válidos
Robot r3€
r3.base = 100¤
