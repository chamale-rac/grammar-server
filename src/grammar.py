from __future__ import annotations


class Grammar:
    '''
    Grammar class

    Args: 
        lines (list[str]): The lines of the grammar file.    
    '''

    def __init__(self, lines: list[str]) -> None:
        self.non_terminals = set()
        self.terminals = set()
        self.productions: dict[str, set[tuple(str, ...)]] = {}
        self.transformLines(lines)

    def __str__(self) -> str:
        return f"""
        Non-terminals: {self.non_terminals}
        Terminals: {self.terminals}
        Productions: {self.productions}
        """

    def __eq__(self, other: Grammar) -> bool:
        if isinstance(other, Grammar):
            return self.non_terminals == other.non_terminals and \
                self.terminals == other.terminals and \
                self.productions == other.productions
        return False

    def transformLines(self, lines) -> list[str]:
        '''
        Transform the received lines into productions. Each line have been already validated.

        Args:
            lines (list[str]): The lines of the grammar file.
        '''

        # Divide each line by non-terminal -> rule | rule | ...
        lines = [line.split('->') for line in lines]

        for line in lines:
            # Remove the spaces from the non-terminal.
            this_non_terminal = line[0].strip()
            # Split the rules string by the pipe symbol.
            this_rules = line[1].split('|')
            # Split the each rule by spaces. This means that each rule will be a list of symbols.
            this_rules = [tuple(rule.strip().split(' '))
                          for rule in this_rules]

            # Add the non-terminal to the productions dictionary.
            if this_non_terminal in self.productions:
                self.productions[this_non_terminal].update(this_rules)
            else:
                self.productions[this_non_terminal] = set(this_rules)

            # Add the non-terminal to the non-terminals set.
            self.non_terminals.add(this_non_terminal)
            for rule in this_rules:
                # Add each symbol to the terminals or non-terminals set.
                for symbol in rule:
                    # if symbol == 'ϵ':
                    #     continue
                    if symbol.isupper():
                        self.non_terminals.add(symbol)
                    else:
                        self.terminals.add(symbol)
