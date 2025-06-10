import json

# Load the JSON data
with open('metadata_scheme_Delta_Enigma-1/keywords/extracted_keywords.json', 'r') as file:
    keywords = json.load(file)

# Create dictionaries to store P08 and P03 keywords
p08_keywords = {}
p03_keywords = {}

# First pass: collect all P08 and P03 keywords
for keyword in keywords:
    identifier = keyword["identifier"]
    if identifier.startswith("SDN:P08::"):
        p08_keywords[identifier.split("::")[1]] = keyword["prefLabel"]
    elif identifier.startswith("SDN:P03::"):
        p03_id = identifier.split("::")[1]
        p03_keywords[p03_id] = {
            "prefLabel": keyword["prefLabel"],
            "p08_broader": keyword["p08_broader"],
            "deprecated": keyword["deprecated"]
        }

# Second pass: create the formatted list
formatted_keywords = []

for p03_id, p03_data in p03_keywords.items():
    # Skip deprecated keywords
    if p03_data["deprecated"]:
        continue
    
    # Get the P08 broader terms
    p08_broader = p03_data["p08_broader"]
    
    # If there are no P08 broader terms, skip or handle as needed
    if not p08_broader:
        # You could add a special case here if needed
        # For example: formatted_keywords.append(f"No P08>{p03_data['prefLabel']}")
        continue
    
    # For each P08 broader term, create an entry
    for p08_id in p08_broader:
        if p08_id in p08_keywords:
            p08_label = p08_keywords[p08_id]
            # Remove the square brackets from the formatted entry
            formatted_entry = f"{p08_label}>{p03_data['prefLabel']}"
            formatted_keywords.append(formatted_entry)

# Sort the list alphabetically
formatted_keywords.sort()

# Print the formatted list
print("[" + ", ".join(f'"{keyword}"' for keyword in formatted_keywords) + "]")

# Optionally, save to a file
with open('formatted_keywords.json', 'w') as outfile:
    json.dump(formatted_keywords, outfile, indent=2)

print(f"Generated {len(formatted_keywords)} keyword entries") 