#!/usr/bin/env python3

SAMPLE_HOUSES = [2.1, 6.2, 8.5, 12, 16, 18, 22, 40, 60, 90]
DEFAULT_TOWER_DISTANCE = 4.0

def cell_tower_placement (house_locations = SAMPLE_HOUSES, max_coverge_distance = DEFAULT_TOWER_DISTANCE):
    house_locations.sort()
    tower_locations = []

    for house_location in house_locations:
        if not tower_locations:
            nearest_tower_location = None
        else: 
            nearest_tower_location = tower_locations[-1]

        if (not nearest_tower_location or abs(house_location - nearest_tower_location > max_coverge_distance)):
            tower_locations.append(house_location + max_coverge_distance)

    return tower_locations

if __name__ == '__main__':
    print(cell_tower_placement())
