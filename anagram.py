"""
Anagram python file to read a file into a python dictionary and produce the outputs for the inputs.
file name: anagram.py
author: Chen Lin
"""


def read_file(d1):
    """
    read file function to read the file into a python dictionary
    :param d1: a dictionary
    """
    with open('american-english.txt', encoding="utf=8") as fp:
        for line in fp:
            line = line.strip()
            lst = list(line)
            lst.sort()
            word = "".join(lst)
            if word in d1:
                d1[word].append(line)
            else:
                d1[word] = [line]


def corresponding_words(word, d1):
    """
    corresponding words function to find the corresponding word for an input string
    :param word: a word
    :param d1: a dictionary
    """
    lst = list(word)
    lst.sort()
    sorted_word = "".join(lst)
    if sorted_word in d1:
        return d1[sorted_word]


def number_of_words(length, d1):
    count = 0
    for word in d1:
        if len(word) == length:
            count = count + 1
        return count


def main():
    """
    a main function to produce the expected outputs for the dictionary
    """
    d1 = dict()
    read_file(d1)

    word = input('Enter input string: ')
    print('corresponding words: ', corresponding_words(word, d1))

    length = int(input('Enter word length: '))
    print('Number of jumble usable words of length', length, ':', number_of_words(length, d1))


if __name__ == '__main__':
    main()
