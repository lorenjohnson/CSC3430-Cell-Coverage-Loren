#!/usr/bin/env python3

SAMPLE_HOUSES = [2.1, 6.2, 8.5, 12, 16, 19.8, 22, 26, 41, 62]
DEFAULT_TOWER_RANGE = 4.0

def optimal_cell_tower_locations (house_locations, max_coverge_distance):
    house_locations.sort()
    tower_locations = [house_locations[0] + max_coverge_distance] 

    for house_location in house_locations[1:]:
        last_tower_location = tower_locations[-1]

        if house_location - last_tower_location > max_coverge_distance:
            tower_locations.append(house_location + max_coverge_distance)

    return tower_locations

if __name__ == '__main__':
    results = optimal_cell_tower_locations(SAMPLE_HOUSES, DEFAULT_TOWER_RANGE)
    print()    
    print('-----------------------------------------------')
    print('Given houses at the following locations:\n')
    print(', '.join(map(str, SAMPLE_HOUSES)))
    print()
    print('And a maxium cell phone tower range of:\n')
    print(DEFAULT_TOWER_RANGE)
    print()    
    print('The optimal placement of cell phone towers will')
    print('be at the following locations:\n')
    print(', '.join(map(str, results)))
    print('-----------------------------------------------')
    print()
