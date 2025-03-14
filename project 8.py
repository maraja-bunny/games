#python quiz games
questions=('how many elements are in the periodic table?:',
           'which animal lays the largest eggs?',
           'what is the most abudant gas in earth surface?:',
           'how many bones are in the humanbody?:',
           'which planet in the solar system is the hottest?:')
options=(('A.116','B.117','C.118','D.119'),
         ('A.WHALE','B.CROCODILE','C.ELEPHANT','D.OSTRICH'),
         ('A.NITROGEN','B.OXYGEN','C.CARBON DIOXIDE','D.HYDROGEN'),
         ('A.206','B.207','C.208','D.209'),
         ('A.MERCURY','B.VENUS','C.EARTH','D.MARS'))
answers=('C','D','A','A','B')
guesses=[]
score=0
question_num=0
for question in questions:
    print('------------------')
    print(question)
    for option in options[question_num]:
        print(option)

    guess=input('Enter(A,B,C,D):').upper()
    guesses.append(guess)
    if guess==answers[question_num]:
        score+=1
        print('CORRECT')
    else:
        print('INCORREECT') 
        print(f'{answers[question_num]} is the correct answer')   
    question_num +=1 
print('---------------')
print('        results     ') 
print('----------------')     
print('answers:',end='')
for answer in answers:
    print(answer,end="")
print() 
score=int(score/len(questions)*100)
print(f'your score is:{score}%')   