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
            # Push Operands into operand_stack, operators to operator_stack
            if token.type == TokenType.LPAREN:
                operator_stack.push(token)
            elif token.type == TokenType.NUMBER:
                node_stack.push(token)
            # For operators
            elif token.precedence > 0:
                # If lower or equal precendence, also handles exponent (evals right to left)
                while (not operator_stack.isEmpty() and operator_stack.get().type is not TokenType.LPAREN
                       and ((token.type is not TokenType.EXPONENT and operator_stack.get().precedence >= token.precedence)
                            or (token.type is TokenType.EXPONENT and operator_stack.get().precedence > token.precedence) )
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
            elif token.type == TokenType.RPAREN:
                # Pop all until LPAREN found
                while (not operator_stack.isEmpty() and operator_stack.get().type is not TokenType.LPAREN):
                    parent = operator_stack.pop()
                    right = node_stack.pop()
                    left = node_stack.pop()

                    sub_tree = BinaryTree(parent, left, right)
                    node_stack.push(sub_tree)

                # Remove LPAREN
                operator_stack.pop()

            print('\nOperator Stack: ' + str(operator_stack.stack_list))
            print('Node Stack: ' + str(node_stack.stack_list))

        print('\nfinishing loop')

        # Empty and build/connect rest of the tree after finishing all tokens
        while (not operator_stack.isEmpty()): 
            parent = operator_stack.pop()
            right = node_stack.pop()
            left = node_stack.pop()

            sub_tree = BinaryTree(parent, left, right)
            node_stack.push(sub_tree)

            print('\nOperator Stack: ' + str(operator_stack.stack_list))
            print('Node Stack: ' + str(node_stack.stack_list))

        print('\nDONE\nOperator Stack: ' + str(operator_stack.stack_list))
        print('Node Stack: ' + str(node_stack.stack_list))

        # Return built expression tree
        tree = node_stack.get()
        print('DONE TREE: ' + str(tree))
        return tree

    def evaluate(self, root): 
        # Empty Tree
        if root is None:
            return 0

        # Is a leaf node (Reached bottom)
        if type(root) is not BinaryTree:
            return root.value

        left_sum = self.evaluate(root.get_left_tree())
        right_sum = self.evaluate(root.get_right_tree())

        # Apply operations
        if root.get_key().type == TokenType.PLUS:
            return left_sum + right_sum
        elif root.get_key().type == TokenType.MINUS:
            return left_sum - right_sum
        elif root.get_key().type == TokenType.MULTIPLY:
            return left_sum * right_sum
        elif root.get_key().type == TokenType.DIVIDE:
            return left_sum / right_sum
        elif root.get_key().type == TokenType.EXPONENT:
            return left_sum ** right_sum

    def print_preorder(self, tree, depth=0): 
        if tree is not None:
            if type(tree) is not BinaryTree:
                print(('-') * depth + str(tree.value))
            else:
                print(('-') * depth + str(tree.get_key()))
                self.print_preorder(tree.get_left_tree(), depth+1)
                self.print_preorder(tree.get_right_tree(), depth+1)

    def print_postorder(self, tree, depth=0): 
        if tree is not None:
            if type(tree) is not BinaryTree:
                print(('-') * depth + str(tree.value))
            else:
                self.print_postorder(tree.get_left_tree(), depth+1)
                self.print_postorder(tree.get_right_tree(), depth+1)
                print(('-') * depth + str(tree.get_key()))

    def print_inorder(self, tree, depth=0): 
        if tree is not None:
            if type(tree) is not BinaryTree:
                print(('-') * depth + str(tree.value))
            else:
                self.print_inorder(tree.get_left_tree(), depth+1)
                print(('-') * depth + str(tree.get_key()))
                self.print_inorder(tree.get_right_tree(), depth+1)



    def has_greater_precedence(op1, op2): 
        return op1.precedence


