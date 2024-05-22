import subprocess
import time
import random

def check_program_status():
    # Zde můžeš provést kontrolu stavu programu. 
    # Například zkontrolovat, zda je proces Pythonu souběžně spuštěn.
    # Můžeš použít modul psutil nebo subprocess pro kontrolu procesů.
    # Tento kód je pouze ukázkou.

    # Příklad: Kontrola běžících procesů pomocí příkazu ps na Linuxu.
    output = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
    if 'python tvuj_program.py' in output.stdout:
        return True
    else:
        return False

def start_program():
    # Zde spustíš svůj program.
    # Můžeš použít subprocess nebo jiný způsob spouštění procesů v Pythonu.
    # Příklad: subprocess.Popen(['python', 'tvuj_program.py'])
    print("Spouštím program...")
    # Uprav cestu k tvému programu dle potřeby
    subprocess.Popen(['python', '/cesta/k/tvuj_program.py'])

def main():
    while True:
        if not check_program_status():
            start_program()
        # Náhodný časový interval pro kontrolu stavu programu
        time.sleep(random.randint(10, 60))  # Zkontroluje stav každých 10-60 sekund

if __name__ == "__main__":
    main()
