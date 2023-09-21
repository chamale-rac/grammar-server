from __future__ import annotations
from collections import defaultdict


class Grammar:
    '''
    Grammar class

    Args: 
        lines (list[str]): The lines of the grammar file.    
    '''

    def __init__(self, lines: list[str]) -> None:
        self.non_terminals: set[str] = set()
        self.nullables: set[str] = set()
        self.terminals: set[str] = set()
        self.production_terminals = defaultdict(set)
        self.production_non_terminals = defaultdict(set)
        self.productions = defaultdict(set)
        self.__transform_lines(lines)
        self.__remove_e_transitions()

    def __str__(self) -> str:
        output = ''
        for production, rules in self.productions.items():
            rules_str = ''
            for rule in rules:
                symbol_str = ' '.join(symbol for symbol in rule)
                rules_str += f'{symbol_str} | '
            output += f'{production} -> {rules_str[:-3]}\n'
        return output[:-1]

    def __eq__(self, other: Grammar) -> bool:
        if isinstance(other, Grammar):
            return self.non_terminals == other.non_terminals and \
                self.terminals == other.terminals and \
                self.productions == other.productions
        return False

    def __transform_lines(self, lines) -> list[str]:
        '''
        Transform the received lines into productions. Each line have been already validated.

        Args:
            lines (list[str]): The lines of the grammar file.
        '''

        # Divide each line by non-terminal -> rule | rule | ...
        productions = [line.split('->') for line in lines]

        for production in productions:
            # Remove the spaces from the non-terminal.
            this_non_terminal = production[0].strip()

            # Split the rules string by the pipe symbol. And then group the symbols in a tuple.
            rule_set = {tuple(rule.strip().split(' '))
                        for rule in production[1].split('|')}

            # Add the non-terminal to the productions dictionary.
            self.productions[this_non_terminal] |= rule_set

            # Add the non-terminal to the non-terminals set.
            self.non_terminals.add(this_non_terminal)
            for rule in rule_set:
                # Add each symbol to the terminals or non-terminals set.
                for symbol in rule:
                    if symbol.isupper():
                        self.non_terminals.add(symbol)
                        self.production_non_terminals[this_non_terminal] |= set(
                            symbol)
                    else:
                        if symbol == 'ϵ':
                            self.nullables.add(this_non_terminal)
                        self.terminals.add(symbol)
                        self.production_terminals[this_non_terminal] |= set(
                            symbol)

    def __remove_e_transitions(self):
        '''
        Remove the e-transitions from the grammar.
        '''
        from itertools import combinations

        def get_combinations(production, non_dynamic: set[str]):

            combinations_set = set()
            n = len(production)

            non_dynamic_len = sum(
                element in non_dynamic for element in production)

            for i in range(1, n+1):
                for comb in combinations(production, i):
                    comb_non_dynamic_len = sum(
                        element in non_dynamic for element in comb)
                    if non_dynamic_len == comb_non_dynamic_len:
                        combinations_set.add(comb)

            return combinations_set

        BREAK_INF_LOOP = False
        nullables_history = set()

        while self.nullables and not BREAK_INF_LOOP:
            for nullable_non_terminal in self.nullables.copy():
                # For each production that contains the nullable non-terminal.
                for non_terminal, non_terminals in self.production_non_terminals.items():
                    if BREAK_INF_LOOP:
                        break

                    if nullable_non_terminal in non_terminals:
                        # Get the productions that contains the nullable non-terminal and have the nullable non-terminal.
                        productions_with_nullable = {
                            production for production in self.productions[non_terminal] if nullable_non_terminal in production}

                        for production in productions_with_nullable:
                            if len(production) == 1 and non_terminal != nullable_non_terminal:
                                # Add the nullable non-terminal to the production.
                                self.productions[non_terminal] |= {('ϵ',)}

                                self.nullables.add(non_terminal)
                                nullables_history.add(non_terminal)

                                if len(nullables_history) == len(self.productions):
                                    BREAK_INF_LOOP = True
                                continue

                            # Get the combinations of the production without the nullable non-terminal.
                            non_dynamic = set(
                                production) - {nullable_non_terminal}

                            combinations_set = get_combinations(
                                production, non_dynamic)

                            # Add the combinations to the production.
                            self.productions[non_terminal] |= combinations_set

                if BREAK_INF_LOOP:
                    for nullable in self.nullables:
                        self.productions[nullable] -= {('ϵ',)}
                    print()
                    break

                # Remove the non-terminal from the nullables set.
                self.nullables.remove(nullable_non_terminal)
                # Quit ϵ from the production.
                self.productions[nullable_non_terminal] -= {('ϵ',)}
