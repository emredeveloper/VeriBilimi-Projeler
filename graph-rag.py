import networkx as nx
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# 2. Metin Kodlayıcı
model = SentenceTransformer('all-MiniLM-L6-v2')

# 3. Düğüm Kodlama
def encode_nodes(G, model):
    node_texts = [str(node) for node in G.nodes()]
    embeddings = model.encode(node_texts)
    for node, embedding in zip(G.nodes(), embeddings):
        G.nodes[node]['embedding'] = embedding
    return G

# 4. Alt Graf Çıkarma
def extract_subgraph(G, query, top_k=5):  # top_k değerini artırdık
    query_embedding = model.encode(query)
    similarities = {
        node: cosine_similarity([query_embedding], [G.nodes[node]['embedding']])[0][0]
        for node in G.nodes() if 'embedding' in G.nodes[node]
    }
    
    relevant_nodes = sorted(similarities, key=similarities.get, reverse=True)[:top_k]
    subgraph = G.subgraph(relevant_nodes)
    return subgraph

# 5. Graf Kodlama
def encode_graph(G):
    embeddings = np.array([G.nodes[node]['embedding'] for node in G.nodes() if 'embedding' in G.nodes[node]])
    return np.mean(embeddings, axis=0) if embeddings.size else np.zeros(model.get_sentence_embedding_dimension())

# 6. Yanıt Üretimi
def generate_response(subgraph, query):
    response = f"'{query}' sorgusuyla ilgili bilgiler:\n"
    for node in subgraph.nodes():
        response += f"\n{node}:\n"
        for neighbor in subgraph.neighbors(node):
            edge_data = subgraph[node][neighbor]
            response += f"  - {edge_data['relation']} {neighbor}\n"
    return response

# GraphRAG ana fonksiyonu
def graphrag(query):
    # 1. Graf Oluşturma
    G = nx.Graph()
    G.add_edge("Türkiye", "İstanbul", relation="şehri")
    G.add_edge("Türkiye", "Ankara", relation="başkenti")
    G.add_edge("İstanbul", "Boğaziçi Köprüsü", relation="landmark")
    G.add_edge("İstanbul", "15 milyon", relation="nüfus")
    G.add_edge("Ankara", "5.6 milyon", relation="nüfus")

    G = encode_nodes(G, model)  # Düğümleri kodla
    subgraph = extract_subgraph(G, query)
    graph_embedding = encode_graph(subgraph)
    response = generate_response(subgraph, query)
    return response, graph_embedding

# Örnek kullanım
query = "İstanbul ve Ankara"
result, embedding = graphrag(query)
print(result)
print(f"\nSorgu embedding boyutu: {len(embedding)}")

import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
G = nx.Graph()

# Add nodes
G.add_node("A")
G.add_node("B")
G.add_node("C")

# Add edges
G.add_edge("A", "B")
G.add_edge("B", "C")
G.add_edge("C", "A")

# Print graph information
print("Nodes:", G.nodes()) # Nodes nedir : düğümler
print("Edges:", G.edges()) # Edge nedir : düğümler arasındaki bağlantılar

# Draw the graph
nx.draw(G, with_labels=True)
plt.show()
