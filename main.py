import sys, queue
from collections import defaultdict

# Get the path and prints the intermediate steps
def find_path(graph, path, origin_city, destination_city):
    current_city = destination_city
    path_final = []
    while current_city is not origin_city:
        path_final.append(current_city)
        current_city = path[current_city]
    path_final.append(origin_city)
    path_final.reverse()
    for i in range(len(path_final)-1):
        city1 = path_final[i]
        city2 = path_final[i+1]
        distance = graph[path_final[i]][path_final[i+1]]
        print(city1, "to", city2, ",", distance, "km")

# Get the arguments
file_name = sys.argv[1]

origin_city = sys.argv[2]
destination_city = sys.argv[3]

file = open(file_name,"r")
lines = file.readlines()

# Reads the file and populates the graph
graph = defaultdict(dict)
for line in lines[:-2]:
    city0 = line.split()[0]
    city1 = line.split()[1]
    distance = int(line.split()[2])

    graph[city0][city1] = distance
    graph[city1][city0] = distance

visited = []
path = {}
queue = queue.PriorityQueue()
queue.put((0, (origin_city, origin_city)))

total_distance = 0

# Keeps going while there are still cities
path[origin_city] = None
while not queue.empty():
    distance, (city, previous_city) = queue.get()
    if city not in visited:
        path[city] = previous_city
        visited.append(city)
        if city == destination_city:
            # A path is found, prints it and exits the program
            print('distance:', distance, 'km')
            print('route:')
            find_path(graph, path, origin_city, city)
            exit(0)
        else:
            for next_city in graph[city].items() :
                if next_city[0] not in visited:
                    new_distance = distance + next_city[1]
                    queue.put((new_distance, (next_city[0], city)))

#Print out the city was never found, if there was no path to it from the source
print('distance: infinity')
print('route:')
print('none')
