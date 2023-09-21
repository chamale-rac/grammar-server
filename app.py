from src.grammar import Grammar
from src.utils.tools import readFile, fileInPath
# !COPY THIS: ϵ


def main():
    file_path = input("Enter file path (./default.txt): ")
    if not file_path or not fileInPath(file_path):
        print("Invalid file path. Using default file.")
        file_path = './default.txt'
    lines = readFile(file_path)

    grammar = Grammar(lines)
    for production in grammar.productions:
        print(production, '->', grammar.productions[production])


if __name__ == '__main__':
    main()
