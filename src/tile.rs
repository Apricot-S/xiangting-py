// SPDX-FileCopyrightText: 2025 Apricot S.
// SPDX-License-Identifier: MIT
// This file is part of https://github.com/Apricot-S/xiangting-py

use ::xiangting::{TileFlags, TileFlagsExt};
use pyo3::prelude::*;

#[pyfunction]
pub(crate) fn to_array(tile_flags: TileFlags) -> [bool; 34] {
    tile_flags.to_array()
}
