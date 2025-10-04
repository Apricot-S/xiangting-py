// SPDX-FileCopyrightText: 2024 Apricot S.
// SPDX-License-Identifier: MIT
// This file is part of https://github.com/Apricot-S/xiangting-py

use pyo3::prelude::*;

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

impl From<self::FuluMianzi> for ::xiangting::FuluMianzi {
    fn from(value: self::FuluMianzi) -> Self {
        match value {
            self::FuluMianzi::Shunzi(t, p) => ::xiangting::FuluMianzi::Shunzi(t, p.into()),
            self::FuluMianzi::Kezi(t) => ::xiangting::FuluMianzi::Kezi(t),
            self::FuluMianzi::Gangzi(t) => ::xiangting::FuluMianzi::Gangzi(t),
        }
    }
}
