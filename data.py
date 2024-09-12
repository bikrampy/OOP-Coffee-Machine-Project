types_of_coffee = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
        },
        "price": 1.50
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150
        },
        "price": 2.50
    },
    "capuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100
        },
        "price": 3.50
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}
money = 0


class Report:
    def report(self):
        print(f"Water: {resources["water"]}")
        print(f"Milk: {resources["milk"]}")
        print(f"Coffee: {resources["coffee"]}")
        print(f"Total Profit: ${money}")


class CheckForQuantity:
    def __init__(self):
        self.less_quantity = False

    def check_for_quantity(self, user_choice_1):
        for items in types_of_coffee[user_choice_1]["ingredients"]:
            if types_of_coffee[user_choice_1]["ingredients"][items] > resources[items]:
                print(f"Sorry, not enough {items}")
                self.less_quantity = True

    def coin_processing(self, user_choice_1):
        if not self.less_quantity:
            no_of_penny = int(input("Penny?"))
            no_of_nickel = int(input("Nickel?"))
            no_of_dime = int(input("Dime?"))
            no_of_quarter = int(input("Quarter?"))
            total_amount = (0.01 * no_of_penny) + (0.05 * no_of_nickel) + (0.1 * no_of_dime) + (0.25 * no_of_quarter)
            if total_amount < types_of_coffee[user_choice_1]["price"]:
                print("Sorry, that's not enough money. Money refunded.")
            else:
                refund = total_amount - types_of_coffee[user_choice_1]["price"]
                print(f"Here's your ${refund} change.")

    def coffee_processing(self, user_choice_1):
        if not self.less_quantity:
            resources["water"] -= types_of_coffee[user_choice_1]["ingredients"]["water"]
            resources["coffee"] -= types_of_coffee[user_choice_1]["ingredients"]["coffee"]
            resources["milk"] -= types_of_coffee[user_choice_1]["ingredients"]["milk"]
            global money
            money += types_of_coffee[user_choice_1]["price"]
            print(f"Here's your {user_choice_1}")
        self.less_quantity = False
