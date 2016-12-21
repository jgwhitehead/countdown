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
            # TODO typecheck
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
    for i in equation:
        if is_number(i):
            stack.insert(0, i)
        else:
            # if len(stack) == 1:
                # return stack.pop(0)
            print('stack: %s' % stack)
            n1 = float(stack.pop(1))
            n2 = float(stack.pop(0))
            result = operations[i](n1, n2)
            stack.insert(0, str(result))
    return result


def generate_equations(numbers):
    # TODO don't need to use all numbers
    equations = []
    equation = ""

    # build all possible operand combinations, then combine with all possible number orders
    # build operations
    # start off with each of the available operations
    operation_combinations = operations.keys()
    # grow the list with all possible combinations

    for length in range(2, 6):
        number_combinations = itertools.permutations(numbers, length)
        # [print(a) for a in number_combinations]

        operator_combinations = itertools.combinations_with_replacement(operations, length-1)
        # [print(a) for a in operator_combinations]


        d = list(number_combinations)
        e = list(operator_combinations)
        # equations.extend((map(list.__add__, d, e)))
        equations.extend(x + y for x,y in zip(d, e))

        [print(a) for a in equations]
        # for i in range(numbers.length - 1):
        #     append_all_combinations(operation_combinations, operations.keys())

        # generate all possible number orderings

        # combine operation_combinations with number combinations
        return equations


def append_all_combinations(existing_stems, combinators):
    new_combinations = []
    for existingStem in existing_stems:
        for combinator in combinators:
            new_combinations.append(existingStem + combinator)
    return new_combinations


if __name__ == '__main__':
    components = [1, 2, 3, 4, 5, 6]
    target = 5

    solutions = []
    equations = generate_equations(components)
    [print(a) for a in equations]

    for equation in equations:
        if calculate(equation) == target:
            solutions.append(equation)

    print('Solutions:')
    for solution in solutions:
        print(solution)
