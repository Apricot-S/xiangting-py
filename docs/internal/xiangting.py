from typing import Self


class ClaimedTilePosition:
    LOW: Self
    MIDDLE: Self
    HIGH: Self


class FuluMianzi:
    """副露面子: Meld.

    Examples
        >>> # 4-56p (Chii 4p Low)
        >>> shunzi = FuluMianzi.Shunzi(12, ClaimedTilePosition.LOW)
        >>> # 1-11z (Pon 1z)
        >>> kezi = FuluMianzi.Kezi(27)
        >>> # 7-777s (Kan 7s)
        >>> gangzi = FuluMianzi.Gangzi(24)
    """


class Shunzi(FuluMianzi):
    """順子: Sequence.

    Args:
        tile (int): The index of the tile. The correspondence between
            the index and the tile is the same as ``bingpai``.
        position (ClaimedTilePosition): The position of the claimed
            tile in the meld. The correspondence between the index
            and the tile is the same as ``bingpai``.

    Examples
        >>> # 1-23m (Chii 1m Low)
        >>> shunzi_low = FuluMianzi.Shunzi(0, ClaimedTilePosition.LOW)
        >>> # 2-13m (Chii 2m Middle)
        >>> shunzi_middle = FuluMianzi.Shunzi(1, ClaimedTilePosition.MIDDLE)
        >>> # 3-12m (Chii 3m High)
        >>> shunzi_high = FuluMianzi.Shunzi(2, ClaimedTilePosition.HIGH)
    """

    def __init__(
        self,
        tile: int,
        position: ClaimedTilePosition,
        /,
    ) -> None: ...


class Kezi(FuluMianzi):
    """刻子: Triplet.

    Args:
        tile (int): The index of the tile. The correspondence between
            the index and the tile is the same as ``bingpai``.

    Examples
        >>> # 1-11m (Pon 1m)
        >>> kezi = FuluMianzi.Kezi(0)
    """

    def __init__(self, tile: int, /) -> None: ...


class Gangzi(FuluMianzi):
    """槓子: Quad.

    Args:
        tile (int): The index of the tile. The correspondence between
            the index and the tile is the same as ``bingpai``.

    Examples
        >>> # 1-111m (Kan 1m)
        >>> gangzi = FuluMianzi.Gangzi(0)
    """

    def __init__(self, tile: int, /) -> None: ...


FuluMianzi.Shunzi = Shunzi  # type: ignore
FuluMianzi.Kezi = Kezi  # type: ignore
FuluMianzi.Gangzi = Gangzi  # type: ignore

del Shunzi
del Kezi
del Gangzi
