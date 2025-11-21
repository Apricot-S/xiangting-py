# SPDX-FileCopyrightText: 2024 Apricot S.
# SPDX-License-Identifier: MIT
# This file is part of https://github.com/Apricot-S/xiangting-py

from xiangting import PlayerCount, calculate_replacement_number

# 123m456p789s11222z
hand = [
    1, 1, 1, 0, 0, 0, 0, 0, 0, # m
    0, 0, 0, 1, 1, 1, 0, 0, 0, # p
    0, 0, 0, 0, 0, 0, 1, 1, 1, # s
    2, 3, 0, 0, 0, 0, 0, # z
]  # fmt: skip

replacement_number = calculate_replacement_number(hand, PlayerCount.FOUR)
assert replacement_number == 0
