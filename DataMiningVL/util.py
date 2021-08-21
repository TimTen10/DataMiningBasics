import math


def lp_metric(p):
    """ Creates Lp-Metric for the given value of p. """

    def distance(x, y) -> float:
        return (sum((abs(xi - yi)) ** p for xi, yi in zip(x, y))) ** (1.0 / p)

    return distance


def main():
    manhattan_dist = lp_metric(1)
    assert manhattan_dist([1, 0], [3, 1]) == 3
    euclidean_dist = lp_metric(2)
    assert euclidean_dist([1, 0], [3, 1]) == math.sqrt(5)


if __name__ == '__main__':
    main()
