import json
import numpy as np
from collections import defaultdict

def main():
    feedback_filepath = "sample_feedback.json"
    labels_filepath = "cluster_labels.npy"
    output_filepath = "clustered_feedback_analyzed.json"
    num_samples_to_print = 4 # Number of feedback samples to print per cluster

    # 1. Load feedback strings
    try:
        with open(feedback_filepath, 'r') as f:
            feedback_strings = json.load(f)
        print(f"Successfully loaded {len(feedback_strings)} feedback strings from {feedback_filepath}")
    except FileNotFoundError:
        print(f"Error: The file {feedback_filepath} was not found.")
        return
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {feedback_filepath}.")
        return
    except Exception as e:
        print(f"An unexpected error occurred while reading {feedback_filepath}: {e}")
        return

    # 2. Load cluster labels
    try:
        cluster_labels = np.load(labels_filepath)
        print(f"Successfully loaded {len(cluster_labels)} cluster labels from {labels_filepath}")
    except FileNotFoundError:
        print(f"Error: The file {labels_filepath} was not found.")
        return
    except Exception as e: # numpy.load can raise various errors, including ValueError for malformed files
        print(f"An unexpected error occurred while reading {labels_filepath}: {e}")
        return

    # Validate inputs
    if not isinstance(feedback_strings, list) or not all(isinstance(item, str) for item in feedback_strings):
        print(f"Error: Expected {feedback_filepath} to contain a list of strings.")
        return
    if not isinstance(cluster_labels, np.ndarray) or not np.issubdtype(cluster_labels.dtype, np.integer):
        print(f"Error: Expected {labels_filepath} to contain a NumPy array of integers.")
        return
    if len(feedback_strings) != len(cluster_labels):
        print(f"Error: Mismatch in length between feedback strings ({len(feedback_strings)}) and cluster labels ({len(cluster_labels)}).")
        return
    
    if not feedback_strings:
        print("Warning: Feedback file is empty. No analysis will be performed.")
        # Create an empty JSON file for consistency
        with open(output_filepath, 'w') as f:
            json.dump([], f)
        print(f"Saved empty list to {output_filepath}")
        return

    # Group feedback by cluster ID for theme analysis
    grouped_feedback = defaultdict(list)
    for feedback, label in zip(feedback_strings, cluster_labels):
        grouped_feedback[label].append(feedback)

    print("\n--- Sample Feedback per Cluster (for manual theme mapping) ---")
    for cluster_id, texts in sorted(grouped_feedback.items()):
        print(f"\nCluster {cluster_id}:")
        for i, text in enumerate(texts[:num_samples_to_print]):
            print(f"  Sample {i+1}: {text}")
    print("\n------------------------------------------------------------")

    # 3. Manually define this map after observing the output above.
    # This is a placeholder. The actual mapping will be determined by inspecting the output.
    cluster_to_theme_map = {
        0: "New Feature Suggestions",
        1: "Customer Support Complaints",
        2: "Pricing Plan Questions",
        3: "Positive Product Usability"
        # Add more if there are more clusters, or adjust based on actual cluster IDs found
    }
    
    # Ensure all found cluster IDs are in the map, if not, assign a default
    unique_cluster_ids = np.unique(cluster_labels)
    for cid in unique_cluster_ids:
        if cid not in cluster_to_theme_map:
            print(f"Warning: Cluster ID {cid} found in labels but not in cluster_to_theme_map. Assigning default theme.")
            cluster_to_theme_map[cid] = f"Unmapped Theme for Cluster {cid}"


    predefined_themes = [
        "Positive Product Usability",
        "Customer Support Complaints",
        "Pricing Plan Questions",
        "New Feature Suggestions"
    ]
    print(f"\nPredefined themes for mapping: {predefined_themes}")
    print("Please update 'cluster_to_theme_map' in the script based on the samples.")


    # 4. Create the list of dictionaries
    analyzed_feedback_list = []
    for feedback, label in zip(feedback_strings, cluster_labels):
        theme_label = cluster_to_theme_map.get(label, "Unknown Theme") # Default if label not in map
        analyzed_feedback_list.append({
            'feedback_text': feedback,
            'cluster_id': int(label), # Ensure label is native int for JSON
            'theme_label': theme_label
        })

    # 5. Save to JSON
    try:
        with open(output_filepath, 'w') as f:
            json.dump(analyzed_feedback_list, f, indent=2)
        print(f"\nAnalyzed feedback saved to {output_filepath}")
    except Exception as e:
        print(f"An error occurred while saving to {output_filepath}: {e}")
        return

    # 6. Print the first 5 entries for verification
    try:
        with open(output_filepath, 'r') as f:
            first_five = json.load(f)[:5]
        print(f"\nFirst 5 entries from {output_filepath}:")
        for i, entry in enumerate(first_five):
            print(f" Entry {i+1}: {entry}")
    except Exception as e:
        print(f"An error occurred while reading back and printing {output_filepath}: {e}")

if __name__ == "__main__":
    main()
