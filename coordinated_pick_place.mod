%%%
  VERSION:1
  LANGUAGE:ENGLISH
%%%
MODULE MOD_R1Program
    ! -------------------------------
    ! Programa coordinado generado automáticamente
    ! Robot: r1
    ! Fecha: 25/07/2025 14:05:38
    ! Posiciones coordinadas: 10
    ! Sin colisiones internas - Movimientos seguros
    ! -------------------------------
    
    ! Tool variables: 
    PERS tooldata RobotiQ2F85Gripper(FullyClosed) := [TRUE,[[45,0,0,0,0,0]],[1,[0,0,20],[1,0,0,0],0,0,0.005]];
    
    ! Reference variables:
    PERS wobjdata Frame2 := [FALSE, TRUE, "", [[45,0,0,0,0,0]],[[45,0,0,0,0,0]]];
    
    PROC Main()
        ConfJ \On;
        ConfL \Off;
        ! Program generated from Robot syntax on 25/07/2025 14:05:38
        ! Movimientos coordinados seguros para r1
        
        ! === POSICIÓN INICIAL SEGURA ===
        MoveAbsJ [[0,0,0,0,0,0]],v50,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;
        
        ! === SECUENCIA DE MOVIMIENTOS COORDINADOS ===
        
        ! Movimiento 1: Movimiento genérico
        MoveAbsJ [[0.0,70.0,35.0,0.0,90.0,0.0]],v50,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;
        WaitTime 2.0;

        ! Movimiento 2: Movimiento genérico
        MoveAbsJ [[45.0,80.0,35.0,0.0,90.0,0.0]],v100,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;
        WaitTime 1.0;

        ! Movimiento 3: Movimiento genérico
        MoveAbsJ [[45.0,80.0,35.0,0.0,90.0,0.0]],v50,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;
        WaitTime 1.0;

        ! Movimiento 4: Movimiento genérico
        MoveAbsJ [[45.0,80.0,35.0,0.0,20.0,0.0]],v50,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;
        WaitTime 1.0;

        ! Movimiento 5: Movimiento genérico
        MoveAbsJ [[45.0,70.0,35.0,0.0,20.0,0.0]],v50,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;
        WaitTime 1.0;

        ! Movimiento 6: Movimiento genérico
        MoveAbsJ [[170.0,80.0,35.0,0.0,20.0,0.0]],v200,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;
        WaitTime 2.0;

        ! Movimiento 7: Movimiento genérico
        MoveAbsJ [[170.0,80.0,35.0,0.0,20.0,0.0]],v50,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;
        WaitTime 1.0;

        ! Movimiento 8: Movimiento genérico
        MoveAbsJ [[170.0,80.0,35.0,0.0,90.0,0.0]],v50,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;
        WaitTime 1.0;

        ! Movimiento 9: Movimiento genérico
        MoveAbsJ [[170.0,70.0,35.0,0.0,90.0,0.0]],v50,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;
        WaitTime 1.0;

        ! Movimiento 10: Movimiento genérico
        MoveAbsJ [[0.0,70.0,35.0,0.0,90.0,0.0]],v300,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;
        WaitTime 2.0;

        ! === REGRESAR A POSICIÓN INICIAL SEGURA ===
        MoveAbsJ [[0,0,0,0,0,0]],v50,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;
        
        ! === FIN DE SECUENCIA COORDINADA ===
        ! Total de movimientos coordinados: 10
        
    ENDPROC
ENDMODULE
