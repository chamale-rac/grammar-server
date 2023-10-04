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
        self.initial_symbol: str = None
        self.__transform_lines(lines)
        self.__remove_e_transitions()
        self.__remove_unary_productions()
        self.__remove_useless_symbols()

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

    def __clean(self) -> None:
        '''
        Clean the grammar references set utils.
        '''

        self.non_terminals.clear()
        self.production_non_terminals.clear()
        self.nullables.clear()
        self.terminals.clear()
        self.production_terminals.clear()

    def __map_rules(self, non_terminal: str, rules: set[tuple[str]]) -> None:
        '''
        Map the rule set to the terminals and non-terminals sets.
        '''
        self.non_terminals.add(non_terminal)

        for rule in rules:
            # Add each symbol to the terminals or non-terminals set.
            for symbol in rule:
                if symbol.isupper():
                    self.non_terminals.add(symbol)
                    self.production_non_terminals[non_terminal] |= set(
                        (symbol,))
                else:
                    if symbol == 'ϵ':
                        self.nullables.add(non_terminal)
                    self.terminals.add(symbol)
                    self.production_terminals[non_terminal] |= set(
                        (symbol,))

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
            rules = {tuple(rule.strip().split(' '))
                     for rule in production[1].split('|')}

            # Add the non-terminal to the productions dictionary.
            self.productions[this_non_terminal] |= rules

            if not self.initial_symbol:
                self.initial_symbol = this_non_terminal
            self.__map_rules(this_non_terminal, rules)

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
                    break

                # Remove the non-terminal from the nullables set.
                self.nullables.remove(nullable_non_terminal)
                # Quit ϵ from the production.
                self.productions[nullable_non_terminal] -= {('ϵ',)}

    def __remove_unary_productions(self):
        '''
        Remove the unary productions from the grammar.
        '''
        # Filter and get only the unary productions for each production
        unary_productions = {production: {rule for rule in rules if len(
            rule) == 1 and rule[0] in self.non_terminals} for production, rules in self.productions.items()}
        # Get no unary productions the same way.
        no_unary_productions = {productions: {rule for rule in rules if len(
            rule) != 1 or rule[0] not in self.non_terminals} for productions, rules in self.productions.items()}

        # For dynamic programming store the already get pairs.
        pairs = set()

        def induction(pair: tuple[str, str]):
            '''
            Create the pairs of the unary productions.
            '''
            if pair in pairs:
                return

            if pair[0] in unary_productions:
                pairs.add(pair)

            if pair[1] not in unary_productions:
                return

            # Get the unary productions of the second element of the pair.
            unary_productions_second = unary_productions[pair[1]]

            # Check if there is no unary productions.
            if not unary_productions_second:
                return

            #  Create new pairs using them as the second element and pair[0] as the first element.
            new_pairs = [(pair[0], unary_production[0])
                         for unary_production in unary_productions_second]

            # Repeat the induction for each new pair.
            for pair in new_pairs:
                induction(pair)

        # Generate the initial pairs, with it selves.
        base = list(zip(self.non_terminals, self.non_terminals))

        # Repeat the induction for each pair.
        for pair in base:
            induction(pair)

        self.simplified_productions = defaultdict(set)

        # For each pair, create a new production [pair[0] -> no_unary_productions[pair[1]]]
        for pair in pairs:
            if pair[1] in no_unary_productions:
                self.simplified_productions[pair[0]
                                            ] |= no_unary_productions[pair[1]]

        self.productions = self.simplified_productions

    def __remove_useless_symbols(self):
        '''
        Remove the useless symbols from the grammar.
        '''

        self.__clean()
        for non_terminal, rules in self.productions.items():
            self.__map_rules(non_terminal, rules)

        # 1. Remove symbols that dont produce anything.
        # TODO this can be optimized by avoid mapping the rules again, and use dynamic programming to store the symbols that produce something.
        for non_terminal, rules in self.productions.items():
            for production_non_terminal in self.production_non_terminals[non_terminal]:
                if production_non_terminal not in self.productions:
                    # Quit any rule that contains the symbol.
                    self.productions[non_terminal] -= {
                        rule for rule in rules if production_non_terminal in rule}

        # TODO can be optimized by avoid mapping the rules again, and use dynamic programming to store the symbols that are reachable.
        self.__clean()
        for non_terminal, rules in self.productions.items():
            self.__map_rules(non_terminal, rules)

        # 2. Remove symbols that are not reachable by the initial symbol.
        reachable_non_terminals: set[str] = set()

        def induction(non_terminal: str):
            '''
            Induction to get the reachable non-terminals.
            '''
            if non_terminal in reachable_non_terminals:
                return

            reachable_non_terminals.add(non_terminal)

            if non_terminal not in self.production_non_terminals:
                return

            for production_non_terminal in self.production_non_terminals[non_terminal]:
                induction(production_non_terminal)

        induction(self.initial_symbol)
        unreachable_non_terminals = self.non_terminals - reachable_non_terminals

        # Remove the unreachable non-terminals from self.productions.
        for unreachable_non_terminal in unreachable_non_terminals:
            self.productions.pop(unreachable_non_terminal)
