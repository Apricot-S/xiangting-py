// SPDX-FileCopyrightText: 2025 Apricot S.
// SPDX-License-Identifier: MIT
// This file is part of https://github.com/Apricot-S/xiangting-py

use pyo3::exceptions::PyValueError;
use pyo3::prelude::*;

pub(crate) struct BingpaiError(::xiangting::BingpaiError);

impl From<self::BingpaiError> for PyErr {
    fn from(err: self::BingpaiError) -> PyErr {
        PyValueError::new_err(err.0.to_string())
    }
}

impl From<::xiangting::BingpaiError> for self::BingpaiError {
    fn from(err: ::xiangting::BingpaiError) -> self::BingpaiError {
        self::BingpaiError(err)
    }
}
