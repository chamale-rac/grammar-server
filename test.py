from itertools import combinations


def generate_combinations(tuple_data, dynamic_element):
    combinations_list = []
    n = len(tuple_data)

    for i in range(1, n+1):
        for comb in combinations(tuple_data, i):
            if len(set(non_dynamic_elements).intersection(set(comb))) == len(non_dynamic_elements):
                combinations_list.append(comb)

    return combinations_list


tuple_data = ('C', 'A', 'C', 'a')
dynamic_element = 'C'
non_dynamic_elements = ['A']
result = generate_combinations(tuple_data, dynamic_element)
print(result)

tuple_data = ('C', 'C')
dynamic_element = 'C'
non_dynamic_elements = []
result = generate_combinations(tuple_data, dynamic_element)
print(result)

non_terminals = {'A', 'B', 'C'}
terminals = {'a', 'b', 'c'}

print(terminals | non_terminals - {'A'})
