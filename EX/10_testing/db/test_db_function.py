#!/opt/homebrew/bin/python3

from somma_da_db import Database

def test_get_valori():
    # Crea un mock del database

    # Verifica che il metodo get_valori restituisca un'eccezione
    db = Database()
    try:
        db.get_valori()
    except NotImplementedError:
        assert True