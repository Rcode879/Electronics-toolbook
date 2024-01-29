#Resistor colour code calculator
#intro
print("Welcome to the resistor colour code calculator!") 
print("This simple program will help you work out the value of your resistor without using any of those silly acronyms!")
#defining colour values:
colours = {
            "black": 0,
            "brown": 1,
            "red": 2,
            "orange": 3, 
            "yellow": 4,
            "green": 5,
            "blue": 6,
            "violet": 7,
            "grey": 8,
            "white": 9,

          }

#creating functions to find the values of different band resistors:
def four_bands(col): #if a resistor is 4 band, the last band is tolerance
    inks = []
    counter = 0
    while counter < 3:
        counter += 1
        print(f"please enter band {counter}")
        temp = input("enter band colour:")
        temp.lower
        colours_matching = 0
        for key, value in colours.items():
            if temp == key:
                colours_matching += 1
        if colours_matching != 1:
            colours_matching = 0
            print("You must've mistyped one of the colours, please try again")
            counter = counter - 1
            continue
        else:

            inks.append(temp)


    multiplier = 10 ** col[inks[2]]
    dig1 = str(col[inks[0]])
    dig2 = str(col[inks[1]])
    digCon = dig1 + dig2
    digCon = int(digCon)
    resistance = digCon * multiplier
    print(f"your resistance is {resistance}")


def five_bands(col): #if a resistor is 6 band, the last 2 bands are tolerance and temperature coefficient
    inks = []
    counter = 0
    while counter < 4:
        counter += 1
        print(f"please enter band {counter}")
        temp = input("enter band colour:")
        temp.lower
        colours_matching = 0
        for key, value in colours.items():
            if temp == key:
                colours_matching += 1
        if colours_matching != 1:
            colours_matching = 0
            print("You must've mistyped one of the colours, please try again")
            counter = counter - 1
            continue
        else:

            inks.append(temp)

    multiplier = 10 ** col[inks[3]]
    dig1 = str(col[inks[0]])
    dig2 = str(col[inks[1]])
    dig3 = str(col[inks[2]])
    digCon = dig1 + dig2 + dig3
    digCon = int(digCon)
    resistance = digCon * multiplier
    print(f"your resistance is {resistance}")

   

#main menu:
while True:
    while True:
        try:
            band_num = int(input("Please enter the number of bands your resistor has (excluding tolerance and temperature coefficient):")) 
            while band_num not in range(3,5):
                print("please enter either 3 or 4")
                band_num = int(input("Please enter the number of bands your resistor has (excluding tolerance and temperature coefficient):"))
        except ValueError:
            print("enter an integer!")
            continue
        else:
            break
    if band_num == 3:
        four_bands(colours)
        continue
    if band_num == 4:
        five_bands(colours)
           
