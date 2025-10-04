// SPDX-FileCopyrightText: 2024 Apricot S.
// SPDX-License-Identifier: MIT
// This file is part of https://github.com/Apricot-S/xiangting-py

use crate::fulu_mianzi::FuluMianzi;
use crate::shoupai::XiangtingError;
use ::xiangting::Bingpai;
use pyo3::prelude::*;
use pyo3::types::PySequence;

/// Calculates the replacement number (= xiangting number + 1) for a given hand.
///
/// This function is for 4-player mahjong.
///
/// In some rulesets, melded tiles are excluded when checking whether
/// a hand contains four identical tiles. In others, melded tiles are
/// included in the calculation. This function allows you to control
/// that behavior via the ``fulu_mianzi_list`` argument:
///
/// - Use ``None`` if melds are excluded in the ruleset
///   (e.g., Tenhou, Mahjong Soul).
/// - Provide ``Sequence[FuluMianzi]`` if melds are included
///   (e.g., World Riichi Championship, M.LEAGUE).
///
/// If fewer melds are provided than required for a complete hand,
/// the missing ones are treated as melds that do not overlap with
/// the tiles in the hand.
/// For example, with the hand 123p1s, three melds are required.
/// If only two are given (e.g., [444p, 777s]), the third is considered
/// to be a non-overlapping meld, such as 111z.
///
/// Args:
///     bingpai (list[int]): A hand excluding melds
///         (兵牌 a.k.a. pure hand, 純手牌).
///     fulu_mianzi_list (Sequence[FuluMianzi] | None):
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
///     >>> hand = [
///     ...     1, 1, 1, 0, 0, 0, 0, 0, 0, # m
///     ...     0, 0, 0, 1, 1, 1, 0, 0, 0, # p
///     ...     0, 0, 0, 0, 0, 0, 1, 1, 1, # s
///     ...     2, 3, 0, 0, 0, 0, 0, # z
///     ... ]
///     >>> r = calculate_replacement_number(hand, None)
///     >>> print(r)
///     0
///     >>> # 123m1z
///     >>> hand = [
///     ...     1, 1, 1, 0, 0, 0, 0, 0, 0, # m
///     ...     0, 0, 0, 0, 0, 0, 0, 0, 0, # p
///     ...     0, 0, 0, 0, 0, 0, 0, 0, 0, # s
///     ...     1, 0, 0, 0, 0, 0, 0, # z
///     ... ]
///     >>> # 456p 7777s 111z
///     >>> melds_3 = [
///     ...     FuluMianzi.Shunzi(12, ClaimedTilePosition.LOW),
///     ...     FuluMianzi.Gangzi(24),
///     ...     FuluMianzi.Kezi(27),
///     ... ]
///     >>> r_wo_melds = calculate_replacement_number(hand, None)
///     >>> print(r_wo_melds)
///     1
///     >>> r_w_melds = calculate_replacement_number(hand, melds_3)
///     >>> print(r_w_melds)
///     2
///     >>> # 456p 7777s
///     >>> melds_2 = [
///     ...     FuluMianzi.Shunzi(12, ClaimedTilePosition.LOW),
///     ...     FuluMianzi.Gangzi(24),
///     ... ]
///     >>> r_w_missing_melds = calculate_replacement_number(hand, melds_2)
///     >>> print(r_w_missing_melds)
///     1
///
#[pyfunction]
#[pyo3(signature = (bingpai, fulu_mianzi_list))]
pub(crate) fn calculate_replacement_number(
    bingpai: Bingpai,
    fulu_mianzi_list: Option<Bound<'_, PySequence>>,
) -> PyResult<u8> {
    let fl: Option<Vec<::xiangting::FuluMianzi>> = fulu_mianzi_list
        .map(|s| s.extract::<Vec<self::FuluMianzi>>())
        .transpose()?
        .map(|v| v.into_iter().map(Into::into).collect());

    ::xiangting::calculate_replacement_number(&bingpai, fl.as_deref())
        .map_err(self::XiangtingError::from)
        .map_err(PyErr::from)
}

/// Calculates the replacement number (= xiangting number + 1) for a given hand.
///
/// This function is for 3-player mahjong.
///
/// Tiles from 2m (二萬) to 8m (八萬) are not used.
/// In addition, melded sequences (明順子) are not allowed.
///
/// In some rulesets, melded tiles are excluded when checking whether
/// a hand contains four identical tiles. In others, melded tiles are
/// included in the calculation. This function allows you to control
/// that behavior via the ``fulu_mianzi_list`` argument:
///
/// - Use ``None`` if melds are excluded in the ruleset
///   (e.g., Tenhou, Mahjong Soul).
/// - Provide ``Sequence[FuluMianzi]`` if melds are included
///   (e.g., World Riichi Championship, M.LEAGUE).
///
/// If fewer melds are provided than required for a complete hand,
/// the missing ones are treated as melds that do not overlap with
/// the tiles in the hand.
/// For example, with the hand 123p1s, three melds are required.
/// If only two are given (e.g., [444p, 777s]), the third is considered
/// to be a non-overlapping meld, such as 111z.
///
/// Args:
///     bingpai (list[int]): A hand excluding melds.
///         (兵牌 a.k.a. pure hand, 純手牌).
///     fulu_mianzi_list (Sequence[FuluMianzi] | None):
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
///     >>> hand = [
///     ...     3, 0, 0, 0, 0, 0, 0, 0, 0, # m
///     ...     0, 0, 0, 1, 1, 1, 0, 0, 0, # p
///     ...     0, 0, 0, 0, 0, 0, 1, 1, 1, # s
///     ...     2, 3, 0, 0, 0, 0, 0, # z
///     ... ]
///     >>> r = calculate_replacement_number(hand, None)
///     >>> print(r)
///     0
///     >>> # 111m1z
///     >>> hand = [
///     ...     3, 0, 0, 0, 0, 0, 0, 0, 0, # m
///     ...     0, 0, 0, 0, 0, 0, 0, 0, 0, # p
///     ...     0, 0, 0, 0, 0, 0, 0, 0, 0, # s
///     ...     1, 0, 0, 0, 0, 0, 0, # z
///     ... ]
///     >>> # 444p 7777s 111z
///     >>> melds_3 = [
///     ...     FuluMianzi.Kezi(12),
///     ...     FuluMianzi.Gangzi(24),
///     ...     FuluMianzi.Kezi(27),
///     ... ]
///     >>> r_wo_melds = calculate_replacement_number(hand, None)
///     >>> print(r_wo_melds)
///     1
///     >>> r_w_melds = calculate_replacement_number(hand, melds_3)
///     >>> print(r_w_melds)
///     2
///     >>> # 444p 7777s
///     >>> melds_2 = [
///     ...     FuluMianzi.Kezi(12),
///     ...     FuluMianzi.Gangzi(24),
///     ... ]
///     >>> r_w_missing_melds = calculate_replacement_number(hand, melds_2)
///     >>> print(r_w_missing_melds)
///     1
///
#[pyfunction]
#[pyo3(signature = (bingpai, fulu_mianzi_list))]
pub(crate) fn calculate_replacement_number_3_player(
    bingpai: Bingpai,
    fulu_mianzi_list: Option<Bound<'_, PySequence>>,
) -> PyResult<u8> {
    let fl: Option<Vec<::xiangting::FuluMianzi>> = fulu_mianzi_list
        .map(|s| s.extract::<Vec<self::FuluMianzi>>())
        .transpose()?
        .map(|v| v.into_iter().map(Into::into).collect());

    ::xiangting::calculate_replacement_number_3_player(&bingpai, fl.as_deref())
        .map_err(self::XiangtingError::from)
        .map_err(PyErr::from)
}
