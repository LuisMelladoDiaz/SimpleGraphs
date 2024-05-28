from graph_converter import *

#Imagine we have a city with a Restaurant, a Market and a Park. We want to go from the Restaurant back to Home, what would be the fastest route?
def shortest_path_example():
    #Load the graph
    City_Graph,*_ = load_graph_from_csv("city")

    #Shortest path computation
    shortest_path = nx.shortest_path(City_Graph, source='Restaurant', target='Home', weight='weight')
    shortest_distance = nx.shortest_path_length(City_Graph, source='Restaurant', target='Home', weight='weight')

    # Output the shortest path and distance
    print("Shortest Path:", shortest_path)
    print("Shortest Distance:", shortest_distance)

    return shortest_path

if __name__ == "__main__":
    draw_graph("city")
    shortest_path = shortest_path_example()
    draw_graph("city", path=shortest_path)
