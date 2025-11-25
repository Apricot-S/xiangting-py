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

Calculates the replacement number, which is equal to the deficiency number (a.k.a. xiàngtīng number, 向聴数) + 1.

```python
from xiangting import PlayerCount, calculate_replacement_number

# 123m456p789s11222z
hand = [
    1, 1, 1, 0, 0, 0, 0, 0, 0, # m
    0, 0, 0, 1, 1, 1, 0, 0, 0, # p
    0, 0, 0, 0, 0, 0, 1, 1, 1, # s
    2, 3, 0, 0, 0, 0, 0, # z
]

replacement_number = calculate_replacement_number(hand, PlayerCount.FOUR)
assert replacement_number == 0
```

### Necessary and Unnecessary Tiles

It is also possible to calculate necessary or unnecessary tiles together with the replacement number.

- Necessary tiles
  - Tiles needed to win with the minimum number of replacements
  - Tiles that reduce the replacement number when drawn
  - In Japanese, these are referred to as *有効牌 (yūkōhai)* or *受け入れ (ukeire)*

- Unnecessary tiles
  - Tiles not needed to win with the minimum number of replacements
  - Tiles that can be discarded without changing the replacement number
  - In Japanese, these are referred to as *不要牌 (fuyōhai)* or *余剰牌 (yojōhai)*

```python
from xiangting import (
    PlayerCount,
    calculate_necessary_tiles,
    calculate_unnecessary_tiles,
)

# 199m146779p12s246z
hand = [
    1, 0, 0, 0, 0, 0, 0, 0, 2, # m
    1, 0, 0, 1, 0, 1, 2, 0, 1, # p
    1, 1, 0, 0, 0, 0, 0, 0, 0, # s
    0, 1, 0, 1, 0, 1, 0, # z
]

replacement_number1, necessary_tiles = calculate_necessary_tiles(
    hand,
    PlayerCount.FOUR,
)
replacement_number2, unnecessary_tiles = calculate_unnecessary_tiles(
    hand,
    PlayerCount.FOUR,
)

assert replacement_number1 == 5
assert replacement_number1 == replacement_number2
# 1239m123456789p1239s1234567z
assert necessary_tiles == 0b1111111_100000111_111111111_100000111
# 1m14679p12s246z
assert unnecessary_tiles == 0b0101010_000000011_101101001_000000001
```

### Support for Three-Player Mahjong

In three-player mahjong, the tiles from 2m (二萬) to 8m (八萬) are not used.

```python
from xiangting import (
    PlayerCount,
    calculate_necessary_tiles,
    calculate_unnecessary_tiles,
)

# 1111m111122233z
hand = [
    4, 0, 0, 0, 0, 0, 0, 0, 0, # m
    0, 0, 0, 0, 0, 0, 0, 0, 0, # p
    0, 0, 0, 0, 0, 0, 0, 0, 0, # s
    4, 3, 2, 0, 0, 0, 0, # z
]

rn_4p, nt_4p = calculate_necessary_tiles(hand, PlayerCount.FOUR)
_, ut_4p = calculate_unnecessary_tiles(hand, PlayerCount.FOUR)
assert rn_4p == 2
assert nt_4p == 0b0000000_000000000_000000000_000000110  # 23m
assert ut_4p == 0b0000001_000000000_000000000_000000000  # 1z

rn_3p, nt_3p = calculate_necessary_tiles(hand, PlayerCount.THREE)
_, ut_3p = calculate_unnecessary_tiles(hand, PlayerCount.THREE)
assert rn_3p == 3
# 9m123456789p123456789s34567z
assert nt_3p == 0b1111100_111111111_111111111_100000000
assert ut_3p == 0b0000001_000000000_000000000_000000001  # 1m1z
```

## License

Copyright (c) Apricot S. All rights reserved.

Licensed under the [MIT license](LICENSE).
