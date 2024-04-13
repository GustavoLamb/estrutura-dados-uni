class Point:

    def __init__(self, x: object, y: object) -> None:
        self.x = x
        self.y = y

    def equals(self, x: object, y: object) -> bool:
        return self.x == x and self.y == y

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'


class Node:

    def __init__(self, x: object, y: object, value: object) -> None:
        self.x = x
        self.y = y
        self.value = value
        self.NW, self.NE, self.SE, self.SW = None, None, None, None

    def __str__(self):
        return f'({self.x}, {self.y}) {self.value}'


class Interval:
    def __init__(self, min: object, max: object) -> None:
        self.min = min
        self.max = max

    def contains(self, number: object) -> bool:
        return self.min <= number <= self.max


class Interval2D:

    def __init__(self, interval_x: Interval, interval_y: Interval) -> None:
        self.interval_x: Interval = interval_x
        self.interval_y: Interval = interval_y

    def contains(self, x: object = None, y: object = None, point: Point = None) -> bool:
        if point is not None:
            return self.interval_x.contains(point.x) and self.interval_y.contains(point.y)
        elif x is not None and y is not None:
            return self.interval_x.contains(x) and self.interval_y.contains(y)

        return False



