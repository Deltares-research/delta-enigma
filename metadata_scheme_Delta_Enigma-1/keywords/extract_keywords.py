import json
import re
import os

def extract_key_info(json_file_path):
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
        
        # Extract identifier
        identifier = concept.get("dc:identifier", "")
        
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
        
        # Extract P08 broader concept
        p08_broader = []
        if "skos:broader" in concept:
            broader_list = concept["skos:broader"]
            if not isinstance(broader_list, list):
                broader_list = [broader_list]
            
            for broader in broader_list:
                if isinstance(broader, dict) and "@id" in broader:
                    broader_id = broader["@id"]
                    # Check if it's a P08 concept
                    if "P08" in broader_id:
                        # Extract just the ID part
                        p08_id = re.search(r'P08/current/([^/]+)', broader_id)
                        if p08_id:
                            p08_broader.append(p08_id.group(1))
                        else:
                            p08_broader.append(broader_id)
        
        # Check if the concept is deprecated
        is_deprecated = False
        if "owl:deprecated" in concept:
            if concept["owl:deprecated"] == "true" or concept["owl:deprecated"] == True:
                is_deprecated = True
        
        # Add to our results
        extracted_info.append({
            "identifier": identifier,
            "prefLabel": pref_label,
            "definition": definition,
            "p08_broader": p08_broader,
            "deprecated": is_deprecated
        })
    
    return extracted_info

def process_all_json_files(directory):
    """Process all JSON files in the given directory and its subdirectories."""
    results = []
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                try:
                    file_results = extract_key_info(file_path)
                    results.extend(file_results)
                    print(f"Processed {file_path}: found {len(file_results)} concepts")
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")
    
    return results

def save_results(results, output_file):
    """Save the extracted information to a JSON file."""
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)
    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    # Directory containing the JSON files
    directory = "."  # Current directory where the script is located
    
    # Process all JSON files
    results = process_all_json_files(directory)
    
    # Save the results
    output_file = "extracted_keywords.json"
    save_results(results, output_file)
    
    # Print a summary
    print(f"\nExtracted {len(results)} keywords in total")
    
    # Count deprecated keywords
    deprecated_count = sum(1 for item in results if item['deprecated'])
    print(f"Found {deprecated_count} deprecated keywords")
    
    print("\nSample of extracted data:")
    for item in results[:3]:  # Show first 3 items
        print(f"Identifier: {item['identifier']}")
        print(f"Label: {item['prefLabel']}")
        print(f"Definition: {item['definition'][:100]}..." if len(item['definition']) > 100 else f"Definition: {item['definition']}")
        print(f"P08 Broader: {', '.join(item['p08_broader'])}")
        print(f"Deprecated: {item['deprecated']}")
        print("-" * 50)