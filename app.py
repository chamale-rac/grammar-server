from src.grammar import Grammar
from src.utils.tools import readFile

# !COPY THIS: ϵ


def main():
    to_read = [
        ('./grammars/test.txt', ['i saw him with the binoculars',
         'the cat drinks the beer', 'she eats a cake with a fork']),
        ('./grammars/test4.txt', ['i saw him with the binoculars']),
        ('./grammars/test_hard.txt',
         ['buffalo buffalo buffalo buffalo buffalo buffalo buffalo buffalo'])
    ]

    to_read = [
        ('./grammars/1.txt', ['id + id', '( id * id ) + id', 'id']),
    ]

    for file_path, sentences in to_read:
        lines = readFile(file_path)
        grammar = Grammar(lines)
        print(f'Results {file_path}\n{grammar}\n{"-"*50}')
        for i, sentence in enumerate(sentences):
            grammar.CYK(sentence, i+1)


main()
