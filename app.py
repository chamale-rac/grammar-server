from src.grammar import Grammar
from src.utils.tools import readFile, fileInPath
# !COPY THIS: ϵ


def main():
    file_path = input("Enter file path (default: ./g.txt): ")
    if not file_path or not fileInPath(file_path):
        print("Invalid file path. Using default file.")
        file_path = './g.txt'
    lines = readFile(file_path)

    grammar = Grammar(lines, verbose=False)
    print('>> Grammar:')
    print(grammar)
    print('>> Solution:')
    print(grammar)


if __name__ == '__main__':
    main()
