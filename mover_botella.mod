%%%
  VERSION:1
  LANGUAGE:ENGLISH
%%%
MODULE MOD_MainProgram

    ! -------------------------------
    ! Programa generado automáticamente desde sintaxis robótica
    ! Robot: brazo_industrial
    ! Fecha: 27/07/2025 19:36:33
    ! Movimientos secuenciales: 43 pasos
    ! -------------------------------

    ! Tool variables: 
    PERS tooldata RobotiQ2F85Gripper(FullyClosed) := [TRUE,[[0.000,0.000,130.000],[1.00000000,0.00000000,0.00000000,0.00000000]],[1,[0,0,20],[1,0,0,0],0,0,0.005]];

    ! Reference variables:
    PERS wobjdata Frame2 := [FALSE, TRUE, "", [[0,0,0],[1,0,0,0]],[[-140.437,-738.971,5.234],[1.00000000,0.00000000,0.00000000,0.00000000]]];

    PROC Main()
        ConfJ \On;
        ConfL \Off;
        
        ! Program generated from Robot syntax on 27/07/2025 19:36:33
        ! Robot: brazo_industrial
        ! Secuencia de 43 movimientos
        
        ! === INICIO DE SECUENCIA DE MOVIMIENTOS ===
        
        ! Paso 1: Mover base de 0.0° a 0.0°
        MoveAbsJ [[0.0,0.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v75,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 2: Mover hombro de 0.0° a 20.0°
        MoveAbsJ [[0.0,20.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v75,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 3: Mover codo de 0.0° a 45.0°
        MoveAbsJ [[0.0,20.0,-45.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v75,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 4: Mover muneca de 0.0° a 0.0°
        MoveAbsJ [[0.0,20.0,-45.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v75,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 5: Mover garra de 90.0° a 90.0°
        MoveAbsJ [[0.0,20.0,-45.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v75,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 6: Esperar 2.0 segundos
        WaitTime 2.0;

        ! Paso 7: Mover base de 0.0° a 45.0°
        MoveAbsJ [[45.0,20.0,-45.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v25,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 8: Esperar 3.0 segundos
        WaitTime 3.0;

        ! Paso 9: Mover hombro de 20.0° a 40.0°
        MoveAbsJ [[45.0,40.0,-45.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v25,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 10: Esperar 2.0 segundos
        WaitTime 2.0;

        ! Paso 11: Mover codo de 45.0° a 70.0°
        MoveAbsJ [[45.0,40.0,-70.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v25,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 12: Esperar 2.0 segundos
        WaitTime 2.0;

        ! Paso 13: Mover hombro de 40.0° a 60.0°
        MoveAbsJ [[45.0,60.0,-70.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v25,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 14: Esperar 1.0 segundos
        WaitTime 1.0;

        ! Paso 15: Mover codo de 70.0° a 90.0°
        MoveAbsJ [[45.0,60.0,-90.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v25,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 16: Esperar 1.0 segundos
        WaitTime 1.0;

        ! Paso 17: Mover garra de 90.0° a 25.0°
        MoveAbsJ [[45.0,60.0,-90.0,0.0,0.0,-75.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v25,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 18: Esperar 2.0 segundos
        WaitTime 2.0;

        ! Paso 19: Mover codo de 90.0° a 70.0°
        MoveAbsJ [[45.0,60.0,-70.0,0.0,0.0,-75.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v25,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 20: Esperar 1.0 segundos
        WaitTime 1.0;

        ! Paso 21: Mover hombro de 60.0° a 40.0°
        MoveAbsJ [[45.0,40.0,-70.0,0.0,0.0,-75.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v25,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 22: Esperar 1.0 segundos
        WaitTime 1.0;

        ! Paso 23: Esperar 1.0 segundos
        WaitTime 1.0;

        ! Paso 24: Mover hombro de 40.0° a 50.0°
        MoveAbsJ [[45.0,50.0,-70.0,0.0,0.0,-75.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v400,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 25: Esperar 1.0 segundos
        WaitTime 1.0;

        ! Paso 26: Mover muneca de 0.0° a 45.0°
        MoveAbsJ [[45.0,50.0,-70.0,45.0,0.0,-75.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v150,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 27: Esperar 1.0 segundos
        WaitTime 1.0;

        ! Paso 28: Mover hombro de 50.0° a 65.0°
        MoveAbsJ [[45.0,65.0,-70.0,45.0,0.0,-75.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v25,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 29: Esperar 1.0 segundos
        WaitTime 1.0;

        ! Paso 30: Mover codo de 70.0° a 85.0°
        MoveAbsJ [[45.0,65.0,-85.0,45.0,0.0,-75.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v25,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 31: Esperar 1.0 segundos
        WaitTime 1.0;

        ! Paso 32: Mover garra de 25.0° a 90.0°
        MoveAbsJ [[45.0,65.0,-85.0,45.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v25,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 33: Esperar 2.0 segundos
        WaitTime 2.0;

        ! Paso 34: Mover codo de 85.0° a 70.0°
        MoveAbsJ [[45.0,65.0,-70.0,45.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v75,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 35: Esperar 1.0 segundos
        WaitTime 1.0;

        ! Paso 36: Mover hombro de 65.0° a 50.0°
        MoveAbsJ [[45.0,50.0,-70.0,45.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v75,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 37: Esperar 1.0 segundos
        WaitTime 1.0;

        ! Paso 38: Mover base de 45.0° a 0.0°
        MoveAbsJ [[0.0,50.0,-70.0,45.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v400,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 39: Mover hombro de 50.0° a 20.0°
        MoveAbsJ [[0.0,20.0,-70.0,45.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v400,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 40: Mover codo de 70.0° a 45.0°
        MoveAbsJ [[0.0,20.0,-45.0,45.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v400,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 41: Mover muneca de 45.0° a 0.0°
        MoveAbsJ [[0.0,20.0,-45.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v400,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 42: Mover garra de 90.0° a 90.0°
        MoveAbsJ [[0.0,20.0,-45.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v400,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 43: Esperar 3.0 segundos
        WaitTime 3.0;

        ! === FIN DE SECUENCIA ===
        ! Total de pasos ejecutados: 43
        
    ENDPROC
ENDMODULE
