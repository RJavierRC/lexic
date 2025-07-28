%%%
  VERSION:1
  LANGUAGE:ENGLISH
%%%
MODULE MOD_R1Program
    ! -------------------------------
    ! Programa generado automáticamente desde sintaxis robótica
    ! Robot: r1
    ! Fecha: 25/07/2025 13:40:34
    ! Movimientos seguros: 30 pasos
    ! Límites aplicados para ABB IRB140-6/0.8
    ! -------------------------------
    
    ! Tool variables: 
    PERS tooldata RobotiQ2F85Gripper(FullyClosed) := [TRUE,[[45,0,0,0,0,0]],[1,[0,0,20],[1,0,0,0],0,0,0.005]];
    
    ! Reference variables:
    PERS wobjdata Frame2 := [FALSE, TRUE, "", [[45,0,0,0,0,0]],[[45,0,0,0,0,0]]];
    
    PROC Main()
        ConfJ \On;
        ConfL \Off;
        ! Program generated from Robot syntax on 25/07/2025 13:40:34
        ! Robot: r1 - Secuencia segura de 30 movimientos
        
        ! === POSICIÓN INICIAL SEGURA ===
        MoveAbsJ [[0,0,0,0,0,0]],v50,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;
        
        ! === INICIO DE SECUENCIA DE MOVIMIENTOS SEGUROS ===
        
        ! Paso 1: Mover base de 0.0° a 0.0°
        MoveAbsJ [[0.0,0.0,0.0,0.0,0.0,0]],v50,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 2: Mover hombro de 0.0° a 90.0°
        MoveAbsJ [[0.0,90.0,0.0,0.0,0.0,0]],v50,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 3: Mover codo de 0.0° a 45.0° (limitado desde 90.0°)
        MoveAbsJ [[0.0,90.0,45.0,0.0,0.0,0]],v50,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 4: Mover garra de 0.0° a 90.0°
        MoveAbsJ [[0.0,90.0,45.0,0.0,90.0,0]],v50,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 5: Esperar 2.0 segundos
        WaitTime 2.0;

        ! Paso 6: Mover base de 0.0° a 45.0°
        MoveAbsJ [[45.0,90.0,45.0,0.0,90.0,0]],v100,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 7: Mover hombro de 90.0° a 100.0° (limitado desde 120.0°)
        MoveAbsJ [[45.0,100.0,45.0,0.0,90.0,0]],v100,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 8: Mover codo de 45.0° a 45.0° (limitado desde 90.0°)
        MoveAbsJ [[45.0,100.0,45.0,0.0,90.0,0]],v100,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 9: Esperar 1.0 segundos
        WaitTime 1.0;

        ! Paso 10: Mover codo de 45.0° a 45.0°
        MoveAbsJ [[45.0,100.0,45.0,0.0,90.0,0]],v50,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 11: Esperar 1.0 segundos
        WaitTime 1.0;

        ! Paso 12: Mover garra de 90.0° a 20.0°
        MoveAbsJ [[45.0,100.0,45.0,0.0,20.0,0]],v50,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 13: Esperar 1.0 segundos
        WaitTime 1.0;

        ! Paso 14: Mover codo de 45.0° a 45.0° (limitado desde 90.0°)
        MoveAbsJ [[45.0,100.0,45.0,0.0,20.0,0]],v50,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 15: Mover hombro de 100.0° a 90.0°
        MoveAbsJ [[45.0,90.0,45.0,0.0,20.0,0]],v50,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 16: Esperar 1.0 segundos
        WaitTime 1.0;

        ! Paso 17: Mover base de 45.0° a 170.0° (limitado desde 180.0°)
        MoveAbsJ [[170.0,90.0,45.0,0.0,20.0,0]],v200,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 18: Mover hombro de 90.0° a 100.0°
        MoveAbsJ [[170.0,100.0,45.0,0.0,20.0,0]],v200,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 19: Esperar 2.0 segundos
        WaitTime 2.0;

        ! Paso 20: Mover codo de 45.0° a 45.0° (limitado desde 60.0°)
        MoveAbsJ [[170.0,100.0,45.0,0.0,20.0,0]],v50,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 21: Esperar 1.0 segundos
        WaitTime 1.0;

        ! Paso 22: Mover garra de 20.0° a 90.0°
        MoveAbsJ [[170.0,100.0,45.0,0.0,90.0,0]],v50,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 23: Esperar 1.0 segundos
        WaitTime 1.0;

        ! Paso 24: Mover codo de 45.0° a 45.0° (limitado desde 90.0°)
        MoveAbsJ [[170.0,100.0,45.0,0.0,90.0,0]],v50,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 25: Mover hombro de 100.0° a 90.0°
        MoveAbsJ [[170.0,90.0,45.0,0.0,90.0,0]],v50,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 26: Esperar 1.0 segundos
        WaitTime 1.0;

        ! Paso 27: Mover base de 170.0° a 0.0°
        MoveAbsJ [[0.0,90.0,45.0,0.0,90.0,0]],v500,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 28: Mover hombro de 90.0° a 90.0°
        MoveAbsJ [[0.0,90.0,45.0,0.0,90.0,0]],v500,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 29: Mover codo de 45.0° a 45.0° (limitado desde 90.0°)
        MoveAbsJ [[0.0,90.0,45.0,0.0,90.0,0]],v500,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 30: Esperar 2.0 segundos
        WaitTime 2.0;

        ! === REGRESAR A POSICIÓN INICIAL SEGURA ===
        MoveAbsJ [[0,0,0,0,0,0]],v50,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;
        
        ! === FIN DE SECUENCIA SEGURA ===
        ! Total de pasos ejecutados: 30
        
    ENDPROC
ENDMODULE
