from CLInterface import CLInterface

cli = CLInterface()
    
while True:
    cli.selection_menu_prompt()
    if (cli.get_current_selection() == '1'): 
        cli.evaluate_expression()
        input("Press enter to continue... ")
    elif (cli.get_current_selection() == '2'):
        cli.sort_evaluate_expression()
        input("Press enter to continue... ")
    elif (cli.get_current_selection() == '3'):
        break