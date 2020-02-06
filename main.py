import sys, queue
from collections import defaultdict

def find_path(graph, path, origin_city, destination_city):
    current_city = destination_city
    path_final = []
    while current_city is not origin_city:
        path_final.append(current_city)
        current_city = path[current_city]
    path_final.append(origin_city)
    path_final.reverse()
    for i in range(len(path_final)-1):
        string1 = path_final[i]
        string2 = path_final[i+1]
        distance = graph[path_final[i]][path_final[i+1]]
        print(string1.strip(), "to", string2.strip(), ",", distance, "km")
        

file_name = sys.argv[1]

origin_city = sys.argv[2]
destination_city = sys.argv[3]

file = open(file_name,"r")
lines = file.readlines()

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

#This variable is used to notify that the target city has been found or not
cityFound = 0;

path[origin_city] = None
while not queue.empty():
    distance, (city, previous_city) = queue.get()
    if city not in visited:
        path[city] = previous_city
        visited.append(city)
        if city == destination_city:
            print('distance:', distance, 'km')
            print('route:')
            find_path(graph, path, origin_city, city)

            #Update cityFound to indicate the target city is found
            cityFound = 1;
        else:
            for next_city in graph[city].items() :
                if next_city[0] not in visited:
                    new_distance = distance + next_city[1]
                    queue.put((new_distance, (next_city[0], city)))

#Print out the city was never found, if there was no path to it from the source
if cityFound == 0:
    print('distance:infinity')
    print('route:')
    print('none')
