%%%
  VERSION:1
  LANGUAGE:ENGLISH
%%%
MODULE MainModule

    ! ========================================
    ! PROGRAMA SIMPLE CORRECTO - RECOGER BOTELLA
    ! Sintaxis BÁSICA y CORRECTA para MoveAbsJ
    ! ========================================

    ! Definición de herramienta simple
    PERS tooldata tGripper := [TRUE,[[0,0,130],[1,0,0,0]],[1,[0,0,20],[1,0,0,0],0,0,0.005]];

    PROC Main()
        ! Configuración inicial
        ConfJ \On;
        ConfL \Off;
        
        ! ===== PROGRAMA PRINCIPAL =====
        TPWrite "🤖 INICIANDO RECOGIDA DE BOTELLA";
        
        ! 1. POSICIÓN INICIAL (VELOCIDAD NORMAL v150)
        TPWrite "📍 Yendo a posición inicial...";
        MoveAbsJ [[0,20,-45,0,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]],v150,z5,tGripper;
        WaitTime 1.5;
        
        ! 2. APROXIMARSE A BOTELLA (VELOCIDAD LENTA v75)
        TPWrite "🎯 Aproximándose a la botella...";
        MoveAbsJ [[45,40,-60,0,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]],v75,z5,tGripper;
        WaitTime 2.0;
        
        ! 3. BAJAR PARA AGARRAR (VELOCIDAD MUY LENTA v25)
        TPWrite "⬇️ Bajando para agarrar...";
        MoveAbsJ [[45,55,-85,0,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]],v25,z1,tGripper;
        WaitTime 3.0;
        
        ! 4. CERRAR GRIPPER (cambiar eje 6 a -70)
        TPWrite "🤏 Cerrando gripper...";
        MoveAbsJ [[45,55,-85,0,0,-70],[9E9,9E9,9E9,9E9,9E9,9E9]],v25,z1,tGripper;
        WaitTime 2.0;
        
        ! 5. LEVANTAR BOTELLA (VELOCIDAD LENTA v75)
        TPWrite "⬆️ Levantando botella...";
        MoveAbsJ [[45,40,-60,0,0,-70],[9E9,9E9,9E9,9E9,9E9,9E9]],v75,z5,tGripper;
        WaitTime 1.5;
        
        ! 6. TRANSPORTAR A DESTINO (VELOCIDAD RÁPIDA v400)
        TPWrite "🚀 Transportando a destino...";
        MoveAbsJ [[-60,40,-60,45,0,-70],[9E9,9E9,9E9,9E9,9E9,9E9]],v400,z10,tGripper;
        WaitTime 1.0;
        
        ! 7. COLOCAR BOTELLA (VELOCIDAD MUY LENTA v25)
        TPWrite "📦 Colocando botella...";
        MoveAbsJ [[-60,55,-85,45,0,-70],[9E9,9E9,9E9,9E9,9E9,9E9]],v25,z1,tGripper;
        WaitTime 2.0;
        
        ! 8. ABRIR GRIPPER (cambiar eje 6 a 0)
        TPWrite "✋ Abriendo gripper...";
        MoveAbsJ [[-60,55,-85,45,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]],v25,z1,tGripper;
        WaitTime 1.5;
        
        ! 9. ALEJARSE (VELOCIDAD NORMAL v150)
        TPWrite "↩️ Alejándose...";
        MoveAbsJ [[-60,40,-60,45,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]],v150,z5,tGripper;
        WaitTime 1.0;
        
        ! 10. REGRESAR A INICIAL (VELOCIDAD RÁPIDA v400)
        TPWrite "🏠 Regresando a posición inicial...";
        MoveAbsJ [[0,20,-45,0,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]],v400,z10,tGripper;
        WaitTime 2.0;
        
        TPWrite "✅ MISIÓN COMPLETADA - BOTELLA RECOGIDA";
        
    ENDPROC

ENDMODULE