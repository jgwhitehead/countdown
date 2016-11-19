import operator

operations = {'+': operator.add,
              '-': operator.sub,
              '*': operator.mul,
              '/': operator.div}


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
            print('stack: %s' % stack)
            n1 = float(stack.pop(1))
            n2 = float(stack.pop(0))
            result = operations[i](n1, n2)
            stack.insert(0, str(result))
    return result

def generate_equations(numbers):
    # TODO don't need to use all numbers
    equations = []
    equation=""

    # build all possible operand combinations, then combine with all possible number orders
    # build operations
    # start off with each of the available operations
    operation_combinations= operations.keys()
    # grow the list with all possible combinations
    for i in range(numbers.length -1):
        append_all_combinations(operation_combinations,operations.keys())

    # generate all possible number orderings

    # combine operation_combinations with number combinations



def append_all_combinations(existing_stems, combinators):
    new_combinations = []
    for existingStem in existing_stems:
        for combinator in combinators:
            new_combinations.append(existingStem + combinator)
    return new_combinations

if __name__ == '__main__':
    components = get_user_input_components()
    target = get_user_input_target()

    solutions = []

    for equation in equations:
        if calculate(equation) == target:
            solutions.append(equation)

    print('Solutions:')
    for solution in solutions:
        print(solution)
