# SPDX-FileCopyrightText: 2025 Apricot S.
# SPDX-License-Identifier: MIT
# This file is part of https://github.com/Apricot-S/xiangting-py

from xiangting import (
    PlayerCount,
    calculate_necessary_tiles,
    calculate_unnecessary_tiles,
)

# 199m146779p12s246z
hand = [
    1, 0, 0, 0, 0, 0, 0, 0, 2, # m
    1, 0, 0, 1, 0, 1, 2, 0, 1, # p
    1, 1, 0, 0, 0, 0, 0, 0, 0, # s
    0, 1, 0, 1, 0, 1, 0, # z
]  # fmt: skip

(replacement_number1, necessary_tiles) = calculate_necessary_tiles(
    hand,
    PlayerCount.FOUR,
)
(replacement_number2, unnecessary_tiles) = calculate_unnecessary_tiles(
    hand,
    PlayerCount.FOUR,
)

assert replacement_number1 == 5
assert replacement_number1 == replacement_number2
# 1239m123456789p1239s1234567z
assert necessary_tiles == 0b1111111_100000111_111111111_100000111
# 1m14679p12s246z
assert unnecessary_tiles == 0b0101010_000000011_101101001_000000001
