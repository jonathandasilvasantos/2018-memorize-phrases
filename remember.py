import sys
import numpy as np
import pickle
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

    if len(second_sentences) != len(first_sentences):
        print("The number of sentences in both files need to be the same.")
        return

    probabilities = []
    indexes = []
    for i in range(0, len(first_sentences)):
        probabilities.append(100)
        indexes.append(i)

    while(True):
        pick_index = np.random.choice(indexes, 1, probabilities)
        index = pick_index[0]
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
            probabilities[index] -= 1
            print("correct!")
        else:
            probabilities[index] += 1
            wrong += 1
            print(b)

        if len(response) <= 0:
            break



if __name__ == '__main__':
        main()
