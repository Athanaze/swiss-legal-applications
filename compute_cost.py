'''
This script calculates the cost to embed data for further use in a Retrieval-Augmented Generation (RAG) system.
It reads a list of data items, processes each file associated with the items, and computes the total number of tokens.
Finally, it estimates the cost based on a predefined cost per million tokens.
'''
import tiktoken
import json
import os

enc = tiktoken.get_encoding("cl100k_base")

# Initialize total token counter
total_t = 0

# Read the global list of items from a JSON file
with open("global_dl_list.json") as f:
    data = json.load(f)

# Iterate over each item in the list
for item in data:
    # Retrieve the UUID of the item to construct the file path
    uuid = item["uuid"]
    file_path = os.path.join("xml_laws", f"{uuid}.xml")
    
    # Read the content of the file
    with open(file_path, "r") as file:
        string = file.read()
        
        # Encode the file content to count the number of tokens
        t = len(enc.encode(string))
        
        # Accumulate the total tokens
        total_t += t

# Define the cost per million tokens
COST_PER_1M_TOKEN = 0.13

# Calculate the total number of tokens and corresponding cost
n_tokens = total_t
cost_usd = COST_PER_1M_TOKEN * (n_tokens / 1000000)

# Output the total number of tokens and estimated cost in USD
print(f"N TOKENS {n_tokens}\nPRICE USD {cost_usd}")
