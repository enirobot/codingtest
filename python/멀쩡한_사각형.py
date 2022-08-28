def GCD(x: int, y: int) -> int:
    return y if x % y == 0 else GCD(y, x % y)


def solution(w, h):
    return w * h - (w + h) + GCD(w, h)