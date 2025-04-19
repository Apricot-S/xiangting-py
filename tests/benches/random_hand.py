# SPDX-FileCopyrightText: 2024 Apricot S.
# SPDX-License-Identifier: MIT
# This file is part of https://github.com/Apricot-S/xiangting-py

from random import Random
from typing import Final


def create_rng() -> Random:
    return Random(42)  # noqa: S311


CHOICES: Final = [1, 2, 4, 5, 7, 8, 10, 11, 13, 14]


def choose_hand_length(rng: Random) -> int:
    return rng.choice(CHOICES)


def fill_hand(wall: list[int], hand_length: int) -> list[int]:
    hand = [0] * 34
    for tile in wall[:hand_length]:
        hand[tile] += 1
    return hand


def generate_random_pure_hand(rng: Random) -> list[int]:
    wall = [i // 4 for i in range(136)]
    rng.shuffle(wall)
    hand_length = choose_hand_length(rng)
    return fill_hand(wall, hand_length)


def generate_random_half_flush_pure_hand(rng: Random) -> list[int]:
    color_start = rng.choice([0, 9, 18])
    suits = [(i // 4 + color_start) for i in range(36)]
    honors = [(i // 4 + 27) for i in range(28)]
    wall = suits + honors
    rng.shuffle(wall)
    hand_length = choose_hand_length(rng)
    return fill_hand(wall, hand_length)


def generate_random_full_flush_pure_hand(rng: Random) -> list[int]:
    color_start = rng.choice([0, 9, 18])
    wall = [(i // 4 + color_start) for i in range(36)]
    rng.shuffle(wall)
    hand_length = choose_hand_length(rng)
    return fill_hand(wall, hand_length)


NON_SIMPLES: Final = [0, 8, 9, 17, 18, 26, 27, 28, 29, 30, 31, 32, 33]


def generate_random_non_simple_pure_hand(rng: Random) -> list[int]:
    wall = [NON_SIMPLES[i % 13] for i in range(52)]
    rng.shuffle(wall)
    hand_length = choose_hand_length(rng)
    return fill_hand(wall, hand_length)
