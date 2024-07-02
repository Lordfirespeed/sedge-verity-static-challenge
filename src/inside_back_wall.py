from dataclasses import dataclass
from typing import Self, Iterator
from itertools import permutations

from src.inside_statues import InsideStatueStates
from src.statue import Statue
from src.symbol import Symbol


@dataclass
class InsideBackWallStates:
    left: list[Symbol]
    middle: list[Symbol]
    right: list[Symbol]

    def __post_init__(self):
        all_symbols = self.left + self.middle + self.right
        assert all_symbols.count(Symbol.Circle) == 2
        assert all_symbols.count(Symbol.Square) == 2
        assert all_symbols.count(Symbol.Triangle) == 2

    def __getitem__(self, item: Statue) -> list[Symbol]:
        if item == Statue.Left: return self.left
        if item == Statue.Middle: return self.middle
        if item == Statue.Right: return self.right
        raise ValueError

    def __str__(self) -> str:
        def format_wall(wall: list[Symbol]) -> str:
            if not wall: return "_"
            return "".join(map(lambda x: x.value, wall))

        return f"{format_wall(self.left)} {format_wall(self.middle)} {format_wall(self.right)}"

    @classmethod
    def from_ordering(cls, ordering: tuple[list[Symbol], list[Symbol], list[Symbol]]):
        return cls(*ordering)

    @staticmethod
    def enumerate_possible_initial_orderings(statue_state: InsideStatueStates) -> Iterator[tuple[list[Symbol], list[Symbol], list[Symbol]]]:
        for left, middle, right in permutations([Symbol.Circle, Symbol.Square, Symbol.Triangle]):
            yield [statue_state.left, left], [statue_state.middle, middle], [statue_state.right, right]  # 0 0 0

            if left != statue_state.left:
                yield [left, statue_state.left], [statue_state.middle, middle], [statue_state.right, right]  # 1 0 0
            if middle != statue_state.middle:
                yield [statue_state.left, left], [middle, statue_state.middle], [statue_state.right, right]  # 0 1 0
            if right != statue_state.right:
                yield [statue_state.left, left], [statue_state.middle, middle], [right, statue_state.right]  # 0 0 1

            if left != statue_state.left and middle != statue_state.middle:
                yield [left, statue_state.left], [middle, statue_state.middle], [statue_state.right, right]  # 1 1 0
            if left != statue_state.left and right != statue_state.right:
                yield [left, statue_state.left], [statue_state.middle, middle], [right, statue_state.right]  # 1 0 1
            if middle != statue_state.middle and right != statue_state.right:
                yield [statue_state.left, left], [middle, statue_state.middle], [right, statue_state.right]  # 0 1 1

            if left != statue_state.left and middle != statue_state.middle and right != statue_state.right:
                yield [left, statue_state.left], [middle, statue_state.middle], [right, statue_state.right]  # 1 1 1

    @classmethod
    def enumerate_possible_initial_states(cls, statue_state: InsideStatueStates) -> Iterator[Self]:
        return map(cls.from_ordering, cls.enumerate_possible_initial_orderings(statue_state))
