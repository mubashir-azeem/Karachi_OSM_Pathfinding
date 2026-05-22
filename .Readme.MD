# 🌆 Karachi OSM Pathfinding using BFS, DFS and A*

An AI-based pathfinding system that finds routes on Karachi road network using BFS, DFS, and A* algorithms with real-world OpenStreetMap data.

---

## 🚀 Project Overview

This project allows users to:
- Select source and destination points directly on Karachi map
- Apply BFS, DFS, and A* pathfinding algorithms
- Visualize routes on an interactive map
- Calculate distance and estimated travel time

The project demonstrates practical implementation of:
- Graph Theory
- Artificial Intelligence Search Algorithms
- Real-world Navigation Systems

---

## 🧠 Features

- Interactive Karachi map
- BFS pathfinding
- DFS pathfinding
- A* shortest path routing
- Real-time route visualization
- Distance calculation
- Estimated travel time
- Interactive Streamlit interface

---

## ⚙️ Technologies Used

- Python
- Streamlit
- OSMnx
- NetworkX
- Folium
- Streamlit-Folium
- OpenStreetMap

---

## 🧩 How It Works

1. Karachi road network is downloaded using OpenStreetMap
2. Roads are converted into graph structure
3. User selects source and destination points
4. Coordinates are converted into nearest graph nodes
5. Selected algorithm runs on the graph
6. Route is displayed on the map
7. Distance and estimated time are calculated

---

## 🗺️ Algorithms Used

### BFS (Breadth First Search)
- Explores graph level-by-level
- Finds shortest path in unweighted graphs
- Slower on large maps

### DFS (Depth First Search)
- Explores deeply before backtracking
- Useful for graph traversal
- Does not always generate shortest route

### A* Algorithm
- Heuristic-based pathfinding
- Fast and optimized routing
- Best suited for navigation systems

---

## 📊 Project Structure

```plaintext
Karachi_OSM_Pathfinding/
│
├── app.py
├── algorithms.py
├── map_loader.py
├── download_graph.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── report/
│   └── Karachi_OSM_Pathfinding_Report.pdf
│
├── screenshots/
│   ├── astar.jpg
│   ├── bfs.jpg
│   ├── dfs.jpg
│   ├── home.jpg
│   └── route.jpg
│
└── demo/
    └── demo.mp4
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone http://github.com/mubashir-azeem/Karachi_OSM_Pathfinding
```

### 2. Navigate to the project folder

```bash
cd Karachi_OSM_Pathfinding
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Download Karachi graph

```bash
python download_graph.py
```

### 5. Run the project

```bash
streamlit run app.py
```

---

## 📸 Screenshots

### Home Interface

![Home](screenshots/home.jpg)

---

### Route Visualization

![Route](screenshots/route.jpg)

---

### BFS Output

![BFS](screenshots/bfs.jpg)

---

### DFS Output

![DFS](screenshots/dfs.jpg)

---

### A* Output

![A Star](screenshots/astar.jpg)

---

## 📄 Project Report

The complete project report is available inside the `report/` folder.

---

## 🎯 Key Learning

This project demonstrates how Artificial Intelligence, Graph Theory, and OpenStreetMap data can be integrated to build real-world navigation and pathfinding systems.

---

## 🔗 Repository Link

GitHub Repository:

http://github.com/mubashir-azeem/Karachi_OSM_Pathfinding

---

## 👨‍💻 Author

Developed by Mubashir Azeem Abbasi
