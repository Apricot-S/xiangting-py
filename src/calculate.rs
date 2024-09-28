// SPDX-FileCopyrightText: 2024 Apricot S.
// SPDX-License-Identifier: MIT
// This file is part of https://github.com/Apricot-S/xiangting-py

use crate::fulu_mianzi::FuluMianzi;
use crate::shoupai::InvalidShoupaiError;
use ::xiangting::Bingpai;
use pyo3::prelude::*;

type FuluMianziList = [Option<self::FuluMianzi>; 4];

/// Calculates the replacement number (= xiangting number + 1) for a given hand.
///
/// This function is for 4-player mahjong.
///
/// If the number of melds in the list is less than the required number
/// of melds for the hand, the missing melds are calculated as melds
/// that do not overlap with the tiles in the hand.
/// For example, if the hand consists of 123p1s, three melds are
/// required. If only two melds are provided, such as [444p, 777s], the
/// missing third meld is calculated as a meld that does not overlap
/// with the tiles in the hand, such as 111z.
///
/// Args:
///     bingpai (list[int]): A hand excluding melds
///         (兵牌 a.k.a. pure hand, 純手牌).
///     fulu_mianzi_list (list[FuluMianzi | None] | None):
///         An optional list of melds.
///
/// Returns:
///     int: The replacement number (= xiangting number + 1).
///
/// Raises:
///     ValueError: If an invalid hand (手牌) is provided.
///
/// Examples:
///     >>> # 123m456p789s11222z
///     >>> hand_14 = [
///     ...     1, 1, 1, 0, 0, 0, 0, 0, 0, # m
///     ...     0, 0, 0, 1, 1, 1, 0, 0, 0, # p
///     ...     0, 0, 0, 0, 0, 0, 1, 1, 1, # s
///     ...     2, 3, 0, 0, 0, 0, 0, # z
///     ... ]
///     >>> r = calculate_replacement_number(hand_14, None)
///     >>> print(r)
///     0
///     >>> # 123m1z (3 melds required)
///     >>> hand_4 = [
///     ...     1, 1, 1, 0, 0, 0, 0, 0, 0, # m
///     ...     0, 0, 0, 0, 0, 0, 0, 0, 0, # p
///     ...     0, 0, 0, 0, 0, 0, 0, 0, 0, # s
///     ...     1, 0, 0, 0, 0, 0, 0, # z
///     ... ]
///     >>> # 456p 7777s 111z (3 melds)
///     >>> melds_3 = [
///     ...     FuluMianzi.Shunzi(12, ClaimedTilePosition.LOW),
///     ...     FuluMianzi.Gangzi(24),
///     ...     FuluMianzi.Kezi(27),
///     ...     None,
///     ... ]
///     >>> r_wo_melds = calculate_replacement_number(hand_4, None)
///     >>> print(r_wo_melds)
///     1
///     >>> r_w_melds = calculate_replacement_number(hand_4, melds_3)
///     >>> print(r_w_melds)
///     2
///     >>> # 456p 7777s (2 melds)
///     >>> melds_2 = [
///     ...     FuluMianzi.Shunzi(12, ClaimedTilePosition.LOW),
///     ...     FuluMianzi.Gangzi(24),
///     ...     None,
///     ...     None,
///     ... ]
///     >>> r_w_missing_melds = calculate_replacement_number(hand_4, melds_2)
///     >>> print(r_w_missing_melds)
///     1
///
#[pyfunction]
#[pyo3(signature = (bingpai, fulu_mianzi_list))]
pub(crate) fn calculate_replacement_number(
    bingpai: Bingpai,
    fulu_mianzi_list: Option<self::FuluMianziList>,
) -> PyResult<u8> {
    let f = fulu_mianzi_list.map(|list| list.map(|opt| opt.map(|val| val.into())));

    ::xiangting::calculate_replacement_number(&bingpai, &f)
        .map_err(self::InvalidShoupaiError::from)
        .map_err(PyErr::from)
}

/// Calculates the replacement number (= xiangting number + 1) for a given hand.
///
/// This function is for 3-player mahjong.
/// Tiles from 2m (二萬) to 8m (八萬) cannot be used.
/// Additionally, melded sequences (明順子) cannot be used.
///
/// If the number of melds in the list is less than the required number
/// of melds for the hand, the missing melds are calculated as melds
/// that do not overlap with the tiles in the hand.
/// For example, if the hand consists of 123p1s, three melds are
/// required. If only two melds are provided, such as [444p, 777s], the
/// missing third meld is calculated as a meld that does not overlap
/// with the tiles in the hand, such as 111z.
///
/// Args:
///     bingpai (list[int]): A hand excluding melds.
///         (兵牌 a.k.a. pure hand, 純手牌).
///     fulu_mianzi_list (list[FuluMianzi | None] | None):
///         An optional list of melds.
///
/// Returns:
///     int: The replacement number (= xiangting number + 1).
///
/// Raises:
///     ValueError: If an invalid hand (手牌) is provided.
///
/// Examples:
///     >>> # 111m456p789s11222z
///     >>> hand_14 = [
///     ...     3, 0, 0, 0, 0, 0, 0, 0, 0, # m
///     ...     0, 0, 0, 1, 1, 1, 0, 0, 0, # p
///     ...     0, 0, 0, 0, 0, 0, 1, 1, 1, # s
///     ...     2, 3, 0, 0, 0, 0, 0, # z
///     ... ]
///     >>> r = calculate_replacement_number(hand_14, None)
///     >>> print(r)
///     0
///     >>> # 111m1z (3 melds required)
///     >>> hand_4 = [
///     ...     3, 0, 0, 0, 0, 0, 0, 0, 0, # m
///     ...     0, 0, 0, 0, 0, 0, 0, 0, 0, # p
///     ...     0, 0, 0, 0, 0, 0, 0, 0, 0, # s
///     ...     1, 0, 0, 0, 0, 0, 0, # z
///     ... ]
///     >>> # 444p 7777s 111z (3 melds)
///     >>> melds_3 = [
///     ...     FuluMianzi.Kezi(12),
///     ...     FuluMianzi.Gangzi(24),
///     ...     FuluMianzi.Kezi(27),
///     ...     None,
///     ... ]
///     >>> r_wo_melds = calculate_replacement_number(hand_4, None)
///     >>> print(r_wo_melds)
///     1
///     >>> r_w_melds = calculate_replacement_number(hand_4, melds_3)
///     >>> print(r_w_melds)
///     2
///     >>> # 444p 7777s (2 melds)
///     >>> melds_2 = [
///     ...     FuluMianzi.Kezi(12),
///     ...     FuluMianzi.Gangzi(24),
///     ...     None,
///     ...     None,
///     ... ]
///     >>> r_w_missing_melds = calculate_replacement_number(hand_4, melds_2)
///     >>> print(r_w_missing_melds)
///     1
///
#[pyfunction]
#[pyo3(signature = (bingpai, fulu_mianzi_list))]
pub(crate) fn calculate_replacement_number_3_player(
    bingpai: Bingpai,
    fulu_mianzi_list: Option<self::FuluMianziList>,
) -> PyResult<u8> {
    let f = fulu_mianzi_list.map(|list| list.map(|opt| opt.map(|val| val.into())));

    ::xiangting::calculate_replacement_number_3_player(&bingpai, &f)
        .map_err(self::InvalidShoupaiError::from)
        .map_err(PyErr::from)
}
