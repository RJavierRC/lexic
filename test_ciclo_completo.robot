# Programa completo: Robot agarra objeto, lo mueve y regresa a posición original
Robot r1
r1.repetir = 3

r1.inicio
    # === POSICIÓN INICIAL DE APROXIMACIÓN ===
    r1.velocidad = 1
    r1.base = 0
    r1.hombro = 90
    r1.codo = 90
    r1.garra = 90
    r1.muneca = 0
    r1.espera = 2
    
    # === IR A POSICIÓN DEL OBJETO ===
    r1.velocidad = 2
    r1.base = 45
    r1.hombro = 120
    r1.codo = 90
    r1.espera = 1
    
    # === BAJAR Y AGARRAR OBJETO ===
    r1.velocidad = 1
    r1.codo = 45
    r1.espera = 1
    
    r1.garra = 20
    r1.espera = 1
    
    # === LEVANTAR OBJETO ===
    r1.codo = 90
    r1.hombro = 90
    r1.espera = 1
    
    # === MOVER A POSICIÓN DE DESTINO ===
    r1.velocidad = 3
    r1.base = 180
    r1.hombro = 100
    r1.muneca = 90
    r1.espera = 2
    
    # === COLOCAR OBJETO ===
    r1.velocidad = 1
    r1.codo = 60
    r1.espera = 1
    
    r1.garra = 90
    r1.espera = 1
    
    # === ALEJARSE DEL OBJETO ===
    r1.codo = 90
    r1.hombro = 90
    r1.espera = 1
    
    # === REGRESAR A POSICIÓN ORIGINAL ===
    r1.velocidad = 4
    r1.base = 0
    r1.hombro = 90
    r1.codo = 90
    r1.muneca = 0
    r1.espera = 2
    
    # === POSICIÓN DE REPOSO FINAL ===
    r1.velocidad = 1
    r1.base = 0
    r1.hombro = 180
    r1.codo = 180
    r1.garra = 0
    r1.muneca = 0
    r1.espera = 1
r1.fin
