%%%
  VERSION:1
  LANGUAGE:ENGLISH
%%%
MODULE MOD_FixedProgram

    ! -------------------------------
    ! Programa CORREGIDO - Mapeo correcto de articulaciones
    ! Robot: r1
    ! Fecha: 27/07/2025 19:08:44
    ! Movimientos: 0 pasos
    ! -------------------------------

    ! Tool variables: 
    PERS tooldata RobotiQ2F85Gripper := [TRUE,[[0.000,0.000,130.000],[1.00000000,0.00000000,0.00000000,0.00000000]],[1,[0,0,20],[1,0,0,0],0,0,0.005]];

    ! Reference variables:
    PERS wobjdata Frame2 := [FALSE, TRUE, "", [[0,0,0],[1,0,0,0]],[[-140.437,-738.971,5.234],[1.00000000,0.00000000,0.00000000,0.00000000]]];

    PROC Main()
        ConfJ \On;
        ConfL \Off;
        
        ! Programa generado 27/07/2025 19:08:44
        ! Robot: r1
        ! MAPEO CORRECTO:
        ! base → Eje 1 (rotación horizontal)
        ! hombro → Eje 2 (brazo inferior arriba/abajo)  
        ! codo → Eje 3 (codo arriba/abajo)
        ! muneca → Eje 4 (rotación antebrazo)
        ! garra → Eje 6 (apertura/cierre gripper)
        
        ! Posición inicial
        MoveAbsJ [[0,0,0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v50,z1,RobotiQ2F85Gripper \WObj:=Frame2;
        
        ! === PROGRAMA TERMINADO ===
        ! Total pasos: 0
        
    ENDPROC
ENDMODULE
