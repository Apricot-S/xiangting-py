# SPDX-FileCopyrightText: 2024 Apricot S.
# SPDX-License-Identifier: MIT
# This file is part of https://github.com/Apricot-S/xiangting-py

import pytest

from xiangting import to_array


def test_to_array_empty() -> None:
    flags = 0b0000000_000000000_000000000_000000000
    assert to_array(flags) == [False] * 34


def test_to_array_all() -> None:
    flags = 0b1111111_111111111_111111111_111111111
    assert to_array(flags) == [True] * 34


def test_to_array_1m456p789s12z() -> None:
    flags = 0b0000011_111000000_000111000_000000001
    arr = [
        True, False, False, False, False, False, False, False, False, # m
        False, False, False, True, True, True, False, False, False, # p
        False, False, False, False, False, False, True, True, True, # s
        True, True, False, False, False, False, False, # z
    ]  # fmt: skip
    assert to_array(flags) == arr


def test_to_array_err_64bit() -> None:
    flags = (1 << 64) - 1
    assert to_array(flags) == [True] * 34


def test_to_array_err_65bit() -> None:
    flags = 1 << 64
    with pytest.raises(OverflowError):
        to_array(flags)
