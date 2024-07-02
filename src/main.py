from dataclasses import dataclass

from src.inside import InsideState
from src.statue import Statue
from src.symbol import Symbol


@dataclass
class Move:
    from_player: Statue
    to_player: Statue
    symbol: Symbol

    def __str__(self) -> str:
        return f"{self.from_player} sends {self.symbol} to {self.to_player}"


def solve_all_matching(problem: InsideState) -> list[Move]:
    return []


def solve_one_matching(problem: InsideState) -> list[Move]:
    return []


def solve_none_matching(problem: InsideState) -> list[Move]:
    moves: list[Move] = []

    person_1 = problem.starting_on
    person_1_back_wall = problem.back_walls[person_1]
    person_1_unmatching_symbol = person_1_back_wall[1] if person_1_back_wall[0] == problem.statues[person_1] else person_1_back_wall[0]
    person_3 = [person for person in Statue if person != person_1 and problem.statues[person] != person_1_unmatching_symbol].pop()
    moves.append(Move(person_1, person_3, person_1_unmatching_symbol))

    person_2 = [person for person in Statue if person != person_1 and person != person_3].pop()
    moves.append(Move(person_1, person_2, problem.statues[person_1]))

    moves.append(Move(person_2, person_1, problem.statues[person_2]))
    moves.append(Move(person_3, person_2, problem.statues[person_3]))
    moves.append(Move(person_2, person_1, problem.statues[person_3]))
    return moves


def solve(problem: InsideState):
    matching_back_walls = (
        problem.back_walls.left[0] == problem.back_walls.left[1],
        problem.back_walls.middle[0] == problem.back_walls.middle[1],
        problem.back_walls.right[0] == problem.back_walls.right[1],
    )

    if all(matching_back_walls):
        return solve_all_matching(problem)

    if any(matching_back_walls):
        return solve_one_matching(problem)

    return solve_none_matching(problem)


if __name__ == "__main__":
    possible_states = list(InsideState.enumerate_all_possible_states())

    for state in possible_states:
        solution = solve(state)
        if not solution: continue
        print(state)
        print("\n".join(map(str, solution)))
        print()
