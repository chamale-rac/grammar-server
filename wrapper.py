from src.grammar import Grammar
from src.utils.tools import to_base64


def wrapper_cyk(lines: list[str], sentence: str, HEIGHT_REGEX, WIDTH_REGEX, prefix, initial_symbol, web=True) -> str:
    '''
    Wrapper for the CYK algorithm.
    '''
    initial_grammar = '\n'.join(lines)
    grammar = Grammar(lines, initial_symbol, prefix)
    grammar.CNF()
    resultant_grammar = str(grammar).split('\n')
    resultant_grammar = resultant_grammar[2:]
    resultant_grammar = '\n'.join(resultant_grammar)
    is_in, images, took = grammar.CYK(sentence, web=True)

    if is_in:
        new_images = []
        for image in images:
            string, width, height = to_base64(image, HEIGHT_REGEX, WIDTH_REGEX)
            data = {
                'src': 'data:image/svg+xml;base64,' + string,
                'alt': 'Parse tree',
                'width': width,
                'height': height,
                'title': 'Parse tree',
                'description': f'\nSentence: {sentence}'
            }
            new_images.append(data)
        return {
            'prefix': prefix,
            'initialSymbol': initial_symbol,
            'initialGrammar': initial_grammar,
            'resultantGrammar': resultant_grammar,
            'images': new_images,
            'took': took,
            'isIn': is_in,
            'sentence': sentence,
        }
    else:
        return {
            'prefix': prefix,
            'initialSymbol': initial_symbol,
            'initialGrammar': initial_grammar,
            'resultantGrammar': resultant_grammar,
            'images': [],
            'took': took,
            'isIn': is_in,
            'sentence': sentence,
        }
