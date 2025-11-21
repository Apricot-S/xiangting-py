# SPDX-FileCopyrightText: 2024 Apricot S.
# SPDX-License-Identifier: MIT
# This file is part of https://github.com/Apricot-S/xiangting-py

from mahjong.tile import TilesConverter

from xiangting import PlayerCount, calculate_replacement_number


def test_calculate_replacement_number_standard_tenpai() -> None:
    bingpai = TilesConverter.one_line_string_to_34_array("123m456p789s1122z")
    assert calculate_replacement_number(bingpai, PlayerCount.FOUR) == 1


def test_calculate_replacement_number_qiduizi_tenpai() -> None:
    bingpai = TilesConverter.one_line_string_to_34_array("1188m288p55s1177z")
    assert calculate_replacement_number(bingpai, PlayerCount.FOUR) == 1


def test_calculate_replacement_number_shisanyao_tenpai() -> None:
    bingpai = TilesConverter.one_line_string_to_34_array("19m19p19s1234567z")
    assert calculate_replacement_number(bingpai, PlayerCount.FOUR) == 1


# Source: https://zenn.dev/tomohxx/articles/aecace4e3a3bc1


def test_calculate_replacement_number_lack_isolated_tile_13_4333() -> None:
    bingpai = TilesConverter.one_line_string_to_34_array("1111222333444z")
    assert calculate_replacement_number(bingpai, PlayerCount.FOUR) == 2


def test_calculate_replacement_number_lack_isolated_tile_13_4432i() -> None:
    bingpai = TilesConverter.one_line_string_to_34_array("11m11112222333z")
    assert calculate_replacement_number(bingpai, PlayerCount.FOUR) == 3


def test_calculate_replacement_number_lack_isolated_tile_13_4432ii() -> None:
    bingpai = TilesConverter.one_line_string_to_34_array("23m11112222333z")
    assert calculate_replacement_number(bingpai, PlayerCount.FOUR) == 3


def test_calculate_replacement_number_lack_isolated_tile_13_4441() -> None:
    bingpai = TilesConverter.one_line_string_to_34_array("1111222233334z")
    assert calculate_replacement_number(bingpai, PlayerCount.FOUR) == 4


def test_calculate_replacement_number_lack_isolated_tile_14_4433() -> None:
    bingpai = TilesConverter.one_line_string_to_34_array("11112222333444z")
    assert calculate_replacement_number(bingpai, PlayerCount.FOUR) == 2


def test_calculate_replacement_number_lack_isolated_tile_14_4442i() -> None:
    bingpai = TilesConverter.one_line_string_to_34_array("11m111122223333z")
    assert calculate_replacement_number(bingpai, PlayerCount.FOUR) == 3


def test_calculate_replacement_number_lack_isolated_tile_14_4442ii() -> None:
    bingpai = TilesConverter.one_line_string_to_34_array("23m111122223333z")
    assert calculate_replacement_number(bingpai, PlayerCount.FOUR) == 3


def test_calculate_replacement_number_3_player_standard_tenpai() -> None:
    bingpai = TilesConverter.one_line_string_to_34_array("111m456p789s1122z")
    assert calculate_replacement_number(bingpai, PlayerCount.THREE) == 1


def test_calculate_replacement_number_3_player_qiduizi_tenpai() -> None:
    bingpai = TilesConverter.one_line_string_to_34_array("1199m288p55s1177z")
    assert calculate_replacement_number(bingpai, PlayerCount.THREE) == 1


def test_calculate_replacement_number_3_player_shisanyao_tenpai() -> None:
    bingpai = TilesConverter.one_line_string_to_34_array("19m19p19s1234567z")
    assert calculate_replacement_number(bingpai, PlayerCount.THREE) == 1
