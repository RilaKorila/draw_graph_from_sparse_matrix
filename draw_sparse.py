import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from scipy.sparse import dok_matrix


def draw_graph(S):
    adj_matrix = S
    num_nodes =  S.shape[0]
    for i in range(num_nodes):
        for j in range(num_nodes):
            if i != j and np.random.rand() < density:
                adj_matrix[i, j] = 1

    # NetworkXグラフを作成
    G = nx.Graph()

    # dok_matrixから隣接情報をNetworkXグラフに追加
    for i, j in adj_matrix.keys():
        G.add_edge(i, j)

    # グラフを描画
    pos = nx.spring_layout(G)  # グラフの配置を計算
    nx.draw(G, pos, with_labels=True, node_size=500, font_size=10, font_color='black')

    plt.title("Visualization of Sparse Adjacency Matrix")
    plt.show()