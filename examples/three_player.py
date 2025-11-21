# SPDX-FileCopyrightText: 2024 Apricot S.
# SPDX-License-Identifier: MIT
# This file is part of https://github.com/Apricot-S/xiangting-py

from xiangting import PlayerCount, calculate_replacement_number

# 1111m111122233z
hand = [
    4, 0, 0, 0, 0, 0, 0, 0, 0, # m
    0, 0, 0, 0, 0, 0, 0, 0, 0, # p
    0, 0, 0, 0, 0, 0, 0, 0, 0, # s
    4, 3, 2, 0, 0, 0, 0, # z
]  # fmt: skip

replacement_number_4p = calculate_replacement_number(hand, PlayerCount.FOUR)
assert replacement_number_4p == 2

replacement_number_3p = calculate_replacement_number(hand, PlayerCount.THREE)
assert replacement_number_3p == 3
