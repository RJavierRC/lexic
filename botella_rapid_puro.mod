%%%
  VERSION:1
  LANGUAGE:ENGLISH
%%%
MODULE MainModule

    ! ========================================
    ! PROGRAMA RAPID PURO - RECOGER BOTELLA
    ! Programado directamente en lenguaje ABB RAPID
    ! Sin generadores - Solo conocimiento de robótica
    ! ========================================

    ! Definición de herramienta (gripper)
    PERS tooldata tGripper := [TRUE,[[0,0,130],[1,0,0,0]],[1,[0,0,20],[1,0,0,0],0,0,0.005]];
    
    ! Definición de objeto de trabajo (mesa)
    PERS wobjdata wMesa := [FALSE,TRUE,"",[[0,0,0],[1,0,0,0]],[[0,0,0],[1,0,0,0]]];
    
    ! Posiciones clave del robot
    CONST robtarget pHome := [[0,0,-30,0,0,0],[0,0,0,0],[0,0,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]];
    CONST robtarget pAproach := [[45,40,-60,0,0,0],[0,0,0,0],[0,0,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]];
    CONST robtarget pGrasp := [[45,55,-85,0,0,-70],[0,0,0,0],[0,0,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]];
    CONST robtarget pLift := [[45,40,-60,0,0,-70],[0,0,0,0],[0,0,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]];
    CONST robtarget pTransport := [[-60,40,-60,45,0,-70],[0,0,0,0],[0,0,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]];
    CONST robtarget pPlace := [[-60,55,-85,45,0,0],[0,0,0,0],[0,0,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]];
    
    ! Velocidades diferenciadas
    CONST speeddata vMuyLenta := [10,50,5000,1000];      ! 10 mm/s - SÚPER LENTA
    CONST speeddata vLenta := [30,100,5000,1000];        ! 30 mm/s - LENTA  
    CONST speeddata vNormal := [80,500,5000,1000];       ! 80 mm/s - NORMAL
    CONST speeddata vRapida := [200,1000,5000,1000];     ! 200 mm/s - RÁPIDA
    
    ! Zonas de precisión
    CONST zonedata zPrecisa := [FALSE,0.3,0.3,0.3,0.03,0.3,0.03];    ! Muy precisa
    CONST zonedata zNormal := [FALSE,2,2,2,0.3,2,0.3];               ! Normal
    CONST zonedata zRapida := [FALSE,10,10,10,1,10,1];               ! Rápida

    PROC Main()
        ! Configuración inicial
        ConfJ \On;
        ConfL \Off;
        
        ! ===== PROGRAMA PRINCIPAL =====
        TPWrite "🤖 INICIANDO RECOGIDA DE BOTELLA";
        
        ! 1. IR A POSICIÓN INICIAL (VELOCIDAD NORMAL)
        TPWrite "📍 Yendo a posición inicial...";
        MoveAbsJ pHome,vNormal,zNormal,tGripper \WObj:=wMesa;
        WaitTime 1.0;
        
        ! 2. APROXIMARSE A LA BOTELLA (VELOCIDAD LENTA)
        TPWrite "🎯 Aproximándose a la botella...";
        MoveAbsJ pAproach,vLenta,zNormal,tGripper \WObj:=wMesa;
        WaitTime 1.5;
        
        ! 3. BAJAR PARA AGARRAR (VELOCIDAD MUY LENTA - PRECISIÓN)
        TPWrite "⬇️ Bajando para agarrar...";
        MoveAbsJ pGrasp,vMuyLenta,zPrecisa,tGripper \WObj:=wMesa;
        WaitTime 2.0;
        
        ! 4. CERRAR GRIPPER (SIMULADO CON POSICIÓN)
        TPWrite "🤏 Cerrando gripper...";
        WaitTime 1.5;
        
        ! 5. LEVANTAR BOTELLA (VELOCIDAD LENTA - CUIDADO)
        TPWrite "⬆️ Levantando botella...";
        MoveAbsJ pLift,vLenta,zNormal,tGripper \WObj:=wMesa;
        WaitTime 1.0;
        
        ! 6. TRANSPORTAR A DESTINO (VELOCIDAD RÁPIDA)
        TPWrite "🚀 Transportando a destino...";
        MoveAbsJ pTransport,vRapida,zRapida,tGripper \WObj:=wMesa;
        WaitTime 0.5;
        
        ! 7. COLOCAR BOTELLA (VELOCIDAD MUY LENTA - PRECISIÓN)
        TPWrite "📦 Colocando botella...";
        MoveAbsJ pPlace,vMuyLenta,zPrecisa,tGripper \WObj:=wMesa;
        WaitTime 2.0;
        
        ! 8. ABRIR GRIPPER (SIMULADO)
        TPWrite "✋ Abriendo gripper...";
        WaitTime 1.0;
        
        ! 9. ALEJARSE (VELOCIDAD NORMAL)
        TPWrite "↩️ Alejándose...";
        MoveAbsJ pTransport,vNormal,zNormal,tGripper \WObj:=wMesa;
        WaitTime 0.5;
        
        ! 10. REGRESAR A INICIAL (VELOCIDAD RÁPIDA)
        TPWrite "🏠 Regresando a posición inicial...";
        MoveAbsJ pHome,vRapida,zRapida,tGripper \WObj:=wMesa;
        WaitTime 1.0;
        
        TPWrite "✅ MISIÓN COMPLETADA - BOTELLA RECOGIDA";
        
    ENDPROC

ENDMODULE