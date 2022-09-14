# convert.py
#
# User inputs speed in mph
# Program outputs speed in kph, ft/s, m/s depending on user choice.
#
# Three functions are defined, each with 1 parameter and returning a value:
#   mph -> kph
#   mph -> ft/s
#   mph -> m/s

# Functions
def mph_to_kph(mph):
    return 1.609*mph

def mph_to_ms(mph):
    return mph_to_kph(mph)*1000/3600

def mph_to_fts(mph):
    return mph*5280/3600

# Input
mph = input("Input speed in mph: ")
mph = float(mph)

# Menu
print("Thank you!")
print("The speed you have input is " + str(mph) + " Miles per Hour.")
print("Please input whether you would like your speed in")
print("1) Kilometers per Hour")
print("2) Feet per Second")
print("3) Meters per Second")
selection = float(input())

# Output
if selection == 1:
    print("Speed in kph is", mph_to_kph(mph))
elif selection == 2:
    print("Speed in m/s is", mph_to_ms(mph))
elif selection == 3:
    print("Speed in ft/s is", mph_to_fts(mph))
else:
    print("That's not a valid choice, sorry!")





