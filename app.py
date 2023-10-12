from src.grammar import Grammar
from src.utils.tools import readFile, fileInPath
from src.utils.constants import regex_str

# from automaton.src.expression import Expression
# from automaton.src._ast import AbstractSyntaxTree as AST
# from automaton.src._nfa import NonDeterministicFiniteAutomaton as NFA
# !COPY THIS: ϵ


def main():
    # regex = Expression(regex_str)
    # regex.shuntingYard()

    # ast = AST(regex)
    # ast.build()

    # nfa = NFA(ast.builded, regex.alphabet)
    # nfa.thompson()

    # def check(string: str) -> bool:
    #     # Replace each '|' with '\|' and 'ϵ' with '\ϵ'
    #     string = string.replace('|', '\|')
    #     string = string.replace('ϵ', '\ϵ')
    #     expression = Expression(string)
    #     expression.format()
    #     expression.format_string()

    #     return nfa.simulate(expression.formatted)

    # file_path = input("Enter file path (default: ./grammars/g.txt): ")
    # if not file_path or not fileInPath(file_path):
    #     print("Invalid file path. Using default file.")
    #     file_path = './grammars/g.txt'
    file_path = './grammars/test.txt'
    lines = readFile(file_path)
    # if not False in [check(line) for line in lines]:
    grammar = Grammar(lines)
    print(f'Results {file_path}')
    print(grammar)
    print('-'*50)
    # else:
    #     print('>> Grammar is invalid.')
    file_path = './grammars/test2.txt'
    lines = readFile(file_path)
    # if not False in [check(line) for line in lines]:
    grammar = Grammar(lines)
    print(f'Results {file_path}')
    print(grammar)
    print('-'*50)

    file_path = './grammars/g1.txt'
    lines = readFile(file_path)
    grammar = Grammar(lines)
    print(f'Results {file_path}')
    print(grammar)
    print('-'*50)

    file_path = './grammars/g2.txt'
    lines = readFile(file_path)
    grammar = Grammar(lines)
    print(f'Results {file_path}')
    print(grammar)
    print('-'*50)

    file_path = './grammars/test3.txt'
    lines = readFile(file_path)
    grammar = Grammar(lines)
    print(f'Results {file_path}')
    print(grammar)
    print('-'*50)


if __name__ == '__main__':
    main()
