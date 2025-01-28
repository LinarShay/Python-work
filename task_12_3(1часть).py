# task_12_3.py

import unittest
from test_runner_12_1 import RunnerTest
from test_tournament_and_runner_12_2 import TournamentTest

def load_tests(loader, tests, pattern):
    suite = unittest.TestSuite()
    # Добавляем тесты из RunnerTest
    suite.addTests(loader.loadTestsFromTestCase(RunnerTest))
    # Добавляем тесты из TournamentTest
    suite.addTests(loader.loadTestsFromTestCase(TournamentTest))
    return suite

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = load_tests(loader, None, None)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)