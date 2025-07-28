%%%
  VERSION:1
  LANGUAGE:ENGLISH
%%%
MODULE MainModule

    ! ========================================
    ! PROGRAMA CON MOVIMIENTOS EXAGERADOS
    ! Pick & Place DRAMÁTICO y VISIBLE
    ! Todos los ángulos trabajando al máximo
    ! ========================================

    ! Definición de herramienta simple
    PERS tooldata tGripper := [TRUE,[[0,0,130],[1,0,0,0]],[1,[0,0,20],[1,0,0,0],0,0,0.005]];

    PROC Main()
        ConfJ \On;
        ConfL \Off;
        
        ! ===== RUTINA PICK & PLACE EXAGERADA =====
        TPWrite "🤖 INICIANDO RUTINA EXAGERADA";
        
        ! 1. POSICIÓN INICIAL MUY ALTA (como un ave) 
        TPWrite "🦅 Posición inicial - ROBOT DESPIERTA";
        MoveAbsJ [[0,10,-30,0,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]],v150,z5,tGripper;
        WaitTime 2.0;
        
        ! 2. GRAN GIRO HACIA LA BOTELLA (base 90°) + PREPARAR BRAZO
        TPWrite "🔄 GRAN GIRO hacia la botella + preparar brazo";
        MoveAbsJ [[90,30,-60,0,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]],v200,z5,tGripper;
        WaitTime 1.5;
        
        ! 3. APROXIMACIÓN ALTA (como helicóptero sobrevolando)
        TPWrite "🚁 Sobrevolando el objetivo";
        MoveAbsJ [[90,60,-90,30,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]],v100,z5,tGripper;
        WaitTime 2.0;
        
        ! 4. DESCENSO DRAMÁTICO (como aterrizar) - TODOS LOS EJES TRABAJAN
        TPWrite "⬇️ DESCENSO DRAMÁTICO - aterrizando";
        MoveAbsJ [[90,80,-120,60,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]],v50,z1,tGripper;
        WaitTime 3.0;
        
        ! 5. POSICIÓN FINAL DE AGARRE (tocando el suelo)
        TPWrite "🎯 POSICIÓN FINAL - tocando suelo";
        MoveAbsJ [[90,85,-130,90,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]],v25,z1,tGripper;
        WaitTime 2.0;
        
        ! 6. CERRAR GARRA (agarre dramático)
        TPWrite "🤏 AGARRE DRAMÁTICO - cerrando garra";
        MoveAbsJ [[90,85,-130,90,0,-80],[9E9,9E9,9E9,9E9,9E9,9E9]],v25,z1,tGripper;
        WaitTime 3.0;
        
        ! 7. DESPEGUE GRADUAL (como grúa levantando)
        TPWrite "🏗️ DESPEGUE como grúa - levantando carga";
        MoveAbsJ [[90,80,-120,60,0,-80],[9E9,9E9,9E9,9E9,9E9,9E9]],v50,z1,tGripper;
        WaitTime 2.0;
        
        ! 8. ELEVACIÓN ALTA (modo transporte aéreo)
        TPWrite "✈️ MODO TRANSPORTE AÉREO - ganando altura";
        MoveAbsJ [[90,60,-90,30,0,-80],[9E9,9E9,9E9,9E9,9E9,9E9]],v100,z5,tGripper;
        WaitTime 1.5;
        
        ! 9. GRAN ROTACIÓN AL DESTINO (base -120°) - ESPECTACULAR
        TPWrite "🌪️ GRAN ROTACIÓN ESPECTACULAR al destino";
        MoveAbsJ [[-120,60,-90,-60,0,-80],[9E9,9E9,9E9,9E9,9E9,9E9]],v300,z10,tGripper;
        WaitTime 1.0;
        
        ! 10. AJUSTE FINO EN DESTINO (todos los ejes se mueven)
        TPWrite "🎪 AJUSTE FINO - todos los ejes trabajando";
        MoveAbsJ [[-120,70,-100,-30,0,-80],[9E9,9E9,9E9,9E9,9E9,9E9]],v75,z5,tGripper;
        WaitTime 1.5;
        
        ! 11. DESCENSO CONTROLADO AL DESTINO
        TPWrite "🪂 DESCENSO CONTROLADO al destino";
        MoveAbsJ [[-120,85,-130,0,0,-80],[9E9,9E9,9E9,9E9,9E9,9E9]],v50,z1,tGripper;
        WaitTime 2.5;
        
        ! 12. SOLTAR CARGA (apertura dramática)
        TPWrite "💥 SOLTAR CARGA - apertura dramática";
        MoveAbsJ [[-120,85,-130,0,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]],v25,z1,tGripper;
        WaitTime 3.0;
        
        ! 13. RETROCESO RÁPIDO (como salto hacia atrás)
        TPWrite "🦘 RETROCESO RÁPIDO - como salto";
        MoveAbsJ [[-120,70,-100,-30,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]],v200,z5,tGripper;
        WaitTime 1.0;
        
        ! 14. ELEVACIÓN FINAL (despegue)
        TPWrite "🚀 ELEVACIÓN FINAL - despegando";
        MoveAbsJ [[-120,50,-80,-60,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]],v150,z5,tGripper;
        WaitTime 1.0;
        
        ! 15. GRAN GIRO DE REGRESO (vuelta completa casi)
        TPWrite "🎡 GRAN GIRO DE REGRESO - vuelta espectacular";
        MoveAbsJ [[150,50,-80,120,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]],v400,z10,tGripper;
        WaitTime 0.5;
        
        ! 16. APROXIMACIÓN FINAL A INICIAL
        TPWrite "🎯 APROXIMACIÓN FINAL a posición inicial";
        MoveAbsJ [[30,30,-60,60,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]],v200,z5,tGripper;
        WaitTime 1.0;
        
        ! 17. ATERRIZAJE FINAL (posición de descanso)
        TPWrite "🛬 ATERRIZAJE FINAL - robot descansa";
        MoveAbsJ [[0,10,-30,0,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]],v100,z5,tGripper;
        WaitTime 2.0;
        
        ! 18. POSICIÓN DE REPOSO (como robot dormido)
        TPWrite "😴 POSICIÓN DE REPOSO - robot duerme";
        MoveAbsJ [[0,0,-20,0,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]],v50,z1,tGripper;
        WaitTime 3.0;
        
        TPWrite "🎉 MISIÓN ESPECTACULAR COMPLETADA";
        TPWrite "🏆 TODOS LOS EJES TRABAJARON AL MÁXIMO";
        
    ENDPROC

ENDMODULE