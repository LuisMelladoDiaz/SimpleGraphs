# SimpleGraphs

[Idea](#idea) | [State of the project](#state-of-the-project) | [What's next?](#whats-next)

## Idea
SimpleGraphs is a straightforward graphical interface for drawing graphs. The project is designed to make it easy to create and define graphs visually, eliminating the need to manually write lists of nodes and edges. For now, the scope of the project is small, focusing on basic functionalities. Users will be able to draw nodes with a single attribute (node name) and edges, which can be either directed or undirected, with weights.

The initial purpose of this tool was educational. I wanted to help some friends understand how finite state machines work. Since finite state machines are essentially directed graphs, having a tool to draw them simplifies the process of designing these machines. As a video game enthusiast, I also thought of another cool application: defining combo structures in fighting games. In these games, some moves connect to create hit strings called combos. I am sure you can imagine how the navigability of a graph can help with this.

## State of the project
### 25/05/2024
Basic drawing tools were introduced to depict nodes and edges. It is possible to drag and drop a node and edit its name and color.    

![25/05/2024](https://github.com/LuisMelladoDiaz/SimpleGraphs/assets/93400291/86e1104b-00be-454b-bb84-026e506ed62b)

### 27/05/2024
There are new functionalities regarding edges. First, edges can have weight. Weights are the usual way to represent how expensive is to traverse an edge. Secondly, now edges can be directed. There are three types of edges availale: directed (->, <-), bidirectional (<-->) and undirected (--).    

Deleting tool was added. It is possible to delete nodes and edges. If you delete a node all its edges will also be deleted. Be careful, the delete tool radius is a little bigger than the cursor's. I expect to improve little things like these in the future to achieve a better user experience but at this point I am focusing on functionality.

Button for edit tool is left as a placeholder. You can use it to modify nodes and edges position, names, color, direction, weights... without having to worry about misclicking left click and drawing something accidentally.

<img src="https://github.com/LuisMelladoDiaz/SimpleGraphs/assets/93400291/5783d74b-6002-48b7-84f8-44a60676af05" width="600">


#### Available Actions
* **Left Click - Draw Node/Edge:** Select a drawing tool at the botton of the screen. There are two drawing tools, node and edge. Left click in the grid to draw nodes. Click on on two nodes to join them with an edge.
* **Right Click - Move Node:** Click and hold on a node to drag and move it to a new position.
* **Double Right Click - Edit NodeName/Weight:** Double right click on a node to rename it. Double right click on an edge to edit its weight. Press enter to confirm.
* **Mouse Wheel Click - Change Color/Direction:** Click the mouse wheel on a node to cycle through different colors for the node. Click the mouse wheel on an edge to cycle through different directions.

### 28/05/2024
You can now save your drawings. Save them in the graphs folder so they can be used later. There is a parsing function in the file grahp_converter.py that can read the generated csv files and convert them into graphs. These graphs are interpretable by the well known graph library NetworkX. Our drawings will look like this after the conversion:       

<img src="https://github.com/LuisMelladoDiaz/SimpleGraphs/assets/93400291/47e4bed4-c010-4ee8-a230-203aea345a53" width="600">

Now that we have real graphs we can solve problems like the travelers tour problem or the shortest path problem. Imagine we have a city with a Restaurant, a Market and a Park. We want to go from the Restaurant back to Home, what would be the fastest route? Please have a look to the file example.py, there you will see how this problem is solved. See the generated solution:       

<img src="https://github.com/LuisMelladoDiaz/SimpleGraphs/assets/93400291/fa9e0f94-3e40-4fbd-907f-68c41e641745" width="600">

## What's next?
My plan is to use SimpleGraphs in various small projects, adding functionalities as needed. The goal is to progressively refine the user experience by working with SimpleGraphs and analyzing its flaws over time. Currently, I'm uncertain whether it’s more practical to draw the graph rather than defining it by writing lists of edges and nodes. While drawing is definitely easier to understand, more visual, and intuitive, I'm unsure if it's more efficient. If anyone reading this is interested in trying it out or collaborating, please feel free to contact me.



