// SPDX-FileCopyrightText: 2025 Apricot S.
// SPDX-License-Identifier: MIT
// This file is part of https://github.com/Apricot-S/xiangting-py

use crate::bingpai::BingpaiError;
use crate::config::PlayerCount;
use ::xiangting::{TileCounts, TileFlags};
use pyo3::prelude::*;

/// Calculates the replacement number (= xiangting number + 1) and unnecessary tiles for a given hand.
///
/// Args:
///     bingpai (list[int]): 兵牌: A hand excluding melds
///         (a.k.a. pure hand, 純手牌).
///     player_count (PlayerCount): The number of players.
///
/// Returns:
///     tuple[int, int]: A tuple (rn, ut), where rn is the replacement
///     number (= xiangting number + 1), and ut is a bit flag set
///     representing unnecessary tiles.
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
///     >>> rn, ut = calculate_unnecessary_tiles(hand, PlayerCount.FOUR)
///     >>> rn
///     5
///     >>> # 1m14679p12s246z
///     >>> ut == 0b0101010_000000011_101101001_000000001
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
///     >>> rn_4p, ut_4p = calculate_unnecessary_tiles(hand, PlayerCount.FOUR)
///     >>> rn_4p
///     2
///     >>> # 1z
///     >>> ut_4p == 0b0000001_000000000_000000000_000000000
///     True
///     >>> rn_3p, ut_3p = calculate_unnecessary_tiles(hand, PlayerCount.THREE)
///     >>> rn_3p
///     3
///     >>> # 1m1z
///     >>> ut_3p == 0b0000001_000000000_000000000_000000001
///     True
///
#[pyfunction]
#[pyo3(signature = (bingpai, player_count))]
pub(crate) fn calculate_unnecessary_tiles(
    bingpai: TileCounts,
    player_count: PlayerCount,
) -> PyResult<(u8, TileFlags)> {
    ::xiangting::calculate_unnecessary_tiles(&bingpai, &player_count.into())
        .map_err(self::BingpaiError::from)
        .map_err(PyErr::from)
}
