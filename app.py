from src.grammar import Grammar
from src.utils.tools import readFile

# !COPY THIS: ϵ


def main():
    file_path = './grammars/test4.txt'
    file_path = './grammars/test.txt'
    lines = readFile(file_path)
    grammar = Grammar(lines)
    print(f'Results {file_path}')
    print(grammar)
    print('-'*50)
    grammar.CYK('i saw him with the binoculars', 1)
    grammar.CYK('the cat drinks the beer', 2)
    grammar.CYK('she eats a cake with a fork', 3)

    file_path = './grammars/test4.txt'
    lines = readFile(file_path)
    grammar = Grammar(lines)
    print(f'Results {file_path}')
    print(grammar)
    print('-'*50)
    grammar.CYK('i saw him with the binoculars', 4)

    file_path = './grammars/test_hard.txt'
    lines = readFile(file_path)
    grammar = Grammar(lines)
    print(f'Results {file_path}')
    print(grammar)
    print('-'*50)
    grammar.CYK(
        'buffalo buffalo buffalo buffalo buffalo buffalo buffalo buffalo', 5)


if __name__ == '__main__':
    main()
