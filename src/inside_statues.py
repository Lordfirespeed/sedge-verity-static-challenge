from dataclasses import dataclass
from typing import Self, Iterator
from itertools import permutations

from src.statue import Statue
from src.symbol import Symbol


@dataclass
class InsideStatueStates:
    left: Symbol
    middle: Symbol
    right: Symbol

    def __post_init__(self):
        assert self.left != self.middle
        assert self.left != self.right
        assert self.middle != self.right

    def __getitem__(self, item: Statue) -> Symbol:
        if item == Statue.Left: return self.left
        if item == Statue.Middle: return self.middle
        if item == Statue.Right: return self.right
        raise ValueError

    def __str__(self) -> str:
        return f"{self.left} {self.middle} {self.right}"

    @classmethod
    def from_ordering(cls, ordering: tuple[Symbol, Symbol, Symbol]):
        return cls(*ordering)

    @staticmethod
    def enumerate_all_possible_orderings() -> Iterator[tuple[Symbol, Symbol, Symbol]]:
        yield from permutations([Symbol.Circle, Symbol.Square, Symbol.Triangle])

    @classmethod
    def enumerate_all_possible_states(cls) -> Iterator[Self]:
        return map(cls.from_ordering, cls.enumerate_all_possible_orderings())
