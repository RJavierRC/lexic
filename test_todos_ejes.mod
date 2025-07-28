%%%
  VERSION:1
  LANGUAGE:ENGLISH
%%%
MODULE MOD_MainProgram

    ! -------------------------------
    ! Programa generado automáticamente desde sintaxis robótica
    ! Robot: r1
    ! Fecha: 28/07/2025 11:53:43
    ! Movimientos secuenciales: 19 pasos
    ! -------------------------------

    ! Tool variables: 
    PERS tooldata RobotiQ2F85Gripper(FullyClosed) := [TRUE,[[0.000,0.000,130.000],[1.00000000,0.00000000,0.00000000,0.00000000]],[1,[0,0,20],[1,0,0,0],0,0,0.005]];

    ! Reference variables:
    PERS wobjdata Frame2 := [FALSE, TRUE, "", [[0,0,0],[1,0,0,0]],[[-140.437,-738.971,5.234],[1.00000000,0.00000000,0.00000000,0.00000000]]];

    PROC Main()
        ConfJ \On;
        ConfL \Off;
        
        ! Program generated from Robot syntax on 28/07/2025 11:53:43
        ! Robot: r1
        ! Secuencia de 19 movimientos
        
        ! === INICIO DE SECUENCIA DE MOVIMIENTOS ===
        
        ! Paso 1: Mover base de 0.0° a 90.0°
        MoveAbsJ [[90.0,0.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z3,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 2: Esperar 1.0 segundos
        WaitTime 1.0;

        ! Paso 3: Mover hombro de 0.0° a 60.0°
        MoveAbsJ [[90.0,60.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z3,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 4: Esperar 1.0 segundos
        WaitTime 1.0;

        ! Paso 5: Mover codo de 0.0° a -45.0°
        MoveAbsJ [[90.0,60.0,-45.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z3,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 6: Esperar 1.0 segundos
        WaitTime 1.0;

        ! Paso 7: Mover muneca de 0.0° a 180.0°
        MoveAbsJ [[90.0,60.0,-45.0,180.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z3,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 8: Esperar 1.0 segundos
        WaitTime 1.0;

        ! Paso 9: Mover inclinacion de 0.0° a -30.0°
        MoveAbsJ [[90.0,60.0,-45.0,180.0,-30.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z3,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 10: Esperar 1.0 segundos
        WaitTime 1.0;

        ! Paso 11: Mover garra de 0.0° a 270.0°
        MoveAbsJ [[90.0,60.0,-45.0,180.0,-30.0,270.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z3,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 12: Esperar 1.0 segundos
        WaitTime 1.0;

        ! Paso 13: Mover base de 90.0° a 0.0°
        MoveAbsJ [[0.0,60.0,-45.0,180.0,-30.0,270.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z3,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 14: Mover hombro de 60.0° a 0.0°
        MoveAbsJ [[0.0,0.0,-45.0,180.0,-30.0,270.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z3,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 15: Mover codo de -45.0° a 0.0°
        MoveAbsJ [[0.0,0.0,0.0,180.0,-30.0,270.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z3,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 16: Mover muneca de 180.0° a 0.0°
        MoveAbsJ [[0.0,0.0,0.0,0.0,-30.0,270.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z3,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 17: Mover inclinacion de -30.0° a 0.0°
        MoveAbsJ [[0.0,0.0,0.0,0.0,0.0,270.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z3,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 18: Mover garra de 270.0° a 0.0°
        MoveAbsJ [[0.0,0.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z3,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 19: Esperar 2.0 segundos
        WaitTime 2.0;

        ! === FIN DE SECUENCIA ===
        ! Total de pasos ejecutados: 19
        
    ENDPROC
ENDMODULE
