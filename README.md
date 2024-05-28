# SimpleGraphs

## Idea
SimpleGraphs is a straightforward graphical interface for drawing graphs. The project is designed to make it easy to create and define graphs visually, eliminating the need to manually write lists of nodes and edges. For now, the scope of the project is small, focusing on basic functionalities. Users will be able to draw nodes with a single attribute (node name) and edges, which can be either directed or undirected, with weights.

The initial purpose of this tool was educational. I wanted to help some friends understand how finite state machines work. Since finite state machines are essentially directed graphs, having a tool to draw them simplifies the process of designing these machines. As a video game enthusiast, I also thought of another cool application: defining combo structures in fighting games. In these games, some moves connect to create hit strings called combos. I am sure you can imagine how the navigability of a graph can help with this.

## State of the project
### 25/05/2024
Basic drawing tools were introduced to depict nodes and edges. It is possible to drag and drop a node and edit its name and color.    

![25/05/2024](https://github.com/LuisMelladoDiaz/SimpleGraphs/assets/93400291/86e1104b-00be-454b-bb84-026e506ed62b)

### 28/05/2024
There are new functionalities regarding edges. First, edges now posses weight. Weights are the usual way to represent how expensive is to traverse an edge. Secondly, know edges can be directed. There are three types of edges availale: directed (->, <-), bidirectional (<-->) and undirected (--).    

Deleting tool was added. It is possible to delete nodes and edges. If you delete a node all its edges will also be deleted. Be careful, the delete tool radius is a little bigger than the cursor's. I expect to improve little things like these in the future to achieve a better user experience but at this point I am focusing on functionality.

Button for edit tool is left as a placeholder for now. You can use it to modify nodes and edges position, names, color, direction, weights... without having to worry about misclicking left click and drawing something accidentally.

<img src="https://github.com/LuisMelladoDiaz/SimpleGraphs/assets/93400291/5783d74b-6002-48b7-84f8-44a60676af05" width="600">


#### Available Actions
* **Left Click - Draw Node/Edge:** Select a drawing tool at the botton of the screen. There are two drawing tools, node and edge. Left click in the grid to draw nodes. Click on on two nodes to join them with an edge.
* **Right Click - Move Node:** Click and hold on a node to drag and move it to a new position.
* **Double Right Click - Edit NodeName/Weight:** Double right click on a node to rename it. Double right click on an edge to edit its weight. Press enter to confirm.
* **Mouse Wheel Click - Change Color/Direction:** Click the mouse wheel on a node to cycle through different colors for the node. Click the mouse wheel on an edge to cycle through different directions.

