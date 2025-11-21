# SPDX-FileCopyrightText: 2024 Apricot S.
# SPDX-License-Identifier: MIT
# This file is part of https://github.com/Apricot-S/xiangting-py

type TileFlags = int

class PlayerCount:
    FOUR: PlayerCount
    THREE: PlayerCount

def calculate_replacement_number(
    bingpai: list[int],
    player_count: PlayerCount,
) -> int: ...
def calculate_necessary_tiles(
    bingpai: list[int],
    player_count: PlayerCount,
) -> tuple[int, TileFlags]: ...
def calculate_unnecessary_tiles(
    bingpai: list[int],
    player_count: PlayerCount,
) -> tuple[int, TileFlags]: ...
