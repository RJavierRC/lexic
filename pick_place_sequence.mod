%%%
  VERSION:1
  LANGUAGE:ENGLISH
%%%
MODULE MOD_MainProgram

    ! -------------------------------
    ! Programa generado automáticamente desde sintaxis robótica
    ! Robot: r1
    ! Fecha: 25/07/2025 13:28:01
    ! Movimientos secuenciales: 30 pasos
    ! -------------------------------

    ! Tool variables: 
    PERS tooldata RobotiQ2F85Gripper(FullyClosed) := [TRUE,[[0.000,0.000,130.000],[1.00000000,0.00000000,0.00000000,0.00000000]],[1,[0,0,20],[1,0,0,0],0,0,0.005]];

    ! Reference variables:
    PERS wobjdata Frame2 := [FALSE, TRUE, "", [[0,0,0],[1,0,0,0]],[[-140.437,-738.971,5.234],[1.00000000,0.00000000,0.00000000,0.00000000]]];

    PROC Main()
        ConfJ \On;
        ConfL \Off;
        
        ! Program generated from Robot syntax on 25/07/2025 13:28:01
        ! Robot: r1
        ! Secuencia de 30 movimientos
        
        ! === INICIO DE SECUENCIA DE MOVIMIENTOS ===
        
        ! Paso 1: Mover base de 0.0° a 0.0°
        MoveAbsJ [[0.000000,0.000000,0.000000,0.000000,90.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v50,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 2: Mover hombro de 0.0° a 90.0°
        MoveAbsJ [[0.000000,90.000000,0.000000,0.000000,90.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v50,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 3: Mover codo de 0.0° a 90.0°
        MoveAbsJ [[0.000000,90.000000,90.000000,0.000000,90.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v50,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 4: Mover garra de 90.0° a 90.0°
        MoveAbsJ [[0.000000,90.000000,90.000000,0.000000,90.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v50,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 5: Esperar 2.0 segundos
        WaitTime 2.0;

        ! Paso 6: Mover base de 0.0° a 45.0°
        MoveAbsJ [[45.000000,90.000000,90.000000,0.000000,90.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 7: Mover hombro de 90.0° a 120.0°
        MoveAbsJ [[45.000000,120.000000,90.000000,0.000000,90.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 8: Mover codo de 90.0° a 90.0°
        MoveAbsJ [[45.000000,120.000000,90.000000,0.000000,90.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 9: Esperar 1.0 segundos
        WaitTime 1.0;

        ! Paso 10: Mover codo de 90.0° a 45.0°
        MoveAbsJ [[45.000000,120.000000,45.000000,0.000000,90.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v50,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 11: Esperar 1.0 segundos
        WaitTime 1.0;

        ! Paso 12: Mover garra de 90.0° a 20.0°
        MoveAbsJ [[45.000000,120.000000,45.000000,0.000000,-20.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v50,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 13: Esperar 1.0 segundos
        WaitTime 1.0;

        ! Paso 14: Mover codo de 45.0° a 90.0°
        MoveAbsJ [[45.000000,120.000000,90.000000,0.000000,-20.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v50,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 15: Mover hombro de 120.0° a 90.0°
        MoveAbsJ [[45.000000,90.000000,90.000000,0.000000,-20.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v50,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 16: Esperar 1.0 segundos
        WaitTime 1.0;

        ! Paso 17: Mover base de 45.0° a 180.0°
        MoveAbsJ [[180.000000,90.000000,90.000000,0.000000,-20.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v200,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 18: Mover hombro de 90.0° a 100.0°
        MoveAbsJ [[180.000000,100.000000,90.000000,0.000000,-20.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v200,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 19: Esperar 2.0 segundos
        WaitTime 2.0;

        ! Paso 20: Mover codo de 90.0° a 60.0°
        MoveAbsJ [[180.000000,100.000000,60.000000,0.000000,-20.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v50,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 21: Esperar 1.0 segundos
        WaitTime 1.0;

        ! Paso 22: Mover garra de 20.0° a 90.0°
        MoveAbsJ [[180.000000,100.000000,60.000000,0.000000,90.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v50,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 23: Esperar 1.0 segundos
        WaitTime 1.0;

        ! Paso 24: Mover codo de 60.0° a 90.0°
        MoveAbsJ [[180.000000,100.000000,90.000000,0.000000,90.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v50,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 25: Mover hombro de 100.0° a 90.0°
        MoveAbsJ [[180.000000,90.000000,90.000000,0.000000,90.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v50,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 26: Esperar 1.0 segundos
        WaitTime 1.0;

        ! Paso 27: Mover base de 180.0° a 0.0°
        MoveAbsJ [[0.000000,90.000000,90.000000,0.000000,90.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v500,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 28: Mover hombro de 90.0° a 90.0°
        MoveAbsJ [[0.000000,90.000000,90.000000,0.000000,90.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v500,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 29: Mover codo de 90.0° a 90.0°
        MoveAbsJ [[0.000000,90.000000,90.000000,0.000000,90.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v500,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 30: Esperar 2.0 segundos
        WaitTime 2.0;

        ! === FIN DE SECUENCIA ===
        ! Total de pasos ejecutados: 30
        
    ENDPROC
ENDMODULE
