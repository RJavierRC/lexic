// Ejemplo de código robótico para probar en macOS
// Este código usa la nueva sintaxis soportada

// Declarar un robot
Robot r1

// Configurar repeticiones
r1.repetir = 3

// Inicio del programa principal
r1.inicio
    // Configurar velocidad de movimiento
    r1.velocidad = 2.5
    
    // Mover componentes del brazo
    r1.base = 45
    r1.hombro = 120
    r1.codo = 90
    r1.garra = 30
    r1.muneca = 180
    
    // Esperar 1 segundo
    r1.espera = 1.0
    
    // Posición de retorno
    r1.base = 0
    r1.hombro = 0
    r1.codo = 0
    r1.garra = 0
    r1.muneca = 0
    
    // Pausa corta
    r1.espera = 0.5
r1.fin

// Ejemplo adicional con otro robot
Robot r2

r2.inicio
    r2.velocidad = 1.5
    r2.base = 90
    r2.espera = 2.0
    r2.garra = 45
r2.fin
