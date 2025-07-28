%%%
  VERSION:1
  LANGUAGE:ENGLISH
%%%
MODULE MOD_MainProgram

    ! -------------------------------
    ! Programa generado automáticamente desde sintaxis robótica
    ! Robot: brazo_dinamico
    ! Fecha: 28/07/2025 12:24:13
    ! Movimientos secuenciales: 17 pasos
    ! -------------------------------

    ! Tool variables: 
    PERS tooldata RobotiQ2F85Gripper(FullyClosed) := [TRUE,[[0.000,0.000,130.000],[1.00000000,0.00000000,0.00000000,0.00000000]],[1,[0,0,20],[1,0,0,0],0,0,0.005]];

    ! Reference variables:
    PERS wobjdata Frame2 := [FALSE, TRUE, "", [[0,0,0],[1,0,0,0]],[[-140.437,-738.971,5.234],[1.00000000,0.00000000,0.00000000,0.00000000]]];

    PROC Main()
        ConfJ \On;
        ConfL \Off;
        
        ! Program generated from Robot syntax on 28/07/2025 12:24:13
        ! Robot: brazo_dinamico
        ! Secuencia de 17 movimientos
        
        ! === INICIO DE SECUENCIA DE MOVIMIENTOS ===
        
        ! Paso 1: Mover base de 0.0° a 120.0°
        MoveAbsJ [[120.0,0.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v250,z2,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 2: Esperar 1.5 segundos
        WaitTime 1.5;

        ! Paso 3: Mover hombro de 0.0° a 75.0°
        MoveAbsJ [[120.0,75.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v250,z2,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 4: Mover inclinacion de 0.0° a -45.0°
        MoveAbsJ [[120.0,75.0,0.0,0.0,-45.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v250,z2,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 5: Esperar 1.0 segundos
        WaitTime 1.0;

        ! Paso 6: Mover garra de 0.0° a 270.0°
        MoveAbsJ [[120.0,75.0,0.0,0.0,-45.0,270.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v250,z2,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 7: Esperar 0.8 segundos
        WaitTime 0.8;

        ! Paso 8: Mover codo de 0.0° a -150.0°
        MoveAbsJ [[120.0,75.0,-150.0,0.0,-45.0,270.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v80,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 9: Mover muneca de 0.0° a 90.0°
        MoveAbsJ [[120.0,75.0,-150.0,90.0,-45.0,270.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v80,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 10: Esperar 2.5 segundos
        WaitTime 2.5;

        ! Paso 11: Mover base de 120.0° a 0.0°
        MoveAbsJ [[0.0,75.0,-150.0,90.0,-45.0,270.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v500,z8,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 12: Mover hombro de 75.0° a 0.0°
        MoveAbsJ [[0.0,0.0,-150.0,90.0,-45.0,270.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v500,z8,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 13: Mover codo de -150.0° a 0.0°
        MoveAbsJ [[0.0,0.0,0.0,90.0,-45.0,270.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v500,z8,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 14: Mover muneca de 90.0° a 0.0°
        MoveAbsJ [[0.0,0.0,0.0,0.0,-45.0,270.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v500,z8,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 15: Mover inclinacion de -45.0° a 0.0°
        MoveAbsJ [[0.0,0.0,0.0,0.0,0.0,270.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v500,z8,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 16: Mover garra de 270.0° a 0.0°
        MoveAbsJ [[0.0,0.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v500,z8,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 17: Esperar 1.0 segundos
        WaitTime 1.0;

        ! === FIN DE SECUENCIA ===
        ! Total de pasos ejecutados: 17
        
    ENDPROC
ENDMODULE
