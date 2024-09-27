# SPDX-FileCopyrightText: 2024 Apricot S.
# SPDX-License-Identifier: MIT
# This file is part of https://github.com/Apricot-S/xiangting-py

import re

import pytest

from xiangting import (
    ClaimedTilePosition,
    FuluMianzi,
    calculate_replacement_number,
    calculate_replacement_number_3_player,
)


def test_calculate_replacement_number_standard_tenpai() -> None:
    bingpai = [
        1, 1, 1, 0, 0, 0, 0, 0, 0, # m
        0, 0, 0, 1, 1, 1, 0, 0, 0, # p
        0, 0, 0, 0, 0, 0, 1, 1, 1, # s
        2, 2, 0, 0, 0, 0, 0, # z
    ]  # fmt: skip
    replacement_number = calculate_replacement_number(bingpai, None)
    assert replacement_number == 1


def test_calculate_replacement_number_shisanyao_tenpai() -> None:
    bingpai = [
        1, 0, 0, 0, 0, 0, 0, 0, 1, # m
        1, 0, 0, 0, 0, 0, 0, 0, 1, # p
        1, 0, 0, 0, 0, 0, 0, 0, 1, # s
        1, 1, 1, 1, 1, 1, 1, # z
    ]  # fmt: skip
    replacement_number = calculate_replacement_number(bingpai, None)
    assert replacement_number == 1


def test_calculate_replacement_number_qiduizi_tenpai() -> None:
    bingpai = [
        2, 0, 0, 0, 0, 0, 0, 2, 0, # m
        0, 1, 0, 0, 0, 0, 0, 2, 0, # p
        0, 0, 0, 0, 2, 0, 0, 0, 0, # s
        2, 0, 0, 0, 0, 0, 2, # z
    ]  # fmt: skip
    replacement_number = calculate_replacement_number(bingpai, None)
    assert replacement_number == 1


def test_calculate_replacement_number_with_meld() -> None:
    bingpai = [
        1, 1, 1, 0, 0, 0, 0, 0, 0, # m
        0, 0, 0, 1, 1, 1, 0, 0, 0, # p
        0, 0, 0, 0, 0, 0, 0, 0, 0, # s
        0, 1, 0, 0, 0, 0, 0, # z
    ]  # fmt: skip
    replacement_number_1 = calculate_replacement_number(bingpai, None)
    assert replacement_number_1 == 1

    fulu_mianzi_list = [
        FuluMianzi.Kezi(27),
        FuluMianzi.Shunzi(24, ClaimedTilePosition.LOW),
        None,
        None,
    ]
    replacement_number_2 = calculate_replacement_number(
        bingpai,
        fulu_mianzi_list,
    )
    assert replacement_number_2 == 1


def test_calculate_replacement_number_empty_bingpai() -> None:
    bingpai = [
        0, 0, 0, 0, 0, 0, 0, 0, 0, # m
        0, 0, 0, 0, 0, 0, 0, 0, 0, # p
        0, 0, 0, 0, 0, 0, 0, 0, 0, # s
        0, 0, 0, 0, 0, 0, 0, # z
    ]  # fmt: skip

    error_msg = "hand is empty"
    with pytest.raises(ValueError, match=error_msg):
        calculate_replacement_number(bingpai, None)


def test_calculate_replacement_number_invalid_meld() -> None:
    bingpai = [
        1, 1, 1, 0, 0, 0, 0, 0, 0, # m
        0, 0, 0, 1, 1, 1, 0, 0, 0, # p
        0, 0, 0, 0, 0, 0, 0, 0, 0, # s
        0, 1, 0, 0, 0, 0, 0, # z
    ]  # fmt: skip

    fulu_mianzi_list: list[FuluMianzi | None] = [
        FuluMianzi.Kezi(34),
        None,
        None,
        None,
    ]

    inner_error_msg = "tile index must be between 0 and 33 but was 34"
    error_msg = f"hand contains an invalid meld ({inner_error_msg})"
    with pytest.raises(ValueError, match=re.escape(error_msg)):
        calculate_replacement_number(bingpai, fulu_mianzi_list)


def test_calculate_replacement_number_3_player_standard_tenpai() -> None:
    bingpai = [
        3, 0, 0, 0, 0, 0, 0, 0, 0, # m
        0, 0, 0, 1, 1, 1, 0, 0, 0, # p
        0, 0, 0, 0, 0, 0, 1, 1, 1, # s
        2, 2, 0, 0, 0, 0, 0, # z
    ]  # fmt: skip
    replacement_number = calculate_replacement_number_3_player(bingpai, None)
    assert replacement_number == 1


def test_calculate_replacement_number_3_player_shisanyao_tenpai() -> None:
    bingpai = [
        1, 0, 0, 0, 0, 0, 0, 0, 1, # m
        1, 0, 0, 0, 0, 0, 0, 0, 1, # p
        1, 0, 0, 0, 0, 0, 0, 0, 1, # s
        1, 1, 1, 1, 1, 1, 1, # z
    ]  # fmt: skip
    replacement_number = calculate_replacement_number_3_player(bingpai, None)
    assert replacement_number == 1


def test_calculate_replacement_number_3_player_qiduizi_tenpai() -> None:
    bingpai = [
        2, 0, 0, 0, 0, 0, 0, 0, 2, # m
        0, 1, 0, 0, 0, 0, 0, 2, 0, # p
        0, 0, 0, 0, 2, 0, 0, 0, 0, # s
        2, 0, 0, 0, 0, 0, 2, # z
    ]  # fmt: skip
    replacement_number = calculate_replacement_number_3_player(bingpai, None)
    assert replacement_number == 1


def test_calculate_replacement_number_3_player_with_meld() -> None:
    bingpai = [
        3, 0, 0, 0, 0, 0, 0, 0, 0, # m
        0, 0, 0, 1, 1, 1, 0, 0, 0, # p
        0, 0, 0, 0, 0, 0, 1, 1, 1, # s
        0, 1, 0, 0, 0, 0, 0, # z
    ]  # fmt: skip
    replacement_number_1 = calculate_replacement_number_3_player(bingpai, None)
    assert replacement_number_1 == 1

    fulu_mianzi_list: list[FuluMianzi | None] = [
        FuluMianzi.Kezi(27),
        None,
        None,
        None,
    ]
    replacement_number_2 = calculate_replacement_number_3_player(
        bingpai,
        fulu_mianzi_list,
    )
    assert replacement_number_2 == 1


def test_calculate_replacement_number_3_player_empty_bingpai() -> None:
    bingpai = [
        0, 0, 0, 0, 0, 0, 0, 0, 0, # m
        0, 0, 0, 0, 0, 0, 0, 0, 0, # p
        0, 0, 0, 0, 0, 0, 0, 0, 0, # s
        0, 0, 0, 0, 0, 0, 0, # z
    ]  # fmt: skip

    error_msg = "hand is empty"
    with pytest.raises(ValueError, match=error_msg):
        calculate_replacement_number_3_player(bingpai, None)


def test_calculate_replacement_number_3_player_invalid_meld() -> None:
    bingpai = [
        3, 0, 0, 0, 0, 0, 0, 0, 0, # m
        0, 0, 0, 1, 1, 1, 0, 0, 0, # p
        0, 0, 0, 0, 0, 0, 0, 0, 0, # s
        0, 1, 0, 0, 0, 0, 0, # z
    ]  # fmt: skip

    fulu_mianzi_list: list[FuluMianzi | None] = [
        FuluMianzi.Kezi(1),
        None,
        None,
        None,
    ]

    error_msg = "Pon-2m cannot be used in 3-player mahjong"
    with pytest.raises(ValueError, match=error_msg):
        calculate_replacement_number_3_player(bingpai, fulu_mianzi_list)
