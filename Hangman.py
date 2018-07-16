"""Hangman game
    By Michael Lenghel"""
import random
import webbrowser
class hangman:
    def __init__(self):
        with open("hangmanWords.txt", "r", encoding="utf-8", errors="ignore") as f:
            # Counts the number of lines in the file
            num_lines = f.read().count('\n')
            # Sets a random integer from 1 to the end of the file
            line_num = random.randint(1, num_lines)
            # Set the file back to the first bit
            f.seek(0, 0)
            for index, line in enumerate(f):
                if line_num == index:
                    self.word = f.readline()
                    # Slice off the trailing \n character at the end which f.readline takes!!
                    self.word = self.word[:-1]
                    self.replay = True
                    break
            # Set a list of bools for each letter in the word
            self.letters = [False] * len(self.word)
            self.lives = 6
            self.print_word()

    def print_word(self):
        for index, line in enumerate(self.word):
            if self.letters[index]:
                print(self.word[index], end=" ")
            else:
                print("_", end=" ")
        print()

    def google_def(self):
        url = "https://www.google.com.tr/search?q={} {}".format("definition of", self.word)
        webbrowser.open(url, new=2)
        # x = urllib.request.urlopen(urllink.url)
        # print(x.read())                                                                                                                                                                                           

def play_game():
    game = hangman()
    score = 0
    letter_match = False

    while game.replay:
        while game.lives != 0:
            user_guess = input("Enter a letter or a full word to guess \n")

            if user_guess == game.word:
                print("You won the game!!!! 10 points")
                score += 10
                print("Score = ", score)
                break
            elif len(user_guess) == 1:
                for index, c in enumerate(game.word):
                    if user_guess == c:
                        # Make sure don't guess same letter twice
                        if not game.letters[index]:
                            game.letters[index] = True
                            letter_match = True
            if not letter_match:
                game.lives -= 1
                print("Lives left: ", game.lives)
                print("Unlucky guess :()")
            # Reset letterMatch
            letter_match = False
            game.print_word()

        while game.replay:
            print("The word was ", game.word, "!", sep="")
            getDef = input("Enter 0 to search for the term, or any other key to skip definition lookup\n")
            if getDef == '0' or getDef == 'o's:
                game.google_def()
            check = input("Do you want to play again? \"Y\" = Yes \"N\" = No \n")
            if check == 'Y' or check == 'y':
                game = hangman()
                break
            elif check == 'N' or check == 'n':
                game.replay = False
            else:
                print("Invalid input, try again")
        


play_game()



