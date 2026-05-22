import os
import osmnx as ox

# =========================================================
# CREATE DATA FOLDER
# =========================================================
os.makedirs("data", exist_ok=True)

# =========================================================
# GRAPH FILE PATH
# =========================================================
GRAPH_FILE = "data/karachi_drive.graphml"

# =========================================================
# CHECK IF FILE EXISTS
# =========================================================
if os.path.exists(GRAPH_FILE):

    print("Graph file already exists.")

else:

    print("Downloading Karachi road network...")

    # Download Karachi road network
    G = ox.graph_from_place(
        "Karachi, Pakistan",
        network_type="drive",
        simplify=True
    )

    print("Saving graph file...")

    # Save graph locally
    ox.save_graphml(
        G,
        GRAPH_FILE
    )

    print("Graph downloaded successfully!")

print("DONE!")