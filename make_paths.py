import pdb
import sys

def main(argv=None):
    """ XXXXXXXXXXXXXXXXXXXXX """
    roads = read_road("./roads_example1.txt")
    routes = read_routes('./routes_example1.txt', roads)

    return 0        # success

def read_road(file_path_roads):
        f = open(file_path_roads, "r")

        file = f.readlines()
        roads = {}

        for line in file:
            road_id, origin_x, origin_y, ending_x, ending_y, velocity = line.split()
            roads['road_id'] = [origin_x, origin_y, ending_y, velocity]


def read_routes(file_path_routes, roads):
        f = open(file_path_routes, "r")

        file = f.readlines()
        roads = {}

        for line in file:
            line_splitted = line.split()
            route_id, number_of_cars = line_splitted[0], line_splitted[1]
            waypoints = line_splitted[2:]

            pdb.set_trace() ############################## Breakpoint ##############################



if __name__ == '__main__':
    main(sys.argv[1:])
