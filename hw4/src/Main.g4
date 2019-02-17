grammar Main;

fragment ALPHA      : [A-Za-z] ;
fragment UPPER      : [A-Z] ;
fragment LOWER      : [a-z] ;
fragment DIGIT      : [0-9] ;

CODE                : '{' ~[{}]* '}' ;
REGEXP              : '"' ~[" \n\r\t\f]* '"' ;
WHITESPACE          : [ \n\r\t\f] -> skip ;
LOWER_IDENT         : (LOWER) (ALPHA | DIGIT | '_')* ;
CAPS_IDENT          : (UPPER) (UPPER | DIGIT | '_')* ;

LPAR                : '(' ;
RPAR                : ')' ;
COLON               : ':' ;
SEMICOLON           : ';' ;
ARROW               : '->' ;
BAR                 : '|' ;
DOT                 : '.' ;
EQ                  : '=' ;
AT                  : '@' (ALPHA | DIGIT | '_')+;



start               : lexingRule* parsingRule* ;

lexingRule          : CAPS_IDENT COLON REGEXP SEMICOLON ;

parsingRule         : LOWER_IDENT COLON parsingExpr CODE? SEMICOLON ;

parsingExpr         : LPAR parsingExpr RPAR
                    | parsingExpr BAR parsingExpr
                    | parsingSolo parsingExpr? ;

parsingSolo         : LOWER_IDENT (AT)?
                    | CAPS_IDENT (AT)? ;





