from itertools import combinations


def generate_combinations(tuple_data, dynamic_element):
    combinations_list = []
    n = len(tuple_data)

    for comb in combinations(tuple_data, n+1):
        print(comb)


tuple_data = ('C', 'A', 'C', 'a')
dynamic_element = 'C'
non_dynamic_elements = ['A']
generate_combinations(tuple_data, dynamic_element)

tuple_data = ('C', 'C')
dynamic_element = 'C'
non_dynamic_elements = []
generate_combinations(tuple_data, dynamic_element)
