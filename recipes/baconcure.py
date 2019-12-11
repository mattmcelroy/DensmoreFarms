# Densmore Farms recipe for bacon cure
# Original recipe from Project Smoke by Steven Raichlen

def cure_recipe(belly):
    salt = belly * 15
    sugar = belly * 20
    pepper = belly * 6.5
    pink = belly * 3
    print("{:>3.0f} g salt".format(salt))
    print("{:>3.0f} g sugar".format(sugar))
    print("{:>3.0f} g black pepper".format(pepper))
    print("{:>3.0f} g pink salt".format(pink))
    
def cure_combined(belly):
    salt = belly * 15
    sugar = belly * 20
    pepper = belly * 6.5
    pink = belly * 3
    
    total_grams = 0
    total_grams += salt
    print ("{:>3.0f} g salt".format(total_grams))    
    total_grams += sugar
    print("{:>3.0f} g sugar".format(total_grams))
    total_grams += pepper
    print("{:>3.0f} g pepper".format(total_grams))
    total_grams += pink
    print("{:>3.0f} g pink salt".format(total_grams))

# input the pounds of the pork belly to be cured
belly = float(input("How many pounds pork belly?: "))
# recipe output
print()
print("Recipe")
cure_recipe(belly)
print()  
print("Combined")
cure_combined(belly)
print()
