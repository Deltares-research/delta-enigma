import json
import os
import re

def load_keywords(p03_file, p08_file):
    """Load the extracted keywords from the JSON files."""
    with open(p03_file, 'r', encoding='utf-8') as f:
        p03_keywords = json.load(f)
    
    with open(p08_file, 'r', encoding='utf-8') as f:
        p08_keywords = json.load(f)
    
    return p03_keywords, p08_keywords

def create_html_visualization(p03_keywords, p08_keywords, output_file):
    """Create an HTML visualization of the P08-P03 keyword relationships."""
    # Create a dictionary of P08 keywords by notation
    p08_dict = {}
    for p08 in p08_keywords:
        # Extract the notation code (e.g., "DS01" from "SDN:P08::DS01")
        notation_match = re.search(r'::([^"]+)', p08['notation'])
        if notation_match:
            code = notation_match.group(1)
            p08_dict[code] = p08
    
    # Create a dictionary to organize P03 keywords by their P08 broader concept
    hierarchy = {}
    
    # First, add all P08 keywords as top-level categories
    for p08 in p08_keywords:
        notation_match = re.search(r'::([^"]+)', p08['notation'])
        if notation_match:
            code = notation_match.group(1)
            hierarchy[code] = {
                'info': p08,
                'children': []
            }
    
    # Then, add P03 keywords under their respective P08 categories
    for p03 in p03_keywords:
        # Skip P08 keywords that were included in the P03 extraction
        if "P08::" in p03['identifier']:
            continue
            
        if p03['p08_broader']:
            for p08_code in p03['p08_broader']:
                if p08_code in hierarchy:
                    hierarchy[p08_code]['children'].append(p03)
        else:
            # For P03 keywords without a P08 broader concept, create a special category
            if "Uncategorized" not in hierarchy:
                hierarchy["Uncategorized"] = {
                    'info': {
                        'notation': 'Uncategorized',
                        'prefLabel': 'Uncategorized',
                        'definition': 'P03 keywords without a P08 broader concept',
                        'deprecated': False
                    },
                    'children': []
                }
            hierarchy["Uncategorized"]['children'].append(p03)
    
    # Count statistics
    p08_count = len([p08 for p08 in p08_keywords if "P08::" in p08['notation']])
    p08_deprecated_count = len([p08 for p08 in p08_keywords if "P08::" in p08['notation'] and p08['deprecated']])
    p03_count = len([p03 for p03 in p03_keywords if "P03::" in p03['identifier']])
    p03_deprecated_count = len([p03 for p03 in p03_keywords if "P03::" in p03['identifier'] and p03['deprecated']])
    
    # Generate the HTML content
    html_parts = []
    
    # HTML header
    html_parts.append("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>P08-P03 Keyword Hierarchy</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        h1 {
            text-align: center;
            margin-bottom: 30px;
        }
        .category {
            margin-bottom: 30px;
            border: 1px solid #ddd;
            border-radius: 5px;
            overflow: hidden;
        }
        .category-header {
            background-color: #f5f5f5;
            padding: 10px 15px;
            cursor: pointer;
            border-bottom: 1px solid #ddd;
        }
        .category-header.deprecated {
            background-color: #ffeeee;
        }
        .category-title {
            font-weight: bold;
            font-size: 18px;
            margin: 0;
        }
        .category-description {
            margin: 5px 0 0;
            font-size: 14px;
        }
        .category-content {
            padding: 0;
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.3s ease-out;
        }
        .category-content.active {
            max-height: 5000px;
            transition: max-height 0.5s ease-in;
        }
        .keyword {
            padding: 10px 15px;
            border-bottom: 1px solid #eee;
        }
        .keyword:last-child {
            border-bottom: none;
        }
        .keyword.deprecated {
            background-color: #ffeeee;
        }
        .keyword-title {
            font-weight: bold;
            margin: 0;
        }
        .keyword-id {
            color: #666;
            font-size: 14px;
            margin: 0;
        }
        .keyword-definition {
            margin: 5px 0 0;
            font-size: 14px;
        }
        .deprecated-label {
            display: inline-block;
            background-color: #ff6b6b;
            color: white;
            padding: 2px 6px;
            border-radius: 3px;
            font-size: 12px;
            margin-left: 10px;
        }
        .stats {
            text-align: center;
            margin-bottom: 20px;
            padding: 10px;
            background-color: #f9f9f9;
            border-radius: 5px;
        }
        .search-container {
            margin-bottom: 20px;
            text-align: center;
        }
        #searchInput {
            padding: 8px;
            width: 300px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>P08-P03 Keyword Hierarchy</h1>
""")
    
    # Stats section
    html_parts.append(f"""        
        <div class="stats">
            <p>Total P08 categories: <strong>{p08_count}</strong> ({p08_deprecated_count} deprecated)</p>
            <p>Total P03 keywords: <strong>{p03_count}</strong> ({p03_deprecated_count} deprecated)</p>
        </div>
        
        <div class="search-container">
            <input type="text" id="searchInput" placeholder="Search keywords...">
        </div>
        
        <div id="hierarchy">
""")
    
    # Add each category and its keywords
    for code, category in sorted(hierarchy.items()):
        info = category['info']
        children = category['children']
        
        # Skip if no children and not a P08 category
        if not children and code == "Uncategorized":
            continue
        
        deprecated_class = "deprecated" if info.get('deprecated', False) else ""
        deprecated_label = '<span class="deprecated-label">Deprecated</span>' if info.get('deprecated', False) else ""
        
        html_parts.append(f"""
            <div class="category" data-code="{code}">
                <div class="category-header {deprecated_class}">
                    <h2 class="category-title">{info['prefLabel']} ({code}) {deprecated_label}</h2>
                    <p class="category-description">{info['definition']}</p>
                </div>
                <div class="category-content">
        """)
        
        # Add each keyword in this category
        for keyword in sorted(children, key=lambda k: k['prefLabel']):
            keyword_code = ""
            if "P03::" in keyword['identifier']:
                keyword_match = re.search(r'::([^"]+)', keyword['identifier'])
                if keyword_match:
                    keyword_code = keyword_match.group(1)
            
            deprecated_class = "deprecated" if keyword.get('deprecated', False) else ""
            deprecated_label = '<span class="deprecated-label">Deprecated</span>' if keyword.get('deprecated', False) else ""
            
            html_parts.append(f"""
                    <div class="keyword {deprecated_class}" data-code="{keyword_code}">
                        <h3 class="keyword-title">{keyword['prefLabel']} {deprecated_label}</h3>
                        <p class="keyword-id">{keyword['identifier']}</p>
                        <p class="keyword-definition">{keyword['definition']}</p>
                    </div>
            """)
        
        html_parts.append("""
                </div>
            </div>
        """)
    
    # Close the HTML content
    html_parts.append("""
        </div>
    </div>
    
    <script>
        // Toggle category content when header is clicked
        document.querySelectorAll('.category-header').forEach(header => {
            header.addEventListener('click', () => {
                const content = header.nextElementSibling;
                content.classList.toggle('active');
            });
        });
        
        // Search functionality
        const searchInput = document.getElementById('searchInput');
        searchInput.addEventListener('input', () => {
            const searchTerm = searchInput.value.toLowerCase();
            
            document.querySelectorAll('.category').forEach(category => {
                const categoryTitle = category.querySelector('.category-title').textContent.toLowerCase();
                const categoryDesc = category.querySelector('.category-description').textContent.toLowerCase();
                const categoryCode = category.dataset.code.toLowerCase();
                
                let categoryVisible = categoryTitle.includes(searchTerm) || 
                                     categoryDesc.includes(searchTerm) || 
                                     categoryCode.includes(searchTerm);
                
                let keywordsVisible = false;
                
                category.querySelectorAll('.keyword').forEach(keyword => {
                    const keywordTitle = keyword.querySelector('.keyword-title').textContent.toLowerCase();
                    const keywordId = keyword.querySelector('.keyword-id').textContent.toLowerCase();
                    const keywordDef = keyword.querySelector('.keyword-definition').textContent.toLowerCase();
                    const keywordCode = keyword.dataset.code.toLowerCase();
                    
                    const keywordVisible = keywordTitle.includes(searchTerm) || 
                                         keywordId.includes(searchTerm) || 
                                         keywordDef.includes(searchTerm) || 
                                         keywordCode.includes(searchTerm);
                    
                    keyword.style.display = keywordVisible || searchTerm === '' ? 'block' : 'none';
                    
                    if (keywordVisible) {
                        keywordsVisible = true;
                    }
                });
                
                category.style.display = (categoryVisible || keywordsVisible || searchTerm === '') ? 'block' : 'none';
                
                if (categoryVisible || keywordsVisible) {
                    category.querySelector('.category-content').classList.add('active');
                } else if (searchTerm !== '') {
                    category.querySelector('.category-content').classList.remove('active');
                }
            });
        });
        
        // Initially expand the first few categories
        const initialCategories = document.querySelectorAll('.category');
        for (let i = 0; i < Math.min(3, initialCategories.length); i++) {
            initialCategories[i].querySelector('.category-content').classList.add('active');
        }
    </script>
</body>
</html>
""")
    
    # Write the HTML content to a file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(''.join(html_parts))
    
    print(f"HTML visualization created: {output_file}")

def create_folder_structure(p03_keywords, p08_keywords, output_dir):
    """Create a folder structure representing the P08-P03 keyword hierarchy."""
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Create a dictionary of P08 keywords by notation
    p08_dict = {}
    for p08 in p08_keywords:
        # Extract the notation code (e.g., "DS01" from "SDN:P08::DS01")
        notation_match = re.search(r'::([^"]+)', p08['notation'])
        if notation_match:
            code = notation_match.group(1)
            p08_dict[code] = p08
    
    # Create a folder for each P08 category
    for p08 in p08_keywords:
        notation_match = re.search(r'::([^"]+)', p08['notation'])
        if notation_match:
            code = notation_match.group(1)
            
            # Create folder name with code and label
            folder_name = f"{code}_{p08['prefLabel'].replace('/', '_')}"
            if p08['deprecated']:
                folder_name += "_DEPRECATED"
            
            folder_path = os.path.join(output_dir, folder_name)
            
            # Create the folder
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            
            # Create a README.md file with information about the P08 category
            readme_path = os.path.join(folder_path, "README.md")
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(f"# {p08['prefLabel']} ({code})\n\n")
                if p08['deprecated']:
                    f.write("**DEPRECATED**\n\n")
                f.write(f"**Definition:** {p08['definition']}\n\n")
                f.write("## P03 Keywords in this category:\n\n")
    
    # Create a folder for P03 keywords without a P08 broader concept
    uncategorized_folder = os.path.join(output_dir, "Uncategorized")
    if not os.path.exists(uncategorized_folder):
        os.makedirs(uncategorized_folder)
    
    # Create a README.md file for the uncategorized folder
    uncategorized_readme = os.path.join(uncategorized_folder, "README.md")
    with open(uncategorized_readme, 'w', encoding='utf-8') as f:
        f.write("# Uncategorized P03 Keywords\n\n")
        f.write("These P03 keywords do not have a P08 broader concept.\n\n")
        f.write("## Keywords:\n\n")
    
    # Add P03 keywords to their respective folders
    for p03 in p03_keywords:
        # Skip P08 keywords that were included in the P03 extraction
        if "P08::" in p03['identifier']:
            continue
            
        # Extract the P03 code
        p03_code_match = re.search(r'::([^"]+)', p03['identifier'])
        if not p03_code_match:
            continue
            
        p03_code = p03_code_match.group(1)
        
        if p03['p08_broader']:
            # Add to each P08 category folder
            for p08_code in p03['p08_broader']:
                if p08_code in p08_dict:
                    # Get the folder name
                    folder_name = f"{p08_code}_{p08_dict[p08_code]['prefLabel'].replace('/', '_')}"
                    if p08_dict[p08_code]['deprecated']:
                        folder_name += "_DEPRECATED"
                    
                    folder_path = os.path.join(output_dir, folder_name)
                    
                    # Append to the README.md file
                    readme_path = os.path.join(folder_path, "README.md")
                    with open(readme_path, 'a', encoding='utf-8') as f:
                        f.write(f"- **{p03['prefLabel']}** ({p03_code})")
                        if p03['deprecated']:
                            f.write(" *DEPRECATED*")
                        f.write(f": {p03['definition'][:100]}")
                        if len(p03['definition']) > 100:
                            f.write("...")
                        f.write("\n")
        else:
            # Add to the uncategorized folder
            with open(uncategorized_readme, 'a', encoding='utf-8') as f:
                f.write(f"- **{p03['prefLabel']}** ({p03_code})")
                if p03['deprecated']:
                    f.write(" *DEPRECATED*")
                f.write(f": {p03['definition'][:100]}")
                if len(p03['definition']) > 100:
                    f.write("...")
                f.write("\n")
    
    print(f"Folder structure created in: {output_dir}")

if __name__ == "__main__":
    # Paths to the extracted keyword files
    p03_file = "extracted_keywords.json"
    p08_file = "extracted_p08_keywords.json"
    
    # Load the keywords
    p03_keywords, p08_keywords = load_keywords(p03_file, p08_file)
    
    # Create the HTML visualization
    html_output = "keyword_hierarchy.html"
    create_html_visualization(p03_keywords, p08_keywords, html_output)
    
    # Create the folder structure
    folder_output = "keyword_hierarchy"
    create_folder_structure(p03_keywords, p08_keywords, folder_output)
    
    print("\nVisualization complete!")
    print(f"HTML visualization: {html_output}")
    print(f"Folder structure: {folder_output}/") 