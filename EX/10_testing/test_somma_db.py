#!/opt/homebrew/bin/python3

import unittest
from somma_da_db import somma, Database
from unittest.mock import MagicMock

class TestSommaDaDB(unittest.TestCase):
    def test_somma_mock_db(self):
        # Crea un mock del database
        mock_db = MagicMock() # Simula il database
        mock_db.get_valori.return_value = (3, 5)

        risultato = somma(mock_db)

        self.assertEqual(risultato, 8)

class TestDatabase(unittest.TestCase):
    def test_db(self):
        db = Database()
        with self.assertRaises(NotImplementedError):
            db.get_valori()


