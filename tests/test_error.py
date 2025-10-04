# SPDX-FileCopyrightText: 2024 Apricot S.
# SPDX-License-Identifier: MIT
# This file is part of https://github.com/Apricot-S/xiangting-py

import pytest
from mahjong.tile import TilesConverter

from xiangting import (
    FuluMianzi,
    calculate_replacement_number,
    calculate_replacement_number_3_player,
)


def test_calculate_replacement_number_empty_bingpai() -> None:
    bingpai = TilesConverter.one_line_string_to_34_array("")

    with pytest.raises(ValueError):  # noqa: PT011
        calculate_replacement_number(bingpai, None)


def test_calculate_replacement_number_invalid_meld() -> None:
    bingpai = TilesConverter.one_line_string_to_34_array("123m456p2z")

    fulu_mianzi_list = [FuluMianzi.Kezi(34)]

    with pytest.raises(ValueError):  # noqa: PT011
        calculate_replacement_number(bingpai, fulu_mianzi_list)


def test_calculate_replacement_number_3_player_empty_bingpai() -> None:
    bingpai = TilesConverter.one_line_string_to_34_array("")

    with pytest.raises(ValueError):  # noqa: PT011
        calculate_replacement_number_3_player(bingpai, None)


def test_calculate_replacement_number_3_player_invalid_meld() -> None:
    bingpai = TilesConverter.one_line_string_to_34_array("111m456p2z")

    fulu_mianzi_list = [FuluMianzi.Kezi(1)]

    with pytest.raises(ValueError):  # noqa: PT011
        calculate_replacement_number_3_player(bingpai, fulu_mianzi_list)
