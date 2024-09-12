from data import Report, CheckForQuantity

machine_continue = True
report = Report()
coffee_machine = CheckForQuantity()
while machine_continue:
    user_choice = input("What would you like? ")
    if user_choice == "off":
        machine_continue = False
    elif user_choice == "report":
        report.report()
    else:
        coffee_machine.check_for_quantity(user_choice)
        coffee_machine.coin_processing(user_choice)
        coffee_machine.coffee_processing(user_choice)
