import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from scipy.sparse import dok_matrix


def draw_graph(S):
    adj_matrix = S

    # NetworkXグラフを作成
    G = nx.Graph()

    # dok_matrixから隣接情報をNetworkXグラフに追加
    for i, j in adj_matrix.keys():
        if i < j:
            G.add_edge(i, j)

    # グラフを描画
    pos = nx.spring_layout(G)  # グラフの配置を計算
    nx.draw(G, pos, node_size=5)

    plt.title("Visualization of Sparse Adjacency Matrix")
    plt.show()
