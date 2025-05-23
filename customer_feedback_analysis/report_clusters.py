import json
from collections import defaultdict

def main():
    """
    Loads analyzed feedback, groups it by theme, and prints a report.
    """
    input_filepath = "clustered_feedback_analyzed.json"

    # 1. Load the analyzed feedback data
    try:
        with open(input_filepath, 'r') as f:
            analyzed_feedback_list = json.load(f)
        print(f"Successfully loaded {len(analyzed_feedback_list)} analyzed feedback items from {input_filepath}\n")
    except FileNotFoundError:
        print(f"Error: The file {input_filepath} was not found.")
        return
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {input_filepath}. Ensure it's a valid JSON file.")
        return
    except Exception as e:
        print(f"An unexpected error occurred while reading {input_filepath}: {e}")
        return

    # Validate loaded data
    if not isinstance(analyzed_feedback_list, list):
        print(f"Error: Expected {input_filepath} to contain a list. Found {type(analyzed_feedback_list)}.")
        return
    
    if not analyzed_feedback_list:
        print(f"Warning: The file {input_filepath} is empty. No report to generate.")
        return

    # 2. Group feedback items by 'theme_label'
    grouped_by_theme = defaultdict(list)
    valid_items = 0
    for i, item in enumerate(analyzed_feedback_list):
        if not isinstance(item, dict):
            print(f"Warning: Item at index {i} is not a dictionary, skipping.")
            continue
        
        theme_label = item.get('theme_label')
        feedback_text = item.get('feedback_text')

        if theme_label is None or feedback_text is None:
            print(f"Warning: Item at index {i} is missing 'theme_label' or 'feedback_text', skipping: {item}")
            continue
        
        if not isinstance(theme_label, str) or not isinstance(feedback_text, str):
            print(f"Warning: 'theme_label' or 'feedback_text' for item at index {i} are not strings, skipping: {item}")
            continue
            
        grouped_by_theme[theme_label].append(feedback_text)
        valid_items += 1
    
    if valid_items == 0 and analyzed_feedback_list: # If there were items, but none were valid
        print("No valid feedback items found after parsing. Ensure items have 'theme_label' and 'feedback_text'.")
        return
    if not grouped_by_theme: # If no items were grouped (e.g. all items were invalid)
        print("No themes found to report.")
        return


    # 3. Print the report
    print("--- Customer Feedback Report by Theme ---")
    
    # Sort themes for consistent output order, e.g., alphabetically
    sorted_themes = sorted(grouped_by_theme.keys())

    for theme in sorted_themes:
        feedback_items = grouped_by_theme[theme]
        print(f"\nTheme: {theme}")
        print(f"Count: {len(feedback_items)}")
        print("Feedback:")
        for i, text in enumerate(feedback_items):
            print(f"  - \"{text}\"")
        print("\n" + "="*50) # Separator line

    print("\n--- End of Report ---")

if __name__ == "__main__":
    main()
