import itertools
import operator
# import sympy

operations = {'+': operator.add,
              '-': operator.sub}


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def calculate(equation):
    # stack = []
    # result = 0
    # try:
    #     for i in equation:
    #         if is_number(i):
    #             stack.insert(0, i)
    #         else:
    #             # print('stack: %s' % stack)
    #             n1 = float(stack.pop(1))
    #             n2 = float(stack.pop(0))
    #             result = operations[i](n2, n1)
    #             stack.insert(0, str(result))
    # except ZeroDivisionError:
    #     return 0
    # return

    # print (eval(equation))
    if eval(equation) ==100:
        # print('*********')
        print(equation)
        # print(eval(equation))
    return eval(equation)


def generate_equations(numbers, oparator_number):
    equations = []
    for i in range(1, len(numbers)):
        add_chunk(numbers, i, oparator_number, '', equations)
    # print(','.join(equations))
    # for ONE operator
    # iterate across numbers 0 to i concat, i to length concat.

    # for TWO iterate across numbers 0 to i concat. For each iterate from i to j concat, j to length con

    numbers
    # for length in range(2, 6):
    #     number_combinations = itertools.permutations(numbers, length)
    #     operator_combinations = itertools.combinations_with_replacement(operations, length - 1)
    #     number_combination_list = list(number_combinations)
    #     operation_combinations_list = list(operator_combinations)
    #     for number_combo in number_combination_list:
    #         for operator_combo in operation_combinations_list:
    #             equations.append(number_combo + operator_combo)

    return equations


def add_chunk(numbers, split_index, remaining_depth, start, equations):
    # print(split_index)
    # if split_index > len(numbers):
    #     return ''
    if remaining_depth > 0:
        remaining_array = numbers[split_index:]
        # print(':'.join(remaining_array))
        for i in range(1, len(remaining_array)):
            # print(i)
            # this return breaks rec

            add_chunk(remaining_array, i, remaining_depth - 1, start+''.join(numbers[0:split_index]) + '+', equations)
            add_chunk(remaining_array, i, remaining_depth - 1, start+''.join(numbers[0:split_index]) + '-', equations)

            # return ''.join(numbers[0:split_index]) + add_chunk(remaining_array, i, remaining_depth - 1) + '+'
    else:
            return equations.append(start + ''.join(numbers));

    # else:
    #     return ''


def get_correct_solutions(target, equations):
    solutions = []
    for equation in equations:
        if calculate(equation) == target:
            solutions.append(equation)
    return solutions


if __name__ == '__main__':
    components = [str(x) for x in range(1, 10)]
    target = 100

    # [print(a) for a in equations]

    correct_solutions = []
    print('Solutions:')
    iteration = 1
    while iteration < 8:
        generated = generate_equations(components, iteration)
        correct_solutions = get_correct_solutions(target, generated)
        iteration += 1

    print("solutions for {target}".format(target=target))
    for solution in correct_solutions:
        print(solution)
