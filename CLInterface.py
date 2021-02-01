from helpers import sort_expressions
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
        prompt = "Please select your choice ('1','2','3')"
        prompt += '\n   1. Evaluate expression'
        prompt += '\n   2. Sort expressions'
        prompt += '\n   3. Exit'
        prompt += '\nEnter choice: '

        self.__current_selection = input(prompt)
        
    # Evaluates Input Expression (Selection 1)
    def evaluate_expression(self):
        exp_str = None
        # If invalid input, keep prompting for input
        while exp_str is None:
            exp_str = input('Please enter the expression you want to evaluate:\n')
            try:
                expression = Expression(exp_str)
            except Exception as e:
                exp_str = None
                print(e)

        exp_tree = expression.parse_tree()
        print(exp_tree)
        

    def get_current_selection(self):
        return self.__current_selection
        

