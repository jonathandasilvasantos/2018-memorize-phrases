import sys
from random import randint

def normalize(line):
    line = line.replace('.', '')
    line = line.lower()
    line = line.replace('?','')
    line = line.replace('!','')
    return line

def main():

    firstfile = sys.argv[1]
    secondfile = sys.argv[2]


    correct = 0
    wrong = 0


    first_sentences = []
    second_sentences = []
    with open(firstfile, 'r') as filereader:
        for line in filereader.read().split('\n'):
            if len(line) > 0:
                first_sentences.append(normalize(line))

    with open(secondfile, 'r') as filereader:
        for line in filereader.read().split('\n'):
            if len(line)> 0:
                second_sentences.append(normalize(line))

    while(True):
        index = randint(0, len(first_sentences)-1)
        a_sentence = first_sentences[index]
        b_sentence = second_sentences[index]
        a = a_sentence
        b = b_sentence
        
        if randint(0,1) == 0:
            a = b_sentence
            b = a_sentence

        score_str = "correct: " + str(correct) + " wrong: " + str(wrong)
        print(score_str)
        print(a)
        response = input()
        response = normalize(response)

        if response.replace(' ', '') == b.replace(' ', ''):
            correct += 1
            print("correct!")
        else:
            wrong += 1
            print(b)

        if len(response) <= 0:
            break



if __name__ == '__main__':
        main()
