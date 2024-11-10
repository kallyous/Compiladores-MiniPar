grammar MiniPar;

prog: channel (seq | par)* EOF;
channel: 'chan' '(' ID ',' ADDR ')' ';';
seq: 'seq' '{' stmt* '}';
par: 'par' '{' stmt* '}';
stmt: atribuicao 
    | condicional 
    | loop 
    | print;
atribuicao: ID '=' expr ';';
condicional: IF '(' expr ')' '{' stmt* '}' condicional_else?;
condicional_else: ELSE '{' stmt* '}';
loop: WHILE '(' expr ')' '{' stmt* '}';
print: PRINT '(' expr ')' ';';
expr: expr op=('+'|'-') expr 
    | expr op=('*'|'/') expr 
    | expr op=('<'|'>'|'<='|'>='|'=='|'!=') expr
    | '(' expr ')' 
    | ID 
    | INT
    | STRING;

IF: 'if';
ELSE: 'else';
WHILE: 'while';
PRINT: 'print';

NEWLINE: [\r\n]+ -> skip;
WHITESPACE: [ \t]+ -> skip;
ID: [a-zA-Z] [a-zA-Z0-9]*;
INT: [0-9]+;
ADDR: [a-zA-Z.0-9]+ ':' [0-9]+;
STRING: '"' ~[\r\n"]* '"';
