# SPDX-FileCopyrightText: 2024 Apricot S.
# SPDX-License-Identifier: MIT
# This file is part of https://github.com/Apricot-S/xiangting-py

from typing import Final

from pytest_benchmark.fixture import BenchmarkFixture

from xiangting import calculate_replacement_number

from . import random_hand

NUM_ROUND: Final = 10_000
NUM_WARMUP_ROUND: Final = 100_000
NUM_HAND: Final = NUM_ROUND + NUM_WARMUP_ROUND


def test_xiangting_normal(benchmark: BenchmarkFixture) -> None:
    rng = random_hand.create_rng()
    hands = [
        random_hand.generate_random_pure_hand(rng) for _ in range(NUM_HAND)
    ]
    hand_iter = iter(hands)

    def setup() -> tuple[tuple[list[int], None], dict]:
        return (next(hand_iter), None), {}

    benchmark.pedantic(
        calculate_replacement_number,
        setup=setup,
        rounds=NUM_ROUND,
        warmup_rounds=NUM_WARMUP_ROUND,
    )


def test_xiangting_half_flush(benchmark: BenchmarkFixture) -> None:
    rng = random_hand.create_rng()
    hands = [
        random_hand.generate_random_half_flush_pure_hand(rng)
        for _ in range(NUM_HAND)
    ]
    hand_iter = iter(hands)

    def setup() -> tuple[tuple[list[int], None], dict]:
        return (next(hand_iter), None), {}

    benchmark.pedantic(
        calculate_replacement_number,
        setup=setup,
        rounds=NUM_ROUND,
        warmup_rounds=NUM_WARMUP_ROUND,
    )


def test_xiangting_full_flush(benchmark: BenchmarkFixture) -> None:
    rng = random_hand.create_rng()
    hands = [
        random_hand.generate_random_full_flush_pure_hand(rng)
        for _ in range(NUM_HAND)
    ]
    hand_iter = iter(hands)

    def setup() -> tuple[tuple[list[int], None], dict]:
        return (next(hand_iter), None), {}

    benchmark.pedantic(
        calculate_replacement_number,
        setup=setup,
        rounds=NUM_ROUND,
        warmup_rounds=NUM_WARMUP_ROUND,
    )


def test_xiangting_non_simple(benchmark: BenchmarkFixture) -> None:
    rng = random_hand.create_rng()
    hands = [
        random_hand.generate_random_non_simple_pure_hand(rng)
        for _ in range(NUM_HAND)
    ]
    hand_iter = iter(hands)

    def setup() -> tuple[tuple[list[int], None], dict]:
        return (next(hand_iter), None), {}

    benchmark.pedantic(
        calculate_replacement_number,
        setup=setup,
        rounds=NUM_ROUND,
        warmup_rounds=NUM_WARMUP_ROUND,
    )
