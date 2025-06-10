#!/usr/bin/env python3
import json
import os

# Path to the p03.json file
p03_file = "metadata_scheme_Delta_Enigma-1/keywords/p03.json"

# Load the JSON data
with open(p03_file, 'r') as f:
    data = json.load(f)

# Extract all prefLabels from non-deprecated entries
preflabels = []

for item in data.get('@graph', []):
    # Check if the item has a prefLabel and is not deprecated
    if 'skos:prefLabel' in item and 'owl:deprecated' in item:
        # Check if it's not deprecated
        if item['owl:deprecated'].lower() != 'true':
            # Extract the prefLabel
            if isinstance(item['skos:prefLabel'], dict) and '@value' in item['skos:prefLabel']:
                preflabel = item['skos:prefLabel']['@value']
                preflabels.append(preflabel)

# Sort the prefLabels alphabetically
preflabels.sort()

# Print the prefLabels in a format suitable for metadata.json
print("List of non-deprecated prefLabels from p03.json:")
print("[\n    \"" + "\",\n    \"".join(preflabels) + "\"\n]")

# Save the prefLabels to a file
output_file = "metadata_scheme_Delta_Enigma-1/keywords/p03_preflabels.json"
with open(output_file, 'w') as f:
    json.dump(preflabels, f, indent=2)

print(f"\nSaved {len(preflabels)} prefLabels to {output_file}") 