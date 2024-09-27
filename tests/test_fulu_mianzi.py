# SPDX-FileCopyrightText: 2024 Apricot S.
# SPDX-License-Identifier: MIT
# This file is part of https://github.com/Apricot-S/xiangting-py

import pytest

from xiangting import ClaimedTilePosition, FuluMianzi


def test_shunzi_display() -> None:
    shunzi_low = FuluMianzi.Shunzi(0, ClaimedTilePosition.LOW)
    assert f"{shunzi_low}" == "Chii-1m-Low"

    shunzi_middle = FuluMianzi.Shunzi(1, ClaimedTilePosition.MIDDLE)
    assert f"{shunzi_middle}" == "Chii-2m-Middle"

    shunzi_high = FuluMianzi.Shunzi(2, ClaimedTilePosition.HIGH)
    assert f"{shunzi_high}" == "Chii-3m-High"


def test_kezi_display() -> None:
    kezi = FuluMianzi.Kezi(0)
    assert f"{kezi}" == "Pon-1m"


def test_gangzi_display() -> None:
    gangzi = FuluMianzi.Gangzi(0)
    assert f"{gangzi}" == "Kan-1m"


def test_invalid_gangzi_display() -> None:
    gangzi = FuluMianzi.Gangzi(34)

    error_msg = "index out of bounds: the len is 34 but the index is 34"
    with pytest.raises(BaseException, match=error_msg):
        f"{gangzi}"
