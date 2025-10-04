# SPDX-FileCopyrightText: 2024 Apricot S.
# SPDX-License-Identifier: MIT
# This file is part of https://github.com/Apricot-S/xiangting-py

from xiangting import (
    ClaimedTilePosition,
    FuluMianzi,
    calculate_replacement_number,
)

# 123m1z
hand = [
    1, 1, 1, 0, 0, 0, 0, 0, 0, # m
    0, 0, 0, 0, 0, 0, 0, 0, 0, # p
    0, 0, 0, 0, 0, 0, 0, 0, 0, # s
    1, 0, 0, 0, 0, 0, 0, # z
]  # fmt: skip

# 456p 7777s 111z
melds = [
    FuluMianzi.Shunzi(12, ClaimedTilePosition.LOW),
    FuluMianzi.Gangzi(24),
    FuluMianzi.Kezi(27),
]

replacement_number_wo_melds = calculate_replacement_number(hand, None)
assert replacement_number_wo_melds == 1

replacement_number_w_melds = calculate_replacement_number(hand, melds)
assert replacement_number_w_melds == 2
