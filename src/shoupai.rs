// SPDX-FileCopyrightText: 2024 Apricot S.
// SPDX-License-Identifier: MIT
// This file is part of https://github.com/Apricot-S/xiangting-py

use pyo3::exceptions::PyValueError;
use pyo3::prelude::*;

pub(crate) struct XiangtingError(::xiangting::XiangtingError);

impl From<self::XiangtingError> for PyErr {
    fn from(err: self::XiangtingError) -> PyErr {
        PyValueError::new_err(err.0.to_string())
    }
}

impl From<::xiangting::XiangtingError> for self::XiangtingError {
    fn from(err: ::xiangting::XiangtingError) -> self::XiangtingError {
        self::XiangtingError(err)
    }
}
