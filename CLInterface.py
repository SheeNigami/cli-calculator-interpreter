from helpers import sort_expressions
from Expression import Expression
from collection import SortedList

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
        exp_str = None
        # If invalid input, keep prompting for input
        while exp_str is None:
            exp_str = input('Please enter the expression you want to evaluate:\n')
            try:
                exp_str.replace(' ', '')
                expression = Expression(exp_str)
                expression.parse_tree()
            except Exception as e:
                exp_str = None
                print(e)

        while True:
            orderprint_selection = self.__print_order_selection()
            if orderprint_selection in ['1', '2', '3']:
                break
            print("Invalid input. Please input either '1', '2' or '3'.\n")


        if orderprint_selection == "1":
            expression.print_preorder()
        elif orderprint_selection == "2":
            expression.print_inorder()
        elif orderprint_selection == "3":
            expression.print_postorder()

        print("\nExpression evaluates to:\n{:.4f}".format(expression.val))

    # Read Write File and Evaluate Expression (Selection 2)
    def sort_evaluate_expression(self):
        #input file prompt
        while True:
            try:
                readfile = input("Please enter input file:")
                input_file = open('./input/'+readfile, 'r')
                input_file = input_file.read()
            except:
                print("The file does not exist. Please enter a valid input (e.g. input.txt)")
                continue
            break
        
        #output file prompt
        while True:
            outfile = input("Please enter output file:")

            if outfile[-4:] != '.txt':
                print("Not a valid filename. Please enter a valid filename ending with .txt (e.g. output.txt)")
                continue

            try:
                output_file = open('./output/'+outfile, 'w')
            except:
                print('Not a valid filename. Please enter a valid filename (e.g. output.txt)\nA valid filename cannot include * . " / \ [ ] : ; | ,')
                continue
        
        print(">>>Evaluation and sorting started:\n")
               
        input_file = input_file.splitlines()
               
        #sorting prompt
        #built prompt
        prompt = "Please select your choice ('1','2')"
        prompt += '\n   1. Sorted list'
        prompt += '\n   2. Merge sort'
        prompt += '\nEnter choice: '

        sort_method = None
        ascending_check = None

        #input and check for 1, 2
        while sort_method not in ['1', '2']:
            sort_method = input(prompt)
            if sort_method not in ['1', '2']:
                print("Invalid input. Please input either '1' or '2'.\n")

        #built prompt
        prompt = "Please select your choice ('1','2')"
        prompt += '\n   1. Sort ascending'
        prompt += '\n   2. Sort descending'
        prompt += '\nEnter choice: '

        #input and check for 1, 2
        while ascending_check not in ['1', '2']:
            ascending_check = input(prompt)
            if ascending_check not in ['1', '2']:
                print("Invalid input. Please input either '1' or '2'.\n")

        if sort_method == '1':
            exp_list = SortedList(ascending_check)
            for i in range(len(input_file)):
                try:
                    input_file[i].replace(' ', '')
                    expression = Expression(input_file[i])
                    expression.parse_tree()
                except Exception as e:
                    print(e)
                    print("Invalid expression at line "+(i+1)+". Skipping expression")
                    continue
                exp_list.insert(expression)

        elif sort_method == '2':
            exp_list = []
            for i in range(len(input_file)):
                try:
                    input_file[i].replace(' ', '')
                    expression = Expression(input_file[i])
                    expression.parse_tree()
                except Exception as e:
                    print(e)
                    print("Invalid expression at line "+(i+1)+". Skipping expression")
                    continue
                exp_list.append(expression)
            exp_list = sort_expressions(exp_list, ascending_check)
        
        current_val = None
        print_str = ""
        for i in range(len(exp_list)):
            if current_val != exp_list[i].val:
                current_val = exp_list[i].val
                print_str+= ("\n*** Expressions with value= " + current_val)
            print_str += (exp_list[i] + "==>" + exp_list[i].val)

        print(print_str)

        output_file.write(print_str)

        print(">>>Evaluation and sorting completed!")
            

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

        

