// SPDX-FileCopyrightText: 2024 Apricot S.
// SPDX-License-Identifier: MIT
// This file is part of https://github.com/Apricot-S/xiangting-py

mod calculate;
mod fulu_mianzi;
mod shoupai;

use crate::calculate::{calculate_replacement_number, calculate_replacement_number_3_player};
use crate::fulu_mianzi::{ClaimedTilePosition, FuluMianzi};
use pyo3::prelude::*;

#[pymodule]
fn xiangting(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<ClaimedTilePosition>()?;
    m.add_class::<FuluMianzi>()?;
    m.add_function(wrap_pyfunction!(calculate_replacement_number, m)?)?;
    m.add_function(wrap_pyfunction!(calculate_replacement_number_3_player, m)?)?;
    Ok(())
}
