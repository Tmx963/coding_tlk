START

DEFINE function play_round:
    PROMPT user to enter a choice (rock, paper, or scissors)
    STORE computer's choice randomly from ["rock", "paper", "scissors"]
    DISPLAY both choices

    IF user_choice == computer_choice:
        DISPLAY "It's a tie!"
    ELSE IF user_choice is "rock":
        IF computer_choice is "scissors":
            DISPLAY "You win!"
        ELSE:
            DISPLAY "You lose."
    ELSE IF user_choice is "paper":
        IF computer_choice is "rock":
            DISPLAY "You win!"
        ELSE:
            DISPLAY "You lose."
    ELSE IF user_choice is "scissors":
        IF computer_choice is "paper":
            DISPLAY "You win!"
        ELSE:
            DISPLAY "You lose."
    ELSE:
        DISPLAY "Invalid input."

REPEAT
    CALL play_round
    PROMPT user to play again (y/n)
UNTIL user says "n"

DISPLAY "Thanks for playing!"
END
