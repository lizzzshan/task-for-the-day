import sys, random

tasks = ["Go to gym", "Do an easy Leetcode question", "Do a medium Leetcode question", "Meditate", "Journal", "Go for a walk"]
time = ["30 mins", "40 mins", "50 mins", "1 hour", "1 hour 30 mins"]
def welcomeMessage():
    print("Hello! Welcome to task generator! \n")
    #TODO: add more explanation here

#this function chooses a random task from it's array
#parameters take in user input, using task array as global variable
def choosetask():
    while True:
        print("Your task for the day is to:\n ", random.choice(tasks), " for ", random.choice(time))
        try_again = input("\nTry again? (Press Enter else n to quit)\n" )
        if try_again.lower() == "n":
            break
    input("\nPress Enter again to exit.")

def main():
    welcomeMessage()
    choosetask()
if __name__ == "__main__":
    main()