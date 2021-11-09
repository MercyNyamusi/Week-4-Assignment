def count_wrongs(count):
    """
    function to tell the player the number of mistakes made
    :param count: the number of wrong answers

    """
    if count == 0:
        print("Congratulations!!!Your man lives.")
    elif count == 1:
        print(f"Your man lives! You made {count} mistake")
    elif count < 6:
        print(f"Your man lives! You made {count} mistakes")
    else:
        print(f"Sorry your man is dead:( You made {count} mistakes")


def quiz():
    """
    function that takes the players answer, compares it to the correct answer
    and counts the number of wrong answers given
    """
    wrong_count = 0
    # a dictionary of the question numbers and the questions asked during the game
    questions = {"Question 1": "When was ALU founded?",
                 "Question 2": "Who is the CEO of ALU?",
                 "Question 3": "Where are ALU campuses?(Please use 'and' as the conjunction)",
                 "Question 4": "How many campuses does ALU have?",
                 "Question 5": "What is the name of ALU Rwanda’s Dean?",
                 "Question 6": "Who is in charge of Student Life?",
                 "Question 7": "What is the name of our Lab?",
                 "Question 8": "How many students do we have in Year 2 CS?",
                 "Question 9": "How many degrees does ALU offer?",
                 "Question 10": "Where are the headquarters of ALU?"}
    # a dictionary of the question numbers and the answers to the questions asked during the game
    answers = {"Question 1": "2015", "Question 2": "fredswaniker",
               "Question 3": ["rwandaandmauritius", "mauritiusandrwanda"],
               "Question 4": "2", "Question 5": "mimimutoni", "Question 6": "silaogidi", "Question 7": "fablab",
               "Question 8": "90", "Question 9": "8", "Question 10": "mauritius"}
    # a loop to go through the questions and compare the user input to the given answers
    for i in questions:
        # removes all spaces in the user input and converts i to lower case
        ans = input(i + "\n" + questions[i]).strip().lower().split()
        # concatenates the elements of the list while removing all spaces
        formatted_ans = "".join(ans)
        # checks whether answer by user is correct by comparing it to the provided answer
        if i == "Question 3" and (formatted_ans == answers[i][0] or formatted_ans == answers[i][1]):
            print("CORRECT")
        elif formatted_ans == answers[i]:
            print("CORRECT")
        else:
            print("You're hanging the man")
            wrong_count += 1
        # checks if user has made six mistakes
        if wrong_count > 5:
            break
    # calls the count_wrongs function with the number of mistakes as the argument
    count_wrongs(wrong_count)


def hangman_game():
    """
    function to start the game

    """
    print("Welcome to ALU Hangman!!!\nMay the games begin!!")
    quiz()
    print("Thank you for playing. See you next time!!")


hangman_game()
