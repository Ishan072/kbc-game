from questions import QUESTIONS


def isAnswerCorrect(question, answer):
    if(question['answer']==answer):
        return True
    else:
        return False
    '''
    :param question: question (Type JSON)
    :param answer:   user's choice for the answer (Type INT)
    :return:
        True if the answer is correct
        False if the answer is incorrect
    '''




def lifeLine(ques):
    print(f'\t\tOptions:')
    if(ques['answer'])==1:
        print(f'\t\t\tOption 1: {ques["option1"]}')
        print(f'\t\t\tOption 4: {ques["option4"]}')
    if(ques['answer'])==2:
        print(f'\t\t\tOption 1: {ques["option1"]}')
        print(f'\t\t\tOption 2: {ques["option2"]}')
    if(ques['answer'])==3:
        print(f'\t\t\tOption 2: {ques["option2"]}')
        print(f'\t\t\tOption 3: {ques["option3"]}')
    if(ques['answer'])==4:
        print(f'\t\t\tOption 3: {ques["option3"]}')
        print(f'\t\t\tOption 4: {ques["option4"]}')
    
    ans = input('Your choice from above options : ')
    '''
    :param ques: The question for which the lifeline is asked for. (Type JSON)
    :return: delete the key for two incorrect options and return the new ques value. (Type JSON)
    '''
    
    return ans

def kbc():
    print("\tWELCOME TO THE GAME")
    print("\tLets Starts Playing")
    '''
        Rules to play KBC:
        * The user will have 15 rounds
        * In each round, user will get a question
        * For each question, there are 4 choices out of which ONLY one is correct.
        * Prompt the user for input of Correct Option number and give feedback about right or wrong.
        * Each correct answer get the user money corresponding to the question and displays the next question.
        * If the user is:
            1. below questions number 5, then the minimum amount rewarded is Rs. 0 (zero)
            2. As he correctly answers question number 5, the minimum reward becomes Rs. 10,000 (First level)
            3. As he correctly answers question number 11, the minimum reward becomes Rs. 3,20,000 (Second Level)
        * If the answer is wrong, then the user will return with the minimum reward.
        * If the user inputs "lifeline" (case insensitive) as input, then hide two incorrect options and
            prompt again for the input of answer.
        * NOTE:
            50-50 lifeline can be used ONLY ONCE.
            There is no option of lifeline for the last question( ques no. 15 ), even if the user has not used it before.
        * If the user inputs "quit" (case insensitive) as input, then user returns with the amount he has won until now,
            instead of the minimum amount.
    '''

    #  Display a welcome message only once to the user at the start of the game.
    #  For each question, display the prize won until now and available life line.
    # For now, the below code works for only one question without LIFE-LINE and QUIT checks
    amount=0
    count_life=0
    for i in range(0,15):
        print('\tQuestion',i+1,f' : {QUESTIONS[i]["name"]}' )
        print(f'\t\tOptions:')
        print(f'\t\t\tOption 1: {QUESTIONS[i]["option1"]}')
        print(f'\t\t\tOption 2: {QUESTIONS[i]["option2"]}')
        print(f'\t\t\tOption 3: {QUESTIONS[i]["option3"]}')
        print(f'\t\t\tOption 4: {QUESTIONS[i]["option4"]}')
        ans = input('Your choice ( 1-4 ) : ')

        # check for the input validations

        if ans.upper()=='LIFELINE' and count_life!=1:
            count_life+=1
            if(i==14):
                print("\nYou dont able to use lifeline for this question")
            else:
                ans=lifeLine(QUESTIONS[i])

        if ans.upper()=='QUIT':
            break
        if isAnswerCorrect(QUESTIONS[i], int(ans) ):
            # print the total money won.
            # See if the user has crossed a level, print that if yes
            print('\nCorrect !')
            amount=amount+ int(f'{QUESTIONS[i]["money"]}')
            print("\n\t Current amount won",amount)
        else:
            # end the game now.
            # also print the correct answer
            print('\n\tIncorrect !')
            print(f'\n\tCorrect Answer is {QUESTIONS[i]["answer"]}')
            if(i<5):
                amount=0
            elif(i>=5 and i<11):
                amount=1000
            elif(i>=11 and i<=15):
                amount=320000
            break
    print("\n\tTotal amount won",amount)

        # print the total money won in the end.


kbc()
