""" This is the main file for this program, my trivia game.
__author__ = "Christopher Bryan" """


def question(question_text, question_answer):
    """ This function both asks the user the trivia question, and checks
    whether they got it correct. If they improperly formatted their answer, it
    tells them and has them try the question again.
    :param question_text: This is the text of the question that will be asked.
    :param question_answer: This is the answer to said question.
    :return: This function returns whether the answer is correct or not. """
    input_is_not_valid = True
    score = 0
    while input_is_not_valid:
        print(question_text)
        user_input = input("Your answer (upper or lower case A, B, C, or D):"
                           " ").capitalize()
        if user_input == question_answer:
            score = 1
            input_is_not_valid = False
        elif user_input == "A" or user_input == "B" or user_input == "C"\
                or user_input == "D":
            score = 0
            input_is_not_valid = False
        else:
            print("Your answer is either not a letter or not A, B, C, or D,"
                  " try again.")
    return score


def main():
    """ This is the main function of the program. It asks the user their name,
    greets them by name, stores all of the questions to ask the user alongside
    their answers, runs the question function, stores the number of questions
    asked and correct answers received, and tells the user the how many
    questions they got right out of the total asked of them.
    :return: No values are returned.
    """
    your_name = input("Enter your name: ")
    print('Welcome to my trivia game,',
          your_name + '! Be prepared to be challenged!')

    correct_total = 0
    total_done = 0

    question_list = ['The Statue of Liberty was given to the US by: '
                     '(A. Britain   B. Spain   C. Canada   D.France) ',
                     'How many have athletes have died in the modern olympics:'
                     ' (A. 5   B. 10   C. 30   D. 15) ',
                     'Which desert is largest: (A. Antarctica   B. Sahara   '
                     'C. Gobi   D. Great Victoria) ',
                     'How many sides does a Toblerone have: (A. 23   B. 38   '
                     'C. 41   D. 5) ',
                     'Which of these is not a berry: (A. Blueberry   '
                     'B. Strawberry   C. Eggplant   D. Banana) ']

    answer_list = ['D', 'B', 'A', 'B', 'B']

    while total_done < 5:
        correct_total += question(question_list[total_done],
                                  answer_list[total_done])
        total_done += 1

    print(your_name + "'s score: ", correct_total, '/', total_done)


main()
