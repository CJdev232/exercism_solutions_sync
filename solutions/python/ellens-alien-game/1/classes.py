"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """
    total_aliens_created = 0
    def __init__(self,x_coordinate_start,y_coordinate_start):
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
        if self._health:
            self._health -= 1
    def is_alive(self):
        return self._health > 0
    def teleport(self,new_x_coordinate,new_y_coordinate):
            self._x_coordinate = new_x_coordinate
            self._y_coordinate = new_y_coordinate
        
    def collision_detection(self,other):
        if (self._x_coordinate == other._x_coordinate and self._y_coordinate == other._y_coordinate):
            return True
        return None
        


#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.
def new_aliens_collection(coordinate_list):
    return [Alien(x,y) for x,y in coordinate_list]
    
