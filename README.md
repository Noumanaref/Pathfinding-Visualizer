# Pathfinding Visualizer

A Python-based Pathfinding Visualizer developed using **Tkinter** to compare the behavior and performance of both **Uninformed** and **Informed** search algorithms on a grid-based environment.

The application allows users to create custom maps, generate random mazes, select heuristic functions, and visualize how different search algorithms explore the grid to find a path from the Start node to the Goal node.

---

## Features

- Dynamic grid size selection
- Interactive placement of Start and Goal nodes
- Manual obstacle creation and removal
- Random maze generation with user-defined obstacle density
- Visualization of search process
- Real-time performance statistics
- Support for multiple heuristic functions

---

## Implemented Algorithms

### Uninformed Search
- Breadth-First Search (BFS)
- Uniform Cost Search (UCS)

### Informed Search
- Greedy Best-First Search (GBFS)
- A* Search

---

## Heuristic Functions

The following heuristics are available for Greedy Best-First Search and A* Search:

- Manhattan Distance
- Euclidean Distance

---

## Visualization

The application uses different colors to represent the search process.

| Color | Meaning |
|--------|---------|
| 🟡 Yellow | Frontier Nodes (Nodes currently in Queue/Priority Queue) |
| 🔵 Light Blue | Visited / Expanded Nodes |
| 🟢 Green | Final Path |
| ⚫ Black | Obstacles |
| 🟩 Green Cell | Start Node |
| 🟥 Red Cell | Goal Node |



---

## Performance Metrics

After each algorithm execution, the following statistics are displayed:

- Algorithm Name
- Nodes Expanded
- Path Length
- Path Cost
- Execution Time (milliseconds)

---

## Technologies Used

- Python 3
- Tkinter
- Queue
- PriorityQueue

---

## Project Structure

```
Pathfinding-Visualizer/
│
├── main.py          # GUI and Visualization
├── algorithms.py    # Search Algorithms
├── utils.py         # Heuristic Functions
└── README.md
```

---

## How to Run

1. Install Python 3.
2. Download or clone this repository.
3. Open the project folder.
4. Run:

```bash
python main.py
```

5. Enter the desired grid size.
6. Select the Start node.
7. Select the Goal node.
8. Create obstacles manually or generate a random maze.
9. Choose a heuristic (for A* or Greedy).
10. Run any search algorithm and observe the visualization.

---

## Comparison of Algorithms

| Algorithm | Complete | Optimal | Uses Heuristic |
|-----------|----------|---------|----------------|
| BFS | Yes | Yes (Unweighted Graph) | No |
| UCS | Yes | Yes | No |
| Greedy Best-First Search | No | No | Yes |
| A* Search | Yes | Yes (Admissible Heuristic) | Yes |

---

## Learning Outcomes

This project demonstrates:

- Difference between uninformed and informed search.
- Effect of heuristic functions on search efficiency.
- Pathfinding on a two-dimensional grid.
- Performance comparison using visualization and metrics.
- Queue and Priority Queue based search implementations.

---

## Future Improvements

- Diagonal movement
- Weighted terrain
- Bidirectional Search
- Dijkstra's Algorithm
- Depth-First Search (DFS)
- Animated frontier updates
- Maze generation algorithms (Recursive Backtracking, Prim's Algorithm)

---

## Author

**Nouman Arif**

Software Engineering Student

FAST National University of Computer and Emerging Sciences
