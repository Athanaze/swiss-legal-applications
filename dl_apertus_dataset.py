import json
import os
from datasets import load_dataset
from tqdm import tqdm

# --- Configuration ---
DATASET_NAME = "swiss-ai/apertus-pretrain-swiss"
SUBSTRING_TO_FILTER = "entscheidsuche_html"
COLUMN_TO_CHECK = "id"
OUTPUT_FILENAME = "filtered_apertus_pretrain_swiss.jsonl"


def filter_function(example):
    """
    Returns True to keep the example, False to discard it.
    We keep the row only if the substring is NOT in the 'id' column.
    """
    return (SUBSTRING_TO_FILTER not in example[COLUMN_TO_CHECK]) and ("fineweb" not in example[COLUMN_TO_CHECK]) and ("This text was translated from" not in example["text"]) and ("This is a text translated from" not in example["text"])

def main():
    """
    Streams, filters, and saves the dataset to a local file.
    """
    print(f"Starting dataset processing...")
    print(f"  - Dataset: {DATASET_NAME}")
    print(f"  - Filtering out rows where '{COLUMN_TO_CHECK}' contains '{SUBSTRING_TO_FILTER}'")
    print(f"  - Output will be saved to: {OUTPUT_FILENAME}\n")

    # Check if the output file already exists to avoid accidental overwrites.
    if os.path.exists(OUTPUT_FILENAME):
        print(f"Warning: Output file '{OUTPUT_FILENAME}' already exists and will be overwritten.")
        input("Press Enter to continue or Ctrl+C to cancel...")

    # 1. Load the dataset in streaming mode to avoid downloading it all at once.
    try:
        streamed_dataset = load_dataset(DATASET_NAME, streaming=True, split="train")
    except Exception as e:
        print(f"Error: Failed to load dataset. Please check your internet connection and dataset name.")
        print(f"Details: {e}")
        return

    # 2. Apply the filter. This is a lazy operation and doesn't process any data yet.
    filtered_stream = streamed_dataset.filter(filter_function)

    # 3. Iterate through the filtered stream and write each item to the file.
    # This processes one item at a time, ensuring low memory usage.
    print("Processing and writing data to file...")
    items_written = 0
    try:
        with open(OUTPUT_FILENAME, "w", encoding="utf-8") as f:
            # Use tqdm for a progress bar. Since it's a stream, it won't show a total,
            # but it will show the number of items processed and the processing rate.
            for example in tqdm(filtered_stream, desc="Writing to file"):
                # Convert the dictionary to a JSON string
                json_line = json.dumps(example, ensure_ascii=False)
                # Write the JSON string followed by a newline character
                f.write(json_line + '\n')
                items_written += 1
                
    except KeyboardInterrupt:
        print("\nProcess interrupted by user. Partially saved file is available.")
    except Exception as e:
        print(f"\nAn error occurred during processing: {e}")
        
    print("\n---------------------------------")
    print("         Processing Complete         ")
    print("---------------------------------")
    print(f"Total items written: {items_written}")
    print(f"Filtered dataset saved to '{OUTPUT_FILENAME}'")

if __name__ == "__main__":
    main()
