# SPDX-FileCopyrightText: 2024 Apricot S.
# SPDX-License-Identifier: MIT
# This file is part of https://github.com/Apricot-S/xiangting-py

from xiangting import (
    PlayerCount,
    calculate_necessary_tiles,
    calculate_unnecessary_tiles,
)

# 1111m111122233z
hand = [
    4, 0, 0, 0, 0, 0, 0, 0, 0, # m
    0, 0, 0, 0, 0, 0, 0, 0, 0, # p
    0, 0, 0, 0, 0, 0, 0, 0, 0, # s
    4, 3, 2, 0, 0, 0, 0, # z
]  # fmt: skip

rn_4p, nt_4p = calculate_necessary_tiles(hand, PlayerCount.FOUR)
_, ut_4p = calculate_unnecessary_tiles(hand, PlayerCount.FOUR)
assert rn_4p == 2
assert nt_4p == 0b0000000_000000000_000000000_000000110  # 23m
assert ut_4p == 0b0000001_000000000_000000000_000000000  # 1z

rn_3p, nt_3p = calculate_necessary_tiles(hand, PlayerCount.THREE)
_, ut_3p = calculate_unnecessary_tiles(hand, PlayerCount.THREE)
assert rn_3p == 3
# 9m123456789p123456789s34567z
assert nt_3p == 0b1111100_111111111_111111111_100000000
assert ut_3p == 0b0000001_000000000_000000000_000000001  # 1m1z
