from CLInterface import CLInterface

cli = CLInterface()
cli.selection_menu_prompt()

print(cli.get_current_selection())
if (cli.get_current_selection() == '1'): 
    cli.evaluate_expression()