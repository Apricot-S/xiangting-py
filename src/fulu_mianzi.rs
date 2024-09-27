// SPDX-FileCopyrightText: 2024 Apricot S.
// SPDX-License-Identifier: MIT
// This file is part of https://github.com/Apricot-S/xiangting-py

use pyo3::prelude::*;
use std::fmt;

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
