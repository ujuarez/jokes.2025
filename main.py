name = input("What is your name? ") # Asks for User's name.
print(f"Welcome {name}!")  # Welcomes the User.

joke = input("Do you want to hear a joke? ")    # Asks the User if they'd like to hear a joke.
joke = joke.lower() # Makes "joke" input lowercase, which allows for all inputs to be recognized no matter the capitilization.
if joke == "no":
    print("Okay suit yourself!")
while joke == "yes":
    print("Great, Let's Play")
    question = input("Do you want to hear a joke about robbers, tanks, or pencils? ") # Gives the User 3 joke options to choose from
    question = question.lower() # Makes "question" input lowercase, which allows for all inputs to be recognized no matter the capitilization.
    
    if question == "robbers": # Joke Option #1.
        input("Knock Knock ")
        input("Calder ")
        print("Calder police - I've been robbed!")
        joke = input("Do you want to hear another joke or are you finished? ")  # Asks the User if they'd like to listen to another joke
        
    elif question == "tanks": # Joke Option #2.
        input("Knock Knock ") 
        input("Tank ")
        print("You are welcome!")
        joke = input("Do you want to hear another joke or are you finished? ")  # Asks the User if they'd like to listen to another joke

    elif question == "pencils": # Joke Option #3.
        input("Knock Knock ")
        input("Broken pencil ")
        print("Nevermind, it's pointless!")
        joke = input("Do you want to hear another joke or are you finished? ")  # Asks the User if they'd like to listen to another joke

def scoring_process(scoring): # Function for scoring process.
        final_score = [] # Purpose: Empty List for the User's score of the game, which allows the scoring process to have a result.

        for score in scoring:
            if joke == "finished":
               score = int((scoring * 10)) 
               final_score.append(score)
               
        return final_score
scoring = input("Please rate our game 1-10! ") # Asks for User's rating.
result = scoring_process(scoring)
print((result), " percent satisfaction rate") # Prints out function result.

if int(result) > 70:
        friend = input("Glad to hear you enjoyed the game! Would you recommend this game to a friend? ") # Asks User if they would recommend this game.
else:
        unfortunate = input("Sad to hear that you didn't enjoy the game.")
if friend == "yes" or friend == "maybe":
        print("Thanks, we appreciate it. ") # If YES or MAYBE, then this will display.
else:
        print("That's okay. ") # If OTHER ANSWER, then this will display.