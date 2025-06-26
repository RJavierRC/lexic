// Código de prueba para lenguaje de brazo robótico
// Este archivo demuestra la sintaxis y comandos del lenguaje

# Definición de la configuración inicial
inicio

// Configuración del componente base
base {
    girai 0          // Posición inicial a 0 grados
    giraf 180        // Rotación hacia la derecha 180 grados
    velocidad 50     // Velocidad moderada
}

// Configuración del hombro
hombro {
    girai 45         // Elevar 45 grados
    giraf 90         // Posición de trabajo
    velocidad 30     // Velocidad lenta para precisión
}

// Configuración del codo
codo {
    girai 0          // Posición extendida
    giraf 45         // Flexión parcial
    espera 2         // Pausa de 2 segundos
}

// Configuración de la muñeca
muneca {
    girai -30        // Rotación negativa
    giraf 15         // Ajuste fino
}

// Configuración de la garra (efector final)
garra {
    abre 90          // Apertura completa
    cierra 0         // Cierre completo
    espera 1         // Pausa breve
}

/* Secuencia de movimientos complejos
   Esta sección demuestra comandos avanzados */

// Secuencia de pick and place
secuencia_principal {
    // Mover a posición inicial
    inicio
    
    // Aproximarse al objeto
    base {
        giraf 45
    }
    hombro {
        giraf 60
    }
    codo {
        giraf 30
    }
    
    // Abrir garra y descender
    garra {
        abre 80
    }
    
    espera 1.5       // Pausa para estabilizar
    
    // Cerrar garra sobre el objeto
    garra {
        cierra 20
    }
    
    // Elevar objeto
    hombro {
        girai 30
    }
    
    // Mover a posición de destino
    base {
        giraf 135
    }
    
    // Depositar objeto
    hombro {
        giraf 45
    }
    garra {
        abre 90
    }
    
    // Retornar a posición home
    home
}

// Función de emergencia
emergencia {
    parar
    garra {
        abre 90      // Liberar cualquier objeto
    }
    home             // Volver a posición segura
}

// Valores de prueba para diferentes tipos de datos
configuracion {
    velocidad_max 100
    velocidad_min 5
    precision 0.5
    timeout 30
    debug verdadero
    modo_seguro activado
}

// Comandos con condiciones
si sensor1 == verdadero entonces {
    garra {
        cierra 50
    }
} sino {
    garra {
        abre 90
    }
}

// Bucle de movimiento repetitivo
mientras contador <= 5 {
    base {
        girai 30
        espera 0.5
        giraf 30
        espera 0.5
    }
    contador = contador + 1
}

fin  // Fin del programa
