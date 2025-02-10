import tkinter as tk
from tkinter import ttk
import math

# ---------------------------
# Calculation functions
# ---------------------------
def xp_per_level(level):
    """
    Calculate the XP required to progress from level 'level' to 'level+1'.
    """
    return 190 * (level - 1)

def total_xp_for_level(level):
    """
    Calculate the total XP required to reach level 'level'.
    The formula is:
        total_xp = 190 * (1 + 2 + ... + (level-1)) = 190 * (level-1)*level/2
    """
    # If level is less than 1, no XP is required
    if level < 1:
        return 0
    """return int(190 * (level - 1) * level / 2)"""
    partial_xp = 0
    for i in range(level):
        partial_xp += i * 190
    return int(partial_xp)

def raw_level_from_xp(xp):
    """
    Calculate the level (in continuous form) that corresponds to a given amount of EXP,
    by solving the equation:
        xp = 190 * (L-1)*L/2   <=>   L^2 - L - (xp/95) = 0
    The positive solution is:
        L = (1 + sqrt(1 + 4*(xp/95)))/2
    """
    """ return (1 + math.sqrt(1 + 4 * (xp / 95))) / 2 """

    return (1 + (xp / 190))

# ---------------------------
# Real-time update functions
# ---------------------------
def update_from_xp(event=None):
    """Update the results in the 'From EXP to Level' tab every time the EXP input changes."""
    try:
        xp_val = int(exp_var.get())
    except ValueError:
        result_level_var.set("Please enter a valid number for XP!")
        result_awarded_level_var.set("")
        result_next_level_var.set("")
        return

    if xp_val < 0:
        result_level_var.set("XP cannot be negative!")
        result_awarded_level_var.set("")
        result_next_level_var.set("")
        return

    # Calculate the raw (continuous) level and the assigned level (integer part)
    raw_level = raw_level_from_xp(xp_val)
    awarded_level = int(math.floor(raw_level))
    # The assigned level is capped at 1000 (even if the continuous progression goes beyond)
    capped_awarded_level = min(1000, awarded_level)

    result_level_var.set(f"Level (raw): {raw_level:.2f}")

    if awarded_level >= 1000:
        xp_for_1000 = total_xp_for_level(1000)
        extra = xp_val - xp_for_1000
        result_awarded_level_var.set(f"Assigned Level (capped at 1000): 1000  (Extra XP: {extra})")
        # If you want to simulate level 1001 beyond the cap:
        xp_for_1001 = total_xp_for_level(1001)
        diff = xp_for_1001 - xp_val
        result_next_level_var.set(f"(Simulated) For level 1001, {xp_for_1001} XP are needed (missing {diff} XP)")
    else:
        result_awarded_level_var.set(f"Assigned Level: {awarded_level}")
        xp_for_next = total_xp_for_level(awarded_level + 1)
        diff = xp_for_next - xp_val
        result_next_level_var.set(f"XP for next level: {xp_for_next} (missing {diff} XP)")

def update_from_level(event=None):
    """Update the results in the 'From Level to EXP' tab every time the level input changes."""
    try:
        level_val = int(level_var.get())
    except ValueError:
        result_xp_var.set("Please enter a valid number for the level!")
        result_xp_next_var.set("")
        return

    if level_val < 1:
        result_xp_var.set("Level must be at least 1.")
        result_xp_next_var.set("")
        return

    total_xp = total_xp_for_level(level_val)
    result_xp_var.set(f"Total EXP required for level {level_val}: {total_xp}")
    xp_next = xp_per_level(level_val)
    result_xp_next_var.set(f"EXP needed to progress from level {level_val} to {level_val+1}: {xp_next}")
    
    result_xp_over_1000.set(f"Hypothetical level assuming above 1000: {level_val-94905000}")

# ---------------------------
# Graphical User Interface with Tkinter
# ---------------------------
root = tk.Tk()
root.title("Fisch's EXP Calculator")

# Use a Notebook (tabs) for the two functions
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True, padx=10, pady=10)

# Tab 1: From EXP to Level
frame1 = ttk.Frame(notebook)
notebook.add(frame1, text="From EXP to Level")

ttk.Label(frame1, text="Enter EXP:").grid(row=0, column=0, padx=5, pady=5, sticky='w')
exp_var = tk.StringVar()
entry_exp = ttk.Entry(frame1, textvariable=exp_var, width=20)
entry_exp.grid(row=0, column=1, padx=5, pady=5)
# Update in real time on each key press
entry_exp.bind("<KeyRelease>", update_from_xp)

result_level_var = tk.StringVar()
result_awarded_level_var = tk.StringVar()
result_next_level_var = tk.StringVar()

ttk.Label(frame1, textvariable=result_level_var, foreground="blue").grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky='w')
ttk.Label(frame1, textvariable=result_awarded_level_var, foreground="green").grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky='w')
ttk.Label(frame1, textvariable=result_next_level_var, foreground="darkred").grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky='w')

# Tab 2: From Level to EXP
frame2 = ttk.Frame(notebook)
notebook.add(frame2, text="From Level to EXP")

ttk.Label(frame2, text="Enter Level:").grid(row=0, column=0, padx=5, pady=5, sticky='w')
level_var = tk.StringVar()
entry_level = ttk.Entry(frame2, textvariable=level_var, width=20)
entry_level.grid(row=0, column=1, padx=5, pady=5)
entry_level.bind("<KeyRelease>", update_from_level)

result_xp_var = tk.StringVar()
result_xp_next_var = tk.StringVar()
result_xp_over_1000 = tk.StringVar()

ttk.Label(frame2, textvariable=result_xp_var, foreground="blue").grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky='w')
ttk.Label(frame2, textvariable=result_xp_next_var, foreground="green").grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky='w')
ttk.Label(frame2, textvariable=result_xp_over_1000, foreground="orange").grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky='w')

# Start the GUI
root.mainloop()
