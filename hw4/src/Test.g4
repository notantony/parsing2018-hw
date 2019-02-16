grammar Test;

IF                      : 'a' ;
WHILE                   : 'b' ;
CONST                   : 'c' ;
CONSUMER1               : 'd' ;
OPERATOR2               : 'e' ;
ASSIGNMENT              : 'f' ;
IDENT                   : 'g';
LPAR                    : 'h' ;
RPAR                    : 'k' ;
EPS                     : 'EPS' ;


start                   : name vars ASSIGNMENT statement statements ;

statements              : statement statements
                        | statement ;

name                    : IDENT ;

vars                    : idents ;

idents                  : IDENT idents
                        | EPS ;

program                 : statement statements ;

statement               : ifElse
                        | ifSingle
                        | whileC
                        | assignment
                        | expr
                        | LPAR program RPAR
                        | action                ;

ifSingle                : IF expr statement ;

whileC                  : WHILE expr statement ;

ifElse                  : IF expr statement statement ;

assignment              : ASSIGNMENT IDENT expr ;

expr                    : CONST
                        | OPERATOR2 expr expr
                        | IDENT
                        | LPAR expr RPAR ;

action                  : CONSUMER1 expr ;


eps                     : EPS ;