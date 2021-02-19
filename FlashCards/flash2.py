import os, random

count = 0
score = 0

file_q = open('questions1.txt', 'r')
file_a = open('answers2.txt', 'r')
file_r = open('answers1.txt', 'r')

f1content = file_q.readlines()
f2content = file_a.readlines()
f3content = file_r.readlines()


while count < 10:
    os.system('clear')

    wordnum = random.randint(0, len(f1content)-1)
    print('FLASH CARDS ------ Kubernetes Glossary ------')
    print('\ndef: ', f1content[wordnum], '')

    options = [random.randint(0, len(f2content)-1),
        random.randint(0, len(f2content)-1),
        random.randint(0, len(f2content)-1)]

    options[random.randint(0, 2)] = wordnum

    print('1 -', f2content[options[0]])
    print('2 -', f2content[options[1]])
    print('3 -', f2content[options[2]])

    answer = input('\nYour Choice: ')
    print(answer)

    if answer[wordnum] in f2content:
        print('Correct!', f2content[wordnum], 'is correct')
        input('\n\nHit enter...')
        score = score + 1

    else:
        print('Wrong!', f2content[wordnum], 'is the correct answer')
        input('\n\nHit enter...')
        count = count + 1

        print('\nYour score is:', score)
