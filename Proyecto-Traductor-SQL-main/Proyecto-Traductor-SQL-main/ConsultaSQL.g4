grammar ConsultaSQL;

consulta
    : mostrar
    | contar
    | borrar
    ;

mostrar
    : 'MOSTRAR' ID (condicion)?
    ;

contar
    : 'CONTAR' ID
    ;

borrar
    : 'BORRAR' ID 'DONDE' ID 'SEA' NUM
    ;

condicion
    : 'CON' ID comparador valor
    ;

comparador
    : 'MAYOR A' | 'MENOR A' | 'IGUAL A'
    ;

valor
    : NUM
    ;

ID  : [A-Z]+ ;
NUM : [0-9]+ ;
WS  : [ \t\r\n]+ -> skip ;
