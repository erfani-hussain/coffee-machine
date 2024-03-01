from data import MENU, resources, profit
from art import logo


# FUNCTIONS
# TODO 4. Check resources sufficient?
def is_resources_sufficient(order_ingredients):
  """Returns True if the order can be made, False if ingredients are insufficient"""
  for key in order_ingredients:
    if order_ingredients[key] > resources[key]:
      print(f"Sorry there is not enough {key}.")
      return False
    else:
      return True

# TODO 5. Process coins.
def process_coins():
  """Returns the total calculated from coins inserted."""
  print("Please insert coins.")
  total = int(input("How many quarters?: ")) * 0.25
  total += int(input("How many dimes?: ")) * 0.1
  total += int(input("How many nickles?: ")) * 0.05
  total += int(input("How many pennies?: ")) * 0.01
  return total

# TODO 6. Check transaction successful?
def is_transaction_successful(money_received, drink_cost):
  """Returns True when payment is accepted, or False if money is insufficient."""
  if money_received >= drink_cost:
    change = round(money_received - drink_cost, 2)
    print(f"Here is ${change} in change.")
    global profit
    profit += drink_cost
    return True
  else:
    print("Sorry that's not enough money. Money refunded.")
    return False

# TODO 7. Make Coffee.
def make_coffee(drink_name, order_ingredients):
  for key in order_ingredients:
    resources[key] -= order_ingredients[key]
  return f"Here is your {drink_name} ☕. Enjoy!"

# Print coffee logo
print(logo)

is_true = True
while is_true:
  # TODO 1. Prompt user by asking “​What would you like? (espresso/latte/cappuccino):​
  choice = input("What would you like? (espresso/latte/cappuccino): ")
  # TODO 2. Turn off the Coffee Machine by entering “​off​” to the prompt.
  if choice == "off":
    is_true = False
  # TODO 3. Print report.
  elif choice == "report":
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")
  else:
    drink = MENU[choice]
    if is_resources_sufficient(drink["ingredients"]):
      payment = process_coins()
      if is_transaction_successful(payment, drink["cost"]):
        print(make_coffee(choice, drink["ingredients"]))
