from typing import List, Optional

class CityMap:
    def __init__(self, cities: List[str], xCoordinates: List[int], yCoordinates: List[int]):
        self.city_to_coord = {} # London: (x, y)
        self.x_map = {} # x: [(London, y)]
        self.y_map = {} # y: [(London, x)]

        for city, x, y in zip(cities, xCoordinates, yCoordinates):
            self.city_to_coord[city] = (x, y)
            self.x_map.setdefault(x, []).append((city, y))
            self.y_map.setdefault(y, []).append((city, x))

    def getNearestCity(self, query: str) -> str:
        if query not in self.city_to_coord:
            return ""
        
        nearest_city, nearest_distance = "", float('inf')
        x, y = self.city_to_coord[query]

        for city, city_x in self.y_map.get(y, []):
            if city != query:
                dist = abs(city_x-x)
                if nearest_distance > dist or (nearest_distance == dist and city < nearest_city):
                    nearest_distance = dist
                    nearest_city = city
        
        for city, city_y in self.x_map.get(x, []):
            if city != query:
                dist = abs(city_y-y)
                if nearest_distance > dist or (nearest_distance == dist and city < nearest_city):
                    nearest_distance = dist
                    nearest_city = city 

        return nearest_city

cities = ["London", "Toronto", "Ajax", "York", "Bayshore", "Paris", "Leduc", "Chicago"]
xs = [0, 1, 2, 4, 5, 0, 1, 0]
ys = [1, 2, 5, 3, 4, 2, 0, 0]

cityMap = CityMap(cities, xs, ys)
assert cityMap.getNearestCity("London") == "Chicago" # Return "Chicago". Cities sharing x = 0 or y = 1 are "Paris", and "Chicago", both are at a distance of 1. "Chicago" is lexicographically smaller than "Paris".
assert cityMap.getNearestCity("Toronto") == "Paris" # Returns "Paris". Cities sharing x = 1 or y = 2 are "Leduc", and "Paris". Paris is the closest with a distance of 1.
assert cityMap.getNearestCity("York") == "" # Return "". No other city shares x = 4 or y = 3
assert cityMap.getNearestCity("Albert") == "" # Return "", because "Albert" is not in the list.
print("All passed!!!")