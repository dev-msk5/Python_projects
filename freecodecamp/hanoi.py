def hanoi_solver(disks: int):
    start = list(range(disks, 0, -1))
    mid = []
    end = []
    history = []
    history.append(f"{start} {mid} {end}")

    def _move(n: int, src, aux, dest) -> None:
        if n == 0:
            return
        _move(n - 1, src, dest, aux)
        dest.append(src.pop())
        history.append(f"{start} {mid} {end}")
        _move(n - 1, aux, src, dest)

    _move(disks, start, mid, end)
    return "\n".join(history)

print(hanoi_solver(2))