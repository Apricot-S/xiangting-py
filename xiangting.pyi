# SPDX-FileCopyrightText: 2024 Apricot S.
# SPDX-License-Identifier: MIT
# This file is part of https://github.com/Apricot-S/xiangting-py

def to_array(tile_flags: int) -> list[bool]:
    """Converts the bit flag set into a boolean array.

    Args:
        tile_flags (int): Bitmask representing the set of tiles.
            Each bit corresponds to a tile index (0-33).
            The least significant bit (bit 0) represents 1m,
            bit 1 represents 2m, …, and bit 33 represents Red (7z).

    Returns:
        list[bool]: A boolean array of length 34, where ``True`` means
        the tile is present.

    Raises:
        OverflowError: If ``tile_flags`` is greater than ``2**64 - 1``.

    Examples:
        >>> # 1m456p789s12z
        >>> flags = 0b0000011_111000000_000111000_000000001
        >>> arr = to_array(flags)
        >>> len(arr)
        34
        >>> arr[0]  # 1m
        True
        >>> arr[12] # 4p
        True
        >>> arr[28] # 2z (South)
        True
        >>> arr[4]  # 5m not in the set
        False
    """

class PlayerCount:
    """The number of players.

    Attributes:
        FOUR: Four-player mahjong (the standard rules).
        THREE: Three-player mahjong.

            - Tiles from 2m (二萬) to 8m (八萬) are not used.
    """

    FOUR: PlayerCount
    THREE: PlayerCount

def calculate_replacement_number(
    bingpai: list[int], player_count: PlayerCount
) -> int:
    """Calculates the replacement number (= xiàngtīng number + 1) for a given hand.

    Args:
        bingpai (list[int]): 兵牌: A hand excluding melds
            (a.k.a. pure hand, 純手牌).
        player_count (PlayerCount): The number of players.

    Returns:
        int: The replacement number (= xiàngtīng number + 1).

    Raises:
        ValueError: If the hand is invalid.

    Examples:
        >>> # 123m456p789s11222z
        >>> hand = [
        ...     1, 1, 1, 0, 0, 0, 0, 0, 0, # m
        ...     0, 0, 0, 1, 1, 1, 0, 0, 0, # p
        ...     0, 0, 0, 0, 0, 0, 1, 1, 1, # s
        ...     2, 3, 0, 0, 0, 0, 0, # z
        ... ]
        >>> calculate_replacement_number(hand, PlayerCount.FOUR)
        0

        In three-player mahjong, the tiles from 2m (二萬) to 8m (八萬) are not used.

        >>> # 1111m111122233z
        >>> hand = [
        ...     4, 0, 0, 0, 0, 0, 0, 0, 0, # m
        ...     0, 0, 0, 0, 0, 0, 0, 0, 0, # p
        ...     0, 0, 0, 0, 0, 0, 0, 0, 0, # s
        ...     4, 3, 2, 0, 0, 0, 0, # z
        ... ]
        >>> calculate_replacement_number(hand, PlayerCount.FOUR)
        2
        >>> calculate_replacement_number(hand, PlayerCount.THREE)
        3
    """

def calculate_necessary_tiles(
    bingpai: list[int],
    player_count: PlayerCount,
) -> tuple[int, int]:
    """Calculates the replacement number (= xiàngtīng number + 1) and necessary tiles for a given hand.

    Args:
        bingpai (list[int]): 兵牌: A hand excluding melds
            (a.k.a. pure hand, 純手牌).
        player_count (PlayerCount): The number of players.

    Returns:
        tuple[int, int]: A tuple (rn, nt), where rn is the replacement
        number (= xiàngtīng number + 1), and nt is a bit flag set
        representing necessary tiles.

    Raises:
        ValueError: If the hand is invalid.

    Examples:
        >>> # 199m146779p12s246z
        >>> hand = [
        ...     1, 0, 0, 0, 0, 0, 0, 0, 2, # m
        ...     1, 0, 0, 1, 0, 1, 2, 0, 1, # p
        ...     1, 1, 0, 0, 0, 0, 0, 0, 0, # s
        ...     0, 1, 0, 1, 0, 1, 0, # z
        ... ]
        >>> rn, nt = calculate_necessary_tiles(hand, PlayerCount.FOUR)
        >>> rn
        5
        >>> # 1239m123456789p1239s1234567z
        >>> nt == 0b1111111_100000111_111111111_100000111
        True

        In three-player mahjong, the tiles from 2m (二萬) to 8m (八萬) are not used.

        >>> # 1111m111122233z
        >>> hand = [
        ...     4, 0, 0, 0, 0, 0, 0, 0, 0, # m
        ...     0, 0, 0, 0, 0, 0, 0, 0, 0, # p
        ...     0, 0, 0, 0, 0, 0, 0, 0, 0, # s
        ...     4, 3, 2, 0, 0, 0, 0, # z
        ... ]
        >>> rn_4p, nt_4p = calculate_necessary_tiles(hand, PlayerCount.FOUR)
        >>> rn_4p
        2
        >>> # 23m
        >>> nt_4p == 0b0000000_000000000_000000000_000000110
        True
        >>> rn_3p, nt_3p = calculate_necessary_tiles(hand, PlayerCount.THREE)
        >>> rn_3p
        3
        >>> # 9m123456789p123456789s34567z
        >>> nt_3p == 0b1111100_111111111_111111111_100000000
        True
    """

def calculate_unnecessary_tiles(
    bingpai: list[int],
    player_count: PlayerCount,
) -> tuple[int, int]:
    """Calculates the replacement number (= xiàngtīng number + 1) and unnecessary tiles for a given hand.

    Args:
        bingpai (list[int]): 兵牌: A hand excluding melds
            (a.k.a. pure hand, 純手牌).
        player_count (PlayerCount): The number of players.

    Returns:
        tuple[int, int]: A tuple (rn, ut), where rn is the replacement
        number (= xiàngtīng number + 1), and ut is a bit flag set
        representing unnecessary tiles.

    Raises:
        ValueError: If the hand is invalid.

    Examples:
        >>> # 199m146779p12s246z
        >>> hand = [
        ...     1, 0, 0, 0, 0, 0, 0, 0, 2, # m
        ...     1, 0, 0, 1, 0, 1, 2, 0, 1, # p
        ...     1, 1, 0, 0, 0, 0, 0, 0, 0, # s
        ...     0, 1, 0, 1, 0, 1, 0, # z
        ... ]
        >>> rn, ut = calculate_unnecessary_tiles(hand, PlayerCount.FOUR)
        >>> rn
        5
        >>> # 1m14679p12s246z
        >>> ut == 0b0101010_000000011_101101001_000000001
        True

        In three-player mahjong, the tiles from 2m (二萬) to 8m (八萬) are not used.

        >>> # 1111m111122233z
        >>> hand = [
        ...     4, 0, 0, 0, 0, 0, 0, 0, 0, # m
        ...     0, 0, 0, 0, 0, 0, 0, 0, 0, # p
        ...     0, 0, 0, 0, 0, 0, 0, 0, 0, # s
        ...     4, 3, 2, 0, 0, 0, 0, # z
        ... ]
        >>> rn_4p, ut_4p = calculate_unnecessary_tiles(hand, PlayerCount.FOUR)
        >>> rn_4p
        2
        >>> # 1z
        >>> ut_4p == 0b0000001_000000000_000000000_000000000
        True
        >>> rn_3p, ut_3p = calculate_unnecessary_tiles(hand, PlayerCount.THREE)
        >>> rn_3p
        3
        >>> # 1m1z
        >>> ut_3p == 0b0000001_000000000_000000000_000000001
        True
    """
