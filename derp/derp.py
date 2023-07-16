"""
141 Tree Lab - Derp the Interpreter

The Derp interpreter parses and evaluates prefix integer expressions 
containing basic arithmetic operators (*,//,-,+). It performs arithmetic with
integer operands that are either literals or variables (read from a 
symbol table).  It dumps the symbol table, prints the infix expression with 
parentheses to denote order of operation, and evaluates the expression to
print the result.

file name: derp.py
Author: Chen Lin
"""

from derp_types import *


def build_symbol_table(file_name):
    """
    create a symbol table
    :param file_name: a file name
    """
    dict = {}
    with open(file_name) as f:
        for line in f.readlines():
            dict[line.split()[0]] = int(line.split()[1])
        return dict


##############################################################################
# parse
############################################################################## 

def parse(tokens):
    """parse: list(String) -> Node
    From a prefix stream of tokens, construct and return the tree,
    as a collection of Nodes, that represent the expression.
    :param tokens: a list of string
    precondition: tokens is a non-empty list of strings
    """
    if len(tokens) == 0:
        raise TypeError('tokens are empty')
    else:
        x = tokens.pop(0)
        if x.isdigit():
            return LiteralNode(int(x))
        elif x.isidentifier():
            return VariableNode(x)
        else:
            return MathNode(parse(tokens), x, parse(tokens))


##############################################################################
# infix
##############################################################################

def infix(tr):
    """infix: tr -> String
    Perform an inorder traversal of the node and return a string that
    represents the infix expression.
    :param tr: a tree
    precondition: node is a valid derp tree node
    """
    if isinstance(tr, LiteralNode):
        return str(tr.val)
    if isinstance(tr, VariableNode):
        return str(tr.name)
    if isinstance(tr, MathNode):
        return str('(' + infix(tr.left) + tr.operator + infix(tr.right) + ')')


##############################################################################
# evaluate
##############################################################################

def evaluate(tr, sym_tbl):
    """evaluate: Node * dict(key=String, value=int) -> int 
    Return the result of evaluating the expression represented by node.
    :param tr: a tree
    :param sym_tbl: a symbol table
    Precondition: all variable names must exist in sym_tbl
    precondition: node is a valid derp tree node
    """
    if isinstance(tr, LiteralNode):
        return int(tr.val)

    if isinstance(tr, VariableNode):
        return sym_tbl[tr.name]

    if isinstance(tr, MathNode):
        left = evaluate(tr.left, sym_tbl)
        right = evaluate(tr.right, sym_tbl)
        if tr.operator == '+':
            return int(left + right)

        if tr.operator == '-':
            return int(left - right)

        if tr.operator == '*':
            return int(left * right)

        if tr.operator == '//':
            return int(left // right)


##############################################################################
# main
##############################################################################

def main():
    """main: None -> None
    The main program prompts for the symbol table file, and a prefix 
    expression.  It produces the infix expression, and the integer result of
    evaluating the expression"""

    print("Hello Herp, welcome to Derp v1.0 :)")

    in_file = input("Herp, enter symbol table file: ")

    # STUDENT: CONSTRUCT AND DISPLAY THE SYMBOL TABLE HERE
    symbol_table = build_symbol_table(in_file)
    print('Derping the symbol table (variable name => integer value)...')
    for key, value in symbol_table.items():
        print(key, '=>', value)

    # input loop prompts for prefix expressions and produces infix version
    # along with its evaluation
    print("Herp, enter prefix expressions, e.g.: + 10 20 (ENTER to quit)...")

    while True:
        prefix_exp = input("derp> ")
        if prefix_exp == "":
            break

        # STUDENT: GENERATE A LIST OF TOKENS FROM THE PREFIX EXPRESSION
        tokens_lst = prefix_exp.split()

        # STUDENT: CALL parse WITH THE LIST OF TOKENS AND SAVE THE ROOT OF
        # THE PARSE TREE.
        tree = parse(tokens_lst)

        # STUDENT: GENERATE THE INFIX EXPRESSION BY CALLING infix AND SAVING
        # THE STRING.
        infix_expression = infix(tree)

        # STUDENT: MODIFY THE print STATEMENT TO INCLUDE RESULT.    
        print("Derping the infix expression:", infix_expression)

        # STUDENT: EVALUTE THE PARSE TREE BY CALLING evaluate AND SAVING THE
        # INTEGER RESULT.

        int_result = evaluate(tree, build_symbol_table(in_file))

        # STUDENT: MODIFY THE print STATEMENT TO INCLUDE RESULT.
        print("Derping the evaluation:", int_result)

    print("Goodbye Herp :(")


if __name__ == "__main__":
    main()
