# Send Custom Message to list of people


# * = Include a varying number of arguments/values - xargs
# def CustomMessage(*names):
#     for name in names:
#         print(f"Hello and Welcome to you {name}")


# CustomMessage("Michael")
# CustomMessage("Joshua", "Caleb", "Moses", "Mariam", "Megue")



#Customers ---> Database ---> 1. Required Data, 2. Optional Data
#Customers will have a varying amount of data for each individual customer

# ** = Include a varying number of KEYWORD arguments - xxargs
def CustomerData(**data):
    print(data)
    
    
CustomerData(name="Joshua", secret="Joshua") #Which one is which
CustomerData(name="Caleb", secret="Mouse", email="caleb@hotmail.com")
#{'name': 'Joshua', 'secret': 'Joshua'}