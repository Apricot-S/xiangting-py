# SPDX-FileCopyrightText: 2024 Apricot S.
# SPDX-License-Identifier: MIT
# This file is part of https://github.com/Apricot-S/xiangting-py

from typing import Final

from kago_utils.hai_group import HaiGroup
from kago_utils.shanten import calculate_shanten
from pytest_benchmark.fixture import BenchmarkFixture

from . import random_hand

NUM_ROUND: Final = 10_000
NUM_WARMUP_ROUND: Final = 100_000
NUM_HAND: Final = NUM_ROUND + NUM_WARMUP_ROUND


def test_kago_normal(benchmark: BenchmarkFixture) -> None:
    rng = random_hand.create_rng()
    hands = [
        HaiGroup.from_counter34(random_hand.generate_random_pure_hand(rng))
        for _ in range(NUM_HAND)
    ]
    hand_iter = iter(hands)

    def setup() -> tuple[tuple[HaiGroup], dict]:
        return (next(hand_iter),), {}

    benchmark.pedantic(
        calculate_shanten,
        setup=setup,
        rounds=NUM_ROUND,
        warmup_rounds=NUM_WARMUP_ROUND,
    )


def test_kago_half_flush(benchmark: BenchmarkFixture) -> None:
    rng = random_hand.create_rng()
    hands = [
        HaiGroup.from_counter34(
            random_hand.generate_random_half_flush_pure_hand(rng),
        )
        for _ in range(NUM_HAND)
    ]
    hand_iter = iter(hands)

    def setup() -> tuple[tuple[HaiGroup], dict]:
        return (next(hand_iter),), {}

    benchmark.pedantic(
        calculate_shanten,
        setup=setup,
        rounds=NUM_ROUND,
        warmup_rounds=NUM_WARMUP_ROUND,
    )


def test_kago_full_flush(benchmark: BenchmarkFixture) -> None:
    rng = random_hand.create_rng()
    hands = [
        HaiGroup.from_counter34(
            random_hand.generate_random_full_flush_pure_hand(rng),
        )
        for _ in range(NUM_HAND)
    ]
    hand_iter = iter(hands)

    def setup() -> tuple[tuple[HaiGroup], dict]:
        return (next(hand_iter),), {}

    benchmark.pedantic(
        calculate_shanten,
        setup=setup,
        rounds=NUM_ROUND,
        warmup_rounds=NUM_WARMUP_ROUND,
    )


def test_kago_non_simple(benchmark: BenchmarkFixture) -> None:
    rng = random_hand.create_rng()
    hands = [
        HaiGroup.from_counter34(
            random_hand.generate_random_non_simple_pure_hand(rng),
        )
        for _ in range(NUM_HAND)
    ]
    hand_iter = iter(hands)

    def setup() -> tuple[tuple[HaiGroup], dict]:
        return (next(hand_iter),), {}

    benchmark.pedantic(
        calculate_shanten,
        setup=setup,
        rounds=NUM_ROUND,
        warmup_rounds=NUM_WARMUP_ROUND,
    )
