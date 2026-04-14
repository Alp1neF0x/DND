import random

def read_file(filename):
    with open(filename, 'r') as file:
        quote_list = file.readlines()
    return quote_list

def check_for_lowroll(roll, quote_list):
    if roll <= 5:
        quote = random.choice(quote_list)
        return quote.strip()
    return None


def role_d4():
    return random.randint(1, 4)
    
def role_d6():
    return random.randint(1,6)
    
def role_d8():
    return random.randint(1,8)

def role_d10():
    return random.randint(1,10)

def role_d12():
    return random.randint(1, 12)

def role_d20():
    return random.randint(1, 20)

def choose_dice(quote_list):
    choice= input("Choose Dice Roll: \n 4 is D4 \n 6 is D6 \n 8 is D8 \n 10 is D10 \n 12 is D12 \n 20 is D20 \n q to quit \n Can I role to seduce the dragon: \n")
    if choice  == "q":
        return False
    dice_number = int(choice)
    if dice_number == 4:
        print(f" the number you rolled is: {role_d4()}")
    elif dice_number == 6:
        print(f" the number you rolled is: {role_d6()}")
    elif dice_number == 8:
        print (f"The number you rolled is: {role_d8()}")
    elif dice_number == 10:
        print(f" the number you rolled is: {role_d10()}")
    elif dice_number == 12:
        print(f" the number you rolled is: {role_d12()}")
    elif dice_number ==20:
        roll = role_d20()
        print(f"the number you rolled is: {roll} \n ")
        quote = check_for_lowroll(roll, quote_list)
        if quote:
            print(quote)
    else:
        dice_number = input("The only complication here is your lack of ability to speak Common. Enter a proper dice roll or have a cup of tea: \n")
    return True

def main():
     quote_list = read_file("lowroll.txt")
     while True:
         if not choose_dice(quote_list):
             print("My steel, unbendable. My will, unbreakable. Thank you for rolling")
             break
    

if __name__ == "__main__":
     main()





