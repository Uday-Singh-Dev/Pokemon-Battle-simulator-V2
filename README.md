# Pokemon Battle Simulator

A turn-based Pokemon battle simulator built in Python using Tkinter, featuring a full type effectiveness system, animated health and XP bars, a stat-based damage formula, and a letter-by-letter text engine.

---
 
## Overview

This is the second version of the Pokemon Simulator, rebuilt from the ground up to be significantly more efficient than the original. Where the first version relied on hardcoded stats, a rigid save system, and repeated logic across functions, this version introduces a proper stat array system, a reusable type effectiveness function, and a generalised damage formula that handles normal, special, and status moves through a single calculation path.

The objective was not only to recreate the feel of a Pokemon battle, but to build systems flexible enough that new Pokemon, moves, and types could be slotted in without rewriting core logic.

---

## Key Features

- Turn-based battle system with speed-based turn order
- Stat-driven damage formula using attack, defence, special attack, and special defence
- Type effectiveness system — super effective, not very effective, and immune
- Miss and evasion mechanics with configurable accuracy per move
- Critical hit and damage variation system
- Animated health bar that decrements in real time
- Animated XP bar with level up detection and stat scaling
- Letter-by-letter text engine for battle messages
- Move kind system — normal, special, and status moves handled separately

---

## Architecture Highlights

- Pokemon stats stored in arrays and referenced consistently across all damage and UI functions
- Damage calculation separated into user and opponent functions, both referencing the same type system
- Type system implemented as a single reusable function passed move type and defender type as arguments
- Speed stat determines turn order each round before any damage is calculated
- Health and XP bars animated by incrementally updating canvas coordinates each frame

---

## Technologies Used

- Python
- Tkinter

---

## What I Learned

- Breaking a complex game system down into discrete, reusable logic
- Designing and implementing a type effectiveness system across multiple types
- Building a stat-based damage formula that scales with level
- Animating canvas elements in real time using coordinate updates and time delays
- Managing turn order and battle flow through a single coordinated fight sequence

---

## Controls

- Fight - Select a move to attack with
- Bag - Access your items
- Pokemon - Switch Pokemon
- Run - Flee the battle

---

## How to Run

1. Install Python 3.x
2. Run the game:
