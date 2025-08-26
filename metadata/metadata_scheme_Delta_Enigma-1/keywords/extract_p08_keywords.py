import json
import re
import os

def extract_p08_keywords(json_file_path):
    """
    Extract keywords from p08.json with skos:notation, skos:prefLabel, skos:definition,
    and skos:narrower IDs for P03 keywords.
    """
    # Load the JSON data
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # List to store the extracted information
    extracted_info = []
    
    # Process each concept in the JSON
    # The structure might vary, so we need to determine where the concepts are stored
    concepts = []
    
    # If the JSON is an array at the top level
    if isinstance(data, list):
        concepts = data
    # If the concepts are nested under a key (common in SKOS)
    elif isinstance(data, dict):
        # Look for arrays that might contain the concepts
        for key, value in data.items():
            if isinstance(value, list) and len(value) > 0 and isinstance(value[0], dict):
                concepts = value
                break
        # If no array found, the whole document might be a single concept
        if not concepts and "@type" in data and "skos:Concept" in data.get("@type", ""):
            concepts = [data]
    
    # Process each concept
    for concept in concepts:
        # Skip if not a SKOS concept
        if "@type" not in concept or "skos:Concept" not in concept.get("@type", ""):
            continue
        
        # Extract notation
        notation = ""
        if "skos:notation" in concept:
            if isinstance(concept["skos:notation"], dict) and "@value" in concept["skos:notation"]:
                notation = concept["skos:notation"]["@value"]
            elif isinstance(concept["skos:notation"], str):
                notation = concept["skos:notation"]
        
        # Extract prefLabel
        pref_label = ""
        if "skos:prefLabel" in concept:
            if isinstance(concept["skos:prefLabel"], dict) and "@value" in concept["skos:prefLabel"]:
                pref_label = concept["skos:prefLabel"]["@value"]
            elif isinstance(concept["skos:prefLabel"], str):
                pref_label = concept["skos:prefLabel"]
        
        # Extract definition
        definition = ""
        if "skos:definition" in concept:
            if isinstance(concept["skos:definition"], dict) and "@value" in concept["skos:definition"]:
                definition = concept["skos:definition"]["@value"]
            elif isinstance(concept["skos:definition"], str):
                definition = concept["skos:definition"]
        
        # Extract P03 narrower concepts
        p03_narrower = []
        if "skos:narrower" in concept:
            narrower_list = concept["skos:narrower"]
            if not isinstance(narrower_list, list):
                narrower_list = [narrower_list]
            
            for narrower in narrower_list:
                if isinstance(narrower, dict) and "@id" in narrower:
                    narrower_id = narrower["@id"]
                    # Check if it's a P03 concept
                    if "P03" in narrower_id:
                        # Extract just the ID part
                        p03_id = re.search(r'P03/current/([^/]+)', narrower_id)
                        if p03_id:
                            p03_narrower.append(p03_id.group(1))
                        else:
                            # Try to extract the full P03 identifier
                            p03_full = re.search(r'P03/current/([^"]+)', narrower_id)
                            if p03_full:
                                p03_narrower.append(p03_full.group(1))
                            else:
                                p03_narrower.append(narrower_id)
        
        # Check if the concept is deprecated
        is_deprecated = False
        if "owl:deprecated" in concept:
            if concept["owl:deprecated"] == "true" or concept["owl:deprecated"] == True:
                is_deprecated = True
        
        # Add to our results
        extracted_info.append({
            "notation": notation,
            "prefLabel": pref_label,
            "definition": definition,
            "p03_narrower": p03_narrower,
            "deprecated": is_deprecated
        })
    
    return extracted_info

def save_results(results, output_file):
    """Save the extracted information to a JSON file."""
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)
    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    # Path to the p08.json file
    p08_file_path = "p08.json"
    
    # Check if the file exists
    if not os.path.exists(p08_file_path):
        print(f"Error: {p08_file_path} not found. Please make sure the file exists in the current directory.")
    else:
        # Process the p08.json file
        results = extract_p08_keywords(p08_file_path)
        
        # Save the results
        output_file = "extracted_p08_keywords.json"
        save_results(results, output_file)
        
        # Print a summary
        print(f"\nExtracted {len(results)} P08 keywords in total")
        
        # Count deprecated keywords
        deprecated_count = sum(1 for item in results if item['deprecated'])
        print(f"Found {deprecated_count} deprecated keywords")
        
        print("\nSample of extracted data:")
        for item in results[:3]:  # Show first 3 items
            print(f"Notation: {item['notation']}")
            print(f"Label: {item['prefLabel']}")
            print(f"Definition: {item['definition'][:100]}..." if len(item['definition']) > 100 else f"Definition: {item['definition']}")
            print(f"P03 Narrower: {', '.join(item['p03_narrower'])}")
            print(f"Deprecated: {item['deprecated']}")
            print("-" * 50) 