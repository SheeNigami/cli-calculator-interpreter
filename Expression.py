from helpers import Tokenizer, TokenType
from collection import Stack, BinaryTree

class Node:
    # Constructor
    def __init__(self):
        self.nextNode = None

class Expression(Node):
    def __init__(self, exp_str):
        super().__init__()
        self.__exp_str = exp_str.replace(" ",  '')
        self.__tokens = self.tokenize_exp()
        self.__tree_root = None
        self.val = None
        self.sort_value = None

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

        prev_token = None
        # Alg states Expect Operand (0), Expect Operator (1), for catching invalid expressions
        alg_state = 0

        for i, token in enumerate(self.__tokens):
            # Push Operands into operand_stack, operators to operator_stack
            if token.type == TokenType.LPAREN:
                if alg_state != 0:
                    raise Exception(f"Expected Operand after {prev_token}")
                operator_stack.push(token)
            elif token.type == TokenType.NUMBER:
                if alg_state != 0:
                    raise Exception(f"Expected Operand after {prev_token}")
                node_stack.push(token)
                alg_state = 1
            # For operators
            elif token.precedence > 0:
                # If unary minus, reverse sign of next number
                if (token.type == TokenType.MINUS) and (prev_token == None or (prev_token.type != TokenType.NUMBER and prev_token.type != TokenType.RPAREN)):
                    if alg_state != 0:
                        raise Exception(f"Expected Operand after {prev_token}")
                    for j in range(i, len(self.__tokens)):
                        if self.__tokens[j].type == TokenType.NUMBER:
                            self.__tokens[j].value = -self.__tokens[j].value
                            break
                        # No number after unary minus
                        elif j == len(self.__tokens)-1:
                            raise Exception(f"No number after unary minus")
                else:
                    if alg_state != 1:
                        raise Exception(f"Expected Operator after {prev_token}")

                    # If lower or equal precendence, also handles exponent (evals right to left)
                    while (not operator_stack.isEmpty() and operator_stack.get().type != TokenType.LPAREN
                        and ((token.type != TokenType.EXPONENT and operator_stack.get().precedence >= token.precedence)
                                or (token.type is TokenType.EXPONENT and operator_stack.get().precedence > token.precedence) )
                    ):
                        operator_stack, node_stack = self.make_subtree(operator_stack, node_stack)

                    # Push currrent token to operator stack
                    operator_stack.push(token)

                    alg_state = 0
            # Handle Parenthesis
            elif token.type == TokenType.RPAREN:
                if alg_state != 1:
                    raise Exception(f"Expected Operator after {prev_token}")
                # Pop all until LPAREN found
                while (not operator_stack.isEmpty() and operator_stack.get().type != TokenType.LPAREN):
                    operator_stack, node_stack = self.make_subtree(operator_stack, node_stack)

                # Remove LPAREN
                operator_stack.pop()

            prev_token = token

        # Empty and build/connect rest of the tree after finishing all tokens
        while (not operator_stack.isEmpty()): 
            operator_stack, node_stack = self.make_subtree(operator_stack, node_stack)

        # Return built expression tree
        self.__tree_root = node_stack.get()
        # print('DONE TREE: ' + str(self.__tree_root))
        self.val = self.evaluate(self.__tree_root)
        return

    # Makes subtree from stacks
    def make_subtree(self, operator_stack, node_stack): 
        # Parent node (top operator from stack)
        parent = operator_stack.pop()

        # Tree cannot have parentheses
        if parent.type == TokenType.LPAREN or parent.type == TokenType.RPAREN:
            raise Exception("Parentheses are mismatched.")

        # Get top operands from stack
        right = node_stack.pop()
        left = node_stack.pop()

        # Make sure no NoneTypes for subtree
        if parent == None or right == None or left == None:
            raise Exception("Ending with an operator")

        # Add subnodes to tree
        sub_tree = BinaryTree(parent, left, right)

        # Append to whole tree (node stack)
        node_stack.push(sub_tree)

        return operator_stack, node_stack

    # Evaluate expression
    def evaluate(self, binary_tree_node): 
        # Empty Tree
        if binary_tree_node is None:
            return 0

        # Is a leaf node (Reached bottom)
        if type(binary_tree_node) != BinaryTree:
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
        elif binary_tree_node.get_key().type == TokenType.MODULO:
            return left_sum % right_sum
        elif binary_tree_node.get_key().type == TokenType.EXPONENT:
            return left_sum ** right_sum

    # Recursively prints the various tree traversals (Preorder, Postorder, Inorder)
    def print_preorder(self, tree=True, depth=0):
        if tree is True:
            tree = self.__tree_root
        if tree != None:
            if type(tree) != BinaryTree:
                # print(('-') * depth + str(tree.value))
                print(('??? ') * depth + str(tree))
            else:
                print(('??? ') * depth + str(tree.get_key()))
                self.print_preorder(tree.get_left_tree(), depth+1)
                self.print_preorder(tree.get_right_tree(), depth+1)

    def print_postorder(self, tree=True, depth=0):
        if tree is True:
            tree = self.__tree_root
        if tree != None:
            if type(tree) != BinaryTree:
                print(('??? ') * depth + str(tree.value))
            else:
                self.print_postorder(tree.get_left_tree(), depth+1)
                self.print_postorder(tree.get_right_tree(), depth+1)
                print(('??? ') * depth + str(tree.get_key()))

    def print_inorder(self, tree=True, depth=0): 
        if tree is True:
            tree = self.__tree_root
        if tree != None:
            if type(tree) != BinaryTree:
                print(('??? ') * depth + str(tree.value))
            else:
                self.print_inorder(tree.get_left_tree(), depth+1)
                print(('??? ') * depth + str(tree.get_key()))
                self.print_inorder(tree.get_right_tree(), depth+1)

    # helping methods
    def set_sort_value(self, value):
        self.sort_value = value
        return

    def sort_value_count(self):
        return self.__tokens.count(self.sort_value)

    # Overloading operators
    def __lt__(self, other):
        if self.sort_value == None:
            if self.val != other.val:
                return self.val < other.val
            elif len(str(self)) != len(str(other)):
                return len(str(self)) < len(str(other))
        else:
            if self.__tokens.count(self.sort_value) != other.__tokens.count(self.sort_value):
                return self.__tokens.count(self.sort_value) < other.__tokens.count(self.sort_value)
            elif self.val != other.val:
                return self.val < other.val
            elif len(str(self)) != len(str(other)):
                return len(str(self)) < len(str(other))


    def __gt__(self, other):
        if self.sort_value == None:
            if self.val != other.val:
                return self.val > other.val
            elif len(str(self)) != len(str(other)):
                return len(str(self)) > len(str(other))
        else:
            if self.__tokens.count(self.sort_value) != other.__tokens.count(self.sort_value):
                return self.__tokens.count(self.sort_value) > other.__tokens.count(self.sort_value)
            elif self.val != other.val:
                return self.val > other.val
            elif len(str(self)) != len(str(other)):
                return len(str(self)) > len(str(other))
    
    def __str__(self):
        return self.__exp_str



