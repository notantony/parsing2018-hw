grammar Main;


fragment ALPHA          : [A-Za-z] ;
fragment DIGIT          : [0-9] ;


WHITESPACE              : [ \n\r\t\f] -> skip ;
IF                      : 'if' ;
WHILE                   : 'while' ;
CONST                   : DIGIT+ | 'true' | 'false' ;
CONSUMER1               : 'print' ;
OPERATOR2               : '+' | '-' | '/' | '*' | '%' | '&&' | '||' | '>=' | '<=' | '<' | '>' | '==' | '!=' ;
ASSIGNMENT              : '=' ;
IDENT                   : (ALPHA | '_') (ALPHA | DIGIT | '_')*;
LPAR                    : '(' ;
RPAR                    : ')' ;



start                   : name vars ASSIGNMENT statement+ ;

name                    : IDENT ;

vars                    : IDENT* ;

program                 : statement+ ;

statement               : ifElse                #ifElseStatement
                        | ifSingle              #ifSingleStatement
                        | whileC                #whileStatement
                        | assignment            #assignmentStatement
                        | expr                  #exprStatement
                        | LPAR program RPAR     #programStatement
                        | action                #actionStatement ;

ifSingle                : IF expr statement ;

whileC                  : WHILE expr statement ;

ifElse                  : IF expr statement statement ;

assignment              : ASSIGNMENT IDENT expr ;

expr                    : CONST
                        | OPERATOR2 expr expr
                        | IDENT
                        | LPAR expr RPAR ;

action                  : CONSUMER1 expr ;





