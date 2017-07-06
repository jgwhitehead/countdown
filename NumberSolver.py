import itertools
import operator

operations = {'+': operator.add,
              '-': operator.sub,
              '*': operator.mul,
              '/': operator.truediv}


def get_user_input_components():
    while True:
        inputted = input('enter 6 numbers:')
        print("{s} numbers entered".format(s=len(inputted.split())))
        if len(inputted.split()) == 6:
            numbers = []
            numbers.extend(inputted.split())
            return numbers


def get_user_input_target():
    while True:
        inputted = input('enter 1 target number:')
        print("{s} numbers entered".format(s=len(inputted.split())))
        if len(inputted.split()) == 1:
            if is_number(inputted.split()[0]):
                return int(inputted.strip())


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

def get_correct_solutions(target, equations):
    solutions = []
    for equation in equations:
        if calculate(equation) == target:
            solutions.append(equation)
    return solutions


if __name__ == '__main__':
    # components = [1, 2, 3, 4, 5, 6]
    # target = 5
    components = get_user_input_components()
    target = get_user_input_target()

    equations = generate_equations(components)
    # [print(a) for a in equations]

    print('Solutions:')
    correct_solutions = get_correct_solutions(target, equations)
    iteration = 0
    while len(correct_solutions) == 0:
        print("no solution for {target}, trying next".format(target=target))
        iteration += 1
        if iteration % 2 == 0:
            target -= iteration
        else:
            target += iteration
        correct_solutions = get_correct_solutions(target, equations)

    print("solutions for {target}".format(target=target))
    for solution in correct_solutions:
        print(solution)
