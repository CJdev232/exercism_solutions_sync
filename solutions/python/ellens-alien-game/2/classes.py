"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate."""

    total_aliens_created = 0

    def __init__(self, x_coordinate_start, y_coordinate_start):
        self._x_coordinate = x_coordinate_start
        self._y_coordinate = y_coordinate_start
        self._health = 3
        Alien.total_aliens_created += 1

    @property
    def x_coordinate(self):
        return self._x_coordinate

    @property
    def y_coordinate(self):
        return self._y_coordinate

    @property
    def health(self):
        return self._health

    def hit(self):
        if self._health > 0:
            self._health -= 1

    def is_alive(self):
        return self._health > 0

    def teleport(self, new_x_coordinate, new_y_coordinate):
        self._x_coordinate = new_x_coordinate
        self._y_coordinate = new_y_coordinate

    def collision_detection(self, other):
        if (
            self._x_coordinate == other.x_coordinate
            and self._y_coordinate == other.y_coordinate
        ):
            return True
        return None


def new_aliens_collection(coordinate_list):
    return [
        Alien(x_coordinate, y_coordinate)
        for x_coordinate, y_coordinate in coordinate_list
    ]
