# SimpleGraphs

## Idea
SimpleGraphs is a straightforward graphical interface for drawing graphs. The project is designed to make it easy to create and define graphs visually, eliminating the need to manually write lists of nodes and edges. For now, the scope of the project is small, focusing on basic functionalities. Users will be able to draw nodes with a single attribute (node name) and edges, which can be either directed or undirected, with weights.

The initial purpose of this tool was educational. I wanted to help some friends understand how finite state machines work. Since finite state machines are essentially directed graphs, having a tool to draw them simplifies the process of designing these machines. As a video game enthusiast, I also thought of another cool application: defining combo structures in fighting games. In these games, some moves connect to create hit strings called combos. I am sure you can imagine how the navigability of a graph can help with this.

## State of the project
### 25/05/2024
![25/05/2024](https://github.com/LuisMelladoDiaz/SimpleGraphs/assets/93400291/86e1104b-00be-454b-bb84-026e506ed62b)

#### Available Actions
* **Left Click - Draw Node/Edge:** Select a drawing tool at the botton of the screen. There are two drawing tools, node and edge. Left click in the grid to draw nodes. Click on on two nodes to join them with an edge.
* **Right Click - Move Node:** Click and hold on a node to drag and move it to a new position.
* **Double Right Click - Rename Node:** Double right click on a node to rename it. Press enter to confirm. You won`t be able to move a node while you edit its name.
* **Mouse Wheel Click - Change Color:** Click the mouse wheel on a node to cycle through different colors for the node.

