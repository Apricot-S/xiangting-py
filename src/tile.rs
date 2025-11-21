// SPDX-FileCopyrightText: 2025 Apricot S.
// SPDX-License-Identifier: MIT
// This file is part of https://github.com/Apricot-S/xiangting-py

use ::xiangting::{TileFlags, TileFlagsExt};
use pyo3::prelude::*;

/// Converts the bit flag set into a boolean array.
///
/// Args:
///     tile_flags (int): Bitmask representing the set of tiles.
///         Each bit corresponds to a tile index (0-33).
///         The least significant bit (bit 0) represents 1m,
///         bit 1 represents 2m, …, and bit 33 represents Red (7z).
///
/// Returns:
///     list[bool]: Boolean array of length 34, where ``True`` means
///         the tile is present.
///
/// Raises:
///     OverflowError: If ``tile_flags`` is greater than ``2**64 - 1``.
///
/// Examples:
///     >>> # 1m456p789s12z
///     >>> flags = 0b0000011_111000000_000111000_000000001
///     >>> arr = to_array(flags)
///     >>> len(arr)
///     34
///     >>> arr[0]  # 1m
///     True
///     >>> arr[12] # 4p
///     True
///     >>> arr[28] # 2z (South)
///     True
///     >>> arr[4]  # 5m not in the set
///     False
///
#[pyfunction]
pub(crate) fn to_array(tile_flags: TileFlags) -> [bool; 34] {
    tile_flags.to_array()
}
