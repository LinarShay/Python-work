# test_runner_12_1.py

import unittest
from runner import Runner

class RunnerTest(unittest.TestCase):
    is_frozen = False  # Установите True или False для заморозки/разморозки тестов

    def setUp(self):
        self.runner = Runner("Alice")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        for _ in range(10):
            self.runner.walk()
        self.assertEqual(self.runner.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        for _ in range(10):
            self.runner.run()
        self.assertEqual(self.runner.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner1 = Runner("Charlie")
        runner2 = Runner("David")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)