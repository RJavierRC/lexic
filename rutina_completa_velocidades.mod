%%%
  VERSION:1
  LANGUAGE:ENGLISH
%%%
MODULE MOD_RutinaCompleta

    ! RUTINA COMPLETA - Demostración de todas las velocidades y movimientos
    ! Sintaxis soportada: base, hombro, codo, muneca, garra, velocidad, espera
    ! Velocidades: 1=v25, 2=v75, 3=v150, 4=v400 (diferencias MÁS NOTORIAS)

    ! Tool variables: 
    PERS tooldata RobotiQ2F85Gripper := [TRUE,[[0.000,0.000,130.000],[1.00000000,0.00000000,0.00000000,0.00000000]],[1,[0,0,20],[1,0,0,0],0,0,0.005]];

    ! Reference variables:
    PERS wobjdata Frame2 := [FALSE, TRUE, "", [[0,0,0],[1,0,0,0]],[[-140.437,-738.971,5.234],[1.00000000,0.00000000,0.00000000,0.00000000]]];

    PROC Main()
        ConfJ \On;
        ConfL \Off;
        
        ! ===== RUTINA COMPLETA DE DEMOSTRACIÓN =====
        
        ! POSICIÓN INICIAL
        MoveAbsJ [[0,0,-45,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z1,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 2.0;
        
        ! ===== DEMOSTRACIÓN VELOCIDAD 1 (v25 - MUY MUY LENTA) =====
        ! Equivale a: r1.velocidad = 1
        
        ! Mover BASE muy lento (r1.base = 45)
        MoveAbsJ [[45,0,-45,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v25,z1,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 3.0;
        
        ! Mover HOMBRO muy lento (r1.hombro = 40)
        MoveAbsJ [[45,40,-45,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v25,z1,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 3.0;
        
        ! Mover CODO muy lento (r1.codo = -70)
        MoveAbsJ [[45,40,-70,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v25,z1,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 3.0;
        
        ! ===== DEMOSTRACIÓN VELOCIDAD 2 (v75 - LENTA) =====
        ! Equivale a: r1.velocidad = 2
        
        ! Mover MUÑECA lento (r1.muneca = 60)
        MoveAbsJ [[45,40,-70,60,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v75,z1,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 2.5;
        
        ! Cambiar BASE lento (r1.base = -30)
        MoveAbsJ [[-30,40,-70,60,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v75,z1,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 2.5;
        
        ! Cambiar GARRA lento (r1.garra = -60) - CIERRE
        MoveAbsJ [[-30,40,-70,60,0,-60],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v75,z1,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 2.5;
        
        ! ===== DEMOSTRACIÓN VELOCIDAD 3 (v150 - MEDIA) =====
        ! Equivale a: r1.velocidad = 3
        
        ! Secuencia MEDIA de movimientos
        MoveAbsJ [[30,60,-90,30,0,-60],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v150,z1,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 2.0;
        
        ! Abrir GARRA media (r1.garra = 45) - APERTURA
        MoveAbsJ [[30,60,-90,30,0,45],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v150,z1,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 2.0;
        
        ! Mover HOMBRO y CODO simultaneo medio
        MoveAbsJ [[30,80,-60,30,0,45],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v150,z1,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 2.0;
        
        ! ===== DEMOSTRACIÓN VELOCIDAD 4 (v400 - RÁPIDA) =====
        ! Equivale a: r1.velocidad = 4
        
        ! Movimiento RÁPIDO múltiple
        MoveAbsJ [[-45,90,-120,90,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v400,z1,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 1.5;
        
        ! BASE rápida (r1.base = 90)
        MoveAbsJ [[90,90,-120,90,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v400,z1,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 1.5;
        
        ! CODO rápido (r1.codo = -45)
        MoveAbsJ [[90,90,-45,90,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v400,z1,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 1.5;
        
        ! ===== SECUENCIA PICK & PLACE COMPLETA =====
        ! Simulando: ir a objeto, agarrar, mover, soltar
        
        ! Ir a posición de objeto (velocidad media)
        MoveAbsJ [[45,70,-80,45,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v150,z1,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 1.0;
        
        ! Bajar para agarrar (velocidad lenta)
        MoveAbsJ [[45,50,-100,45,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v75,z1,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 1.0;
        
        ! Cerrar garra (muy lento)
        MoveAbsJ [[45,50,-100,45,0,-75],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v25,z1,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 2.0;
        
        ! Levantar objeto (velocidad media)
        MoveAbsJ [[45,70,-80,45,0,-75],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v150,z1,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 1.0;
        
        ! Mover a destino (velocidad rápida)
        MoveAbsJ [[-60,70,-80,-45,0,-75],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v400,z1,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 1.0;
        
        ! Bajar en destino (velocidad lenta)
        MoveAbsJ [[-60,50,-100,-45,0,-75],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v75,z1,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 1.0;
        
        ! Soltar objeto (muy lento)
        MoveAbsJ [[-60,50,-100,-45,0,30],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v25,z1,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 2.0;
        
        ! Alejarse (velocidad media)
        MoveAbsJ [[-60,70,-80,-45,0,30],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v150,z1,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 1.0;
        
        ! ===== REGRESO A POSICIÓN INICIAL (RÁPIDO) =====
        MoveAbsJ [[0,0,-45,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v400,z1,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 2.0;
        
        ! ===== RUTINA COMPLETA TERMINADA =====
        
    ENDPROC

ENDMODULE