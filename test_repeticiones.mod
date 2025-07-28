%%%
  VERSION:1
  LANGUAGE:ENGLISH
%%%
MODULE MOD_MainProgram

    ! -------------------------------
    ! Programa generado automáticamente desde sintaxis robótica
    ! Robot: r1
    ! Fecha: 28/07/2025 08:37:13
    ! Movimientos secuenciales: 23 pasos
    ! -------------------------------

    ! Tool variables: 
    PERS tooldata RobotiQ2F85Gripper(FullyClosed) := [TRUE,[[0.000,0.000,130.000],[1.00000000,0.00000000,0.00000000,0.00000000]],[1,[0,0,20],[1,0,0,0],0,0,0.005]];

    ! Reference variables:
    PERS wobjdata Frame2 := [FALSE, TRUE, "", [[0,0,0],[1,0,0,0]],[[-140.437,-738.971,5.234],[1.00000000,0.00000000,0.00000000,0.00000000]]];

    PROC Main()
        ConfJ \On;
        ConfL \Off;
        
        ! Program generated from Robot syntax on 28/07/2025 08:37:13
        ! Robot: r1
        ! Secuencia de 23 movimientos
        
        ! === INICIO DE SECUENCIA DE MOVIMIENTOS ===
        
        ! Paso 1: Mover base de 0.0° a 0.0°
        MoveAbsJ [[0.0,0.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 2: Mover hombro de 0.0° a 0.0°
        MoveAbsJ [[0.0,0.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 3: Esperar 1.0 segundos
        WaitTime 1.0;

        ! Paso 4: Mover base de 0.0° a 45.0°
        MoveAbsJ [[45.0,0.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 5: Mover hombro de 0.0° a 30.0°
        MoveAbsJ [[45.0,30.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 6: Esperar 1.0 segundos
        WaitTime 1.0;

        ! Paso 7: Mover base de 45.0° a 0.0°
        MoveAbsJ [[0.0,30.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 8: Mover hombro de 30.0° a 0.0°
        MoveAbsJ [[0.0,0.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 9: Esperar 1.0 segundos
        WaitTime 1.0;

        ! === REPETICIÓN 2 de 3 ===

        ! Paso 10: Mover base de 0.0° a 45.0°
        MoveAbsJ [[45.0,0.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 11: Mover hombro de 0.0° a 30.0°
        MoveAbsJ [[45.0,30.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 12: Esperar 1.0 segundos
        WaitTime 1.0;

        ! Paso 13: Mover base de 45.0° a 0.0°
        MoveAbsJ [[0.0,30.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 14: Mover hombro de 30.0° a 0.0°
        MoveAbsJ [[0.0,0.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 15: Esperar 1.0 segundos
        WaitTime 1.0;

        ! === REPETICIÓN 3 de 3 ===

        ! Paso 16: Mover base de 0.0° a 45.0°
        MoveAbsJ [[45.0,0.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 17: Mover hombro de 0.0° a 30.0°
        MoveAbsJ [[45.0,30.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 18: Esperar 1.0 segundos
        WaitTime 1.0;

        ! Paso 19: Mover base de 45.0° a 0.0°
        MoveAbsJ [[0.0,30.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 20: Mover hombro de 30.0° a 0.0°
        MoveAbsJ [[0.0,0.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 21: Esperar 1.0 segundos
        WaitTime 1.0;

        ! === FIN DE SECUENCIA ===
        ! Total de pasos ejecutados: 21
        
    ENDPROC
ENDMODULE
