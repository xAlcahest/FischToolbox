import tkinter as tk
from tkinter import ttk
import math

def total_xp_for_level(level):
    """
    Calcola il totale di XP necessari per raggiungere il livello 'level'
    usando la formula: total_xp = 190 * (level-1) * level / 2
    """
    if level < 1:
        return 0
    return int(190 * (level - 1) * level / 2)

def calculate_over1000(extra_xp):
    """
    Dato un quantitativo di XP extra oltre il livello 1000,
    calcola:
      - XP totali (aggiungendo i 94.905.000 di base per il livello 1000)
      - Livello "raw" (continuo) e assegnato (parte intera)
      - Livelli extra (oltre il 1000)
      - XP extra necessari per raggiungere il prossimo livello
    """
    # XP necessari per il livello 1000
    xp_1000 = 94905000
    total_xp = xp_1000 + extra_xp

    # Risolviamo l'equazione: L^2 - L - (total_xp/95) = 0
    discriminant = 1 + 4 * (total_xp / 95)
    L_raw = (1 + math.sqrt(discriminant)) / 2
    L_awarded = math.floor(L_raw)
    extra_levels = L_awarded - 1000  # livelli oltre il 1000

    # XP extra totali necessari per raggiungere il livello successivo
    next_level_total_xp = total_xp_for_level(L_awarded + 1)
    extra_xp_next = next_level_total_xp - xp_1000
    xp_remaining = extra_xp_next - extra_xp

    return L_raw, L_awarded, extra_levels, total_xp, extra_xp_next, xp_remaining

def update_over1000(event=None):
    try:
        extra_xp_val = int(extra_xp_var.get())
    except ValueError:
        result_var.set("Inserisci un numero valido per gli XP extra!")
        return

    if extra_xp_val < 0:
        result_var.set("Gli XP extra non possono essere negativi!")
        return

    L_raw, L_awarded, extra_levels, total_xp, extra_xp_next, xp_remaining = calculate_over1000(extra_xp_val)

    result = (
        f"XP Totali: {total_xp}\n"
        f"Livello (raw): {L_raw:.2f}\n"
        f"Livello assegnato: {L_awarded}\n"
        f"Livello extra sopra 1000: {extra_levels}\n"
        f"XP extra per il prossimo livello: {extra_xp_next} (mancano {xp_remaining} XP)"
    )
    result_var.set(result)

# Creazione della finestra principale
root = tk.Tk()
root.title("Calcolatrice Over1000 di Fisch")

frame = ttk.Frame(root, padding=10)
frame.pack(fill="both", expand=True)

# Campo di input per gli XP extra oltre il livello 1000
ttk.Label(frame, text="Inserisci XP extra (oltre il livello 1000):").grid(row=0, column=0, sticky="w")
extra_xp_var = tk.StringVar()
entry_extra = ttk.Entry(frame, textvariable=extra_xp_var, width=20)
entry_extra.grid(row=0, column=1, padx=5, pady=5)
entry_extra.bind("<KeyRelease>", update_over1000)

# Label per mostrare i risultati
result_var = tk.StringVar()
result_label = ttk.Label(frame, textvariable=result_var, foreground="blue", justify="left")
result_label.grid(row=1, column=0, columnspan=2, sticky="w", padx=5, pady=5)

root.mainloop()
