#!/opt/homebrew/bin/python3

import os

def rimuovi_prime_due_righe_da_py():
    for root, _, files in os.walk('.'):
        for file in files:
            if file.endswith('.py'):
                path_file = os.path.join(root, file)
                with open(path_file, 'r', encoding='utf-8') as f:
                    righe = f.readlines()
                
                # Evita errori se il file ha meno di due righe
                nuove_righe = righe[2:] if len(righe) >= 2 else []

                with open(path_file, 'w', encoding='utf-8') as f:
                    f.writelines(nuove_righe)

if __name__ == '__main__':
    rimuovi_prime_due_righe_da_py()