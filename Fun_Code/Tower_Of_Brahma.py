def tower_of_brahma_iterative(n, source, intermediate, destination):
    rods = {source: list(range(n, 0, -1)), intermediate: [], destination: []}
    print(rods)
    moves = []
    total_moves = 2 ** n - 1
    if n % 2 == 0:
        intermediate, destination = destination, intermediate

    for move in range(1, total_moves + 1):
        if move % 3 == 1:
            print(move, move % 3)
            from_rod, to_rod = source, destination
        elif move % 3 == 2:
            # print(move, move % 2)
            from_rod, to_rod = source, intermediate
        else:
            # print(move)
            from_rod, to_rod = intermediate, destination
        if not rods[from_rod]:
            disk = rods[to_rod].pop()
            rods[from_rod].append(disk)
            moves.append(f"Move disk {disk} from {to_rod} to {from_rod}")
        elif not rods[to_rod]:
            disk = rods[from_rod].pop()
            rods[to_rod].append(disk)
            moves.append(f"Move disk {disk} from {from_rod} to {to_rod}")
        elif rods[from_rod][-1] < rods[to_rod][-1]:
            disk = rods[from_rod].pop()
            rods[to_rod].append(disk)
            moves.append(f"Move disk {disk} from {from_rod} to {to_rod}")
        else:
            disk = rods[to_rod].pop()
            rods[from_rod].append(disk)
            moves.append(f"Move disk {disk} from {to_rod} to {from_rod}")
    for move in moves:
        print(move)
    print(rods)
    # print(total_moves)


def tower_of_brahma_recursion(n, source, destination, intermediate):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    tower_of_brahma_recursion(n-1, source, intermediate, destination)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_brahma_recursion(n-1, intermediate, destination, source)


tower_of_brahma_iterative(4, 'A', 'B', 'C')
tower_of_brahma_recursion(4, 'A', 'C', 'B')