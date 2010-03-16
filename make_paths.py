import pdb
import sys

import math

TOTAL_SIM_TIME = 500

def main(argv=None):
    """ XXXXXXXXXXXXXXXXXXXXX """
    roads = read_road("./roads_example1.txt")
    routes = read_routes('./routes_example1.txt', roads)

    verify_routes(roads, routes)

    calc_points(roads, routes)

    return 0        # success

def read_road(file_path_roads):
        f = open(file_path_roads, "r")

        file = f.readlines()
        roads = {}

        for line in file:
            road_id, origin_x, origin_y, ending_x, ending_y, velocity = line.split()
            roads[road_id] = [origin_x, origin_y, ending_x, ending_y, velocity]
        return roads


def read_routes(file_path_routes, roads):
        f = open(file_path_routes, "r")

        file = f.readlines()
        routes = {}

        for line in file:
            line_splitted = line.split()

            route_id, number_of_cars = line_splitted[0], line_splitted[1]
            car_interval = line_splitted[2]
            roads = line_splitted[3:]

            routes[route_id] = {'n_cars':number_of_cars,
                                'car_interval':car_interval,
                                'road_ids':roads}

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
    x_vect = float(destiny_x) - float(origin_x)
    y_vect = float(destiny_y) - float(origin_y)

    distance =  math.sqrt(math.pow(x_vect,2) + math.pow(y_vect,2))
    time_arrival = float(distance) / float(speed)

    return time_arrival

def calc_points(roads, routes):

    for route in routes.values():
        time =  0
        number_of_cars = int(route['n_cars'])
        car_interval = int(route['car_interval'])

        for i in xrange(number_of_cars):
            time = i * car_interval

            for road_id in route['road_ids']:
                road = roads[road_id]
                print_coordinate(0, time, road[0], road[1])
                time = time + calc_time_arrival(*road)

            last_point = roads[route['road_ids'][-1]]
            print_coordinate(0, time, last_point[2], last_point[3])

def print_coordinate(node, time, x, y):
    print ("%d %ds (%f, %f, 0) 0 0" % (int(node), int(time), float(x), float(y)))

if __name__ == '__main__':
    main(sys.argv[1:])
