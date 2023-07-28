def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    open_parens = 1
    closed_parens = 1
    if parens[0] != "(" or parens[-1] != ")":
        return False
    else:
        for paren in parens:
            if paren == "(":
                open_parens += 1
            elif paren == ")":
                closed_parens += 1
    if open_parens != closed_parens:
        return False
    return True