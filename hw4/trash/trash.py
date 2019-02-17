
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
                @0.val = eval(str(@a1.val) + @op + str(@a2.val))
            elif @op == "&&":
                @0.val = int(bool(@a1.val and @a2.val))
            elif @op == "||":
                @0.val = int(bool(@a1.val and @a2.val))
            else:
                @0.val = @a1.val // @a2.val
            print("Optimized: " + str(@0.val))
    elif @id is not None:
        @0.STR = @id
    elif @e is not None:
        if hasattr(@e, "val"):
            @0.val = @e.val
        else:
            @0.val = "(" + @e.STR + ")"
    if hasattr(@0, "val"):
        @0.STR = str(@0.val)
    if not hasattr(@0, "STR"):
        @0.STR = (@a1.STR + " " + @op + " " + @a2.STR)