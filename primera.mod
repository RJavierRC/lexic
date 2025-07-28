%%%
  VERSION:1
  LANGUAGE:ENGLISH
%%%
MODULE MOD_MainProgram

    ! -------------------------------
    ! Programa generado automáticamente desde sintaxis robótica
    ! Robot: r1
    ! Fecha: 28/07/2025 12:22:54
    ! Movimientos secuenciales: 3 pasos
    ! -------------------------------

    ! Tool variables: 
    PERS tooldata RobotiQ2F85Gripper(FullyClosed) := [TRUE,[[0.000,0.000,130.000],[1.00000000,0.00000000,0.00000000,0.00000000]],[1,[0,0,20],[1,0,0,0],0,0,0.005]];

    ! Reference variables:
    PERS wobjdata Frame2 := [FALSE, TRUE, "", [[0,0,0],[1,0,0,0]],[[-140.437,-738.971,5.234],[1.00000000,0.00000000,0.00000000,0.00000000]]];

    PROC Main()
        ConfJ \On;
        ConfL \Off;
        
        ! Program generated from Robot syntax on 28/07/2025 12:22:54
        ! Robot: r1
        ! Secuencia de 3 movimientos
        
        ! === INICIO DE SECUENCIA DE MOVIMIENTOS ===
        
        ! Paso 1: Mover base de 0.0° a 45.0°
        MoveAbsJ [[45.0,0.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v150,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! Paso 2: Esperar 1.0 segundos
        WaitTime 1.0;

        ! Paso 3: Mover base de 45.0° a 0.0°
        MoveAbsJ [[0.0,0.0,0.0,0.0,0.0,0.0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v150,z5,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;

        ! === FIN DE SECUENCIA ===
        ! Total de pasos ejecutados: 3
        
    ENDPROC
ENDMODULE
