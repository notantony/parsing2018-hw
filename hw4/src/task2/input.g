LBRACKET    : "\(" ;
RBRACKET    : "\)" ;
PTR         : "\*" ;
SEMICOLON   : ";" ;
COMMA       : "," ;
IDENT       : "[_a-zA-Z]\w*" ;


start       : type_ IDENT LBRACKET args RBRACKET SEMICOLON
{
    @0.data = "S"
};

type_       : IDENT modifier
{
    @0.data = "T"
};

args        : (type_ IDENT args_) | EPS
{
    if @ne is not None:
        @0.ne = True
    @0.data = "A"
};

args_       : (COMMA type_@ne IDENT args_) | EPS
{
    if @ne is not None:
        @0.ne = True
    @0.data = "A'"
};

modifier    : (PTR modifier@ne) | EPS
{
    if @ne is not None:
        @0.ne = True
    @0.data = "M"
};