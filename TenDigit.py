import itertools
import operator

operations = {'+': operator.add,
              '-': operator.sub}


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def calculate(equation):
    stack = []
    result = 0
    try:
        for i in equation:
            if is_number(i):
                stack.insert(0, i)
            else:
                # print('stack: %s' % stack)
                n1 = float(stack.pop(1))
                n2 = float(stack.pop(0))
                result = operations[i](n2, n1)
                stack.insert(0, str(result))
    except ZeroDivisionError:
        return 0
    return result


def generate_equations(numbers):
    equations = []
    for length in range(2, 6):
        number_combinations = itertools.permutations(numbers, length)
        operator_combinations = itertools.combinations_with_replacement(operations, length - 1)
        number_combination_list = list(number_combinations)
        operation_combinations_list = list(operator_combinations)
        # equations.extend((map(list.__add__, number_combination_list, operation_combinations_list)))
        for number_combo in number_combination_list:
            for operator_combo in operation_combinations_list:
                equations.append(number_combo + operator_combo)

    return equations


def append_all_combinations(existing_stems, combinators, operator_number):
    new_combinations = []
    for existingStem in existing_stems:
        for combinator in combinators:
            new_combinations.append(existingStem + combinator)
    return new_combinations


def get_correct_solutions(target, equations):
    solutions = []
    for equation in equations:
        if calculate(equation) == target:
            solutions.append(equation)
    return solutions


if __name__ == '__main__':
    components = range(1, 11)
    target = 100

    # [print(a) for a in equations]

    correct_solutions = []
    print('Solutions:')
    iteration = 1
    while len(correct_solutions) == 0:
        equations = generate_equations(components)
        correct_solutions = get_correct_solutions(target, equations, iteration)
        iteration += 1

    print("solutions for {target}".format(target=target))
    for solution in correct_solutions:
        print(solution)
