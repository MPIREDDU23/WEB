#!/opt/homebrew/bin/python3

import os

SHEBANG = "#!/opt/homebrew/bin/python3"

def add_shebang_to_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Salta i file già corretti
    if lines and lines[0].strip() == SHEBANG:
        return

    # controlla se c'è uno shebang diverso, se sì lo rimuove
    if lines and lines[0].startswith("#!"):
        # rimuove la prima riga
        lines = lines[1:]

    # finché il file ha ancora righe e le righe non contengono caratteri != " " rimuovile
    while lines and lines[0].strip() == "":
        lines = lines[1:]

    # Se il file è vuoto, non aggiungere lo shebang
    if not lines:
        return

    # Prepara il nuovo contenuto
    new_lines = [SHEBANG + "\n", "\n"] + lines

    with open(filepath, "w", encoding="utf-8") as f:
        f.writelines(new_lines)

    print(f"[✔] Aggiornato: {filepath}")

def find_and_fix_py_files(start_dir):
    for root, _, files in os.walk(start_dir):
        for file in files:
            if file.endswith(".py"):
                filepath = os.path.join(root, file)
                add_shebang_to_file(filepath)

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    find_and_fix_py_files(current_dir)