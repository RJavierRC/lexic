# Ejemplo completo de sintaxis extendida para brazo robótico

// Declaración de robot
Robot r1

// Configuración inicial
r1.velocidad = 2.5
r1.base = 90
r1.hombro = 45

// Comando de espera simple
espera 1.5

// Definición de rutina con repeticiones
inicio tomar_y_colocar repetir 3 veces
    r1.base = 45
    espera 1.0
    r1.garra = 20
    espera 0.5
    r1.hombro = 90
    r1.codo = 135
    espera 2.0
    r1.garra = 80
    espera 0.3
fin

// Más configuraciones después de la rutina
r1.muneca = 180
espera 0.8

// Otra rutina sin repeticiones
inicio posicion_home repetir 1 veces
    r1.base = 0
    r1.hombro = 0
    r1.codo = 0
    r1.garra = 0
    r1.muneca = 0
    espera 3.0
fin
