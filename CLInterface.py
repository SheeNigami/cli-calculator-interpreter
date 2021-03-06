from helpers import sort_expressions, Tokenizer
from Expression import Expression
from collection import SortedList

class CLInterface:
    def __init__(self):
        self.__current_selection = None

        # Prints Init str when app is started
        print("*" * 65)
        print("* ST107 DSAA: Expression Evaluator & Sorter                     *")
        print("*" + ("-" * 63) + "*")
        print("*  - Done by: Yeo Sheen Hern (1902257) & Kaedan Tan (1935529)   *")
        print("*  - Class DIT/FT/2B/11                                         *")
        print("*" * 65)

    # Prompts user for selection 
    def selection_menu_prompt(self):
        self.__current_selection = None

        #built prompt
        prompt = "\nPlease select your choice ('1','2','3')"
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
            exp_str = input('\nPlease enter the expression you want to evaluate:\n')
            try:
                exp_str = exp_str.replace(' ', '')
                expression = Expression(exp_str)
                expression.parse_tree()
            except Exception as e:
                exp_str = None
                print('Invalid Expression, ' + str(e))

        # checking for print order
        orderprint_selection = self.__print_order_selection()

        if orderprint_selection == "1":
            expression.print_preorder()
        elif orderprint_selection == "2":
            expression.print_inorder()
        elif orderprint_selection == "3":
            expression.print_postorder()

        # writes into a history file
        with open('./history.txt', 'a') as history_file:
            history_file.write("Expression {} evaluates to: {:.3f}\n".format(str(expression), expression.val))
        with open('./input/input_history.txt', 'a') as history_file:
            history_file.write('\n' + str(expression))

        # printing
        print("\nExpression evaluates to:\n{:.3f}".format(expression.val))

    # Read Write File and Evaluate Expression (Selection 2)
    def sort_evaluate_expression(self):
        #input file prompt
        while True:
            # tries to read the file
            try:
                readfile = input("Please enter input file: ")
                with open('./input/'+readfile, 'r') as input_file:
                    input_file = input_file.read()
            except:
                print("The file does not exist. Please enter a valid input (e.g. input.txt)")
                continue
            break
        
        #output file prompt
        while True:
            outfile = input("Please enter output file: ")
            # checks if filename has .txt
            if outfile[-4:] != '.txt':
                print("Not a valid filename. Please enter a valid filename ending with .txt (e.g. output.txt)")
                continue
            
            # tries to create/open the file
            try:
                output_file = open('./output/'+outfile, 'w')
            except:
                print('Not a valid filename. Please enter a valid filename (e.g. output.txt)\nA valid filename cannot include * . " / \ [ ] : ; | ,')
                continue
            break
        
        # splits inputfiles by \n new lines, if file has no line breaks it is considered as one expression

        input_file = input_file.splitlines()
               
        # sorting prompt
        sort_method = self.__print_sort_selection()
        ascending_check = self.__print_asc_check()
        sort_by = self.__print_sort_by_selection()

        sort_by_value = None
        if sort_by == "2":
            while True:
                sort_by_value = input('\nPlease enter the value (operator/number) you want to sort by:\n')
                try:
                    sort_by_value = sort_by_value.replace(' ', '')
                    if sort_by_value == "":
                        raise Exception("Please input a value")
                    tokenizer = Tokenizer(sort_by_value)
                    sort_by_value = list(tokenizer.generate_tokens())
                    if len(sort_by_value) > 1:
                        raise Exception("Value cannot be an expression")
                except Exception as e:
                    sort_by_value = None
                    print('Invalid input, ' + str(e))
                    continue
                break
            sort_by_value = sort_by_value[0]

        print("\n\n>>>Evaluation and sorting started:\n")

        # parses and evauates the input_file after splitting to an array by line breaks
        exp_list = self.__parsefile(input_file, sort_method, ascending_check, sort_by_value)
        
        # defining variables for printing
        current_val = None
        print_str = ""

        # building of final print and output write string
        if sort_by_value == None:
            for i in range(len(exp_list)):
                # if the current value not yet been printined print
                if current_val != exp_list[i].val:
                    print_str+= "\n\n*** Expressions with value= {:.3f}\n".format(exp_list[i].val)
                    current_val = exp_list[i].val
                # always prints expression=>value
                print_str += ("{}==>{:.3f}\n".format(str(exp_list[i]), exp_list[i].val))
        else:
            for i in range(len(exp_list)):
                # if the current value not yet been printined print
                if current_val != exp_list[i].sort_value_count():
                    print_str+= "\n\n*** Expressions with a total of {}x '{}'s\n".format(exp_list[i].sort_value_count(), sort_by_value)
                    current_val = exp_list[i].sort_value_count()
                # always prints expression=>value
                print_str += ("{}==>{:.3f}\n".format(str(exp_list[i]), exp_list[i].val))

        # prints actual output
        print(print_str)

        # writing output to file
        output_file.write(print_str)
        output_file.close()

        print("\n\n>>>Evaluation and sorting completed!")
            

    def get_current_selection(self):
        return self.__current_selection

    # Private functions___________________________________________________________________________________________________________________________
    
    # Parses input file to expressions
    def __parsefile(self, input_file, sort_method, ascending_check, sort_by_value):
        # checks for sorting method and creates object accordingly
        if sort_method == "1":
            exp_list = SortedList(ascending_check)
        elif sort_method == "2":
            exp_list = []

        for i in range(len(input_file)):
            try:
                input_file[i].replace(' ', '')
                expression = Expression(input_file[i])
                expression.parse_tree()
                expression.set_sort_value(sort_by_value)
            except Exception as e:
                print("\nInvalid expression at line "+str(i+1)+". Skipping expression")
                print(e)
                continue
            if sort_method =="1":
                exp_list.insert(expression)
            elif sort_method =="2":
                exp_list.append(expression)

        if sort_method == "2":
           sort_expressions(exp_list, ascending_check)
        return exp_list

    # Prompts for 
    def __print_sort_by_selection(self):
        sort_by_selection = None

        #built prompt
        prompt = "\nPlease select your choice ('1','2')"
        prompt += '\n   1. Sort by value then length'
        prompt += '\n   2. Sort by count of user input'
        prompt += '\nEnter choice: '

        #input and check for 1 2 or 3
        while sort_by_selection not in ['1', '2']:
            sort_by_selection = input(prompt)
            if sort_by_selection not in ['1', '2']:
                print("Invalid input. Please input either '1' or '2'\n")
        
        return sort_by_selection

    # Prompts for print order selection
    def __print_order_selection(self):
        orderprint_selection = None

        #built prompt
        prompt = "\nPlease select your choice ('1','2','3')"
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

    # prompts sort
    def __print_sort_selection(self):
        #built prompt
        prompt = "\nPlease select your choice ('1','2')"
        prompt += '\n   1. Sorted list'
        prompt += '\n   2. Merge sort'
        prompt += '\nEnter choice: '

        sort_method = None

        #input and check for 1, 2
        while sort_method not in ['1', '2']:
            sort_method = input(prompt)
            if sort_method not in ['1', '2']:
                print("Invalid input. Please input either '1' or '2'\n")
        return sort_method
        
    #prompts sort type
    def __print_asc_check(self):
        #built prompt
        prompt = "\nPlease select your choice ('1','2')"
        prompt += '\n   1. Sort ascending'
        prompt += '\n   2. Sort descending'
        prompt += '\nEnter choice: '

        ascending_check = None

        #input and check for 1, 2
        while ascending_check not in ['1', '2']:
            ascending_check = input(prompt)
            if ascending_check not in ['1', '2']:
                print("Invalid input. Please input either '1' or '2'\n")
        return ascending_check
