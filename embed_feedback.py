import json
import numpy as np
from sentence_transformers import SentenceTransformer

def main():
    """
    Loads feedback, generates embeddings, and saves them.
    """
    feedback_filepath = "sample_feedback.json"
    embeddings_filepath = "feedback_embeddings.npy"
    model_name = 'all-MiniLM-L6-v2'

    # 1. Load the list of feedback strings from sample_feedback.json
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

    if not isinstance(feedback_strings, list) or not all(isinstance(item, str) for item in feedback_strings):
        print(f"Error: Expected {feedback_filepath} to contain a list of strings.")
        return
    
    if not feedback_strings:
        print(f"Warning: {feedback_filepath} is empty or contains no feedback strings. No embeddings will be generated.")
        # Create an empty npy file for consistency if needed, or just return
        empty_embeddings = np.array([])
        np.save(embeddings_filepath, empty_embeddings)
        print(f"Saved empty embeddings to {embeddings_filepath}. Shape: {empty_embeddings.shape}")
        return

    # 2. Initialize the SentenceTransformer model
    try:
        print(f"Initializing model: {model_name}...")
        model = SentenceTransformer(model_name)
        print("Model initialized successfully.")
    except Exception as e:
        print(f"Error initializing SentenceTransformer model: {e}")
        return

    # 3. Encode the feedback strings into embeddings
    try:
        print("Encoding feedback strings...")
        embeddings = model.encode(feedback_strings, show_progress_bar=True)
        print("Encoding complete.")
    except Exception as e:
        print(f"Error encoding feedback strings: {e}")
        return

    # Ensure embeddings is a NumPy array (it should be by default from encode)
    if not isinstance(embeddings, np.ndarray):
        embeddings_array = np.array(embeddings)
    else:
        embeddings_array = embeddings

    # 4. Save the resulting embeddings as a NumPy array
    try:
        np.save(embeddings_filepath, embeddings_array)
        print(f"Embeddings saved to {embeddings_filepath}")
    except Exception as e:
        print(f"Error saving embeddings to {embeddings_filepath}: {e}")
        return

    # 5. Print the shape of the embeddings array
    print(f"Shape of the embeddings array: {embeddings_array.shape}")

if __name__ == "__main__":
    main()
