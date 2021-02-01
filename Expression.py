from helpers import Tokenizer, TokenType
from collection import Stack, BinaryTree

class Expression:
    def __init__(self, exp_str):
        self.__exp_str = exp_str
        self.__tokens = self.tokenize_exp()

    # Tokenize Expression with our tokenizer
    def tokenize_exp(self): 
        tokenizer = Tokenizer(self.__exp_str)
        tokens = tokenizer.generate_tokens()
        # return tokens
        return list(tokens)

    # Parse tokens into tree with shunting-yard algorithm
    def parse_tree(self):
        # Stacks to hold operators/operands for alg
        operator_stack = Stack()        
        node_stack = Stack()
        print('Tokens: ' + str(self.__tokens))
        for token in self.__tokens:
            print('\nOperator Stack: ' + str(operator_stack.stack_list))
            print('Node Stack: ' + str(node_stack.stack_list))
            # Push Operands into operand_stack, operators to operator_stack
            if token.type == TokenType.LPAREN:
                operator_stack.push(token)
            elif token.type == TokenType.NUMBER:
                node_stack.push(token)
            # For operators
            elif token.precedence > 0:
                # If lower or equal precendence, also handles exponent (evals right to left)
                while (not operator_stack.isEmpty() and operator_stack.get() is not TokenType.LPAREN
                       and ((token.type is not TokenType.EXPONENT and operator_stack.get().precedence >= token.precedence)
                            or (token.type is not TokenType.EXPONENT and operator_stack.get().precedence > token.precedence) )
                ):
                    # Parent node (top operator from stack)
                    parent = operator_stack.pop()

                    # Get top operands from stack
                    n1 = node_stack.pop()
                    n2 = node_stack.pop()

                    # Add subnodes to tree
                    sub_tree = BinaryTree(parent, n2, n1)

                    # Append to whole tree (node stack)
                    node_stack.push(sub_tree)

                # Push currrent token to opeartor stack
                operator_stack.push(token)
            # Handle Parenthesis
            elif token == TokenType.RPAREN:
                # Pop all until LPAREN found
                while (not operator_stack.isEmpty() and operator_stack.get() is not TokenType.LPAREN):
                    parent = operator_stack.pop()
                    n1 = node_stack.pop()
                    n2 = node_stack.pop()

                    sub_tree = BinaryTree(parent, n2, n1)
                    node_stack.push(sub_tree)

                # Remove LPAREN
                operator_stack.pop()

        # Return built expression tree
        tree = node_stack.get()
        return tree


    def has_greater_precedence(op1, op2): 
        return op1.precedence


