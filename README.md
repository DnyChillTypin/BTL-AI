# Branch and Bound Pathfinding Project

This project implements a **Branch and Bound** algorithm to find the optimal (minimum cost) path between two nodes in a weighted graph. It uses heuristic values to guide the search and prune sub-optimal branches, ensuring efficiency.

## 🚀 Variable Definitions

In this implementation, several key variables are used to track costs and nodes. Understanding these is crucial for understanding how the algorithm works:

### Core Variables (`h`, `g`, `f`)
- **`v` (Vertex/Node)**: Represents a specific point in the graph (e.g., 'A', 'B', 'C').
- **`h(v)` (Heuristic)**: The **estimated cost** from node `v` to the goal. This value is provided in the `#HEURISTIC` section of the input file.
- **`g(v)` (Actual Cost)**: The **accrued cost** required to reach node `v` from the starting node.
- **`f(v)` (Total Estimate)**: The **total estimated cost** of the entire path if it passes through node `v`. 
  - Calculated as: `f(v) = g(v) + h(v)`
- **`k(u, v)` (Edge Weight)**: The specific cost to travel directly from node `u` to its neighbor `v`.

### Storage & List Variables
- **`L` (Search Queue)**: A list that stores all "open" paths currently being explored.
- **`L1` (Child List)**: A temporary list containing the neighbors (children) of the node currently being expanded.
- **`best_cost` (Bound)**: The cost of the best path found so far. This value is used to **prune** (discard) any path where `f(v)` is already greater than or equal to `best_cost`.

---

## 🛠 Functions Overview

### 1. `class NodeState`
This class is a container for the state of a path at any given node.
- **Stores**: `node` (name), `g` (actual cost so far), `f` (total estimate), and `path` (the full history of nodes visited to reach this point).

### 2. `read_input(file_path)`
Parses the input text file to build the graph and heuristic table.
- **Input**: Path to a file containing `#HEURISTIC` and `#GRAPH` headers.
- **Returns**: `start_node`, `end_node`, `heuristics` dictionary, and `graph` adjacency list.

### 3. `branch_and_bound(...)`
The main logic of the project.
- **Execution Flow**:
  1. Starts at `start_node` and adds it to `L`.
  2. While `L` has nodes:
     - Pops the first state (`current`).
     - Checks if the path is worth exploring (`f(v) < best_cost`).
     - If the target is reached, updates `best_cost`.
     - Otherwise, expands neighbors, sorts them by `f`, and adds them to the **front** of `L`.
  3. Outputs a detailed trace table to `output.txt`.

---

## 📖 How to Run

1. Prepare an `input.txt` file (see examples in the repository).
2. Run the script:
   ```bash
   python Branch_And_Bound.py
   ```
3. Check `output.txt` for the step-by-step trace and the final optimal path.
