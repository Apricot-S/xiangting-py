// SPDX-FileCopyrightText: 2025 Apricot S.
// SPDX-License-Identifier: MIT
// This file is part of https://github.com/Apricot-S/xiangting-py

use crate::bingpai::BingpaiError;
use crate::config::PlayerCount;
use ::xiangting::{TileCounts, TileFlags};
use pyo3::prelude::*;

/// Calculates the replacement number (= xiangting number + 1) and necessary tiles for a given hand.
///
/// Args:
///     bingpai (list[int]): 兵牌: A hand excluding melds
///         (a.k.a. pure hand, 純手牌).
///     player_count (PlayerCount): The number of players.
///
/// Returns:
///     int: The replacement number (= xiangting number + 1).
///
/// Raises:
///     ValueError: If the hand is invalid.
///
/// Examples:
///     >>> # 199m146779p12s246z
///     >>> hand = [
///     ...     1, 0, 0, 0, 0, 0, 0, 0, 2, # m
///     ...     1, 0, 0, 1, 0, 1, 2, 0, 1, # p
///     ...     1, 1, 0, 0, 0, 0, 0, 0, 0, # s
///     ...     0, 1, 0, 1, 0, 1, 0, # z
///     ... ]
///     >>> rn, nt = calculate_necessary_tiles(hand, PlayerCount.FOUR)
///     >>> rn
///     5
///     >>> # 1239m123456789p1239s1234567z
///     >>> nt == 0b1111111_100000111_111111111_100000111
///     True
///
///     In three-player mahjong, the tiles from 2m (二萬) to 8m (八萬) are not used.
///
///     >>> # 1111m111122233z
///     >>> hand = [
///     ...     4, 0, 0, 0, 0, 0, 0, 0, 0, # m
///     ...     0, 0, 0, 0, 0, 0, 0, 0, 0, # p
///     ...     0, 0, 0, 0, 0, 0, 0, 0, 0, # s
///     ...     4, 3, 2, 0, 0, 0, 0, # z
///     ... ]
///     >>> rn_4p, nt_4p = calculate_necessary_tiles(hand, PlayerCount.FOUR)
///     >>> rn_4p
///     2
///     >>> # 23m
///     >>> nt_4p == 0b0000000_000000000_000000000_000000110
///     True
///     >>> rn_3p, nt_3p = calculate_necessary_tiles(hand, PlayerCount.THREE)
///     >>> rn_3p
///     3
///     >>> # 9m123456789p123456789s34567z
///     >>> nt_3p == 0b1111100_111111111_111111111_100000000
///     True
///
#[pyfunction]
#[pyo3(signature = (bingpai, player_count))]
pub(crate) fn calculate_necessary_tiles(
    bingpai: TileCounts,
    player_count: PlayerCount,
) -> PyResult<(u8, TileFlags)> {
    ::xiangting::calculate_necessary_tiles(&bingpai, &player_count.into())
        .map_err(self::BingpaiError::from)
        .map_err(PyErr::from)
}
