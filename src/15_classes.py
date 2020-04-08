# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor
class LatLon():
    def __init__(self, lat, lon):
        pass


# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name
        self.lat = lat
        self.lon = lon
    def __str__(self):
        return 'Waypoint: '+self.name+' ( Lat: '+str(self.lat)+' | Lon: ' + str(self.lon) + ' )'

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        self.name = name
        self.lat = lat
        self.lon = lon
        self.size = size
        self.difficulty = difficulty
    def __str__(self):
        return 'Geocache: '+self.name+' (Diff '+str(self.difficulty)+' Size '+str(self.size)+' Lat '+str(self.lat)+' Lon '+str(self.lon)+' )'
# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521
new_waypoint = Waypoint("Catacombs", 41.7505, -121.51521)
# new_waypoint = Waypoint
# new_waypoint.name = "Catacombs"
# new_waypoint.lat = 41.70505
# new_waypoint.lon = -121.51521
#print(new_waypoint.name, new_waypoint.lat, new_waypoint.lon)
print('-------------------->\n', new_waypoint)
#print('-------------------->\n', Waypoint)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(Waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

new_geocache = Geocache("Newberry Views", 1.5,2,44.052137,-121.41556)
print('-------------------->\n', new_geocache)

# Print it--also make this print more nicely
print(Geocache)
