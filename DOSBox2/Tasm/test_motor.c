/*
 * Simulador de control de motores para Proteus
 * Programa: test_motor  
 * Generado: 2025-07-14 16:56:28
 * Simula comportamiento de assembly para control de 3 motores paso a paso
 */

#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

// Definiciones de puertos 8255 (simulados)
#define PORTA   0x00
#define PORTB   0x02  
#define PORTC   0x04
#define CONFIG  0x06

// Patrones de stepping para motores paso a paso
unsigned char step_patterns[] = {0x06, 0x0C, 0x09, 0x03};

// Funcin para simular OUT (escritura a puerto)
void outport(int port, unsigned char value) {
    printf("OUT Port 0x%02X = 0x%02X\n", port, value);
    // En Proteus, esto controlara los motores reales
}

// Funcin para simular delay
void delay(int cycles) {
    Sleep(cycles / 1000); // Convertir ciclos a ms aproximado
}

int main() {
    printf("=== CONTROL DE 3 MOTORES PASO A PASO ===\n");
    printf("Programa: test_motor.exe\n");
    printf("Simulando comportamiento para Proteus\n\n");
    
    // Configurar 8255 - todos los puertos como salida
    printf("Configurando 8255...\n");
    outport(CONFIG, 0x80);
    
    // MOTOR A (BASE) - Secuencia de pasos
    printf("\n--- MOTOR A (BASE) ---\n");
    for(int i = 0; i < 4; i++) {
        outport(PORTA, step_patterns[i]);
        delay(65535);
    }
    
    // MOTOR B (HOMBRO) - Secuencia de pasos  
    printf("\n--- MOTOR B (HOMBRO) ---\n");
    for(int i = 0; i < 4; i++) {
        outport(PORTB, step_patterns[i]);
        delay(65535);
    }
    
    // MOTOR C (CODO) - Secuencia de pasos
    printf("\n--- MOTOR C (CODO) ---\n"); 
    for(int i = 0; i < 4; i++) {
        outport(PORTC, step_patterns[i]);
        delay(65535);
    }
    
    printf("\n=== SECUENCIA COMPLETADA ===\n");
    printf("Los 3 motores han ejecutado sus secuencias de pasos\n");
    
    return 0;
}
