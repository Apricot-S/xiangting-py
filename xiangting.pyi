# SPDX-FileCopyrightText: 2024 Apricot S.
# SPDX-License-Identifier: MIT
# This file is part of https://github.com/Apricot-S/xiangting-py

from collections.abc import Sequence

class ClaimedTilePosition:
    LOW: ClaimedTilePosition
    MIDDLE: ClaimedTilePosition
    HIGH: ClaimedTilePosition

class FuluMianzi:
    class Shunzi(FuluMianzi):
        def __init__(
            self,
            tile: int,
            position: ClaimedTilePosition,
            /,
        ) -> None: ...

    class Kezi(FuluMianzi):
        def __init__(self, tile: int, /) -> None: ...

    class Gangzi(FuluMianzi):
        def __init__(self, tile: int, /) -> None: ...

def calculate_replacement_number(
    bingpai: list[int],
    fulu_mianzi_list: Sequence[FuluMianzi] | None,
) -> int: ...
def calculate_replacement_number_3_player(
    bingpai: list[int],
    fulu_mianzi_list: Sequence[FuluMianzi] | None,
) -> int: ...
