import pdb
import sys

import math

def main(argv=None):
    """ XXXXXXXXXXXXXXXXXXXXX """
    roads = read_road("./roads_example1.txt")
    routes = read_routes('./routes_example1.txt', roads)

    verify_routes(roads, routes)

    return 0        # success

def read_road(file_path_roads):
        f = open(file_path_roads, "r")

        file = f.readlines()
        roads = {}

        for line in file:
            road_id, origin_x, origin_y, ending_x, ending_y, velocity = line.split()
            roads[road_id] = [origin_x, origin_y, ending_y, velocity]
        return roads


def read_routes(file_path_routes, roads):
        f = open(file_path_routes, "r")

        file = f.readlines()
        routes = {}

        for line in file:
            line_splitted = line.split()
            route_id, number_of_cars = line_splitted[0], line_splitted[1]
            roads = line_splitted[2:]

            routes[route_id] = {'n_cars':number_of_cars, 'road_ids':roads}

        return routes

def verify_routes(roads, routes):
    """
    Verify if the roads in the routes exist

    roads -- 
    routes -- 
    """
    for route in routes.values():
        for road_id in route['road_ids']:
            if not road_id in roads:
                print("Error")

def calc_time_arrival(origin_x, origin_y, destiny_x, destiny_y, speed):
    """
        0 0
        100 100
        20
    """
    x_vect = destiny_x - origin_x
    y_vect = destiny_y - origin_y

    distance =  math.sqrt(math.pow(x_vect,2) + math.pow(y_vect,2))
    time_arrival = distance / speed

    return time_arrival

if __name__ == '__main__':
    main(sys.argv[1:])
