# juste_prix

1. The line from random import randint imports the randint function from the random module, which is used to generate a random number between two given values.

2. The line x = randint(1, 100) generates a random number x between 1 and 100. This is the number the user has to guess.

3. The life variable is initialized to 10. It represents the number of lives the user has to guess the correct number.

4. The while loop life > 0: is a while loop that continues as long as the user still has lives (i.e. as long as life is greater than zero).

5. At each turn of the loop, the program displays the number of lives remaining to the user with print(f"You have {life} lives left").

6. Then the program asks the user to input a number with rep = int(input("What's your number?")). The user's response is converted to an integer with int() and stored in the rep variable.

7. The program checks if the user's answer rep is equal to the random number x with if rep == x:. If so, the program displays "Congratulations, you passed the game!" with print("Congratulations, you have passed the game!") and the while loop ends with break.

8. If the user's answer rep is not equal to x, the program checks if it is greater than x with elif rep > x:. If so, it stores "large" in the status variable, otherwise it stores "small".

9. Then the program displays a message indicating whether the user's number is too large or too small with print(f"your number is too {status}").

10. The life variable is decremented by 1 with life -= 1 at each turn of the loop, which means that the user loses a life on each try.

11. The loop continues until the life reaches zero, in which case the loop ends.

12. After the end of the while loop, the program displays "You have lost". with print("You lost.") to indicate to the user that he has no more lives and has lost the game.
