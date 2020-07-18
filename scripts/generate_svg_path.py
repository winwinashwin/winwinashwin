import math


class PVector:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y


def polar2cartesian(center: PVector, radius: int, angleDeg: float):
    angleRad = (angleDeg - 90) * math.pi / 180

    result = PVector()
    result.x = center.x + (radius * math.cos(angleRad))
    result.y = center.y + (radius * math.sin(angleRad))

    return result


def describeArc(center: PVector, radius, percentage):
    angStart = -135
    angEnd = 2.7 * percentage + angStart
    start = polar2cartesian(center, radius, angEnd)
    end = polar2cartesian(center, radius, angStart)

    if (angEnd - angStart <= 180):
        largleArcFlag = "0"
    else:
        largleArcFlag = "1"

    d = [
        "M", start.x, start.y,
        "A", radius, radius, 0, largleArcFlag, 0, end.x, end.y
    ]

    return " ".join(str(x) for x in d)


if __name__ == "__main__":
    print(describeArc(PVector(40, 40), 32, 80))
