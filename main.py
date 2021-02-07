from CLInterface import CLInterface

cli = CLInterface()
    
while True:
    cli.selection_menu_prompt()
    if (cli.get_current_selection() == '1'): 
        cli.evaluate_expression()
    elif (cli.get_current_selection() == '2'):
        cli.sort_evaluate_expression()
    elif (cli.get_current_selection() == '3'):
        break