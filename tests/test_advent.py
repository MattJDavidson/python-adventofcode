import importlib

from click.testing import CliRunner
import pytest

from advent import __version__

num_problems_solved = int(__version__.split('.')[1])
problem_modules = [importlib.import_module('advent.problem_{:02d}'.format(i))
                   for i in range(1, num_problems_solved+1)]

def test_problems():
    with open('data/solutions.txt') as solutions_file:
        all_solutions = solutions_file.read().split()

    grouped_solutions = [(int(sol), int(all_solutions[i*2+1]))
                         for i, sol in enumerate(all_solutions[::2])]

    for i, module in enumerate(problem_modules):
        with open('data/{:02d}.txt'.format(i+1)) as source:
            data = source.read()

            first_solution = problem_modules[i].calculate_solution_1(data)
            assert first_solution == grouped_solutions[i][0]

            second_solution = problem_modules[i].calculate_solution_2(data)
            assert second_solution == grouped_solutions[i][1]


if __name__ == "__main__":
    test_problems()
