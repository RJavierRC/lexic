%%%
  VERSION:1
  LANGUAGE:ENGLISH
%%%
MODULE MOD_DemoSeguro

    ! Programa SEGURO - Ángulos dentro de límites ABB IRB140
    ! LÍMITES SEGUROS ABB IRB140:
    ! Eje 1 (base): -180° a +180°
    ! Eje 2 (hombro): -90° a +110° 
    ! Eje 3 (codo): -230° a +50°
    ! Eje 4 (muñeca): -200° a +200°
    ! Eje 5: -120° a +120°
    ! Eje 6 (garra): -400° a +400°

    ! Tool variables: 
    PERS tooldata RobotiQ2F85Gripper := [TRUE,[[0.000,0.000,130.000],[1.00000000,0.00000000,0.00000000,0.00000000]],[1,[0,0,20],[1,0,0,0],0,0,0.005]];

    ! Reference variables:
    PERS wobjdata Frame2 := [FALSE, TRUE, "", [[0,0,0],[1,0,0,0]],[[-140.437,-738.971,5.234],[1.00000000,0.00000000,0.00000000,0.00000000]]];

    PROC Main()
        ConfJ \On;
        ConfL \Off;
        
        ! === DEMO VELOCIDADES CON ÁNGULOS SEGUROS ===
        
        ! Posición inicial SEGURA
        MoveAbsJ [[0,0,-45,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v50,z1,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 1.0;
        
        ! VELOCIDAD 1 (v50 - MUY LENTA): Base a 30°
        MoveAbsJ [[30,0,-45,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v50,z1,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 2.0;
        
        ! VELOCIDAD 2 (v100 - LENTA): Hombro a 30° (SEGURO)
        MoveAbsJ [[30,30,-45,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z1,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 2.0;
        
        ! VELOCIDAD 3 (v200 - MEDIA): Codo a -60° (SEGURO)
        MoveAbsJ [[30,30,-60,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v200,z1,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 1.5;
        
        ! VELOCIDAD 4 (v500 - RÁPIDA): Base a 60°, hombro a 45°
        MoveAbsJ [[60,45,-60,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v500,z1,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 1.0;
        
        ! DEMO MUÑECA (v200): Rotar muñeca a 45°
        MoveAbsJ [[60,45,-60,45,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v200,z1,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 1.0;
        
        ! DEMO GARRA LENTA (v50): Cerrar garra (eje 6 a -45°)
        MoveAbsJ [[60,45,-60,45,0,-45],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v50,z1,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 2.0;
        
        ! DEMO GARRA: Abrir garra (eje 6 a 0°)
        MoveAbsJ [[60,45,-60,45,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v50,z1,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 1.5;
        
        ! MOVIMIENTO COMPLEJO (v300): Cambiar varios ejes
        MoveAbsJ [[-30,60,-90,90,0,30],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v300,z1,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 1.0;
        
        ! REGRESO RÁPIDO A INICIAL (v500)
        MoveAbsJ [[0,0,-45,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v500,z1,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 1.0;
        
        ! === PROGRAMA COMPLETADO SIN ERRORES ===
        
    ENDPROC

ENDMODULE