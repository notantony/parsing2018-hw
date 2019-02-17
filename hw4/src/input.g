IF                      : "if" ;
WHILE                   : "while" ;
CONST                   : "\d+|(true)|(false)" ;
CONSUMER1               : "print" ;
OPERATOR2               : "(&&)|(\|\|)|(>=)|(<=)|(==)|(!=)|[+-/*%<>]" ;
ASSIGNMENT              : "=" ;
IDENT                   : "([a-zA-z]|_)([a-zA-z]|[0-9]|_)*";
LPAR                    : "\(" ;
RPAR                    : "\)" ;



start                   : IDENT@id idents@ids ASSIGNMENT statements@sts EOF
{
    @0.name = @id
    @0.sts = @sts.sts
    @0.vars = @ids.ids
};

statements              : (statement@this statements@also) | EPS
{
    if @this is None:
        @0.sts = []
    else:
        @0.sts = [@this] + @also.sts
};

idents                  : (IDENT@this idents@also) | EPS
{
    if @this is None:
        @0.ids = []
    else:
        @0.ids = [@this] + @also.ids
};


statement               : ifC
                        | whileC
                        | assignment
                        | (LPAR statement@this statements@also RPAR)
                        | action
{
    if @this is not None:
        @0.sts = [@this] + @also.sts
};


ifC                     : IF expr@expr statement@stat ifPost@post
{
    @0.COND = "if (" + @expr.STR + ") "
    @0.stat = @stat
    @0.post = @post
};

ifPost                  : statement@stat | EPS
{
    @0.post = @stat
};

whileC                  : WHILE expr@expr statement@stat
{
    @0.COND = "while (" + @expr.STR + ") "
    @0.stat = @stat
};

assignment              : ASSIGNMENT IDENT@id expr@expr
{
    @0.IDENT = @id
    @0.STR = @id + " = " + @expr.STR
};

expr                    : CONST@c
                        | (OPERATOR2@op expr@a1 expr@a2)
                        | IDENT@id
                        | (LPAR expr@e RPAR)
{
    if @c is not None:
        if @c == "true":
            @0.val = 1
        elif @c == "false":
            @0.val = 0
        else:
            @0.val = int(@c)
    elif @op is not None:
        if getattr(@a1, "val", None) is not None and getattr(@a2, "val", None) is not None:
            if @op in "+-*%<>" or @op == ">=" or @op == "<=" or @op == "!=" or @op == "==":
                @0.val = int(eval(str(@a1.val) + @op + str(@a2.val)))
            elif @op == "&&":
                @0.val = int(bool(@a1.val and @a2.val))
            elif @op == "||":
                @0.val = int(bool(@a1.val or @a2.val))
            else:
                @0.val = @a1.val // @a2.val
            print("Optimized: " + str(@a1.val) + @op + str(@a2.val) + " = " + str(@0.val))
    elif @id is not None:
        @0.STR = @id
    elif @e is not None:
        if hasattr(@e, "val"):
            @0.val = @e.val
        else:
            @0.STR = "(" + @e.STR + ")"
    if hasattr(@0, "val"):
        @0.STR = str(@0.val)
    if not hasattr(@0, "STR"):
        @0.STR = (@a1.STR + " " + @op + " " + @a2.STR)
};

action                  : CONSUMER1@C expr@expr
{
    @0.STR = "std::cout << " + @expr.STR
};