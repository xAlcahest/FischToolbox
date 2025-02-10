# Fisch's EXP Calculator: README

This repository contains two Python scripts: `EXPCalc.py` and `over1000.py`. Both scripts are designed to calculate experience points (XP) and levels in a game-like system, with a focus on levels exceeding the cap of 1000. These applications use `Tkinter` for their graphical user interfaces (GUIs).

## Features Overview

### `EXPCalc.py`
A comprehensive EXP calculator with two main functionalities:
1. Calculate the level based on a given amount of XP.
2. Calculate the total XP required to reach a specific level.

### `over1000.py`
A specialized calculator for handling XP and levels above the level 1000 cap. This script computes the extended level, total XP, and XP requirements for progression.

---

## EXPCalc.py: Detailed Overview

### Purpose
This script is designed to calculate:
1. The level corresponding to a given XP value.
2. The total XP required to achieve a specific level.
3. Remaining XP to reach the next level.

### GUI Tabs
The application has two tabs:
1. **From EXP to Level**:
   - Input: XP amount.
   - Output:
     - Raw (continuous) level.
     - Capped level (up to 1000).
     - XP needed for the next level.
     - Simulated information for levels exceeding 1000.

2. **From Level to EXP**:
   - Input: Level.
   - Output:
     - Total XP required to reach the specified level.
     - XP required to progress to the next level.
     - Hypothetical levels above 1000.

### Core Functions
1. **`xp_per_level(level)`**: Calculates XP required to advance from `level` to `level + 1`.
2. **`total_xp_for_level(level)`**: Computes the total XP required to reach `level`.
3. **`raw_level_from_xp(xp)`**: Calculates the continuous level for a given XP amount.

### Usage
Run the script:
```bash
python EXPCalc.py
