#!/opt/homebrew/bin/python3

class Database:
    def get_valori(self):
        # Simula il recupero di valori da un database
        raise NotImplementedError

def somma(db: Database):
    a, b = db.get_valori()
    return a + b


