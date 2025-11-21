# SPDX-FileCopyrightText: 2024 Apricot S.
# SPDX-License-Identifier: MIT
# This file is part of https://github.com/Apricot-S/xiangting-py

import pytest
from mahjong.tile import TilesConverter

from xiangting import PlayerCount, calculate_replacement_number


def test_calculate_replacement_number_bingpai_empty() -> None:
    bingpai = TilesConverter.one_line_string_to_34_array("")

    with pytest.raises(ValueError):  # noqa: PT011
        calculate_replacement_number(bingpai, PlayerCount.FOUR)


def test_calculate_replacement_number_bingpai_len_35() -> None:
    bingpai = [0] * 35
    bingpai[0] = 1

    with pytest.raises(ValueError):  # noqa: PT011
        calculate_replacement_number(bingpai, PlayerCount.FOUR)


def test_calculate_replacement_number_bingpai_3_tiles() -> None:
    bingpai = TilesConverter.one_line_string_to_34_array("2p3s7z")

    with pytest.raises(ValueError):  # noqa: PT011
        calculate_replacement_number(bingpai, PlayerCount.FOUR)


def test_calculate_replacement_number_bingpai_15_tiles() -> None:
    bingpai = TilesConverter.one_line_string_to_34_array("111222333444555m")

    with pytest.raises(ValueError):  # noqa: PT011
        calculate_replacement_number(bingpai, PlayerCount.FOUR)


def test_calculate_replacement_number_bingpai_5_same_tiles() -> None:
    bingpai = TilesConverter.one_line_string_to_34_array("")
    bingpai[0] = 5

    with pytest.raises(ValueError):  # noqa: PT011
        calculate_replacement_number(bingpai, PlayerCount.FOUR)


def test_calculate_replacement_number_3_player_bingpai_8m() -> None:
    bingpai = TilesConverter.one_line_string_to_34_array("8m")

    with pytest.raises(ValueError):  # noqa: PT011
        calculate_replacement_number(bingpai, PlayerCount.THREE)
