#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# homework_1.py
# MIT OCW 6.189 (January IAP 2011)
# Author: Aleksey Lunev
# Fer 20, 2017

from __future__ import print_function


# ===========================     Exercise   1.7     ===========================
# Determine the result of a rock, paper, scissors game, given Player 1 and
# Player 2's choices.
#
# A truth table for all the possible choices for player 1 and 2, and the
# outcome of the game:
#
#   Player 1  |  Player 2  |   Result
# ---------------------------------------
#     Rock    |    Rock    |    Tie
#     Rock    |  Scissors  |  Player 1
#     Rock    |   Paper    |  Player 2
#   Scissors  |    Rock    |  Player 2
#   Scissors  |  Scissors  |    Tie
#   Scissors  |   Paper    |  Player 1
#    Paper    |    Rock    |  Player 1
#    Paper    |  Scissors  |  Player 2
#    Paper    |   Paper    |    Tie

print("    Exercise   1.7    ".center(80, "="))
print()
print("A rock, paper, scissors game.\n")

toys = frozenset(("ROCK", "PAPER", "SCISSORS"))

while True:
    player_one = input("Player 1? ").upper()
    if player_one in toys:
        break
    else:
        print("This is not a valid object selection")

while True:
    player_two = input("Player 2? ").upper()
    if player_two in toys:
        break
    else:
        print("This is not a valid object selection")

if (player_one == "ROCK" and player_two == "SCISSORS"
    or player_one == "SCISSORS" and player_two == "PAPER"
    or player_one == "PAPER" and player_two == "ROCK"):
    print("Player 1 wins.")
elif player_one == player_two:
    print("Tie.")
else:
    print("Player 2 wins.")
