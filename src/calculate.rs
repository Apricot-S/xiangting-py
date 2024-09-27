// SPDX-FileCopyrightText: 2024 Apricot S.
// SPDX-License-Identifier: MIT
// This file is part of https://github.com/Apricot-S/xiangting-py

use crate::fulu_mianzi::FuluMianzi;
use crate::shoupai::InvalidShoupaiError;
use ::xiangting::Bingpai;
use pyo3::prelude::*;

type FuluMianziList = [Option<self::FuluMianzi>; 4];

#[pyfunction]
#[pyo3(signature = (bingpai, fulu_mianzi_list))]
pub(crate) fn calculate_replacement_number(
    bingpai: Bingpai,
    fulu_mianzi_list: Option<self::FuluMianziList>,
) -> PyResult<u8> {
    let f = fulu_mianzi_list.map(|list| list.map(|opt| opt.map(|val| val.into())));

    ::xiangting::calculate_replacement_number(&bingpai, &f)
        .map_err(self::InvalidShoupaiError::from)
        .map_err(PyErr::from)
}

#[pyfunction]
#[pyo3(signature = (bingpai, fulu_mianzi_list))]
pub(crate) fn calculate_replacement_number_3_player(
    bingpai: Bingpai,
    fulu_mianzi_list: Option<self::FuluMianziList>,
) -> PyResult<u8> {
    let f = fulu_mianzi_list.map(|list| list.map(|opt| opt.map(|val| val.into())));

    ::xiangting::calculate_replacement_number_3_player(&bingpai, &f)
        .map_err(self::InvalidShoupaiError::from)
        .map_err(PyErr::from)
}
