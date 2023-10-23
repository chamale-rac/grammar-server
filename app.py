from src.grammar import Grammar
from src.utils.tools import readFile
import os


def main():
    file_path = input("Enter file path: ")
    if not os.path.isfile(file_path) or os.path.splitext(file_path)[1] != '.txt':
        print("Invalid file path or not a .txt file")
        return
    lines = readFile(file_path)
    grammar = Grammar(lines)
    index = 0
    print('Original read grammar:')
    print(grammar)
    print('-' * 50)
    grammar.CNF()
    while True:
        print("1. CNF")
        print("2. Phrase (CYK)")
        print("3. Exit")
        option = int(input(">> Enter choice (1-3): "))
        if option == 1:
            print('-' * 50)
            print(grammar)
            print('-' * 50)
        elif option == 2:
            sentence = input(">> Enter sentence: ")
            print('-' * 50)
            grammar.CYK(sentence, index=index, folder='./imgs/')
            print('-' * 50)
            index += 1
        elif option == 3:
            break
        else:
            print("Invalid option")


if __name__ == '__main__':
    main()
