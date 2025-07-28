%%%
  VERSION:1
  LANGUAGE:ENGLISH
%%%
MODULE MOD_BRAZO_INDUSTRIALProgram

    ! -------------------------------
    ! Programa generado automáticamente desde sintaxis robótica
    ! Robot: brazo_industrial
    ! Fecha: 25/07/2025 13:08:41
    ! -------------------------------

    ! Tool variables: 
    PERS tooldata RobotiQ2F85Gripper(FullyClosed) := [TRUE,[[0.000,0.000,130.000],[1.00000000,0.00000000,0.00000000,0.00000000]],[1,[0,0,20],[1,0,0,0],0,0,0.005]];

    ! Reference variables:
    PERS wobjdata Frame2 := [FALSE, TRUE, "", [[0,0,0],[1,0,0,0]],[[-140.437,-738.971,5.234],[1.00000000,0.00000000,0.00000000,0.00000000]]];

    PROC base()
        ConfJ \On;
        ConfL \Off;
        MoveAbsJ [[0.000000,0.000000,0.000000,0.000000,0.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v500,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;
        MoveAbsJ [[90.000000,0.000000,0.000000,0.000000,0.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v500,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;
        MoveAbsJ [[-90.000000,0.000000,0.000000,0.000000,0.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v500,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;
        MoveAbsJ [[0.000000,0.000000,0.000000,0.000000,0.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v500,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;
    ENDPROC
    PROC hombro()
        ConfJ \On;
        ConfL \Off;
        MoveAbsJ [[0.000000,0.000000,0.000000,0.000000,0.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v500,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;
        MoveAbsJ [[0.000000,45.000000,0.000000,0.000000,0.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v500,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;
        MoveAbsJ [[0.000000,-45.000000,0.000000,0.000000,0.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v500,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;
        MoveAbsJ [[0.000000,0.000000,0.000000,0.000000,0.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v500,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;
    ENDPROC
    PROC codo()
        ConfJ \On;
        ConfL \Off;
        MoveAbsJ [[0.000000,0.000000,0.000000,0.000000,0.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v500,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;
        MoveAbsJ [[0.000000,0.000000,60.000000,0.000000,0.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v500,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;
        MoveAbsJ [[0.000000,0.000000,-60.000000,0.000000,0.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v500,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;
        MoveAbsJ [[0.000000,0.000000,0.000000,0.000000,0.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v500,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;
    ENDPROC
    PROC muneca()
        ConfJ \On;
        ConfL \Off;
        MoveAbsJ [[0.000000,0.000000,0.000000,0.000000,0.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v500,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;
        MoveAbsJ [[0.000000,0.000000,0.000000,30.000000,0.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v500,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;
        MoveAbsJ [[0.000000,0.000000,0.000000,-30.000000,0.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v500,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;
        MoveAbsJ [[0.000000,0.000000,0.000000,0.000000,0.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v500,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;
    ENDPROC
    PROC garra()
        ConfJ \On;
        ConfL \Off;
        MoveAbsJ [[0.000000,0.000000,0.000000,0.000000,0.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v500,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;
        MoveAbsJ [[0.000000,0.000000,0.000000,0.000000,15.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v500,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;
        MoveAbsJ [[0.000000,0.000000,0.000000,0.000000,-15.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v500,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;
        MoveAbsJ [[0.000000,0.000000,0.000000,0.000000,0.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v500,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;
    ENDPROC
    PROC Main()
        ConfJ \On;
        ConfL \Off;
        ! Program generated from Robot syntax on 25/07/2025 13:08:41
        ! Robot: brazo_industrial
        ! Extracted values: base=90.0°, hombro=45.0°, codo=60.0°, muneca=30.0°, garra=15.0°
        
        base;
        hombro;
        codo;
        muneca;
        garra;
    ENDPROC
ENDMODULE
