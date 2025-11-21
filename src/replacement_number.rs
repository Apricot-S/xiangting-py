// SPDX-FileCopyrightText: 2025 Apricot S.
// SPDX-License-Identifier: MIT
// This file is part of https://github.com/Apricot-S/xiangting-py

use crate::bingpai::BingpaiError;
use crate::config::PlayerCount;
use ::xiangting::TileCounts;
use pyo3::prelude::*;

/// Calculates the replacement number (= xiangting number + 1) for a given hand.
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
///     >>> # 123m456p789s11222z
///     >>> hand = [
///     ...     1, 1, 1, 0, 0, 0, 0, 0, 0, # m
///     ...     0, 0, 0, 1, 1, 1, 0, 0, 0, # p
///     ...     0, 0, 0, 0, 0, 0, 1, 1, 1, # s
///     ...     2, 3, 0, 0, 0, 0, 0, # z
///     ... ]
///     >>> calculate_replacement_number(hand, None)
///     0
///
#[pyfunction]
#[pyo3(signature = (bingpai, player_count))]
pub(crate) fn calculate_replacement_number(
    bingpai: TileCounts,
    player_count: PlayerCount,
) -> PyResult<u8> {
    ::xiangting::calculate_replacement_number(&bingpai, &player_count.into())
        .map_err(self::BingpaiError::from)
        .map_err(PyErr::from)
}
