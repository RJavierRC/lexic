%%%
  VERSION:1
  LANGUAGE:ENGLISH
%%%
MODULE MainModule

    ! ========================================
    ! PROGRAMA RAPID CORREGIDO - RECOGER BOTELLA
    ! Usando SOLO posiciones de articulaciones (jointtarget)
    ! Compatible con MoveAbsJ
    ! ========================================

    ! Definición de herramienta (gripper)
    PERS tooldata tGripper := [TRUE,[[0,0,130],[1,0,0,0]],[1,[0,0,20],[1,0,0,0],0,0,0.005]];
    
    ! Definición de objeto de trabajo (mesa)
    PERS wobjdata wMesa := [FALSE,TRUE,"",[[0,0,0],[1,0,0,0]],[[0,0,0],[1,0,0,0]]];
    
    ! POSICIONES DE ARTICULACIONES (jointtarget) - COMPATIBLES CON MoveAbsJ
    CONST jointtarget jHome := [[0,20,-45,0,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]];
    CONST jointtarget jAproach := [[45,40,-60,0,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]];
    CONST jointtarget jGrasp := [[45,55,-85,0,0,-70],[9E9,9E9,9E9,9E9,9E9,9E9]];
    CONST jointtarget jLift := [[45,40,-60,0,0,-70],[9E9,9E9,9E9,9E9,9E9,9E9]];
    CONST jointtarget jTransport := [[-60,40,-60,45,0,-70],[9E9,9E9,9E9,9E9,9E9,9E9]];
    CONST jointtarget jPlace := [[-60,55,-85,45,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]];
    CONST jointtarget jAway := [[-60,40,-60,45,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]];
    
    ! Velocidades diferenciadas para movimientos de articulaciones
    CONST speeddata vMuyLenta := v25;      ! MUY LENTA
    CONST speeddata vLenta := v75;         ! LENTA  
    CONST speeddata vNormal := v150;       ! NORMAL
    CONST speeddata vRapida := v400;       ! RÁPIDA
    
    ! Zonas de precisión
    CONST zonedata zPrecisa := z1;         ! Muy precisa
    CONST zonedata zNormal := z5;          ! Normal
    CONST zonedata zRapida := z10;         ! Rápida

    PROC Main()
        ! Configuración inicial
        ConfJ \On;
        ConfL \Off;
        
        ! ===== PROGRAMA PRINCIPAL =====
        TPWrite "🤖 INICIANDO RECOGIDA DE BOTELLA";
        
        ! 1. IR A POSICIÓN INICIAL (VELOCIDAD NORMAL)
        TPWrite "📍 Yendo a posición inicial...";
        MoveAbsJ jHome,vNormal,zNormal,tGripper \WObj:=wMesa;
        WaitTime 1.5;
        
        ! 2. APROXIMARSE A LA BOTELLA (VELOCIDAD LENTA)
        TPWrite "🎯 Aproximándose a la botella...";
        MoveAbsJ jAproach,vLenta,zNormal,tGripper \WObj:=wMesa;
        WaitTime 2.0;
        
        ! 3. BAJAR PARA AGARRAR (VELOCIDAD MUY LENTA - PRECISIÓN)
        TPWrite "⬇️ Bajando para agarrar...";
        MoveAbsJ jGrasp,vMuyLenta,zPrecisa,tGripper \WObj:=wMesa;
        WaitTime 3.0;
        
        ! 4. CERRAR GRIPPER (SIMULADO CON MENSAJE)
        TPWrite "🤏 Cerrando gripper...";
        WaitTime 2.0;
        
        ! 5. LEVANTAR BOTELLA (VELOCIDAD LENTA - CUIDADO)
        TPWrite "⬆️ Levantando botella...";
        MoveAbsJ jLift,vLenta,zNormal,tGripper \WObj:=wMesa;
        WaitTime 1.5;
        
        ! 6. TRANSPORTAR A DESTINO (VELOCIDAD RÁPIDA)
        TPWrite "🚀 Transportando a destino...";
        MoveAbsJ jTransport,vRapida,zRapida,tGripper \WObj:=wMesa;
        WaitTime 1.0;
        
        ! 7. COLOCAR BOTELLA (VELOCIDAD MUY LENTA - PRECISIÓN)
        TPWrite "📦 Colocando botella...";
        MoveAbsJ jPlace,vMuyLenta,zPrecisa,tGripper \WObj:=wMesa;
        WaitTime 3.0;
        
        ! 8. ABRIR GRIPPER (SIMULADO)
        TPWrite "✋ Abriendo gripper...";
        WaitTime 1.5;
        
        ! 9. ALEJARSE (VELOCIDAD NORMAL)
        TPWrite "↩️ Alejándose...";
        MoveAbsJ jAway,vNormal,zNormal,tGripper \WObj:=wMesa;
        WaitTime 1.0;
        
        ! 10. REGRESAR A INICIAL (VELOCIDAD RÁPIDA)
        TPWrite "🏠 Regresando a posición inicial...";
        MoveAbsJ jHome,vRapida,zRapida,tGripper \WObj:=wMesa;
        WaitTime 2.0;
        
        TPWrite "✅ MISIÓN COMPLETADA - BOTELLA RECOGIDA";
        
    ENDPROC

ENDMODULE