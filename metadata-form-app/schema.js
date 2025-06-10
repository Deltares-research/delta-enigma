// This file contains the metadata schema for the Delta Enigma project
const metadataSchema = {
    "$id": "https://yoda.surf.nl/schemas/delta-enigma-1/metadata.json",
    "$schema": "http://json-schema.org/draft-07/schema",
    "definitions": {
        "stringNormal": {
            "type": "string",
            "maxLength": 255
        },
        "stringNormalNullable": {
            "type": ["string", "null"],
            "maxLength": 255
        },
        "stringLong": {
            "type": "string",
            "maxLength": 2700
        },
        "optionsAcquisitionSensor": {
            "type": "string",
            "enum": [
                "13h Repeat transect ADCP",
                "3D laser scanner",
                "ADCP",
                "ADV",
                "AQUAscat",
                "AQUAscat 1000R",
                "Autonomuous ship",
                "Backpack laser scanner",
                "Benthic sampling",
                "Biolive flume",
                "Camera observations",
                "Continuous centrifuge SPM",
                "Continuous flow centrifuge",
                "CTD",
                "Current flume (PIV system)",
                "Field sediment sampling",
                "Fluorimeter",
                "Global change mesocosms",
                "Groundwater",
                "Horizontal ADCPs",
                "Lidar drone",
                "LISST200X",
                "Luminescence lab",
                "Metronome",
                "Microtec MRB Camsizer p4",
                "Microtec MRB Camsizer XL",
                "Multibeam",
                "Multibeam bedload transport sampling",
                "Multibeam CTD casts",
                "Multisprectral drone",
                "NDVI",
                "OBS",
                "Optical sediment microscope",
                "Pressure sensor",
                "Repeat transect ADCP",
                "Salinity",
                "Salinity sensor",
                "Sediment grain size analysis",
                "Soil moisture",
                "Tilt sensor",
                "Unmanned surface vessel",
                "Vegetation cameras",
                "Vegetation cameras dune foot",
                "Vegetation drone surveys",
                "Vegetation field quadrants",
                "Vegetation recording drone",
                "Vibrocores sediment bed",
                "Water sampler",
                "Wave current flume",
                "Weather station"
            ]
        },
        "optionsDataType": {
            "type": "string",
            "enum": [
                "Dataset",
                "Series",
                "Service"
            ]
        },
        "optionsNameIdentifierScheme": {
            "type": "string",
            "enum": [
                "ORCID",
                "DAI",
                "Author identifier (Scopus)",
                "ResearcherID (Web of Science)",
                "ISNI"
            ]
        },
        "optionsPersistentIdentifierScheme": {
            "type": "string",
            "enum": [
                "ARK",
                "arXiv",
                "bibcode",
                "DOI",
                "EAN13",
                "EISSN",
                "Handle",
                "IGSN",
                "ISBN",
                "ISSN",
                "ISTC",
                "LISSN",
                "LSID",
                "PMID",
                "PURL",
                "UPC",
                "URL",
                "URN"
            ]
        },
        "optionsDomain": {
            "type": "string",
            "enum": [
                "Administration and dimensions",
                "Atmosphere",
                "Biological oceanography",
                "Chemical oceanography",
                "Cross-discipline",
                "Cryosphere",
                "Environment",
                "Human activities",
                "Marine geology",
                "Physical oceanography",
                "Terrestrial"
            ]
        },
        "optionsTopicCategory": {
            "type": "string",
            "enum": [
                "Acoustics",
                "Administration and dimensions",
                "Amino acids",
                "Aquaculture",
                "Area Management/Designation",
                "Atmospheric chemistry",
                "Bacteria and viruses",
                "Biota abundance, biomass and diversity",
                "Biota composition",
                "Birds, mammals and reptiles",
                "Cables",
                "Carbon, nitrogen and phosphorus",
                "Carbonate system",
                "Construction and structures",
                "Cryosphere",
                "Cultural Heritage",
                "Currents",
                "Disease, damage and mortality",
                "Dissolved gases",
                "Energy",
                "Fatty acids",
                "Field geophysics",
                "Fish",
                "Fisheries",
                "Fluxes",
                "Geochronology and stratigraphy",
                "Geothermal measurements",
                "Gravity, magnetics and bathymetry",
                "Habitat",
                "Halocarbons (including freons)",
                "Hydrocarbon extraction",
                "Hydrocarbons",
                "Isotopes",
                "Macroalgae and seagrass",
                "Marine geomorphology",
                "Metal and metalloid concentrations",
                "Meteorology",
                "Microzooplankton",
                "Mining",
                "Nutrients",
                "Optical properties",
                "Other biological measurements",
                "Other inorganic chemical measurements",
                "Other organic chemical measurements",
                "Other physical oceanographic measurements",
                "PCBs and organic micropollutants",
                "Palaeoclimate",
                "Phytoplankton and microphytobenthos",
                "Pigments",
                "Pipelines",
                "Pollution",
                "Rate measurements (including production, excretion and grazing)",
                "Rock and sediment biota",
                "Rock and sediment chemistry",
                "Rock and sediment lithology and mineralogy",
                "Rock and sediment physical properties",
                "Rock and sediment sedimentology",
                "Salt extraction",
                "Sea level",
                "Sediment pore water chemistry",
                "Sedimentation and erosion processes",
                "Sonar and seismics",
                "Suspended particulate material",
                "Terrestrial",
                "Tourism",
                "Transport",
                "Underwater photography",
                "Water column temperature and salinity",
                "Waves",
                "Zooplankton"
            ]
        },
        "optionsTypeNoContact": {
            "type": "string",
            "enum": [
                "Custodian",
                "Distributor",
                "Orginator",
                "Principal investigator",
                "Processor",
                "Publisher",
                "Resource provider",
                "Rights holder",
                "User"
            ]
        },
        "optionsLicense": {
            "type": "string",
            "enum": [
                "Creative Commons Attribution 4.0 International Public License (CC-BY)",
                "Creative Commons Attribution-ShareAlike 4.0 International Public License (CC-BY-SA)",
                "Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International Public License (CC-BY-SA-NC)",
                "Creative Commons Zero v1.0 Universal (CC-0)",
                "Open Data Commons Attribution License v1.0 (ODC-By)",
                "Custom"
            ]
        },
        "optionsAccess_Rights": {
            "type": "string",
            "enum": [
                "Publicly accessible",
                "Has access restrictions",
                "Not public"
            ]
        },
        "optionsApplicable_Legislation": {
            "type": "string",
            "enum": [
                "High-Value Datasets",
                "INSPIRE",
                "Data Governance Act (DGA)",
                "General Data Protection Regulation (GDPR / AVG)",
                "Kaderrichtlijn Water",
                "Wet openbaarheid van bestuur (WOB)",
                "Wet hergebruik van overheidsinformatie (Who)",
                "Wet markt en overheid (Wmo)",
                "Wet implementatie open data richtlijn"
            ]
        },
        "optionsRelationType": {
            "type": "string",
            "enum": [
                "IsCitedBy",
                "Cites",
                "IsSupplementTo",
                "IsSupplementedBy",
                "IsContinuedBy",
                "Continues",
                "IsNewVersionOf",
                "IsPreviousVersionOf",
                "IsPartOf",
                "HasPart",
                "IsReferencedBy",
                "References",
                "IsDocumentedBy",
                "Documents",
                "IsCompiledBy",
                "Compiles",
                "IsVariantFormOf",
                "IsOriginalFormOf",
                "IsIdenticalTo",
                "HasMetadata",
                "IsMetadataFor",
                "Reviews",
                "IsReviewedBy",
                "IsDerivedFrom",
                "IsSourceOf",
                "Describes",
                "IsDescribedBy",
                "HasVersion",
                "IsVersionOf",
                "Requires",
                "IsRequiredBy",
                "Obsoletes",
                "IsObsoletedBy"
            ]
        },
        "optionsReferenceSystem": {
            "type": "string",
            "enum": [
                "WGS84",
                "Rijksdriehoekstelsel",
                "ETRS89"
            ],
            "default": "WGS84"
        },
        "optionsWorkPackage": {
            "type": "string",
            "enum": [
                "WP1. Sustained high-resolution field observations in rivers",
                "WP2. Sustained high-resolution field observations in estuaries",
                "WP3. Sustained high-resolution field observations on beaches and dunes",
                "WP4. Observation of extreme events",
                "WP5. Laboratory equipment for process studies",
                "WP6. Productive Knowledge Interaction (PROD) Facility",
                "WP7. ICT backbone for FAIR data management",
                "WP8. Project Governance"
            ]
        }
    },
    "title": "",
    "type": "object",
    "additionalProperties": false,
    "required": [
        "links",
        "Title",
        "Description",
        "Documentation",
        "Domain",
        "Topic_Category",
        "Version",
        "Language",
        "Temporal_Coverage",
        "Geographical_Coverage",
        "Acquisition_Sensor",
        "Related_Resource",
        "Creation_Date",
        "Release_Date",
        "Resource_Type",
        "Creator",
        "Contact_Point",
        "License_Document",
        "Access_Rights"
    ],
    "properties": {
        "links": {
            "type": "array",
            "minItems": 1,
            "maxItems": 1,
            "items": {
                "type": "object",
                "additionalProperties": false,
                "required": ["rel", "href"],
                "properties": {
                    "rel": { "const": "describedby" },
                    "href": { "const": "https://yoda.surf.nl/schemas/delta-enigma-1/metadata.json" }
                }
            }
        },
        "Title": {
            "$ref": "#/definitions/stringNormal",
            "title": "Title"
        },
        "Description": {
            "$ref": "#/definitions/stringLong",
            "title": "Abstract",
            "default": "[Summarize the data collection process and the data content]"
        },
        "Documentation": {
            "type": "array",
            "minItems": 1,
            "title": "Dataset Documentation",
            "items": {
                "type": "object",
                "additionalProperties": false,
                "properties": {
                    "Title_document": {
                        "$ref": "#/definitions/stringNormal",
                        "title": "Title document"
                    },
                    "Link_document": {
                        "$ref": "#/definitions/stringNormal",
                        "title": "Link document"
                    }
                }
            }
        },
        "Domain": {
            "type": "array",
            "minItems": 1,
            "title": "Domain",
            "items": {
                "$ref": "#/definitions/optionsDomain",
                "title": "Domain field"
            }
        },
        "Topic_Category": {
            "type": "array",
            "minItems": 1,
            "title": "Topic Category",
            "items": {
                "$ref": "#/definitions/optionsTopicCategory",
                "title": "Topic Category"
            }
        },
        "Work_Package": {
            "$ref": "#/definitions/optionsWorkPackage",
            "title": "Work Package"
        },
        "Version": {
            "$ref": "#/definitions/stringNormal",
            "title": "Version",
            "default": "1.0"
        },
        "Language": {
            "$ref": "#/definitions/stringNormal",
            "title": "Language of the data",
            "default": "en - English"
        },
        "Temporal_Coverage": {
            "type": "object",
            "additionalProperties": false,
            "title": "Collection period",
            "required": [
                "Start_Date",
                "End_Date"
            ],
            "properties": {
                "Start_Date": {
                    "type": "string",
                    "format": "date",
                    "title": "Start date"
                },
                "End_Date": {
                    "type": "string",
                    "format": "date",
                    "title": "End date"
                }
            }
        },
        "Geographical_Coverage": {
            "type": "array",
            "minItems": 1,
            "items": {
                "type": "object",
                "additionalProperties": false,
                "properties": {
                    "geoLocationBox": {
                        "type": "object",
                        "additionalProperties": false,
                        "title": "Geographical coverage",
                        "properties": {
                            "northBoundLatitude": {
                                "type": "number"
                            },
                            "westBoundLongitude": {
                                "type": "number"
                            },
                            "southBoundLatitude": {
                                "type": "number"
                            },
                            "eastBoundLongitude": {
                                "type": "number"
                            }
                        }
                    },
                    "Description_Spatial": {
                        "$ref": "#/definitions/stringNormal",
                        "title": "Description"
                    },
                    "Reference_System": {
                        "$ref": "#/definitions/optionsReferenceSystem",
                        "title": "Reference System"
                    }
                }
            }
        },
        "Expedition": {
            "type": "array",
            "title": "Expedition / Collection",
            "items": {
                "$ref": "#/definitions/stringNormal",
                "title": "Expedition / Collection",
                "default": null
            }
        },
        "Acquisition_Sensor": {
            "type": "array",
            "minItems": 1,
            "title": "Acquisition sensor",
            "items": {
                "$ref": "#/definitions/optionsAcquisitionSensor",
                "title": "Acquisition sensor",
                "default": null
            }
        },
        "Keyword": {
            "type": "array",
            "minItems": 1,
            "title": "Free keyword",
            "items": {
                "$ref": "#/definitions/stringNormal",
                "title": "Free keyword",
                "default": null
            }
        },
        "Related_Resource": {
            "title": "Related resource",
            "type": "array",
            "minItems": 1,
            "items": {
                "type": "object",
                "additionalProperties": false,
                "properties": {
                    "Relation_Type": {
                        "$ref": "#/definitions/optionsRelationType",
                        "title": "Related resource"
                    },
                    "Title": {
                        "$ref": "#/definitions/stringLong",
                        "title": "Title"
                    },
                    "Persistent_Identifier": {
                        "type": "object",
                        "additionalProperties": false,
                        "title": "Persistent identifier",
                        "properties": {
                            "Identifier_Scheme": {
                                "$ref": "#/definitions/optionsPersistentIdentifierScheme",
                                "title": "Type"
                            },
                            "Identifier": {
                                "$ref": "#/definitions/stringNormal",
                                "title": "Identifier"
                            }
                        }
                    }
                }
            }
        },
        "Funding_Reference": {
            "type": "array",
            "minItems": 1,
            "title": "Funding reference",
            "items": {
                "type": "object",
                "additionalProperties": false,
                "properties": {
                    "Funder_Name": {
                        "$ref": "#/definitions/stringNormal",
                        "title": "Funder name"
                    },
                    "Award_Number": {
                        "$ref": "#/definitions/stringNormal",
                        "title": "Grant number"
                    },
                    "Award_Name": {
                        "$ref": "#/definitions/stringNormal",
                        "title": "Grant name"
                    }
                }
            }
        },
        "Creation_Date": {
            "type": "string",
            "format": "date",
            "title": "Creation date"
        },
        "Release_Date": {
            "type": "string",
            "format": "date",
            "title": "Release date"
        },
        "Applicable_Legislation": {
            "$ref": "#/definitions/optionsApplicable_Legislation",
            "title": "Applicable legislation"
        },
        "Resource_Type": {
            "$ref": "#/definitions/optionsDataType",
            "title": "Resource type",
            "default": "Dataset"
        },
        "Creator": {
            "type": "array",
            "minItems": 1,
            "items": {
                "type": "object",
                "additionalProperties": false,
                "required": [
                    "Name",
                    "Affiliation",
                    "Person_Identifier"
                ],
                "properties": {
                    "Name": {
                        "type": "object",
                        "additionalProperties": false,
                        "required": [
                            "Given_Name",
                            "Family_Name"
                        ],
                        "properties": {
                            "Given_Name": {
                                "$ref": "#/definitions/stringNormal",
                                "title": "First Name"
                            },
                            "Family_Name": {
                                "$ref": "#/definitions/stringNormal",
                                "title": "Family Name"
                            }
                        }
                    },
                    "Email": {
                        "type": "string",
                        "title": "E-mail"
                    },
                    "URL": {
                        "type": "string",
                        "title": "URL"
                    },
                    "Affiliation": {
                        "type": "array",
                        "minItems": 1,
                        "default": [],
                        "items": {
                            "type": "object",
                            "additionalProperties": false,
                            "required": ["Affiliation_Name", "Affiliation_Identifier"],
                            "properties": {
                                "Affiliation_Name": {
                                    "$ref": "#/definitions/stringNormal",
                                    "title": "Affiliation Name"
                                },
                                "Affiliation_Identifier": {
                                    "$ref": "#/definitions/stringNormal",
                                    "title": "Affiliation Identifier"
                                }
                            }
                        }
                    },
                    "Person_Identifier": {
                        "title": "Person identifier",
                        "type": "array",
                        "minItems": 1,
                        "items": {
                            "type": "object",
                            "additionalProperties": false,
                            "properties": {
                                "Name_Identifier_Scheme": {
                                    "$ref": "#/definitions/optionsNameIdentifierScheme",
                                    "title": "Type"
                                },
                                "Name_Identifier": {
                                    "$ref": "#/definitions/stringNormal",
                                    "title": "Identifier"
                                }
                            }
                        }
                    }
                }
            }
        },
        "Contributor": {
            "type": "array",
            "minItems": 1,
            "items": {
                "type": "object",
                "additionalProperties": false,
                "properties": {
                    "Name": {
                        "type": "object",
                        "additionalProperties": false,
                        "required": [
                            "Given_Name",
                            "Family_Name"
                        ],
                        "properties": {
                            "Given_Name": {
                                "$ref": "#/definitions/stringNormal",
                                "title": "First Name"
                            },
                            "Family_Name": {
                                "$ref": "#/definitions/stringNormal",
                                "title": "Family Name"
                            }
                        }
                    },
                    "Type": {
                        "$ref": "#/definitions/optionsTypeNoContact",
                        "title": "Contributor type"
                    },
                    "Email": {
                        "type": "string",
                        "title": "E-mail"
                    },
                    "URL": {
                        "type": "string",
                        "title": "URL"
                    },
                    "Affiliation": {
                        "type": "array",
                        "minItems": 1,
                        "default": [],
                        "items": {
                            "type": "object",
                            "additionalProperties": false,
                            "properties": {
                                "Affiliation_Name": {
                                    "$ref": "#/definitions/stringNormal",
                                    "title": "Affiliation Name"
                                },
                                "Affiliation_Identifier": {
                                    "$ref": "#/definitions/stringNormal",
                                    "title": "Affiliation Identifier"
                                }
                            }
                        }
                    },
                    "Person_Identifier": {
                        "title": "Person identifier",
                        "type": "array",
                        "minItems": 1,
                        "items": {
                            "type": "object",
                            "additionalProperties": false,
                            "properties": {
                                "Name_Identifier_Scheme": {
                                    "$ref": "#/definitions/optionsNameIdentifierScheme",
                                    "title": "Type"
                                },
                                "Name_Identifier": {
                                    "$ref": "#/definitions/stringNormal",
                                    "title": "Identifier"
                                }
                            }
                        }
                    }
                }
            }
        },
        "Contact_Point": {
            "type": "array",
            "minItems": 1,
            "items": {
                "type": "object",
                "additionalProperties": false,
                "required": [
                    "Name",
                    "Affiliation"
                ],
                "properties": {
                    "Name": {
                        "type": "object",
                        "additionalProperties": false,
                        "required": [
                            "Given_Name",
                            "Family_Name"
                        ],
                        "properties": {
                            "Given_Name": {
                                "$ref": "#/definitions/stringNormal",
                                "title": "First Name"
                            },
                            "Family_Name": {
                                "$ref": "#/definitions/stringNormal",
                                "title": "Family Name"
                            }
                        }
                    },
                    "Position": {
                        "type": "string",
                        "title": "Position"
                    },
                    "Email": {
                        "type": "string",
                        "title": "E-mail"
                    },
                    "Affiliation": {
                        "type": "array",
                        "minItems": 1,
                        "default": [],
                        "items": {
                            "type": "object",
                            "additionalProperties": false,
                            "required": ["Affiliation_Name", "Affiliation_Identifier"],
                            "properties": {
                                "Affiliation_Name": {
                                    "$ref": "#/definitions/stringNormal",
                                    "title": "Affiliation Name"
                                },
                                "Affiliation_Identifier": {
                                    "$ref": "#/definitions/stringNormal",
                                    "title": "Affiliation Identifier"
                                }
                            }
                        }
                    },
                    "Person_Identifier": {
                        "title": "Person identifier",
                        "type": "array",
                        "minItems": 1,
                        "items": {
                            "type": "object",
                            "additionalProperties": false,
                            "properties": {
                                "Name_Identifier_Scheme": {
                                    "$ref": "#/definitions/optionsNameIdentifierScheme",
                                    "title": "Type"
                                },
                                "Name_Identifier": {
                                    "$ref": "#/definitions/stringNormal",
                                    "title": "Identifier"
                                }
                            }
                        }
                    }
                }
            }
        },
        "License_Document": {
            "$ref": "#/definitions/optionsLicense",
            "title": "License Document",
            "default": "Creative Commons Attribution 4.0 International Public License (CC-BY)"
        },
        "Access_Rights": {
            "$ref": "#/definitions/optionsAccess_Rights",
            "title": "Access Rights",
            "default": "Publicly accessible"
        },
        "Rights": {
            "$ref": "#/definitions/stringLong",
            "title": "Rights Statement"
        }
    }
};

// Example metadata for reference
const metadataExample = {
    "links": [
        {
            "rel": "describedby", 
            "href": "https://yoda.surf.nl/schemas/delta-enigma-1/metadata.json"
        }
    ], 
    "Description": "[Summarize the data collection process and the data content]", 
    "Documentation": [
        {}
    ], 
    "Domain": [
        "Bathymetry"
    ], 
    "Topic_Category": [
        "Geoscientific Information"
    ], 
    "Version": "1.0", 
    "Language": "en - English", 
    "Temporal_Coverage": {
        "Start_Date": "2025-02-19", 
        "End_Date": "2025-02-20"
    }, 
    "Geographical_Coverage": [
        {
            "Reference_System": "WGS84", 
            "geoLocationBox": {
                "northBoundLatitude": 52.61915208081608, 
                "westBoundLongitude": 4.619035696145405, 
                "southBoundLatitude": 52.61915208081608, 
                "eastBoundLongitude": 4.619035696145405
            }, 
            "Description_Spatial": "Egmond"
        }
    ], 
    "Acquisition_Sensor": [
        "Water sampler"
    ], 
    "Keyword": [
        "Water sampler"
    ], 
    "Related_Resource": [
        {}
    ], 
    "Funding_Reference": [
        {}
    ], 
    "Resource_Type": "Dataset", 
    "Creator": [
        {
            "Name": {
                "Given_Name": "Vincent ", 
                "Family_Name": "Brunst"
            }, 
            "Affiliation": [
                {
                    "Affiliation_Name": "Utrecht University", 
                    "Affiliation_Identifier": "https://ror.org/04pp8hn57"
                }
            ], 
            "Person_Identifier": [
                {}
            ]
        }
    ], 
    "Contributor": [
        {
            "Affiliation": [
                {}
            ], 
            "Person_Identifier": [
                {}
            ], 
            "Name": {
                "Given_Name": "Vincent", 
                "Family_Name": "Brunst"
            }
        }
    ], 
    "Contact_Point": [
        {
            "Name": {
                "Given_Name": "Vincent ", 
                "Family_Name": "Brunst"
            }, 
            "Affiliation": [
                {
                    "Affiliation_Name": "Utrecht University", 
                    "Affiliation_Identifier": "https://ror.org/04pp8hn57"
                }
            ], 
            "Person_Identifier": [
                {}
            ]
        }
    ], 
    "License_Document": "Creative Commons Attribution 4.0 International Public License (CC-BY)", 
    "Access_Rights": "Publicly accessible", 
    "Title": "Water sampler 1 - Egmond", 
    "Work_Package": "WP1. Sustained high-resolution field observations in rivers", 
    "Creation_Date": "2025-02-19", 
    "Release_Date": "2025-02-28"
}; 