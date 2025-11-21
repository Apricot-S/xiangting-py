// SPDX-FileCopyrightText: 2025 Apricot S.
// SPDX-License-Identifier: MIT
// This file is part of https://github.com/Apricot-S/xiangting-py

use pyo3::prelude::*;

/// The number of players.
///
/// Attributes:
///     FOUR: Four-player mahjong (the standard rules).
///     THREE: Three-player mahjong.
///
///         - Tiles from 2m (二萬) to 8m (八萬) are not used.
///
#[pyclass(eq, eq_int, rename_all = "UPPERCASE")]
#[derive(Clone, PartialEq)]
pub(crate) enum PlayerCount {
    Four,
    Three,
}

impl From<self::PlayerCount> for ::xiangting::PlayerCount {
    fn from(value: self::PlayerCount) -> Self {
        match value {
            self::PlayerCount::Four => ::xiangting::PlayerCount::Four,
            self::PlayerCount::Three => ::xiangting::PlayerCount::Three,
        }
    }
}
