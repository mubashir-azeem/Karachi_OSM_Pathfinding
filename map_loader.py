import os
import osmnx as ox
import streamlit as st

# =========================================================
# GRAPH FILE
# =========================================================
GRAPH_FILENAME = "data/karachi_drive.graphml"

# =========================================================
# LOAD KARACHI GRAPH
# =========================================================
@st.cache_resource
def load_karachi_graph():

    # -----------------------------------------------------
    # LOAD EXISTING GRAPH
    # -----------------------------------------------------
    if os.path.exists(GRAPH_FILENAME):

        print("Loading graph from disk...")

        G = ox.load_graphml(
            GRAPH_FILENAME
        )

    # -----------------------------------------------------
    # DOWNLOAD GRAPH
    # -----------------------------------------------------
    else:

        print("Downloading Karachi graph...")

        G = ox.graph_from_place(
            "Karachi, Pakistan",
            network_type="drive",
            simplify=True
        )

        print("Saving graph...")

        ox.save_graphml(
            G,
            GRAPH_FILENAME
        )

    return G
