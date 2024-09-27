// SPDX-FileCopyrightText: 2024 Apricot S.
// SPDX-License-Identifier: MIT
// This file is part of https://github.com/Apricot-S/xiangting-py

use pyo3::exceptions::PyValueError;
use pyo3::prelude::*;

pub(crate) struct InvalidShoupaiError(::xiangting::InvalidShoupaiError);

impl From<self::InvalidShoupaiError> for PyErr {
    fn from(err: self::InvalidShoupaiError) -> PyErr {
        PyValueError::new_err(err.0.to_string())
    }
}

impl From<::xiangting::InvalidShoupaiError> for self::InvalidShoupaiError {
    fn from(err: ::xiangting::InvalidShoupaiError) -> self::InvalidShoupaiError {
        self::InvalidShoupaiError(err)
    }
}
