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
    # print(equation)
    # if eval(equation) == 100:
        # print(equation)
    return eval(equation)


def generate_equations(numbers, oparator_number):
    equations = []
    for i in range(1, len(numbers)):
        add_chunk(numbers, i, oparator_number, '', equations)
    return equations


def add_chunk(numbers, split_index, remaining_depth, start, equations):
    if remaining_depth >= 0:
        remaining_array = numbers[split_index:]
        for i in range(1, len(remaining_array)+1):
            add_chunk(remaining_array, i, remaining_depth - 1, start+''.join(numbers[0:split_index]) + '+', equations)
            add_chunk(remaining_array, i, remaining_depth - 1, start+''.join(numbers[0:split_index]) + '-', equations)
    else:
            return equations.append(start + ''.join(numbers));


def get_correct_solutions(target, equations):
    solutions = []
    for equation in equations:
        if calculate(equation) == target:
            solutions.append(equation)
    return solutions


if __name__ == '__main__':
    components = [str(x) for x in range(1, 10)]
    target = 100

    correct_solutions = []
    print('Solutions:')
    iteration = 1
    while iteration < 8:
        generated = generate_equations(components, iteration)
        this_correct_solutions = get_correct_solutions(target, generated)

        correct_solutions += this_correct_solutions if this_correct_solutions is not None else []
        iteration += 1

    print("solutions for {target}".format(target=target))
    for solution in correct_solutions:
        print(solution)
