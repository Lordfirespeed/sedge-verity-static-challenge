from copy import deepcopy
from dataclasses import dataclass
from typing import Self, Iterator

from src.statue import Statue
from src.inside_back_wall import InsideBackWallStates
from src.inside_statues import InsideStatueStates


@dataclass
class InsideState:
    statues: InsideStatueStates
    back_walls: InsideBackWallStates
    starting_on: Statue

    def __post_init__(self):
        assert self.statues.left in self.back_walls.left
        assert self.statues.middle in self.back_walls.middle
        assert self.statues.right in self.back_walls.right

    def __str__(self) -> str:
        return f"Statues: {self.statues}    Walls: {self.back_walls}    Starting: {self.starting_on}"

    @classmethod
    def enumerate_all_possible_states(cls) -> Iterator[Self]:
        for statues_state in InsideStatueStates.enumerate_all_possible_states():
            for back_wall_state in InsideBackWallStates.enumerate_possible_initial_states(statues_state):
                for starting_on in Statue:
                    yield cls(deepcopy(statues_state), back_wall_state, starting_on)
