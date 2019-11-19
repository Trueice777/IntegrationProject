# Christopher Bryan
# This is my trivia game.

def question(questionText, questionAnswer):
    answerValid = False
    while answerValid == False:
        print(questionText)
        x = input("Your answer (upper or lower case A, B, C, or D): ").capitalize()
        if x == questionAnswer:
            return 1
            answerValid = True
        elif x == "A" or x == "B" or x == "C" or x == "D":
            return 0
            answerValid = True
        else:
            print("Your answer is either not a letter or an invalid one, try again.")

def main():
    yourName = input("Enter your name: ")
    print('Welcome to my trivia game,', yourName + '! Be prepared to be challenged!')

    correctTotal = 0
    totalDone = 0

    questionList = ['The Statue of Liberty was given to the US by: (A. Britain   B. Spain   C. Canada   D.France) ',
                    'How many have athletes have died in the modern olympics: (A. 5   B. 10   C. 30   D. 15) ',
                    'Which desert is largest: (A. Antarctica   B. Sahara   C. Gobi   D. Great Victoria) ',
                    'How many sides does a Toblerone have: (A. 23   B. 38   C. 41   D. 5) ',
                    'Which of these is not a berry: (A. Blueberry   B. Strawberry   C. Eggplant   D. Banana) ']

    answerList = ['D', 'B', 'A', 'B', 'B']

    while totalDone < 5:
        correctTotal += question(questionList[totalDone], answerList[totalDone])
        totalDone += 1

    print(yourName + "'s score: ", correctTotal, '/', totalDone)

main()
