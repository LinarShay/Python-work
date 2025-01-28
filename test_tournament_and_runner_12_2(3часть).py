# test_tournament_and_runner_12_2.py

import unittest
from runner_and_tournament import Tournament
from runner import Runner

class TournamentTest(unittest.TestCase):
    is_frozen = True  # Установите True или False для заморозки/разморозки тестов

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        print("\nAll results:")
        for key, value in cls.all_results.items():
            formatted_result = {k: str(v) for k, v in value.items()}
            print(f"{key}: {formatted_result}")

    def _run_tournament(self, participants):
        tournament = Tournament(90, *participants)
        result = tournament.start()
        max_key = max(result.keys())
        last_runner = str(result[max_key])
        formatted_result = {k: str(v) for k, v in result.items()}
        self.all_results[len(self.all_results) + 1] = formatted_result
        return last_runner

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_usain_and_nick(self):
        last_runner = self._run_tournament([self.usain, self.nick])
        self.assertTrue(last_runner == "Ник")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_andrey_and_nick(self):
        last_runner = self._run_tournament([self.andrey, self.nick])
        self.assertTrue(last_runner == "Ник")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_usain_andrey_and_nick(self):
        last_runner = self._run_tournament([self.usain, self.andrey, self.nick])
        self.assertTrue(last_runner == "Ник")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_correct_order(self):
        usain = Runner("Усэйн", 10)
        andrey = Runner("Андрей", 9)
        nick = Runner("Ник", 3)
        tournament = Tournament(90, usain, andrey, nick)
        result = tournament.start()
        self.assertEqual(str(result[1]), "Усэйн")
        self.assertEqual(str(result[2]), "Андрей")
        self.assertEqual(str(result[3]), "Ник")