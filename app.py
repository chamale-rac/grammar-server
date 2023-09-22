from src.grammar import Grammar
from src.utils.tools import readFile, fileInPath
from src.utils.constants import regex_str

from automaton.src.expression import Expression
from automaton.src._ast import AbstractSyntaxTree as AST
from automaton.src._nfa import NonDeterministicFiniteAutomaton as NFA
# !COPY THIS: ϵ


def main():
    regex = Expression(regex_str)
    regex.shuntingYard()

    ast = AST(regex)
    ast.build()

    nfa = NFA(ast.builded, regex.alphabet)
    nfa.thompson()

    def check(string: str) -> bool:
        # Replace each '|' with '\|' and 'ϵ' with '\ϵ'
        string = string.replace('|', '\|')
        string = string.replace('ϵ', '\ϵ')
        expression = Expression(string)
        expression.format()
        expression.format_string()

        return nfa.simulate(expression.formatted)

    file_path = input("Enter file path (default: ./grammars/g.txt): ")
    if not file_path or not fileInPath(file_path):
        print("Invalid file path. Using default file.")
        file_path = './grammars/g.txt'
    lines = readFile(file_path)
    print()
    if not False in [check(line) for line in lines]:
        grammar = Grammar(lines)
        print('>> Solution:')
        print(grammar)
    else:
        print('>> Grammar is invalid.')


if __name__ == '__main__':
    main()
