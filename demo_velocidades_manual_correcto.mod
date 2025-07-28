%%%
  VERSION:1
  LANGUAGE:ENGLISH
%%%
MODULE MOD_DemoVelocidades

    ! Programa CORREGIDO - Mapeo correcto de articulaciones ABB IRB140
    ! Fecha: 27/07/2025 19:15:00
    ! MAPEO CORRECTO:
    ! base → Eje 1 (rotación horizontal)
    ! hombro → Eje 2 (brazo inferior arriba/abajo)  
    ! codo → Eje 3 (codo arriba/abajo)
    ! muneca → Eje 4 (rotación antebrazo)
    ! Eje 5 → 0 (no usado)
    ! garra → Eje 6 (apertura/cierre gripper)

    ! Tool variables: 
    PERS tooldata RobotiQ2F85Gripper := [TRUE,[[0.000,0.000,130.000],[1.00000000,0.00000000,0.00000000,0.00000000]],[1,[0,0,20],[1,0,0,0],0,0,0.005]];

    ! Reference variables:
    PERS wobjdata Frame2 := [FALSE, TRUE, "", [[0,0,0],[1,0,0,0]],[[-140.437,-738.971,5.234],[1.00000000,0.00000000,0.00000000,0.00000000]]];

    PROC Main()
        ConfJ \On;
        ConfL \Off;
        
        ! === DEMO DE VELOCIDADES CORREGIDO ===
        
        ! Posición inicial (todos los ejes en 0)
        MoveAbsJ [[0,0,0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v50,z1,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 1.0;
        
        ! VELOCIDAD 1 (v50 - MUY LENTA): Mover base a 30°
        MoveAbsJ [[30,0,0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v50,z1,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 3.0;
        
        ! VELOCIDAD 2 (v100 - LENTA): Mover hombro a 45°  
        MoveAbsJ [[30,45,0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z1,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 2.0;
        
        ! VELOCIDAD 3 (v200 - MEDIA): Mover codo a 60°
        MoveAbsJ [[30,45,60,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v200,z1,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 2.0;
        
        ! VELOCIDAD 4 (v500 - RÁPIDA): Mover base a 90°, hombro a 90°
        MoveAbsJ [[90,90,60,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v500,z1,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 1.0;
        
        ! DEMO GARRA (VELOCIDAD LENTA): Cerrar garra (eje 6 a -70°)
        MoveAbsJ [[90,90,60,0,0,-70],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v50,z1,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 2.0;
        
        ! DEMO GARRA: Abrir garra (eje 6 a 0°)
        MoveAbsJ [[90,90,60,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v50,z1,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 2.0;
        
        ! REGRESO RÁPIDO A POSICIÓN INICIAL (v500)
        MoveAbsJ [[0,0,0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v500,z1,RobotiQ2F85Gripper \WObj:=Frame2;
        
        ! === PROGRAMA TERMINADO ===
        
    ENDPROC

ENDMODULE