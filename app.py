# =========================================================
# Karachi OSM Pathfinding App
# =========================================================

import streamlit as st
import osmnx as ox
import folium
from streamlit_folium import st_folium

from map_loader import load_karachi_graph
from algorithms import bfs, dfs, astar

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="Karachi OSM Pathfinding",
    page_icon="🌆",
    layout="wide"
)

# =========================================================
# LOAD GRAPH
# =========================================================
G = load_karachi_graph()

# =========================================================
# TITLE
# =========================================================
st.title("🌆 Karachi Pathfinding using OpenStreetMap")
st.markdown("### BFS | DFS | A* Algorithms")

# =========================================================
# SIDEBAR
# =========================================================
st.sidebar.header("⚙️ Controls")

algorithm = st.sidebar.selectbox(
    "Select Algorithm",
    ["A*", "BFS", "DFS"]
)

st.sidebar.markdown("""
### Instructions
1. Click Start Point  
2. Click Goal Point  
3. Click Find Path
""")

# =========================================================
# SESSION STATE
# =========================================================
if "start" not in st.session_state:
    st.session_state.start = None

if "goal" not in st.session_state:
    st.session_state.goal = None

if "path" not in st.session_state:
    st.session_state.path = None

# =========================================================
# CREATE MAP
# =========================================================
m = folium.Map(
    location=[24.8607, 67.0011],
    zoom_start=12
)

# =========================================================
# START MARKER
# =========================================================
if st.session_state.start:

    folium.Marker(
        st.session_state.start,
        tooltip="Start",
        icon=folium.Icon(color="green")
    ).add_to(m)

# =========================================================
# GOAL MARKER
# =========================================================
if st.session_state.goal:

    folium.Marker(
        st.session_state.goal,
        tooltip="Goal",
        icon=folium.Icon(color="red")
    ).add_to(m)

# =========================================================
# DRAW ROUTE
# =========================================================
if st.session_state.path:

    route_coords = []

    for node in st.session_state.path:

        lat = G.nodes[node]["y"]
        lon = G.nodes[node]["x"]

        route_coords.append((lat, lon))

    folium.PolyLine(
        route_coords,
        color="blue",
        weight=5,
        opacity=0.8
    ).add_to(m)

# =========================================================
# RENDER MAP
# =========================================================
map_data = st_folium(
    m,
    width=1200,
    height=600
)

# =========================================================
# HANDLE MAP CLICKS
# =========================================================
if map_data and map_data.get("last_clicked"):

    lat = map_data["last_clicked"]["lat"]
    lon = map_data["last_clicked"]["lng"]

    # Start Point
    if st.session_state.start is None:

        st.session_state.start = (lat, lon)

        st.success(
            f"✅ Start Selected: {lat:.4f}, {lon:.4f}"
        )

        st.rerun()

    # Goal Point
    elif st.session_state.goal is None:

        st.session_state.goal = (lat, lon)

        st.success(
            f"✅ Goal Selected: {lat:.4f}, {lon:.4f}"
        )

        st.rerun()

# =========================================================
# FIND PATH
# =========================================================
if st.sidebar.button(
    "🚀 Find Path",
    use_container_width=True
):

    if (
        st.session_state.start is None
        or st.session_state.goal is None
    ):

        st.error("❌ Please select both points.")

    else:

        try:

            # =============================================
            # NEAREST NODES
            # =============================================
            start_node = ox.distance.nearest_nodes(
                G,
                X=st.session_state.start[1],
                Y=st.session_state.start[0]
            )

            goal_node = ox.distance.nearest_nodes(
                G,
                X=st.session_state.goal[1],
                Y=st.session_state.goal[0]
            )

            # =============================================
            # RUN ALGORITHM
            # =============================================
            with st.spinner(
                f"Running {algorithm}..."
            ):

                if algorithm == "BFS":

                    path = bfs(
                        G,
                        start_node,
                        goal_node
                    )

                elif algorithm == "DFS":

                    path = dfs(
                        G,
                        start_node,
                        goal_node
                    )

                else:

                    path = astar(
                        G,
                        start_node,
                        goal_node
                    )

            # =============================================
            # CHECK RESULT
            # =============================================
            if path is None:

                st.error(
                    f"{algorithm} could not find route."
                )

            else:

                st.session_state.path = path

                st.success(
                    f"{algorithm} Route Found!"
                )

                st.rerun()

        except Exception as e:

            st.error(f"Error: {e}")

# =========================================================
# ROUTE INFORMATION
# =========================================================
if st.session_state.path:

    total_distance = 0

    for u, v in zip(
        st.session_state.path[:-1],  
        st.session_state.path[1:] 
    ):

        edge_data = G.get_edge_data(u, v)

        if edge_data:

            edge = list(
                edge_data.values()
            )[0]

            total_distance += edge.get(
                "length",
                0
            )

    # Distance in KM
    distance_km = total_distance / 1000

    # Estimated Time
    avg_speed = 40

    estimated_time = (
        distance_km / avg_speed
    ) * 60

    st.subheader("📍 Route Information")

    col1, col2 = st.columns(2)

    col1.metric(
        "🛣️ Distance (km)",
        f"{distance_km:.2f}"
    )

    col2.metric(
        "⏱️ Estimated Time (minutes)",
        f"{estimated_time:.1f}"
    )

# =========================================================
# RESET BUTTON
# =========================================================
if st.sidebar.button(
    "🔄 Reset",
    use_container_width=True
):

    st.session_state.start = None
    st.session_state.goal = None
    st.session_state.path = None

    st.rerun()