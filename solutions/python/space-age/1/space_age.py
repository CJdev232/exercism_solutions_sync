class SpaceAge:
    PLANETS = {
        'mercury': 0.2408467,
        'venus': 0.61519726,
        'earth': 1.0,
        'mars': 1.8808158,
        'jupiter': 11.862615,
        'saturn': 29.447498,
        'uranus': 84.016846,
        'neptune': 164.79132,
    }
    SECONDS_PER_EARTH_YEAR = 31557600
    def __init__(self, seconds):
        self.seconds = seconds
    def _age_on_planet(self,orbit_time):
        earth_years = self.seconds / self.SECONDS_PER_EARTH_YEAR
        planet_years = earth_years / orbit_time
        return round(planet_years,2)
for planet, orbital_period in SpaceAge.PLANETS.items():
    method = lambda self, op=orbital_period: self._age_on_planet(op)
    setattr(SpaceAge, f'on_{planet}', method)
        
        
        
