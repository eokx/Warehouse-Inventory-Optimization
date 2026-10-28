# 📦 OptiWarehouse: Smart Inventory & Route Optimization System
> **A Design and Analysis of Algorithms (DAA) Mini Project**

[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Algorithms](https://img.shields.io/badge/DAA-DP%20%2B%20Greedy-emerald.svg)](#-core-daa-algorithms-used)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Interface](https://img.shields.io/badge/UI-CLI%20%2B%20Web%20Dashboard-cyan.svg)](#-user-interfaces)

---

## 📌 Project Overview

In automated logistics and e-commerce fulfillment hubs (e.g., Amazon, Flipkart), operational efficiency relies on two fundamental algorithmic decisions:

1. **Storage Payload Maximization (What to pick?):** Selecting the highest-value combination of discrete, indivisible packages that fit within transport cart or shelf weight limits.
2. **Order Picking Navigation (How to pick?):** Directing an Autonomous Guided Vehicle (AGV) or floor picker along the shortest physical path across warehouse aisles to collect items and reach the dispatch bay with minimal battery and time consumption.

**OptiWarehouse** solves both problems end-to-end using two classical algorithmic paradigms: **Dynamic Programming** and **Greedy Graph Theory**.

---

## 🧠 Core DAA Algorithms Used

| Algorithm | Paradigm | Role in Warehouse | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- | :--- |
| **0/1 Knapsack** | Dynamic Programming | Maximizes total value of packed items under weight constraint $W$ | $\mathcal{O}(n \cdot W)$ | $\mathcal{O}(n \cdot W)$ |
| **Dijkstra's Algorithm** | Greedy (Min-Heap) | Finds the shortest path across warehouse aisle graph $G = (V, E)$ | $\mathcal{O}((V + E) \log V)$ | $\mathcal{O}(V)$ |

### 1. Dynamic Programming (0/1 Knapsack)
* **Why not Fractional Knapsack?** Warehouse units (e.g., electronic crates, diagnostic equipment) are discrete and indivisible. Fractional greedy heuristics fail to guarantee optimality.
* **Recurrence Relation:**
  $$\text{DP}[i][w] = \begin{cases} 
  \text{DP}[i-1][w] & \text{if } w_i > w \\ 
  \max(\text{DP}[i-1][w], \; \text{DP}[i-1][w - w_i] + v_i) & \text{if } w_i \le w 
  \end{cases}$$
* Includes **backtracking** from $\text{DP}[n][W]$ to identify the exact items packed.

### 2. Greedy Graph Theory (Dijkstra's Shortest Path)
* **Warehouse Floor Model:** A weighted undirected graph with 7 key nodes (`Entry_Dock`, `Aisle_A`, `Aisle_B`, `Aisle_C`, `Aisle_D`, `Cold_Storage`, `Packaging_Bay`).
* **Greedy Invariant:** Employs a binary Min-Heap to extract the closest unvisited node. Because all aisle distances are non-negative ($c \ge 0$), locally optimal decisions guarantee the global shortest route.

---

## ✨ Key Features

- 🎒 **0/1 Knapsack DP Solver:** Bottom-up tabulation matrix with customizable weight capacities and dynamic inventory management.
- 🗺️ **Multi-Stop Dijkstra Pathfinding:** Computes turn-by-turn route legs from Entry Dock $\to$ Item Bays $\to$ Packaging Bay.
- 🤖 **Interactive Web Dashboard:** Modern dark-mode UI with an HTML5 Canvas floor plan and real-time animated AGV picker robot.
- 📊 **Interactive 2D DP Matrix Viewer:** Visual representation of subproblem states for academic viva demonstrations.
- 📈 **Automated Matplotlib Analytics:** Generates comparative bar charts for packed vs. skipped cargo and leg distances.

---

## 📊 Sample Benchmark Results

Using a standard manifest of 8 candidate packages and a **45 kg cart capacity**:

* **Knapsack Optimization:**
  * **Payload Used:** 44 kg / 45 kg (**97.8% utilization**)
  * **Optimized Order Value:** **$4,550** (5 items selected, 3 heavy/low-value items skipped)
* **Dijkstra Route Navigation:**
  * **Sequence:** $\text{Entry\_Dock} \xrightarrow{25\text{m}} \text{Aisle\_B} \xrightarrow{15\text{m}} \text{Aisle\_D} \xrightarrow{18\text{m}} \text{Cold\_Storage} \xrightarrow{12\text{m}} \text{Aisle\_C} \xrightarrow{25\text{m}} \text{Packaging\_Bay}$
  * **Total Distance:** **95 meters** (vs. 175 meters naive traversal &rarr; **45.7% distance saved**)

---

## 🚀 Quick Start & Usage

### 1. Run the Python CLI Tool
```bash
python warehouse_inventory_system.py
