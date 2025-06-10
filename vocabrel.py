# vocabulary mapping
#
# Alexander Barth, 2014

import os.path
import json
import urllib.request
import xml.etree.ElementTree as ET

namespaces = {'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
              'skos': 'http://www.w3.org/2004/02/skos/core#',
              'dc': 'http://purl.org/dc/terms/',
              'rdfs': 'http://www.w3.org/2000/01/rdf-schema#',
              'grg': 'http://www.isotc211.org/schemas/grg/',
              'owl': 'http://www.w3.org/2002/07/owl#',
              'void': 'http://rdfs.org/ns/void#'}


def narrower_concepts(tree,concept_prefix,narrower_prefix):
    """returns a dictonary with all relating all concepts from the XML tree to narrower concepts"""

    concepts = tree.findall('skos:Collection/skos:member/skos:Concept',namespaces)

    mapping = {}


    for concept in concepts:
        concept_notation = concept.find('skos:notation',namespaces).text

        assert(concept_notation.startswith(concept_prefix))
        concept_notation = concept_notation[len(concept_prefix):]
        
        urls = [n.attrib['{%s}resource' % namespaces['rdf']] for n in concept.findall('skos:narrower',namespaces)]

        ids = [url[len(narrower_prefix):].replace('/','') for url in urls if url.startswith(narrower_prefix)]

        mapping[concept_notation] = ids


    return mapping

def getXMLtree(collection):
    cachdir = '/tmp/'
    if not os.path.exists(cachdir):
        print(''.join(['path ',cachdir,' does not exist and will be set to current directory']))
        cachdir = '.'  # Use current directory instead of undefined 'path' variable

    fname = os.path.join(cachdir,'cached-' + collection + '.xml')

    try:
        url = 'http://vocab.nerc.ac.uk/collection/' + collection + '/current/'
        print('Downloading',collection,'from',url)
        response = urllib.request.urlopen(url)
        xml = response.read()
        
        # Decode bytes to string for XML parsing
        xml_str = xml.decode('utf-8')
        
        # Open file in text mode and write the decoded string
        with open(fname, 'w', encoding='utf-8') as localFile:
            localFile.write(xml_str)
            
        tree = ET.fromstring(xml_str)
        return tree
        
    except Exception as e:
        print(f"Error downloading or parsing XML: {str(e)}")
        # If the cached file exists, try to use it as fallback
        if os.path.isfile(fname) and os.path.getsize(fname) > 0:
            print(f"Trying to use cached file: {fname}")
            tree = ET.parse(fname)
            return tree
        raise  # Re-raise the exception if we can't recover

def sdn_mapping(collection,tocollection):
    tree = getXMLtree(collection)

    narrower_prefix = 'http://vocab.nerc.ac.uk/collection/' + tocollection + '/current/'
    concept_prefix = 'SDN:' + collection + '::'

    mapping = narrower_concepts(tree,concept_prefix,narrower_prefix)
    return mapping
    

def sea_bbox(collection):
    tree = getXMLtree(collection)

    """returns a dictonary with all relating all concepts from the XML tree to narrower concepts"""

    concepts = tree.findall('skos:Collection/skos:member/skos:Concept',namespaces)

    mapping = {}

    for concept in concepts:
        concept_notation = concept.find('skos:notation',namespaces).text
        concept_definition = concept.find('skos:definition',namespaces).text

        try:            
            tmp = json.loads(concept_definition)
            mapping[concept_notation] = tmp['Spatial_Coverage']
        except:
            print("no definition for ",concept.find('skos:prefLabel',namespaces).text)


    return mapping

def test():    
    mapping = sdn_mapping('P35','P01')
    #mapping = sdn_mapping('P02','P01')
    #mapping = sea_bbox('C19')
        
    #print mapping
    print('P35 WATERTEMP corresponds to ',mapping['WATERTEMP'])
    c = 0
    for k in mapping:
        for v in mapping[k]:
            c = c+1
            print(c, k, v)
    
def main():
    test()

# Add this standard Python idiom to run main() when the script is run directly
if __name__ == "__main__":
    main()
