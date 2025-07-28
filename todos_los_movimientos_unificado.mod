%%%
  VERSION:1
  LANGUAGE:ENGLISH
%%%
MODULE MainModule

    ! ========================================
    ! DEMOSTRACIÓN COMPLETA DE TODOS LOS EJES
    ! Basado en análisis de archivos individuales
    ! Cada eje se muestra en su rango completo
    ! ========================================

    ! Definición de herramienta
    PERS tooldata RobotiQ2F85Gripper := [TRUE,[[0,0,130],[1,0,0,0]],[1,[0,0,20],[1,0,0,0],0,0,0.005]];
    PERS wobjdata Frame2 := [FALSE, TRUE, "", [[0,0,0],[1,0,0,0]],[[-140.437,-738.971,5.234],[1,0,0,0]]];

    PROC Main()
        ConfJ \On;
        ConfL \Off;
        
        ! ===== DEMOSTRACIÓN COMPLETA DE TODOS LOS EJES =====
        TPWrite "🤖 INICIANDO DEMOSTRACIÓN COMPLETA";
        TPWrite "📋 BASADA EN ARCHIVOS INDIVIDUALES DE MOVIMIENTOS";
        
        ! POSICIÓN INICIAL
        TPWrite "🏠 Posición inicial";
        MoveAbsJ [[0,0,0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v200,z5,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 2.0;
        
        ! ===== EJE 1 - BASE (Rotación horizontal) =====
        TPWrite "🔄 DEMOSTRANDO EJE 1 - BASE (rotación horizontal)";
        
        ! Giro a 180° (como en base.mod)
        TPWrite "➡️ Base girando a 180°";
        MoveAbsJ [[180,0,0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v150,z5,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 2.0;
        
        ! Giro a -180° (como en base.mod)
        TPWrite "⬅️ Base girando a -180°";
        MoveAbsJ [[-180,0,0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v150,z5,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 2.0;
        
        ! Regreso a 0°
        TPWrite "🔄 Base regresando a 0°";
        MoveAbsJ [[0,0,0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v150,z5,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 1.5;
        
        ! ===== EJE 2 - HOMBRO/BRAZO (Elevación) =====
        TPWrite "💪 DEMOSTRANDO EJE 2 - HOMBRO (elevación arriba/abajo)";
        
        ! Preparar base (como en brazo.mod)
        TPWrite "🔄 Preparando base a 46.47°";
        MoveAbsJ [[46.47,0,0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z5,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 1.0;
        
        ! Hombro hacia arriba (como en brazo.mod)
        TPWrite "⬆️ Hombro subiendo a 93.09°";
        MoveAbsJ [[46.46,93.09,0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v75,z5,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 2.5;
        
        ! Hombro hacia abajo (como en brazo.mod)
        TPWrite "⬇️ Hombro bajando a -83°";
        MoveAbsJ [[46.46,-83,0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v75,z5,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 2.5;
        
        ! Regreso
        TPWrite "↩️ Hombro regresando a posición";
        MoveAbsJ [[0,0,0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z5,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 1.5;
        
        ! ===== EJE 3 - CODO (Articulación intermedia) =====
        TPWrite "⚙️ DEMOSTRANDO EJE 3 - CODO (articulación intermedia)";
        
        ! Preparar base (como en codo.mod)
        TPWrite "🔄 Preparando base a -73.18°";
        MoveAbsJ [[-73.18,0,0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z5,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 1.0;
        
        ! Codo al límite inferior (como en codo.mod)
        TPWrite "⬇️ Codo al límite inferior -230°";
        MoveAbsJ [[-73.17,0,-230,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v50,z1,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 3.0;
        
        ! Codo al límite superior (como en codo.mod)
        TPWrite "⬆️ Codo al límite superior +50°";
        MoveAbsJ [[-73.17,0,50,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v50,z1,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 3.0;
        
        ! Regreso
        TPWrite "↩️ Codo regresando a posición";
        MoveAbsJ [[0,0,0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z5,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 1.5;
        
        ! ===== EJE 4 - MUÑECA/ANTEBRAZO (Rotación) =====
        TPWrite "🔧 DEMOSTRANDO EJE 4 - MUÑECA (rotación antebrazo)";
        
        ! Preparar base (como en muniek.mod)
        TPWrite "🔄 Preparando base a 46.46°";
        MoveAbsJ [[46.46,0,0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z5,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 1.0;
        
        ! Muñeca a -200° (como en muniek.mod)
        TPWrite "🔄 Muñeca girando a -200°";
        MoveAbsJ [[46.46,0,0,-200,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z5,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 2.0;
        
        ! Muñeca a +200° (como en muniek.mod)
        TPWrite "🔄 Muñeca girando a +200°";
        MoveAbsJ [[46.46,0,0,200,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z5,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 2.0;
        
        ! Regreso
        TPWrite "↩️ Muñeca regresando a posición";
        MoveAbsJ [[0,0,0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z5,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 1.5;
        
        ! ===== EJE 5 - GARRA BASE (Inclinación) =====
        TPWrite "🤏 DEMOSTRANDO EJE 5 - GARRA BASE (inclinación)";
        
        ! Preparar base (como en garrabase.mod)
        TPWrite "🔄 Preparando base a 46.47°";
        MoveAbsJ [[46.47,0,0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z5,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 1.0;
        
        ! Eje 5 a -120° (como en garrabase.mod)
        TPWrite "⬇️ Eje 5 inclinando a -120°";
        MoveAbsJ [[46.47,0,0,0,-120,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v75,z5,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 2.0;
        
        ! Eje 5 a +120° (como en garrabase.mod)
        TPWrite "⬆️ Eje 5 inclinando a +120°";
        MoveAbsJ [[46.47,0,0,0,120,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v75,z5,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 2.0;
        
        ! Regreso
        TPWrite "↩️ Eje 5 regresando a posición";
        MoveAbsJ [[0,0,0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z5,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 1.5;
        
        ! ===== EJE 6 - GARRA GIRO (Rotación final) =====
        TPWrite "🌀 DEMOSTRANDO EJE 6 - GARRA GIRO (rotación final)";
        
        ! Preparar base (como en garragiro.mod)
        TPWrite "🔄 Preparando base a -73.18°";
        MoveAbsJ [[-73.18,0,0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z5,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 1.0;
        
        ! Eje 6 giro completo a 400° (como en garragiro.mod)
        TPWrite "🌀 Eje 6 giro COMPLETO a 400°";
        MoveAbsJ [[-73.18,0,0,0,0,400],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v200,z10,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 2.0;
        
        ! Eje 6 posición intermedia (como en garragiro.mod)
        TPWrite "🔄 Eje 6 a posición 10.68°";
        MoveAbsJ [[-73.18,0,0,0,0,10.68],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v100,z5,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 1.5;
        
        ! ===== REGRESO FINAL =====
        TPWrite "🏠 REGRESO A POSICIÓN INICIAL";
        MoveAbsJ [[0,0,0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v200,z5,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 2.0;
        
        ! ===== SECUENCIA FINAL ESPECTACULAR =====
        TPWrite "🎪 SECUENCIA FINAL - TODOS LOS EJES TRABAJANDO";
        
        ! Movimiento coordinado de TODOS los ejes
        TPWrite "🤸 Movimiento coordinado - TODOS los ejes";
        MoveAbsJ [[90,45,-120,90,-60,180],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v300,z10,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 2.0;
        
        ! Movimiento opuesto coordinado
        TPWrite "🤸 Movimiento opuesto - TODOS los ejes";
        MoveAbsJ [[-90,-45,45,-90,60,-180],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v300,z10,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 2.0;
        
        ! Regreso final
        TPWrite "🎉 DEMOSTRACIÓN COMPLETADA";
        MoveAbsJ [[0,0,0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v200,z5,RobotiQ2F85Gripper \WObj:=Frame2;
        WaitTime 3.0;
        
        TPWrite "✅ TODOS LOS 6 EJES DEMOSTRADOS COMPLETAMENTE";
        TPWrite "🏆 BASADO EN ANÁLISIS DE ARCHIVOS INDIVIDUALES";
        
    ENDPROC

ENDMODULE