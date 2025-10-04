# SPDX-FileCopyrightText: 2024 Apricot S.
# SPDX-License-Identifier: MIT
# This file is part of https://github.com/Apricot-S/xiangting-py

import pytest
from mahjong.tile import TilesConverter

from xiangting import (
    ClaimedTilePosition,
    FuluMianzi,
    calculate_replacement_number,
    calculate_replacement_number_3_player,
)


def test_calculate_replacement_number_bingpai_empty() -> None:
    bingpai = TilesConverter.one_line_string_to_34_array("")

    with pytest.raises(ValueError):  # noqa: PT011
        calculate_replacement_number(bingpai, None)


def test_calculate_replacement_number_bingpai_len_35() -> None:
    bingpai = [0] * 35
    bingpai[0] = 1

    with pytest.raises(ValueError):  # noqa: PT011
        calculate_replacement_number(bingpai, None)


def test_calculate_replacement_number_bingpai_3_tiles() -> None:
    bingpai = TilesConverter.one_line_string_to_34_array("2p3s7z")

    with pytest.raises(ValueError):  # noqa: PT011
        calculate_replacement_number(bingpai, None)


def test_calculate_replacement_number_bingpai_15_tiles() -> None:
    bingpai = TilesConverter.one_line_string_to_34_array("111222333444555m")

    with pytest.raises(ValueError):  # noqa: PT011
        calculate_replacement_number(bingpai, None)


def test_calculate_replacement_number_bingpai_5_same_tiles() -> None:
    bingpai = TilesConverter.one_line_string_to_34_array("")
    bingpai[0] = 5

    with pytest.raises(ValueError):  # noqa: PT011
        calculate_replacement_number(bingpai, None)


def test_calculate_replacement_number_fulu_index_out_of_range() -> None:
    bingpai = TilesConverter.one_line_string_to_34_array("1m")
    fulu_mianzi_list = [FuluMianzi.Kezi(34)]

    with pytest.raises(ValueError):  # noqa: PT011
        calculate_replacement_number(bingpai, fulu_mianzi_list)


def test_calculate_replacement_number_fulu_shunzi_with_zipai() -> None:
    bingpai = TilesConverter.one_line_string_to_34_array("1p")
    fulu_mianzi_list = [FuluMianzi.Shunzi(27, ClaimedTilePosition.LOW)]

    with pytest.raises(ValueError):  # noqa: PT011
        calculate_replacement_number(bingpai, fulu_mianzi_list)


def test_calculate_replacement_number_fulu_invalid_shunzi_combination() -> (
    None
):
    bingpai = TilesConverter.one_line_string_to_34_array("1p")
    fulu_mianzi_list = [FuluMianzi.Shunzi(0, ClaimedTilePosition.MIDDLE)]

    with pytest.raises(ValueError):  # noqa: PT011
        calculate_replacement_number(bingpai, fulu_mianzi_list)


def test_calculate_replacement_number_shoupai_too_many_fulu_mianzi() -> None:
    bingpai = TilesConverter.one_line_string_to_34_array("11122233344455m")
    fulu_mianzi_list = [FuluMianzi.Kezi(5)]

    with pytest.raises(ValueError):  # noqa: PT011
        calculate_replacement_number(bingpai, fulu_mianzi_list)


def test_calculate_replacement_number_shoupai_5_same_tiles() -> None:
    bingpai = TilesConverter.one_line_string_to_34_array("1m")
    fulu_mianzi_list = [FuluMianzi.Gangzi(0)]

    with pytest.raises(ValueError):  # noqa: PT011
        calculate_replacement_number(bingpai, fulu_mianzi_list)


def test_calculate_replacement_number_3_player_bingpai_8m() -> None:
    bingpai = TilesConverter.one_line_string_to_34_array("8m")

    with pytest.raises(ValueError):  # noqa: PT011
        calculate_replacement_number_3_player(bingpai, None)


def test_calculate_replacement_number_3_player_fulu_123p() -> None:
    bingpai = TilesConverter.one_line_string_to_34_array("1m")

    fulu_mianzi_list = [FuluMianzi.Shunzi(9, ClaimedTilePosition.LOW)]

    with pytest.raises(ValueError):  # noqa: PT011
        calculate_replacement_number_3_player(bingpai, fulu_mianzi_list)


def test_calculate_replacement_number_3_player_fulu_222m() -> None:
    bingpai = TilesConverter.one_line_string_to_34_array("1m")

    fulu_mianzi_list = [FuluMianzi.Kezi(1)]

    with pytest.raises(ValueError):  # noqa: PT011
        calculate_replacement_number_3_player(bingpai, fulu_mianzi_list)
