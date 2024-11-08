grammar Language;

start_ : statement+ ;
statement: declaration ';' | expression ';' ;
declaration: ('int' | 'float') ID ('=' expr)? ;
expression: ID '=' expr ;
expr: expr '+' term | term ;
term: ID | NUMBER ;

ID: [a-zA-Z_][a-zA-Z0-9_]* ;
NUMBER: [0-9]+('.'[0-9]+)? ;
WS: [ \t\n\r]+ -> skip ;
COMMENT: '//' ~[\r\n]* -> skip ;  // Ignorare i commenti a fine riga
