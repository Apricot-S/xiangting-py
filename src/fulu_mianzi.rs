// SPDX-FileCopyrightText: 2024 Apricot S.
// SPDX-License-Identifier: MIT
// This file is part of https://github.com/Apricot-S/xiangting-py

use pyo3::prelude::*;
use std::fmt;

/// Position of the claimed tile in the melded sequence.
///
/// Used in ``FuluMianzi.Shunzi``.
///
/// Attributes:
///     LOW: The claimed tile is the lowest in the sequence.
///         For example, claiming a 3 to form a sequence of 3-4-5.
///     MIDDLE: The claimed tile is the middle in the sequence.
///         For example, claiming a 4 to form a sequence of 3-4-5.
///     HIGH: The claimed tile is the highest in the sequence.
///         For example, claiming a 5 to form a sequence of 3-4-5.
///
#[pyclass(eq, eq_int, rename_all = "UPPERCASE")]
#[derive(Clone, PartialEq)]
pub(crate) enum ClaimedTilePosition {
    Low,
    Middle,
    High,
}

impl From<self::ClaimedTilePosition> for ::xiangting::ClaimedTilePosition {
    fn from(value: self::ClaimedTilePosition) -> Self {
        match value {
            self::ClaimedTilePosition::Low => ::xiangting::ClaimedTilePosition::Low,
            self::ClaimedTilePosition::Middle => ::xiangting::ClaimedTilePosition::Middle,
            self::ClaimedTilePosition::High => ::xiangting::ClaimedTilePosition::High,
        }
    }
}

/// 副露面子: Meld.
///
/// Attributes:
///     Shunzi: 順子: Sequence.
///         The first argument represents the index of the tile.
///         The second argument represents the position of the claimed
///         tile in the meld. The correspondence between the index and
///         the tile is the same as ``bingpai``.
///     Kezi: 刻子: Triplet.
///         The argument represents the index of the tile.
///         The correspondence between the index and the tile is the
///         same as ``bingpai``.
///     Gangzi: 槓子: Quad.
///         The argument represents the index of the tile.
///         The correspondence between the index and the tile is the
///         same as ``bingpai``.
///
/// Examples
///     >>> # 4-56p (Chii 4p Low)
///     >>> shunzi = FuluMianzi.Shunzi(12, ClaimedTilePosition.LOW)
///     >>> # 1-11z (Pon 1z)
///     >>> kezi = FuluMianzi.Kezi(27)
///     >>> # 7-777s (Kan 7s)
///     >>> gangzi = FuluMianzi.Gangzi(24)
///
#[pyclass]
#[derive(Clone)]
pub(crate) enum FuluMianzi {
    Shunzi(u8, self::ClaimedTilePosition),
    Kezi(u8),
    Gangzi(u8),
}

#[pymethods]
impl FuluMianzi {
    fn __str__(&self) -> String {
        self.to_string()
    }
}

impl From<self::FuluMianzi> for ::xiangting::FuluMianzi {
    fn from(value: self::FuluMianzi) -> Self {
        match value {
            self::FuluMianzi::Shunzi(t, p) => ::xiangting::FuluMianzi::Shunzi(t, p.into()),
            self::FuluMianzi::Kezi(t) => ::xiangting::FuluMianzi::Kezi(t),
            self::FuluMianzi::Gangzi(t) => ::xiangting::FuluMianzi::Gangzi(t),
        }
    }
}

const TILE_NAMES: [&str; 34] = [
    "1m", "2m", "3m", "4m", "5m", "6m", "7m", "8m", "9m", // m
    "1p", "2p", "3p", "4p", "5p", "6p", "7p", "8p", "9p", // p
    "1s", "2s", "3s", "4s", "5s", "6s", "7s", "8s", "9s", // s
    "1z", "2z", "3z", "4z", "5z", "6z", "7z", // z
];

impl fmt::Display for self::FuluMianzi {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            FuluMianzi::Shunzi(index, position) => {
                let position_str = match position {
                    ClaimedTilePosition::Low => "Low",
                    ClaimedTilePosition::Middle => "Middle",
                    ClaimedTilePosition::High => "High",
                };
                f.write_str(&format!(
                    "Chii-{}-{}",
                    TILE_NAMES[*index as usize], &position_str
                ))
            }
            FuluMianzi::Kezi(index) => f.write_str(&format!("Pon-{}", TILE_NAMES[*index as usize])),
            FuluMianzi::Gangzi(index) => {
                f.write_str(&format!("Kan-{}", TILE_NAMES[*index as usize]))
            }
        }
    }
}
