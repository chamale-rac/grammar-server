from src.grammar import Grammar
from src.utils.tools import readFile

# !COPY THIS: ϵ


def main():
    file_path = './grammars/test.txt'
    lines = readFile(file_path)
    grammar = Grammar(lines)
    print(f'Results {file_path}')
    print(grammar)
    print('-'*50)
    grammar.CYK('she eats a fish with a fork')


if __name__ == '__main__':
    main()
