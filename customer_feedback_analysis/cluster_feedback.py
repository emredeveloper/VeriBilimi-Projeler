import numpy as np
from sklearn.cluster import KMeans

def main():
    """
    Loads embeddings, performs K-Means clustering, and saves cluster labels.
    """
    embeddings_filepath = "feedback_embeddings.npy"
    labels_filepath = "cluster_labels.npy"
    n_clusters = 4  # As specified: 4 themes
    random_state = 42 # For reproducibility

    # 1. Load the embeddings from feedback_embeddings.npy
    try:
        embeddings = np.load(embeddings_filepath)
        print(f"Successfully loaded embeddings from {embeddings_filepath}. Shape: {embeddings.shape}")
    except FileNotFoundError:
        print(f"Error: The file {embeddings_filepath} was not found.")
        return
    except Exception as e:
        print(f"An unexpected error occurred while reading {embeddings_filepath}: {e}")
        return

    # Validate embeddings
    if embeddings.ndim != 2:
        print(f"Error: Embeddings are not a 2D array. Shape is {embeddings.shape}.")
        return
    if embeddings.shape[0] == 0:
        print(f"Error: Embeddings file {embeddings_filepath} is empty. Cannot perform clustering.")
        # Save empty labels for consistency if other scripts expect this file
        np.save(labels_filepath, np.array([]))
        print(f"Saved empty labels to {labels_filepath}.")
        return
    if embeddings.shape[0] < n_clusters:
        print(f"Error: Number of samples ({embeddings.shape[0]}) is less than number of clusters ({n_clusters}).")
        # Optionally, still save labels if that's desired (e.g., all as -1 or similar)
        # For now, just returning. Or one could assign all to cluster 0 or handle as per requirements.
        return


    # 2. Perform K-Means clustering
    try:
        print(f"Performing K-Means clustering with n_clusters={n_clusters} and random_state={random_state}...")
        kmeans = KMeans(n_clusters=n_clusters, random_state=random_state, n_init='auto')
        kmeans.fit(embeddings)
        cluster_labels = kmeans.labels_
        print("K-Means clustering complete.")
    except Exception as e:
        print(f"An error occurred during K-Means clustering: {e}")
        return

    # 3. Save the resulting cluster labels
    try:
        np.save(labels_filepath, cluster_labels)
        print(f"Cluster labels saved to {labels_filepath}")
    except Exception as e:
        print(f"Error saving cluster labels to {labels_filepath}: {e}")
        return

    # 4. Print unique cluster labels and counts
    unique_labels, counts = np.unique(cluster_labels, return_counts=True)
    print("Cluster analysis:")
    print(f"  Unique labels: {unique_labels}")
    print(f"  Counts per cluster: {counts}")
    for label, count in zip(unique_labels, counts):
        print(f"  Cluster {label}: {count} items")

if __name__ == "__main__":
    main()
