# Christopher Bryan
# This is my trivia game.


def question(questionText, questionAnswer):
    x = raw_input(questionText)
    if x == questionAnswer:
        return 1
    else:
        return 0


print('Welcome to my trivia game! Be prepared to be challenged!')

correctTotal = 0
totalDone = 0

questionList = ['The Statue of Liberty was given to the US by: (A. Britain B. Spain C. Canada D.France) ',
                'How many have athletes have died in the modern olympics: (A. 5   B. 10   C. 30   D. 15) ']

answerList = ['D', 'B']

while totalDone < 2:
    particularQuestion = questionList[totalDone]
    particularAnswer = answerList[totalDone]
    correctTotal += question(particularQuestion, particularAnswer)
    totalDone += 1

print('Your score: ', correctTotal, '/', totalDone)

      

      

