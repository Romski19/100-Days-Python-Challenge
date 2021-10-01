from art import logo
from replit import clear



def add(n1,n2):
  return n1 + n2

def subtract(n1,n2):
  return n1 - n2

def multiply(n1,n2):
  return n1 * n2
  
def divide(n1,n2):
  return n1 / n2
  
operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
  }

#recursive function

def calculations():
  print(logo)

  num1 = float(input("What's the first number: "))

  for symbol in operations:
    print(symbol)

  to_continue = True
  while to_continue:

    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number: "))
    calc_function = operations[operation_symbol]
    answer = calc_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}" )
    
    continue_this = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculations: ").lower()

    if continue_this == "y":
      num1 = answer
    else:
      to_continue = False
      clear()
      calculations()

calculations()