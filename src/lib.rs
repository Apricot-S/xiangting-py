// SPDX-FileCopyrightText: 2024 Apricot S.
// SPDX-License-Identifier: MIT
// This file is part of https://github.com/Apricot-S/xiangting-py

mod calculate;
mod fulu_mianzi;
mod shoupai;

use crate::calculate::{calculate_replacement_number, calculate_replacement_number_3_player};
use crate::fulu_mianzi::{ClaimedTilePosition, FuluMianzi};
use pyo3::prelude::*;

/// Python bindings for `xiangting <https://crates.io/crates/xiangting>`_.
///
/// See also `xiangting <https://crates.io/crates/xiangting>`_ for
/// more information.
///
/// The hand is represented as an array of ``list[int]``, where each
/// element represents the count of a specific tile. The correspondence
/// between the index and the tile is shown in the table below.
///
/// +-------+-----+-----+-----+-----+-----+-----+-----+-----+-----+
/// | Index | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   |
/// +-------+-----+-----+-----+-----+-----+-----+-----+-----+-----+
/// | Tile  | 1m  | 2m  | 3m  | 4m  | 5m  | 6m  | 7m  | 8m  | 9m  |
/// +-------+-----+-----+-----+-----+-----+-----+-----+-----+-----+
///
/// +-------+-----+-----+-----+-----+-----+-----+-----+-----+-----+
/// | Index | 9   | 10  | 11  | 12  | 13  | 14  | 15  | 16  | 17  |
/// +-------+-----+-----+-----+-----+-----+-----+-----+-----+-----+
/// | Tile  | 1p  | 2p  | 3p  | 4p  | 5p  | 6p  | 7p  | 8p  | 9p  |
/// +-------+-----+-----+-----+-----+-----+-----+-----+-----+-----+
///
/// +-------+-----+-----+-----+-----+-----+-----+-----+-----+-----+
/// | Index | 18  | 19  | 20  | 21  | 22  | 23  | 24  | 25  | 26  |
/// +-------+-----+-----+-----+-----+-----+-----+-----+-----+-----+
/// | Tile  | 1s  | 2s  | 3s  | 4s  | 5s  | 6s  | 7s  | 8s  | 9s  |
/// +-------+-----+-----+-----+-----+-----+-----+-----+-----+-----+
///
/// +-------+-----------+------------+-----------+------------+------------+------------+----------+
/// | Index | 27        | 28         | 29        | 30         | 31         | 32         | 33       |
/// +-------+-----------+------------+-----------+------------+------------+------------+----------+
/// | Tile  | East (1z) | South (2z) | West (3z) | North (4z) | White (5z) | Green (6z) | Red (7z) |
/// +-------+-----------+------------+-----------+------------+------------+------------+----------+
///
/// Example:
///     >>> # 123m456p789s11222z
///     >>> hand_14 = [
///     ...     1, 1, 1, 0, 0, 0, 0, 0, 0, # m
///     ...     0, 0, 0, 1, 1, 1, 0, 0, 0, # p
///     ...     0, 0, 0, 0, 0, 0, 1, 1, 1, # s
///     ...     2, 3, 0, 0, 0, 0, 0, # z
///     ... ]
///     >>> r = calculate_replacement_number(hand_14, None)
///     >>> print(r)
///     0
///
#[pymodule]
fn xiangting(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<ClaimedTilePosition>()?;
    m.add_class::<FuluMianzi>()?;
    m.add_function(wrap_pyfunction!(calculate_replacement_number, m)?)?;
    m.add_function(wrap_pyfunction!(calculate_replacement_number_3_player, m)?)?;
    Ok(())
}
