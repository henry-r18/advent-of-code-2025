# Wasn't able to solve this one, but found this answer on Reddit interesting.
# See @https://www.reddit.com/r/adventofcode/comments/1ph3tfc/comment/nt0o0tw/
# Learned about Disjoin Set Unions today

# from collections import defaultdict
from itertools import combinations
from math import dist, prod

PUZZLE_INPUT = "puzzle_input.txt"


class DisjointSetUnion:
    def __init__(self, nodes):
        self.n = len(nodes)
        self.parent = {u: u for u in nodes}
        self.size = dict.fromkeys(nodes, 1)

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return
        if self.size[pu] < self.size[pv]:
            pu, pv = pv, pu
        self.parent[pv] = pu
        self.size[pu] += self.size[pv]
        self.n -= 1


def calculate_product_largest_circuits_part_two(junction_boxes: list[tuple]) -> int:
    """Given a list of tuples representing the positions of junction boxes in 3D space,
    return the product of the sizes of the three largest circuits."""
    dsu = DisjointSetUnion(junction_boxes)

    edges = sorted(combinations(junction_boxes, 2), key=lambda x: dist(x[0], x[1]))

    for u, v in edges:
        dsu.union(u, v)
        if dsu.n == 1:
            return u[0] * v[0]
    return 0


def calculate_product_largest_circuits_part_one(junction_boxes: list[tuple]) -> int:
    """Given a list of tuples representing the positions of junction boxes in 3D space,
    return the product of the sizes of the three largest circuits."""
    dsu = DisjointSetUnion(junction_boxes)

    edges = sorted(combinations(junction_boxes, 2), key=lambda x: dist(x[0], x[1]))

    for u, v in edges[:1000]:
        dsu.union(u, v)
    roots = {dsu.find(u) for u in dsu.parent}
    sizes = sorted(dsu.size[r] for r in roots)
    return prod(sizes[-3:])

    # junction_combos = combinations(junction_boxes, 2)
    # distances_map = defaultdict(float)
    # for combo in junction_combos:
    #     distances_map[combo] = dist(combo[0], combo[1])

    # sorted_distances = sorted(distances_map.items(), key=lambda item: item[1])

    # visited = set()
    # circuits = []
    # for junction_box in junction_boxes:
    #     if junction_box not in visited:
    #         stack = [junction_box]
    #         current_circuit = []

    #         while stack:
    #             current_junction_box = stack.pop()
    #             if current_junction_box not in visited:
    #                 visited.add(current_junction_box)
    #                 current_circuit.append(current_junction_box)
    #                 stack.extend()

    # nearest_neighbor_map = defaultdict(list[tuple[tuple, float]])
    # for i, junction_box in enumerate(junction_boxes):
    #     other_junction_boxes = junction_boxes[:i] + junction_boxes[i + 1 :]
    #     distances = [
    #         (other_box, dist(junction_box, other_box))
    #         for other_box in other_junction_boxes
    #     ]

    #     nearest_neighbor_map[junction_box] = sorted(
    #         distances, key=lambda distance: distance[1]
    #     )

    # for junction_box, distances in nearest_neighbor_map.items():
    #     nearest_neighbor = distances[0]
    #     print(
    #         f"{junction_box} is closest to {nearest_neighbor[0]} at distance {nearest_neighbor[1]}"
    #     )


def load_input(file: str = PUZZLE_INPUT):
    """Load the input file and read box positions to a list of tuples."""
    with open(file, "r", encoding="utf-8") as f:
        return [tuple(map(int, line.strip().split(","))) for line in f.readlines()]


def main():
    junction_boxes = load_input()

    print(f"Part one: {calculate_product_largest_circuits_part_one(junction_boxes)}")
    print(f"Part two: {calculate_product_largest_circuits_part_two(junction_boxes)}")


if __name__ == "__main__":
    main()
