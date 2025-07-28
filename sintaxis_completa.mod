%%%
  VERSION:1
  LANGUAGE:ENGLISH
%%%
MODULE MOD_MainProgram

    ! -------------------------------
    ! Programa generado automáticamente desde sintaxis robótica
    ! Robot: brazo_avanzado
    ! Fecha: 27/07/2025 21:51:17
    ! Movimientos secuenciales: 61 pasos
    ! -------------------------------

    ! Tool variables: 
    PERS tooldata RobotiQ2F85Gripper(FullyClosed) := [TRUE,[[0.000,0.000,130.000],[1.00000000,0.00000000,0.00000000,0.00000000]],[1,[0,0,20],[1,0,0,0],0,0,0.005]];

    ! Reference variables:
    PERS wobjdata Frame2 := [FALSE, TRUE, "", [[0,0,0],[1,0,0,0]],[[-140.437,-738.971,5.234],[1.00000000,0.00000000,0.00000000,0.00000000]]];

    PROC Main()
        ConfJ \On;
        ConfL \Off;
        
        ! Program generated from Robot syntax on 27/07/2025 21:51:17
        ! Robot: brazo_avanzado
        ! Secuencia de 61 movimientos
        
        ! === INICIO DE SECUENCIA DE MOVIMIENTOS ===
        
        ! Paso 1: Mover base de 0.0° a 0.0°
        MoveAbsJ [[0.0,0.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v150,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 2: Mover hombro de 0.0° a 0.0°
        MoveAbsJ [[0.0,0.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v150,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 3: Mover codo de 0.0° a 0.0°
        MoveAbsJ [[0.0,0.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v150,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 4: Mover muneca de 0.0° a 0.0°
        MoveAbsJ [[0.0,0.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v150,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 5: Mover garra de 0.0° a 0.0°
        MoveAbsJ [[0.0,0.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v150,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 6: Esperar 2.0 segundos
        WaitTime 2.0;

        ! Paso 7: Mover base de 0.0° a 180.0°
        MoveAbsJ [[180.0,0.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v75,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 8: Esperar 3.0 segundos
        WaitTime 3.0;

        ! Paso 9: Esperar 3.0 segundos
        WaitTime 3.0;

        ! Paso 10: Mover base de 180.0° a 0.0°
        MoveAbsJ [[0.0,0.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v75,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 11: Esperar 2.0 segundos
        WaitTime 2.0;

        ! Paso 12: Mover base de 0.0° a 46.0°
        MoveAbsJ [[46.0,0.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 13: Esperar 1.0 segundos
        WaitTime 1.0;

        ! Paso 14: Mover hombro de 0.0° a 93.0°
        MoveAbsJ [[46.0,93.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 15: Esperar 2.0 segundos
        WaitTime 2.0;

        ! Paso 16: Esperar 2.0 segundos
        WaitTime 2.0;

        ! Paso 17: Mover hombro de 93.0° a 0.0°
        MoveAbsJ [[46.0,0.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 18: Mover base de 46.0° a 0.0°
        MoveAbsJ [[0.0,0.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 19: Esperar 2.0 segundos
        WaitTime 2.0;

        ! Paso 20: Esperar 1.0 segundos
        WaitTime 1.0;

        ! Paso 21: Esperar 3.0 segundos
        WaitTime 3.0;

        ! Paso 22: Mover codo de 0.0° a 50.0°
        MoveAbsJ [[0.0,0.0,-50.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v50,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 23: Esperar 3.0 segundos
        WaitTime 3.0;

        ! Paso 24: Mover codo de 50.0° a 0.0°
        MoveAbsJ [[0.0,0.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v50,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 25: Mover base de 0.0° a 0.0°
        MoveAbsJ [[0.0,0.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v50,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 26: Esperar 2.0 segundos
        WaitTime 2.0;

        ! Paso 27: Mover base de 0.0° a 46.0°
        MoveAbsJ [[46.0,0.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v125,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 28: Esperar 1.0 segundos
        WaitTime 1.0;

        ! Paso 29: Esperar 2.0 segundos
        WaitTime 2.0;

        ! Paso 30: Mover muneca de 0.0° a 200.0°
        MoveAbsJ [[46.0,0.0,0.0,200.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v125,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 31: Esperar 2.0 segundos
        WaitTime 2.0;

        ! Paso 32: Mover muneca de 200.0° a 0.0°
        MoveAbsJ [[46.0,0.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v125,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 33: Mover base de 46.0° a 0.0°
        MoveAbsJ [[0.0,0.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v125,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 34: Esperar 2.0 segundos
        WaitTime 2.0;

        ! Paso 35: Mover base de 0.0° a 46.0°
        MoveAbsJ [[46.0,0.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v75,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 36: Esperar 1.0 segundos
        WaitTime 1.0;

        ! Paso 37: Esperar 2.0 segundos
        WaitTime 2.0;

        ! Paso 38: Esperar 2.0 segundos
        WaitTime 2.0;

        ! Paso 39: Mover base de 46.0° a 0.0°
        MoveAbsJ [[0.0,0.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v75,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 40: Esperar 2.0 segundos
        WaitTime 2.0;

        ! Paso 41: Esperar 1.0 segundos
        WaitTime 1.0;

        ! Paso 42: Mover garra de 0.0° a 400.0°
        MoveAbsJ [[0.0,0.0,0.0,0.0,0.0,400.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v200,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 43: Esperar 2.0 segundos
        WaitTime 2.0;

        ! Paso 44: Mover garra de 400.0° a 10.0°
        MoveAbsJ [[0.0,0.0,0.0,0.0,0.0,10.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v200,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 45: Esperar 1.0 segundos
        WaitTime 1.0;

        ! Paso 46: Mover garra de 10.0° a 0.0°
        MoveAbsJ [[0.0,0.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v200,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 47: Mover base de 0.0° a 0.0°
        MoveAbsJ [[0.0,0.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v200,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 48: Esperar 2.0 segundos
        WaitTime 2.0;

        ! Paso 49: Mover base de 0.0° a 90.0°
        MoveAbsJ [[90.0,0.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v400,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 50: Mover hombro de 0.0° a 45.0°
        MoveAbsJ [[90.0,45.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v400,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 51: Mover muneca de 0.0° a 90.0°
        MoveAbsJ [[90.0,45.0,0.0,90.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v400,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 52: Mover garra de 0.0° a 180.0°
        MoveAbsJ [[90.0,45.0,0.0,90.0,0.0,180.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v400,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 53: Esperar 2.0 segundos
        WaitTime 2.0;

        ! Paso 54: Mover codo de 0.0° a 45.0°
        MoveAbsJ [[90.0,45.0,-45.0,90.0,0.0,180.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v400,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 55: Esperar 2.0 segundos
        WaitTime 2.0;

        ! Paso 56: Mover base de 90.0° a 0.0°
        MoveAbsJ [[0.0,45.0,-45.0,90.0,0.0,180.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v200,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 57: Mover hombro de 45.0° a 0.0°
        MoveAbsJ [[0.0,0.0,-45.0,90.0,0.0,180.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v200,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 58: Mover codo de 45.0° a 0.0°
        MoveAbsJ [[0.0,0.0,0.0,90.0,0.0,180.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v200,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 59: Mover muneca de 90.0° a 0.0°
        MoveAbsJ [[0.0,0.0,0.0,0.0,0.0,180.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v200,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 60: Mover garra de 180.0° a 0.0°
        MoveAbsJ [[0.0,0.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v200,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 61: Esperar 3.0 segundos
        WaitTime 3.0;

        ! === FIN DE SECUENCIA ===
        ! Total de pasos ejecutados: 61
        
    ENDPROC
ENDMODULE
