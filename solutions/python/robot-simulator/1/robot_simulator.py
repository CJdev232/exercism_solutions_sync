import math

# Global direction constants (complex numbers represent directions)
NORTH = 0+1j
EAST = 1+0j
SOUTH = 0-1j
WEST = -1+0j


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self._x = x_pos  # Use private attributes to avoid conflicts
        self._y = y_pos
    
    @property
    def coordinates(self):
        """Return current position as (x, y) tuple"""
        return (self._x, self._y)
    
    def move(self, move_string):
        """Execute a series of commands: R (right), L (left), A (advance)"""
        for command in move_string:
            if command == 'R':
                self.direction *= -1j  # Rotate clockwise 90°
            elif command == 'L':
                self.direction *= 1j   # Rotate counterclockwise 90°
            elif command == 'A':
                # Advance one step in current direction
                self._x += int(self.direction.real)
                self._y += int(self.direction.imag)