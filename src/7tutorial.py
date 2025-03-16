import networkx as nx
from collections import deque
import matplotlib.pyplot as plt  # Impor modul matplotlib.pyplot

def create_graph(edges: list[tuple[int, int]]) -> nx.Graph:
    """
    Membuat graf tidak berarah berdasarkan daftar sisi yang diberikan.

    Parameter:
    edges (list of tuple[int, int]): Daftar sisi yang menghubungkan dua simpul.

    Output:
    nx.Graph: Objek graf dari networkx.
    """
    graph = nx.Graph()
    graph.add_edges_from(edges)
    return graph

def get_degree(G: nx.Graph, node: int) -> int:
    """
    Menghitung derajat dari simpul tertentu.

    Parameter:
    G (nx.Graph): Graf yang telah dibuat.
    node (int): Simpul yang ingin dihitung derajatnya.

    Output:
    int: Derajat dari simpul tersebut.
    """
    if node in G:
        return G.degree[node]
    else:
        raise ValueError(f"Simpul {node} tidak ada dalam graf.")

def dfs_traversal(G: nx.Graph, start: int) -> list[int]:
    """
    Melakukan pencarian secara Depth-First Search (DFS) mulai dari simpul tertentu.

    Parameter:
    G (nx.Graph): Graf yang telah dibuat.
    start (int): Simpul awal.

    Output:
    list[int]: Urutan traversal berdasarkan DFS.
    """
    visited = set()
    traversal_order = []

    def dfs(node):
        visited.add(node)
        traversal_order.append(node)
        for neighbor in G.neighbors(node):
            if neighbor not in visited:
                dfs(neighbor)

    dfs(start)
    return traversal_order

def bfs_traversal(G: nx.Graph, start: int) -> list[int]:
    """
    Melakukan pencarian secara Breadth-First Search (BFS) mulai dari simpul tertentu.

    Parameter:
    G (nx.Graph): Graf yang telah dibuat.
    start (int): Simpul awal.

    Output:
    list[int]: Urutan traversal berdasarkan BFS.
    """
    visited = set()
    traversal_order = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            traversal_order.append(node)
            for neighbor in G.neighbors(node):
                if neighbor not in visited:
                    queue.append(neighbor)

    return traversal_order

def find_shortest_path(G: nx.Graph, source: int, target: int) -> list[int]:
    """
    Mencari jalur terpendek antara dua simpul dalam graf.

    Parameter:
    G (nx.Graph): Graf yang telah dibuat.
    source (int): Simpul awal.
    target (int): Simpul tujuan.

    Output:
    list[int]: Urutan simpul yang membentuk jalur terpendek dari source ke target.
    """
    try:
        path = nx.shortest_path(G, source=source, target=target)
        return path
    except nx.NetworkXNoPath:
        return []
    except nx.NodeNotFound as e:
        raise ValueError(f"Simpul tidak ditemukan: {e}")

def visualize_graph(G: nx.Graph) -> None:
    """
    Memvisualisasikan graf menggunakan matplotlib.

    Parameter:
    G (nx.Graph): Graf yang telah dibuat.

    Output:
    Tidak ada (hanya menampilkan visualisasi graf).
    """
    plt.figure(figsize=(8, 6))  # Ukuran gambar
    pos = nx.spring_layout(G)  # Mengatur posisi simpul
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=15, font_color='black', font_weight='bold', edge_color='gray')
    plt.title("Visualisasi Graf")
    plt.savefig("graph_visualization.png")  # Menyimpan visualisasi ke file .png
    plt.show()  # Menampilkan graf

def test_functions():
    """
    Fungsi untuk menguji semua fungsi yang telah dibuat.
    """
    # Membuat graf contoh
    edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (3, 4)]
    graph = create_graph(edges)

    # Menampilkan informasi graf
    print("Nodes:", graph.nodes())
    print("Edges:", graph.edges())

    # Menguji fungsi get_degree
    node = 1
    degree = get_degree(graph, node)
    print(f"Derajat dari simpul {node} adalah: {degree}")

    # Menguji fungsi dfs_traversal
    start_node = 0
    dfs_result = dfs_traversal(graph, start_node)
    print(f"Urutan traversal DFS mulai dari simpul {start_node}: {dfs_result}")

    # Menguji fungsi bfs_traversal
    bfs_result = bfs_traversal(graph, start_node)
    print(f"Urutan traversal BFS mulai dari simpul {start_node}: {bfs_result}")

    # Menguji fungsi find_shortest_path
    source_node = 0
    target_node = 4
    shortest_path = find_shortest_path(graph, source_node, target_node)
    print(f"Jalur terpendek dari simpul {source_node} ke {target_node}: {shortest_path}")

    # Menguji fungsi visualize_graph
    visualize_graph(graph)

# Jalankan fungsi uji
if __name__ == "__main__":
    test_functions()