// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Get references to DOM elements
    const form = document.getElementById('metadata-form');
    const generateBtn = document.getElementById('generate-btn');
    const downloadBtn = document.getElementById('download-btn');
    const resetBtn = document.getElementById('reset-btn');
    const jsonOutput = document.getElementById('json-output');
    
    // Initialize the form
    initializeForm();
    
    // Add event listeners for buttons
    generateBtn.addEventListener('click', generateJSON);
    downloadBtn.addEventListener('click', downloadJSON);
    resetBtn.addEventListener('click', resetForm);
    
    // Function to initialize the form with fields based on schema
    function initializeForm() {
        // Clear the form first
        form.innerHTML = '';
        
        // Create form sections based on schema
        createBasicFields();
        createDomainFields();
        createTemporalCoverageFields();
        createGeographicalCoverageFields();
        createDocumentationFields();
        createRelatedResourceFields();
    }
    
    // Function to create basic fields
    function createBasicFields() {
        createSectionHeader('Basic Information');
        
        // Create Title field
        createTextField('Title', 'Title', false);
        
        // Create Description field
        createTextAreaField('Description', 'Abstract', false, metadataSchema.properties.Description.default);
        
        // Create Version field
        createTextField('Version', 'Version', false, metadataSchema.properties.Version.default);
        
        // Create Language field
        createSelectField('Language', 'Language of the data', false, [
            'en - English',
            'nl - Dutch',
            'de - German',
            'fr - French',
            'es - Spanish'
        ], metadataSchema.properties.Language.default);
        
        // Create Resource Type field
        createSelectField('Resource_Type', 'Resource type', false, [
            'Dataset',
            'Series',
            'Service'
        ], metadataSchema.properties.Resource_Type.default);
        
        // Create date fields
        createDateField('Creation_Date', 'Creation date', false);
        createDateField('Release_Date', 'Release date', false);
    }
    
    // Function to create domain fields
    function createDomainFields() {
        createSectionHeader('Domain Information');
        
        // Create Domain field with multiple selection
        createTagSelectField('Domain', 'Domain (select multiple)', false, [
            'Administration and dimensions',
            'Atmosphere',
            'Biological oceanography',
            'Chemical oceanography',
            'Cross-discipline',
            'Cryosphere',
            'Environment',
            'Human activities',
            'Marine geology',
            'Physical oceanography',
            'Terrestrial'
        ]);
        
        // Create Topic Category field with multiple selection
        createTagSelectField('Topic_Category', 'Topic Category (select multiple)', false, [
            'Acoustics',
            'Administration and dimensions',
            'Amino acids',
            'Aquaculture',
            'Area Management/Designation',
            'Atmospheric chemistry',
            'Bacteria and viruses',
            'Biota abundance, biomass and diversity',
            'Biota composition',
            'Birds, mammals and reptiles',
            'Cables',
            'Carbon, nitrogen and phosphorus',
            'Carbonate system',
            'Construction and structures',
            'Cryosphere',
            'Cultural Heritage',
            'Currents',
            'Disease, damage and mortality',
            'Dissolved gases',
            'Energy',
            'Fatty acids',
            'Field geophysics',
            'Fish',
            'Fisheries',
            'Fluxes',
            'Geochronology and stratigraphy',
            'Geothermal measurements',
            'Gravity, magnetics and bathymetry',
            'Habitat',
            'Halocarbons (including freons)',
            'Hydrocarbon extraction',
            'Hydrocarbons',
            'Isotopes',
            'Macroalgae and seagrass',
            'Marine geomorphology',
            'Metal and metalloid concentrations',
            'Meteorology',
            'Microzooplankton',
            'Mining',
            'Nutrients',
            'Optical properties',
            'Other biological measurements',
            'Other inorganic chemical measurements',
            'Other organic chemical measurements',
            'Other physical oceanographic measurements',
            'PCBs and organic micropollutants',
            'Palaeoclimate',
            'Phytoplankton and microphytobenthos',
            'Pigments',
            'Pipelines',
            'Pollution',
            'Rate measurements (including production, excretion and grazing)',
            'Rock and sediment biota',
            'Rock and sediment chemistry',
            'Rock and sediment lithology and mineralogy',
            'Rock and sediment physical properties',
            'Rock and sediment sedimentology',
            'Salt extraction',
            'Sea level',
            'Sediment pore water chemistry',
            'Sedimentation and erosion processes',
            'Sonar and seismics',
            'Suspended particulate material',
            'Terrestrial',
            'Tourism',
            'Transport',
            'Underwater photography',
            'Water column temperature and salinity',
            'Waves',
            'Zooplankton'
        ]);
        
        // Create Acquisition Sensor field with multiple selection
        createTagSelectField('Acquisition_Sensor', 'Acquisition sensor (select multiple)', false, [
            '13h Repeat transect ADCP',
            '3D laser scanner',
            'ADCP',
            'ADV',
            'AQUAscat',
            'AQUAscat 1000R',
            'Autonomuous ship',
            'Backpack laser scanner',
            'Benthic sampling',
            'Biolive flume',
            'Camera observations',
            'Continuous centrifuge SPM',
            'Continuous flow centrifuge',
            'CTD',
            'Current flume (PIV system)',
            'Field sediment sampling',
            'Fluorimeter',
            'Global change mesocosms',
            'Groundwater',
            'Horizontal ADCPs',
            'Lidar drone',
            'LISST200X',
            'Luminescence lab',
            'Metronome',
            'Microtec MRB Camsizer p4',
            'Microtec MRB Camsizer XL',
            'Multibeam',
            'Multibeam bedload transport sampling',
            'Multibeam CTD casts',
            'Multisprectral drone',
            'NDVI',
            'OBS',
            'Optical sediment microscope',
            'Pressure sensor',
            'Repeat transect ADCP',
            'Salinity',
            'Salinity sensor',
            'Sediment grain size analysis',
            'Soil moisture',
            'Tilt sensor',
            'Unmanned surface vessel',
            'Vegetation cameras',
            'Vegetation cameras dune foot',
            'Vegetation drone surveys',
            'Vegetation field quadrants',
            'Vegetation recording drone',
            'Vibrocores sediment bed',
            'Water sampler',
            'Wave current flume',
            'Weather station'
        ]);
    }
    
    // Function to create temporal coverage fields
    function createTemporalCoverageFields() {
        createSectionHeader('Temporal Coverage');
        
        // Create Start Date field
        createDateField('Temporal_Coverage_Start_Date', 'Start date', false);
        
        // Create End Date field
        createDateField('Temporal_Coverage_End_Date', 'End date', false);
    }
    
    // Function to create geographical coverage fields
    function createGeographicalCoverageFields() {
        createSectionHeader('Geographical Coverage');
        
        // Create Description field
        createTextField('Geographical_Coverage_Description', 'Description', false);
        
        // Create Reference System field with hardcoded options
        createSelectField('Geographical_Coverage_Reference_System', 'Reference System', false, [
            'WGS84',
            'Rijksdriehoekstelsel',
            'ETRS89'
        ], 'WGS84');
        
        // Create Bounding Box fields
        createNumberField('Geographical_Coverage_North', 'North Bound Latitude', false);
        createNumberField('Geographical_Coverage_South', 'South Bound Latitude', false);
        createNumberField('Geographical_Coverage_East', 'East Bound Longitude', false);
        createNumberField('Geographical_Coverage_West', 'West Bound Longitude', false);
    }
    
    // Function to create documentation fields
    function createDocumentationFields() {
        createSectionHeader('Documentation');
        
        // Create container for documentation items
        const docContainer = document.createElement('div');
        docContainer.id = 'documentation-container';
        form.appendChild(docContainer);
        
        // Create initial documentation item
        addDocumentationItem(docContainer);
        
        // Add button to add more documentation items
        const addButton = document.createElement('button');
        addButton.type = 'button';
        addButton.className = 'add-button';
        addButton.textContent = 'Add Documentation';
        addButton.addEventListener('click', function() {
            addDocumentationItem(docContainer);
        });
        form.appendChild(addButton);
    }
    
    // Function to add a documentation item
    function addDocumentationItem(container) {
        const itemDiv = document.createElement('div');
        itemDiv.className = 'array-item';
        
        // Create Title field
        const titleGroup = document.createElement('div');
        titleGroup.className = 'form-group';
        
        const titleLabel = document.createElement('label');
        titleLabel.textContent = 'Document Title';
        
        const titleInput = document.createElement('input');
        titleInput.type = 'text';
        titleInput.className = 'doc-title form-control';
        titleInput.placeholder = 'Enter document title';
        
        titleGroup.appendChild(titleLabel);
        titleGroup.appendChild(titleInput);
        itemDiv.appendChild(titleGroup);
        
        // Create Link field
        const linkGroup = document.createElement('div');
        linkGroup.className = 'form-group';
        
        const linkLabel = document.createElement('label');
        linkLabel.textContent = 'Document Link';
        
        const linkInput = document.createElement('input');
        linkInput.type = 'text';
        linkInput.className = 'doc-link form-control';
        linkInput.placeholder = 'Enter document URL';
        
        linkGroup.appendChild(linkLabel);
        linkGroup.appendChild(linkInput);
        itemDiv.appendChild(linkGroup);
        
        // Add remove button
        const removeButton = document.createElement('button');
        removeButton.type = 'button';
        removeButton.className = 'remove-button';
        removeButton.textContent = 'Remove';
        removeButton.addEventListener('click', function() {
            container.removeChild(itemDiv);
        });
        itemDiv.appendChild(removeButton);
        
        container.appendChild(itemDiv);
    }
    
    // Function to create related resource fields
    function createRelatedResourceFields() {
        createSectionHeader('Related Resources');
        
        // Create container for related resource items
        const relatedContainer = document.createElement('div');
        relatedContainer.id = 'related-resource-container';
        form.appendChild(relatedContainer);
        
        // Create initial related resource item
        addRelatedResourceItem(relatedContainer);
        
        // Add button to add more related resource items
        const addButton = document.createElement('button');
        addButton.type = 'button';
        addButton.className = 'add-button';
        addButton.textContent = 'Add Related Resource';
        addButton.addEventListener('click', function() {
            addRelatedResourceItem(relatedContainer);
        });
        form.appendChild(addButton);
    }
    
    // Function to add a related resource item
    function addRelatedResourceItem(container) {
        const itemDiv = document.createElement('div');
        itemDiv.className = 'array-item';
        
        // Create Relation Type field
        const typeGroup = document.createElement('div');
        typeGroup.className = 'form-group';
        
        const typeLabel = document.createElement('label');
        typeLabel.textContent = 'Relation Type';
        
        const typeSelect = document.createElement('select');
        typeSelect.className = 'relation-type form-control';
        
        // Add empty option
        const emptyOption = document.createElement('option');
        emptyOption.value = '';
        emptyOption.textContent = '-- Select Relation Type --';
        typeSelect.appendChild(emptyOption);
        
        // Complete relation type options from schema
        const relationTypeOptions = [
            'IsCitedBy',
            'Cites',
            'IsSupplementTo',
            'IsSupplementedBy',
            'IsContinuedBy',
            'Continues',
            'IsNewVersionOf',
            'IsPreviousVersionOf',
            'IsPartOf',
            'HasPart',
            'IsReferencedBy',
            'References',
            'IsDocumentedBy',
            'Documents',
            'IsCompiledBy',
            'Compiles',
            'IsVariantFormOf',
            'IsOriginalFormOf',
            'IsIdenticalTo',
            'HasMetadata',
            'IsMetadataFor',
            'Reviews',
            'IsReviewedBy',
            'IsDerivedFrom',
            'IsSourceOf',
            'Describes',
            'IsDescribedBy',
            'HasVersion',
            'IsVersionOf',
            'Requires',
            'IsRequiredBy',
            'Obsoletes',
            'IsObsoletedBy'
        ];
        
        relationTypeOptions.forEach(option => {
            const optionElement = document.createElement('option');
            optionElement.value = option;
            optionElement.textContent = option;
            typeSelect.appendChild(optionElement);
        });
        
        typeGroup.appendChild(typeLabel);
        typeGroup.appendChild(typeSelect);
        itemDiv.appendChild(typeGroup);
        
        // Create Title field
        const titleGroup = document.createElement('div');
        titleGroup.className = 'form-group';
        
        const titleLabel = document.createElement('label');
        titleLabel.textContent = 'Resource Title';
        
        const titleInput = document.createElement('input');
        titleInput.type = 'text';
        titleInput.className = 'resource-title form-control';
        titleInput.placeholder = 'Enter resource title';
        
        titleGroup.appendChild(titleLabel);
        titleGroup.appendChild(titleInput);
        itemDiv.appendChild(titleGroup);
        
        // Add remove button
        const removeButton = document.createElement('button');
        removeButton.type = 'button';
        removeButton.className = 'remove-button';
        removeButton.textContent = 'Remove';
        removeButton.addEventListener('click', function() {
            container.removeChild(itemDiv);
        });
        itemDiv.appendChild(removeButton);
        
        container.appendChild(itemDiv);
    }
    
    // Helper function to create a section header
    function createSectionHeader(title) {
        const header = document.createElement('h2');
        header.className = 'section-header';
        header.textContent = title;
        form.appendChild(header);
    }
    
    // Function to create a text field
    function createTextField(id, label, required, defaultValue = '') {
        const formGroup = document.createElement('div');
        formGroup.className = 'form-group';
        
        const labelElement = document.createElement('label');
        labelElement.htmlFor = id;
        labelElement.textContent = label;
        
        const input = document.createElement('input');
        input.type = 'text';
        input.id = id;
        input.name = id;
        input.className = 'form-control';
        input.value = defaultValue;
        
        formGroup.appendChild(labelElement);
        formGroup.appendChild(input);
        form.appendChild(formGroup);
    }
    
    // Function to create a text area field
    function createTextAreaField(id, label, required, defaultValue = '') {
        const formGroup = document.createElement('div');
        formGroup.className = 'form-group';
        
        const labelElement = document.createElement('label');
        labelElement.htmlFor = id;
        labelElement.textContent = label;
        
        const textarea = document.createElement('textarea');
        textarea.id = id;
        textarea.name = id;
        textarea.className = 'form-control';
        textarea.rows = 3;
        textarea.value = defaultValue;
        
        formGroup.appendChild(labelElement);
        formGroup.appendChild(textarea);
        form.appendChild(formGroup);
    }
    
    // Function to create a select field
    function createSelectField(id, label, required, options, defaultValue = '') {
        const formGroup = document.createElement('div');
        formGroup.className = 'form-group';
        
        const labelElement = document.createElement('label');
        labelElement.htmlFor = id;
        labelElement.textContent = label;
        
        const select = document.createElement('select');
        select.id = id;
        select.name = id;
        select.className = 'form-control';
        
        // Add empty option
        const emptyOption = document.createElement('option');
        emptyOption.value = '';
        emptyOption.textContent = '-- Select --';
        select.appendChild(emptyOption);
        
        // Add options
        options.forEach(option => {
            const optionElement = document.createElement('option');
            optionElement.value = option;
            optionElement.textContent = option;
            if (option === defaultValue) {
                optionElement.selected = true;
            }
            select.appendChild(optionElement);
        });
        
        formGroup.appendChild(labelElement);
        formGroup.appendChild(select);
        form.appendChild(formGroup);
    }
    
    // Function to create a date field
    function createDateField(id, label, required, defaultValue = '') {
        const formGroup = document.createElement('div');
        formGroup.className = 'form-group';
        
        const labelElement = document.createElement('label');
        labelElement.htmlFor = id;
        labelElement.textContent = label;
        
        const input = document.createElement('input');
        input.type = 'date';
        input.id = id;
        input.name = id;
        input.className = 'form-control';
        input.value = defaultValue;
        
        formGroup.appendChild(labelElement);
        formGroup.appendChild(input);
        form.appendChild(formGroup);
    }
    
    // Function to create a number field
    function createNumberField(id, label, required, defaultValue = '') {
        const formGroup = document.createElement('div');
        formGroup.className = 'form-group';
        
        const labelElement = document.createElement('label');
        labelElement.htmlFor = id;
        labelElement.textContent = label;
        
        const input = document.createElement('input');
        input.type = 'number';
        input.id = id;
        input.name = id;
        input.className = 'form-control';
        input.value = defaultValue;
        input.step = 'any';
        
        formGroup.appendChild(labelElement);
        formGroup.appendChild(input);
        form.appendChild(formGroup);
    }
    
    // Function to create a tag-based select field with search
    function createTagSelectField(id, label, required, options) {
        const formGroup = document.createElement('div');
        formGroup.className = 'form-group';
        
        const labelElement = document.createElement('label');
        labelElement.htmlFor = id;
        labelElement.textContent = label;
        
        // Create search input
        const searchInput = document.createElement('input');
        searchInput.type = 'text';
        searchInput.className = 'form-control search-input';
        searchInput.placeholder = 'Search options...';
        
        // Create visible select element
        const visibleSelect = document.createElement('select');
        visibleSelect.className = 'form-control';
        visibleSelect.multiple = true;
        visibleSelect.size = 5;
        
        // Create hidden select element for data storage
        const hiddenSelect = document.createElement('select');
        hiddenSelect.id = id;
        hiddenSelect.name = id;
        hiddenSelect.multiple = true;
        hiddenSelect.style.display = 'none';
        
        // Create tags container
        const tagsContainer = document.createElement('div');
        tagsContainer.className = 'tags-container';
        
        // Helper text
        const helperText = document.createElement('div');
        helperText.className = 'helper-text';
        helperText.textContent = 'Click an option to select it';
        
        // Add options to both selects
        options.forEach(option => {
            const visibleOption = document.createElement('option');
            visibleOption.value = option;
            visibleOption.textContent = option;
            visibleSelect.appendChild(visibleOption);
            
            const hiddenOption = document.createElement('option');
            hiddenOption.value = option;
            hiddenOption.textContent = option;
            hiddenSelect.appendChild(hiddenOption);
        });
        
        // Add event listener for search
        searchInput.addEventListener('input', function() {
            const searchTerm = this.value.toLowerCase();
            Array.from(visibleSelect.options).forEach(option => {
                const optionText = option.textContent.toLowerCase();
                option.style.display = optionText.includes(searchTerm) ? '' : 'none';
            });
        });
        
        // Add event listener for selection
        visibleSelect.addEventListener('click', function(e) {
            if (e.target.tagName === 'OPTION') {
                const selectedOption = e.target;
                const value = selectedOption.value;
                const text = selectedOption.textContent;
                
                // Check if already selected
                const isAlreadySelected = Array.from(hiddenSelect.options).some(option => 
                    option.value === value && option.selected);
                
                if (!isAlreadySelected) {
                    // Select in hidden select
                    Array.from(hiddenSelect.options).forEach(option => {
                        if (option.value === value) {
                            option.selected = true;
                        }
                    });
                    
                    // Add tag
                    addTag(tagsContainer, hiddenSelect, value, text);
                }
            }
        });
        
        // Append elements
        formGroup.appendChild(labelElement);
        formGroup.appendChild(searchInput);
        formGroup.appendChild(visibleSelect);
        formGroup.appendChild(hiddenSelect);
        formGroup.appendChild(helperText);
        formGroup.appendChild(tagsContainer);
        form.appendChild(formGroup);
    }
    
    // Function to add a tag
    function addTag(container, hiddenSelect, value, text) {
        const tag = document.createElement('div');
        tag.className = 'tag';
        tag.dataset.value = value;
        
        const tagText = document.createElement('span');
        tagText.textContent = text;
        
        const removeBtn = document.createElement('span');
        removeBtn.className = 'tag-remove';
        removeBtn.textContent = '×';
        removeBtn.addEventListener('click', function() {
            // Deselect in hidden select
            Array.from(hiddenSelect.options).forEach(option => {
                if (option.value === value) {
                    option.selected = false;
                }
            });
            
            // Remove tag
            container.removeChild(tag);
        });
        
        tag.appendChild(tagText);
        tag.appendChild(removeBtn);
        container.appendChild(tag);
    }
    
    // Function to generate JSON from form data
    function generateJSON() {
        // Remove form validation check
        // if (!form.checkValidity()) {
        //     form.reportValidity();
        //     return;
        // }
        
        // Create metadata object
        const metadata = {
            Title: document.getElementById('Title').value || "Untitled",
            Description: document.getElementById('Description').value || "[No description provided]",
            Version: document.getElementById('Version').value || "1.0",
            Language: document.getElementById('Language').value || "en - English",
            Resource_Type: document.getElementById('Resource_Type').value || "Dataset",
            Creation_Date: document.getElementById('Creation_Date').value || new Date().toISOString().split('T')[0],
            Release_Date: document.getElementById('Release_Date').value || new Date().toISOString().split('T')[0]
        };
        
        // Add Domain, Topic Category, and Acquisition Sensor (now as multi-select fields)
        metadata.Domain = Array.from(document.getElementById('Domain').selectedOptions).map(option => option.value);
        if (metadata.Domain.length === 0) metadata.Domain = ["Terrestrial"]; // Default value if empty
        
        metadata.Topic_Category = Array.from(document.getElementById('Topic_Category').selectedOptions).map(option => option.value);
        if (metadata.Topic_Category.length === 0) metadata.Topic_Category = ["Other biological measurements"]; // Default value if empty
        
        metadata.Acquisition_Sensor = Array.from(document.getElementById('Acquisition_Sensor').selectedOptions).map(option => option.value);
        if (metadata.Acquisition_Sensor.length === 0) metadata.Acquisition_Sensor = ["Water sampler"]; // Default value if empty
        
        // Add Temporal Coverage
        const startDate = document.getElementById('Temporal_Coverage_Start_Date').value || new Date().toISOString().split('T')[0];
        const endDate = document.getElementById('Temporal_Coverage_End_Date').value || new Date().toISOString().split('T')[0];
        
        metadata.Temporal_Coverage = {
            Start_Date: startDate,
            End_Date: endDate
        };
        
        // Add Geographical Coverage with default values if empty
        const northValue = document.getElementById('Geographical_Coverage_North').value || "52.0";
        const southValue = document.getElementById('Geographical_Coverage_South').value || "51.0";
        const eastValue = document.getElementById('Geographical_Coverage_East').value || "5.0";
        const westValue = document.getElementById('Geographical_Coverage_West').value || "4.0";
        
        metadata.Geographical_Coverage = [{
            Description_Spatial: document.getElementById('Geographical_Coverage_Description').value || "Default location",
            Reference_System: document.getElementById('Geographical_Coverage_Reference_System').value || "WGS84",
            geoLocationBox: {
                northBoundLatitude: parseFloat(northValue),
                southBoundLatitude: parseFloat(southValue),
                eastBoundLongitude: parseFloat(eastValue),
                westBoundLongitude: parseFloat(westValue)
            }
        }];
        
        // Add Documentation
        metadata.Documentation = [];
        const docTitles = document.querySelectorAll('.doc-title');
        const docLinks = document.querySelectorAll('.doc-link');
        for (let i = 0; i < docTitles.length; i++) {
            // Include even if fields are empty - we'll provide default values
            metadata.Documentation.push({
                Title_document: docTitles[i].value || "Untitled Document",
                Link_document: docLinks[i].value || "https://example.org/document"
            });
        }
        
        // Add default documentation if empty
        if (metadata.Documentation.length === 0) {
            metadata.Documentation = [{
                Title_document: "Default Documentation",
                Link_document: "https://example.org/default-document"
            }];
        }
        
        // Add Related Resources
        metadata.Related_Resource = [];
        const relationTypes = document.querySelectorAll('.relation-type');
        const resourceTitles = document.querySelectorAll('.resource-title');
        for (let i = 0; i < relationTypes.length; i++) {
            // Include even if fields are empty - we'll provide default values
            metadata.Related_Resource.push({
                Relation_Type: relationTypes[i].value || "IsReferencedBy",
                Title: resourceTitles[i].value || "Untitled Related Resource"
            });
        }
        
        // Add default related resource if empty
        if (metadata.Related_Resource.length === 0) {
            metadata.Related_Resource = [{
                Relation_Type: "IsReferencedBy",
                Title: "Default Related Resource"
            }];
        }
        
        // Add required fields with default values
        metadata.links = [{
            rel: "describedby",
            href: "https://yoda.surf.nl/schemas/delta-enigma-1/metadata.json"
        }];
        
        // Add Creator and Contact Point with default values
        metadata.Creator = [{
            Name: {
                Given_Name: "Example",
                Family_Name: "User"
            },
            Affiliation: [{
                Affiliation_Name: "Example Organization",
                Affiliation_Identifier: "https://example.org"
            }],
            Person_Identifier: [{}]
        }];
        
        metadata.Contact_Point = [{
            Name: {
                Given_Name: "Example",
                Family_Name: "User"
            },
            Affiliation: [{
                Affiliation_Name: "Example Organization",
                Affiliation_Identifier: "https://example.org"
            }],
            Person_Identifier: [{}]
        }];
        
        // Add License and Access Rights with default values
        metadata.License_Document = "Creative Commons Attribution 4.0 International Public License (CC-BY)";
        metadata.Access_Rights = "Publicly accessible";
        
        // Display the generated JSON
        jsonOutput.textContent = JSON.stringify(metadata, null, 2);
        jsonOutput.style.display = 'block';
        downloadBtn.style.display = 'inline-block';
    }
    
    // Function to download JSON
    function downloadJSON() {
        const jsonString = jsonOutput.textContent;
        const blob = new Blob([jsonString], { type: 'application/json' });
        const url = URL.createObjectURL(blob);
        
        const a = document.createElement('a');
        a.href = url;
        a.download = 'metadata.json';
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
    }
    
    // Function to reset the form
    function resetForm() {
        initializeForm();
        jsonOutput.textContent = '';
        jsonOutput.style.display = 'none';
        downloadBtn.style.display = 'none';
    }
}); 