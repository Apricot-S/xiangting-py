# xiangting-py

[![PyPI](https://img.shields.io/pypi/v/xiangting.svg)](https://pypi.org/project/xiangting)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/xiangting.svg)](https://pypi.python.org/pypi/xiangting)
[![API](https://img.shields.io/badge/api-main-yellow.svg)](https://apricot-s.github.io/xiangting-py)

Python bindings for [xiangting](https://crates.io/crates/xiangting).

See also [xiangting](https://crates.io/crates/xiangting) for more information.

Documentation:

- [API reference (main branch)](https://apricot-s.github.io/xiangting-py/)

## Installation

There are 2 options to install this library:

### Option 1: Install from PyPI

```sh
pip install xiangting
```

### Option 2: Build from source

Requires `cargo`:

```sh
xiangting-py$ pip install .
```

## Usage

### Basic Usage

The hand is represented as an array of `list[int]`, where each element represents the count of a specific tile.
The correspondence between the index and the tile is shown in the table below.

| Index | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tile  | 1m  | 2m  | 3m  | 4m  | 5m  | 6m  | 7m  | 8m  | 9m  |

| Index | 9   | 10  | 11  | 12  | 13  | 14  | 15  | 16  | 17  |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tile  | 1p  | 2p  | 3p  | 4p  | 5p  | 6p  | 7p  | 8p  | 9p  |

| Index | 18  | 19  | 20  | 21  | 22  | 23  | 24  | 25  | 26  |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tile  | 1s  | 2s  | 3s  | 4s  | 5s  | 6s  | 7s  | 8s  | 9s  |

| Index | 27        | 28         | 29        | 30         | 31         | 32         | 33       |
| ----- | --------- | ---------- | --------- | ---------- | ---------- | ---------- | -------- |
| Tile  | East (1z) | South (2z) | West (3z) | North (4z) | White (5z) | Green (6z) | Red (7z) |

Calculates the replacement number, which is equal to the deficiency number (a.k.a. xiangting number, 向聴数) + 1.

```python
from xiangting import calculate_replacement_number

# 123m456p789s11222z
hand = [
    1, 1, 1, 0, 0, 0, 0, 0, 0, # m
    0, 0, 0, 1, 1, 1, 0, 0, 0, # p
    0, 0, 0, 0, 0, 0, 1, 1, 1, # s
    2, 3, 0, 0, 0, 0, 0, # z
]

replacement_number = calculate_replacement_number(hand, None)
assert replacement_number == 0
```

### Handling Melds

In the calculation for a hand with melds (副露),
the melded tiles can be included or excluded when counting tiles to determine if a hand contains four identical ones.

If melds are excluded (e.g., 天鳳 (Tenhou), 雀魂 (Mahjong Soul)), specify `None` for `fulu_mianzi_list`.

If melds are included (e.g., World Riichi Championship, M.LEAGUE), the melds should be included in the `fulu_mianzi_list`.

```python
from xiangting import (
    ClaimedTilePosition,
    FuluMianzi,
    calculate_replacement_number,
)

# 123m1z
hand = [
    1, 1, 1, 0, 0, 0, 0, 0, 0, # m
    0, 0, 0, 0, 0, 0, 0, 0, 0, # p
    0, 0, 0, 0, 0, 0, 0, 0, 0, # s
    1, 0, 0, 0, 0, 0, 0, # z
]

# 456p 7777s 111z
melds = [
    FuluMianzi.Shunzi(12, ClaimedTilePosition.LOW),
    FuluMianzi.Gangzi(24),
    FuluMianzi.Kezi(27),
]

replacement_number_wo_melds = calculate_replacement_number(hand, None)
assert replacement_number_wo_melds == 1

replacement_number_w_melds = calculate_replacement_number(hand, melds)
assert replacement_number_w_melds == 2
```

### Support for Three-Player Mahjong

In three-player mahjong, the tiles from 2m (二萬) to 8m (八萬) are not used.
In addition, melded sequences (明順子) are not allowed.

```python
from xiangting import (
    calculate_replacement_number,
    calculate_replacement_number_3_player,
)

# 1111m111122233z
hand = [
    4, 0, 0, 0, 0, 0, 0, 0, 0, # m
    0, 0, 0, 0, 0, 0, 0, 0, 0, # p
    0, 0, 0, 0, 0, 0, 0, 0, 0, # s
    4, 3, 2, 0, 0, 0, 0, # z
]

replacement_number_4p = calculate_replacement_number(hand, None)
assert replacement_number_4p == 2

replacement_number_3p = calculate_replacement_number_3_player(hand, None)
assert replacement_number_3p == 3
```

## License

Copyright (c) Apricot S. All rights reserved.

Licensed under the [MIT license](LICENSE).
