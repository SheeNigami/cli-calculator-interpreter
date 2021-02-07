from helpers import validate_input, sort_expressions
from Expression import Expression

class CLInterface:
    def __init__(self):
        self.__current_selection = None

        # Prints Init str when app is started
        print("*" * 65)
        print("* ST107 DSAA: Expression Evaluator & Sorter                     *")
        print("*" + ("-" * 63) + "*")
        print("*  - Done by: Yeo Sheen Hern (1902257) & Kaedan Tan (19*****)   *")
        print("*  - Class DIT/FT/2B/11                                         *")
        print("*" * 65)

    # Prompts user for selection 
    def selection_menu_prompt(self):
        self.__current_selection = None

        #built prompt
        prompt = "Please select your choice ('1','2','3')"
        prompt += '\n   1. Evaluate expression'
        prompt += '\n   2. Sort expressions'
        prompt += '\n   3. Exit'
        prompt += '\nEnter choice: '

        #input and check for 1 2 or 3
        while self.__current_selection not in ['1', '2' ,'3']:
            self.__current_selection = input(prompt)
            if self.__current_selection not in ['1', '2' ,'3']:
                print("Invalid input. Please input either '1', '2', or '3'\n")

    # Evaluates Input Expression (Selection 1)
    def evaluate_expression(self):
        # If invalid input, keep prompting for input
        while True:
            exp_str = input('Please enter the expression you want to evaluate:\n')
            if not validate_input(exp_str): 
                print('Please enter a valid expression\n')
                exp_str = None
            else:
                break

        expression = Expression(exp_str)

        orderprint_selection = self.__print_order_selection()

        value = None #expression.evaluate_expression()

        #expression.printorder(orderprint_selection)

        print("\n Expression evaluates to:\n{}", value)

    # Read Write File and Evaluate Expression (Selection 2)
    def sort_evaluate_expression(self):
        readfile = input("Please enter input file:")
        outfile = input("Please enter output file:")
                

    def get_current_selection(self):
        return self.__current_selection

    # Private functions___________________________________________________________________________________________________________________________
    
    # Prompts for print order selection
    def __print_order_selection(self):
        orderprint_selection = None

        #built prompt
        prompt = "Please select your choice ('1','2','3')"
        prompt += '\n   1. Print Preorder'
        prompt += '\n   2. Print Inorder'
        prompt += '\n   3. Print Postorder'
        prompt += '\nEnter choice: '

        #input and check for 1 2 or 3
        while orderprint_selection not in ['1', '2' ,'3']:
            orderprint_selection = input(prompt)
            if orderprint_selection not in ['1', '2' ,'3']:
                print("Invalid input. Please input either '1', '2', or '3'\n")
        
        return orderprint_selection

        

