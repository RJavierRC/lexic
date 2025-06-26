// Archivo de prueba para el analizador léxico
public class TestCode {
    // Declaración de variables
    private int contador = 0;
    private String mensaje = "Hola mundo";
    private boolean activo = true;
    private double precio = 19.99;
    
    // Constructor
    public TestCode() {
        this.contador = 10;
    }
    
    // Método principal
    public static void main(String[] args) {
        TestCode test = new TestCode();
        test.procesarDatos();
        
        // Bucle for
        for (int i = 0; i < 5; i++) {
            System.out.println("Iteración: " + i);
        }
        
        // Condicional if-else
        if (test.activo) {
            System.out.println("El objeto está activo");
        } else {
            System.out.println("El objeto está inactivo");
        }
    }
    
    // Método con parámetros
    public void procesarDatos() {
        // Operaciones aritméticas
        int suma = 10 + 20;
        int resta = 50 - 15;
        int multiplicacion = 5 * 6;
        int division = 100 / 4;
        int modulo = 17 % 3;
        
        // Operadores de incremento y decremento
        contador++;
        --contador;
        
        // Operadores de comparación
        boolean mayor = suma > resta;
        boolean menor = division < multiplicacion;
        boolean igual = modulo == 2;
        boolean diferente = suma != resta;
        
        // Operadores lógicos
        boolean resultado = mayor && menor;
        boolean resultado2 = igual || diferente;
        boolean negacion = !activo;
        
        // Operador ternario
        String estado = activo ? "Encendido" : "Apagado";
        
        // Arreglos
        int[] numeros = {1, 2, 3, 4, 5};
        String[] nombres = new String[3];
        
        // Bucle while
        int j = 0;
        while (j < numeros.length) {
            System.out.println("Número: " + numeros[j]);
            j++;
        }
        
        // Switch
        switch (contador) {
            case 1:
                System.out.println("Uno");
                break;
            case 2:
                System.out.println("Dos");
                break;
            default:
                System.out.println("Otro");
                break;
        }
        
        // Try-catch
        try {
            int resultado3 = 10 / 0;
        } catch (ArithmeticException e) {
            System.out.println("Error: " + e.getMessage());
        } finally {
            System.out.println("Bloque finally");
        }
    }
    
    /* Comentario de múltiples líneas
       Este es un ejemplo de comentario
       que abarca varias líneas */
    
    // Método con diferentes tipos de datos
    public void tiposDeDatos() {
        byte b = 127;
        short s = 32767;
        int i = 2147483647;
        long l = 9223372036854775807L;
        float f = 3.14f;
        double d = 3.141592653589793;
        char c = 'A';
        boolean bool = false;
        String str = null;
    }
}
