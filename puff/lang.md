
PLUS:        expression + expression
MINUS:       expression - expression
DIVIDE:      expression / expression
PRODUCT:     expression * expression

GREATERTHAN: expression > expression
LESSTHAN:    expression < expression
EQUALS:      expression == expression

SEMICOLON:   ;


FUNCTION_DEF: def <name> OPENPAREN (<arg> (, <arg>)*) CLOSEPAREN OPENBRACKET
    (EXPR SEMICOLON)*
CLOSEBRACKET

ASSIGNMENT:  var <name> = EXPRESSION

