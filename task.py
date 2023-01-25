import random
#global variable task array
tasks = ["Go to gym", "Do an easy Leetcode question", "Do a mediun Leetcode question", "Meditate", "Journal", "Go for a walk"]

def welcomeMessage():
    print("Hello! Welcome to task generator! \n")
    #TODO: add more explanation here

#this function gets user input upon initialization
#TODO: Turn this into a menu with number input as options
def getInput():
    val = input("Enter a number between 1-10: ")
    number = int(val)
    if number in range(1,10):
        print("You have chosen ", number)
    else:
        print("Oops! Your option is invalid!")
    return number

#this function chooses a random task from it's array
#parameters take in user input, using task array as global variable
def choosetask(input: int):
    print(random.choice(tasks))
def main():
    welcomeMessage()
    num = getInput()
    choosetask(num)
if __name__ == "__main__":
    main()