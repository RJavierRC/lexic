%%%
  VERSION:1
  LANGUAGE:ENGLISH
%%%
MODULE MOD_MainProgram

    ! -------------------------------
    ! Programa generado automáticamente desde sintaxis robótica
    ! Robot: r1
    ! Fecha: 28/07/2025 08:33:30
    ! Movimientos secuenciales: 14 pasos
    ! -------------------------------

    ! Tool variables: 
    PERS tooldata RobotiQ2F85Gripper(FullyClosed) := [TRUE,[[0.000,0.000,130.000],[1.00000000,0.00000000,0.00000000,0.00000000]],[1,[0,0,20],[1,0,0,0],0,0,0.005]];

    ! Reference variables:
    PERS wobjdata Frame2 := [FALSE, TRUE, "", [[0,0,0],[1,0,0,0]],[[-140.437,-738.971,5.234],[1.00000000,0.00000000,0.00000000,0.00000000]]];

    PROC Main()
        ConfJ \On;
        ConfL \Off;
        
        ! Program generated from Robot syntax on 28/07/2025 08:33:30
        ! Robot: r1
        ! Secuencia de 14 movimientos
        
        ! === INICIO DE SECUENCIA DE MOVIMIENTOS ===
        
        ! Paso 1: Mover base de 0.0° a 0.0°
        MoveAbsJ [[0.0,0.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v50,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 2: Mover hombro de 0.0° a 0.0°
        MoveAbsJ [[0.0,0.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v50,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 3: Esperar 1.0 segundos
        WaitTime 1.0;

        ! Paso 4: Mover base de 0.0° a 45.0°
        MoveAbsJ [[45.0,0.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v50,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 5: Esperar 2.0 segundos
        WaitTime 2.0;

        ! Paso 6: Mover hombro de 0.0° a 60.0°
        MoveAbsJ [[45.0,60.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v150,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 7: Esperar 2.0 segundos
        WaitTime 2.0;

        ! Paso 8: Mover base de 45.0° a 90.0°
        MoveAbsJ [[90.0,60.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v150,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 9: Mover hombro de 60.0° a 30.0°
        MoveAbsJ [[90.0,30.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v150,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 10: Esperar 2.0 segundos
        WaitTime 2.0;

        ! Paso 11: Mover base de 90.0° a 0.0°
        MoveAbsJ [[0.0,30.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v150,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 12: Mover hombro de 30.0° a 0.0°
        MoveAbsJ [[0.0,0.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v150,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 13: Mover codo de 0.0° a 0.0°
        MoveAbsJ [[0.0,0.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v150,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 14: Esperar 1.0 segundos
        WaitTime 1.0;

        ! === FIN DE SECUENCIA ===
        ! Total de pasos ejecutados: 14
        
    ENDPROC
ENDMODULE
