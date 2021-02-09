from helpers import Tokenizer, TokenType
from collection import Stack, BinaryTree

class Node:
    # Constructor
    def __init__(self):
        self.nextNode = None

class Expression(Node):
    def __init__(self, exp_str):
        super().__init__()
        self.__exp_str = exp_str
        self.__tokens = self.tokenize_exp()
        self.__tree_root = None
        self.val = None

    # Tokenize Expression with our tokenizer
    def tokenize_exp(self): 
        tokenizer = Tokenizer(self.__exp_str)
        tokens = tokenizer.generate_tokens()
        # return tokens
        return list(tokens)

    # Parse tokens into tree with shunting-yard algorithm
    # TODO: Pron turn tree into its own class with variables operator and node stack, can also separate build sub_tree method to reduce duplicate code
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
        self.__tree_root = node_stack.get()
        print('DONE TREE: ' + str(self.__tree_root))
        self.val = self.evaluate(self.__tree_root)
        return

    def evaluate(self, binary_tree_node): 
        # Empty Tree
        if binary_tree_node is None:
            return 0

        # Is a leaf node (Reached bottom)
        if type(binary_tree_node) is not BinaryTree:
            return binary_tree_node.value

        left_sum = self.evaluate(binary_tree_node.get_left_tree())
        right_sum = self.evaluate(binary_tree_node.get_right_tree())

        # Apply operations
        if binary_tree_node.get_key().type == TokenType.PLUS:
            return left_sum + right_sum
        elif binary_tree_node.get_key().type == TokenType.MINUS:
            return left_sum - right_sum
        elif binary_tree_node.get_key().type == TokenType.MULTIPLY:
            return left_sum * right_sum
        elif binary_tree_node.get_key().type == TokenType.DIVIDE:
            return left_sum / right_sum
        elif binary_tree_node.get_key().type == TokenType.EXPONENT:
            return left_sum ** right_sum

    # Recursively prints the various tree traversals (Preorder, Postorder, Inorder)
    def print_preorder(self, tree=True, depth=0):
        if tree is True:
            tree = self.__tree_root
        if tree is not None:
            if type(tree) is not BinaryTree:
                print(('-') * depth + str(tree.value))
            else:
                print(('-') * depth + str(tree.get_key()))
                self.print_preorder(tree.get_left_tree(), depth+1)
                self.print_preorder(tree.get_right_tree(), depth+1)

    def print_postorder(self, tree=True, depth=0):
        if tree is True:
            tree = self.__tree_root
        if tree is not None:
            if type(tree) is not BinaryTree:
                print(('-') * depth + str(tree.value))
            else:
                self.print_postorder(tree.get_left_tree(), depth+1)
                self.print_postorder(tree.get_right_tree(), depth+1)
                print(('-') * depth + str(tree.get_key()))

    def print_inorder(self, tree=True, depth=0): 
        if tree is True:
            tree = self.__tree_root
        if tree is not None:
            if type(tree) is not BinaryTree:
                print(('-') * depth + str(tree.value))
            else:
                self.print_inorder(tree.get_left_tree(), depth+1)
                print(('-') * depth + str(tree.get_key()))
                self.print_inorder(tree.get_right_tree(), depth+1)

    # Overloading operators
    def __lt__(self):
        if self.val != other.val:
            return self.val < other.val
        else:
            return len(str(self)) < len(str(other))
    def __gt__(self):
        if self.val != other.val:
            return self.val > other.val
        else:
            return len(str(self)) > len(str(other))
    
    def __str__(self):
        return self.__exp_str



