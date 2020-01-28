import sys, queue

def find_path(path, origin_city, destination_city):
    current_city = destination_city
    path_final = []
    while current_city is not origin_city:
        path_final.append(current_city)
        current_city = path[current_city]
    path_final.append(origin_city)
    path_final.reverse()
    for i in range(len(path_final)-1):
        print(path_final[i], " to ", path_final[i+1])

file_name = sys.argv[1]

origin_city = sys.argv[2]
destination_city = sys.argv[3]

file = open(file_name,"r")
lines = file.readlines()

graph = {}

for line in lines[:-2]:
    city0 = line.split()[0]
    city1 = line.split()[1]
    distance = int(line.split()[2])

    if city0 in graph:
        graph[city0].append((city1, distance))
    else:
        graph[city0] = [(city1, distance)]
    if city1 in graph:
        graph[city1].append((city0, distance))
    else:
        graph[city1] = [(city0, distance)]
        
visited = []
path = {}
queue = queue.PriorityQueue()
queue.put((0, (origin_city, origin_city)))

total_distance = 0

path[origin_city] = None
while queue:
    distance, (city, previous_city) = queue.get()
    if city not in visited:
        path[city] = previous_city
        visited.append(city)
        if city == destination_city:
            print('route found ', distance)
            
            find_path(path, origin_city, city)
            exit(0)
        else:
            for next_city in graph[city]:
                if next_city[0] not in visited:
                    new_distance = distance + next_city[1]
                    queue.put((new_distance, (next_city[0], city)))
print('route not found')
