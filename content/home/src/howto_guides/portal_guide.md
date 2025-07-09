# The NMDC Data Portal User Guide

## Introduction

The NMDC Data Portal (<https://data.microbiomedata.org>) provides
a resource for consistently processed multi-omics data that is
integrated to enable search, access, analysis, and download. Open-source
bioinformatics workflows are used to process raw multi-omics data and
produce interoperable and reusable annotated data from metagenome,
metatranscriptome, metaproteome, metabolome, and natural organic matter
characterizations. The NMDC Data Portal offers several search and
navigation components, and data can be downloaded through the graphical
user interface using an ORCiD authentication, with associated download
metrics, or retrieved through available RESTful APIs. All multi-omics
data are available under a Creative Commons 4.0 license, which enables
public use with attribution, as outlined in the NMDC Data Use Policy
(<https://microbiomedata.org/nmdc-data-use-policy>). The first
iteration of the NMDC Data Portal was released in March 2021 and 
continues to expand its data hosting and functionality on an ongoing basis.

There is a short video tutorial showing how to navigate the portal on
YouTube ([https://youtu.be/JV-8QWoL4aY](https://youtu.be/JV-8QWoL4aY)).

## User-Centered Design Process

The NMDC is a resource designed together with and for the scientific
community. We have engaged in extensive user research through interviews
and direct collaboration with the scientific community that have
informed the design, development, and display of data through the NMDC
Data Portal. This methodology (1) enables the scientific community to
provide feedback, iterative and continuous improvement of our systems,
and ensures that our systems enable a high level of scientific
productivity. Feedback collected from the scientific community during
user research can be linked to the features and
design directions found in the current release. Our community-centered
design approach ensures that the NMDC can evolve with the needs of the
microbiome research community, but will also be important for uncovering
creative design solutions, clarifying expectations, reducing redesign,
and perhaps most importantly, enabling shared ownership (2) of the NMDC.
We hope that this inclusive approach will enable us to expand our
engagements with the microbiome research community and the utility of
the NMDC Data Portal.

## Available Studies & Data

Data hostings include studies, biosamples, and multi-omics data from a breadth of
environmental microbiomes, spanning river sediments, subsurface shale
carbon reservoirs, plant-microbe associations, and temperate and
tropical soils.

## Standards

The NMDC team works closely with several standards groups and
organizations. We have adopted the Genomic Standards Consortium (GSC)
Minimum Information about any (x) Sequence (MIxS) templates (3). This
provides a standard data dictionary of sample descriptors (e.g.,
location, biome, altitude, depth) organized into seventeen environmental
packages (<https://www.gensc.org/pages/standards-intro.html>) for sequence data. The NMDC team has
mapped fields used to describe samples in the GOLD database to MIxS
version 6.1 elements. In addition, we are adopting the MIxS standards
for sequence data types (e.g., sequencing method, pcr primers and
conditions, etc.), and are leveraging standards and controlled
vocabularies developed by the Proteomics Standards Initiative (4), the
National Cancer Institute's Proteomic Data Commons
(<https://pdc.cancer.gov/data-dictionary/dictionary.html>), and the
Metabolomics Standards Initiative (5) for mass spectrometry data types
(e.g., ionization mode, mass resolution, scan rate, etc.).

### *MIxS environmental packages*

The GSC has developed standards for describing genomic and metagenomic
sequences, and the environment from which a biological sample
originates. These "[Minimum Information about any (x)
Sequence](https://www.gensc.org/pages/standards-intro.html)" (MIxS) packages provides
standardized sample descriptors (e.g., location, environment, elevation,
altitude, depth, etc.) for 17 different sample environments.

### *Environment Ontology (EnvO)*

EnvO (6) is a community-led ontology that represents environmental entities
such as biomes, environmental features, and environmental materials.
These EnvO entities are the recommended values for several of the
mandatory terms in the MIxS packages, often referred to as the "MIxS
triad".  Where appropriate, we also support terms from the Plant Ontology (PO) (7) and Uberon (8), 
an anatomical ontology. 

### *Genomes OnLine Database (GOLD)*

GOLD (9) is an open-access repository of genome, metagenome, and
metatranscriptome sequencing projects with their associated metadata.
Biosamples (defined as the physical material collected from an
environment) are described using a five-level ecosystem classification
path that goes from ecosystem down to the type of environmental material
that describes the sample.

## Data Types

A suite of data can be generated from available
biosamples, and the value of associating these data through a common
sample source enables researchers to probe function. The NMDC data
schema offers an approach to link data to their source
biosample (for example, multiple organic matter characterizations can be
generated from a single sample through extraction with various solvents;
e.g., chloroform, methanol, and water fractionation). For details on workflow processing, refer to 
our [workflow documentation](https://github.com/microbiomedata/workflow_documentation/tree/master/docs/chapters).

## Portal Functionality

### Faceted search and access

### *Search by investigator name*

[![](../_static/images/howto_guides/portal_guide/PI_search.png)](../_static/images/howto_guides/portal_guide/PI_search.png)

NMDC-linked data can be filtered by the associated principal
investigator by selecting 'PI Name' from the left query term bar. This
selection will display studies and samples associated with that PI, and
selecting the arrow on the right side of the study name will open up
more information about that study and that principal investigator.

### *Search by data generation information*

[![](../_static/images/howto_guides/portal_guide/instrument_name.png)](../_static/images/howto_guides/portal_guide/instrument_name.png)

[![](../_static/images/howto_guides/portal_guide/data_types.png)](../_static/images/howto_guides/portal_guide/data_types.png)

[![](../_static/images/howto_guides/portal_guide/processing_institution.png)](../_static/images/howto_guides/portal_guide/processing_institution.png)

Samples can be queried by various data generation terms
including instrument name, data type (processing runs sorted by data
type can also be queried using the bar plot on the main portal page),
processing institution, mass spectrometry method, and chromatography method.

### *Search by function*

[![](../_static/images/howto_guides/portal_guide/functional_search_2024.png)](../_static/images/howto_guides/portal_guide/functional_search_2024.png)

[![](../_static/images/howto_guides/portal_guide/kegg_search_2024.png)](../_static/images/howto_guides/portal_guide/kegg_search_2024.png)

Under 'Function' on the query term bar users are able to search by Kyoto Encyclopedia of Genes and Genomes (KEGG) (10) , the protein families database (Pfam) (11) , Clusters of Orthologous Genes (COG) (12) and Gene Ontology (GO) (13) terms to limit the query to samples with datasets that
include at least one of the listed terms. For KEGG we support search by orthologies, modules or pathways. For Pfam we support entries and clans. For COG we support terms, categories and pathways. Search by GO terms is supported via mappings to Pfam and KEGG terms.  Users may list multiple 
terms, but it is important to note that adding multiple terms will limit
the search to datasets that include at least one of those identifiers, not
all of the added terms.

### *Search by environmental descriptors*

[![](../_static/images/howto_guides/portal_guide/depth_meter.png)](../_static/images/howto_guides/portal_guide/depth_meter.png)

[![](../_static/images/howto_guides/portal_guide/date_slider.png)](../_static/images/howto_guides/portal_guide/date_slider.png)

[![](../_static/images/howto_guides/portal_guide/latitude.png)](../_static/images/howto_guides/portal_guide/latitude.png)

[![](../_static/images/howto_guides/portal_guide/longitude.png)](../_static/images/howto_guides/portal_guide/longitude.png)

[![](../_static/images/howto_guides/portal_guide/geographic_name.png)](../_static/images/howto_guides/portal_guide/geographic_name.png)

The query term bar also includes several environmental descriptor
filtering fields of where the samples were isolated from. Users can
filter by sample isolation depth, collection date, latitude and
longitude (can also filter by latitude and longitude using the
interactive map on the omics main page), as well as geographic location
name.

### *Search by ecosystem classifications*

[![](../_static/images/howto_guides/portal_guide/gold_classification.png)](../_static/images/howto_guides/portal_guide/gold_classification.png)

[![](../_static/images/howto_guides/portal_guide/mixs_env_triad.png)](../_static/images/howto_guides/portal_guide/mixs_env_triad.png)

Samples can also be queried by ecosystem classifications using GOLD
and/or MIxS Environmental Triad terms. Selecting GOLD classification in the query term bar
opens up a hierarchy that can be navigated through to select ecosystem
classification(s) of interest. Users can select everything under a
certain classification at any point, or can continue navigating to more
specific classifications. The Sankey diagram on the 'Environment' page
provides an interactive visualization of the GOLD classification system.

Similarly, ENVO, PO and Uberon terms are classification systems that can be used to
describe environments where samples were collected from which can be used to query the portal.  
Users can search by broad-scale environmental context, local environmental context, 
and environmental medium.  These terms are required by NMDC because they are required by
the GSC.

### *Search by workflow processing*

[![](../_static/images/howto_guides/portal_guide/metap_analysis_category.png)](../_static/images/howto_guides/portal_guide/metap_analysis_category.png)
Workflow results can be searched by metaproteomics analysis category. 


## Interactive visualizations

### *Data Type*

#### Barplot

[![](../_static/images/howto_guides/portal_guide/bar_plot.png)](../_static/images/howto_guides/portal_guide/bar_plot.png)

The barplot on the omics page displays the number of omics processing
runs (not number of samples) for each data type available: organic
matter, metagenomic, metatranscriptomic, proteomic, and metabolomic.
Selecting the bar of a data type will limit the search to just that data
type.

#### Geographic map

[![](../_static/images/howto_guides/portal_guide/geographic_map.png)](../_static/images/howto_guides/portal_guide/geographic_map.png)

The geographic map allows for samples to be queried by
the geographic location from which they were isolated. The map displays
the geographical location (latitude, longitude) of the sample collection
sites as clusters with colors corresponding to the number of samples
from that area. The map can be zoomed in and out of, and clusters can be
selected to focus on that specific area. After zooming and moving around
the map to a region of interest, selecting the 'Search this region'
button will limit the search to the current map bounds.

#### Temporal slider

[![](../_static/images/howto_guides/portal_guide/date.png)](../_static/images/howto_guides/portal_guide/date.png)

Samples can also be queried by a sample collection date range by
clicking and holding to select a date range. Sample
collection dates are grouped by month. The selected date range will be highlighted in gray.

#### Upset plot

[![](../_static/images/howto_guides/portal_guide/upset_plot.png)](../_static/images/howto_guides/portal_guide/upset_plot.png)

The upset plot on the omics page displays the number of samples that
have various combinations of associated data. The axis at the top
of the plot refers to the different omics types (MG: metagenomic, MT:
metatranscriptomic, MP: metaproteomic, MB: metabolomic, NOM: natural
organic matter) and the dots and lines in the graph below represent the
combinations of the data types. The numbers and bars on the right
side represent the number of samples searchable in the NMDC data portal
with each corresponding combination of omics data types. Clicking either on the bar 
portion or the number beside it will apply a filter.

### *Environment Page*

#### Sankey diagram

[![](../_static/images/howto_guides/portal_guide/sankey_diagram.png)](../_static/images/howto_guides/portal_guide/sankey_diagram.png)

On the environment page, the Sankey diagram displays the environments
that NMDC-linked samples were isolated from. This visualization is based
on the GOLD ecosystem classification path, and the diagram is fully
interactive, so environments of interest can be chosen at descending
levels of specificity. This will then limit your search to samples that
came from that selected environment.

### Download

### *Individual file*

[![](../_static/images/howto_guides/portal_guide/download_individual_file.png)](../_static/images/howto_guides/portal_guide/download_individual_file.png)

Various output data files are available from samples findable through
the NMDC that have been run through the NMDC standardized workflows.
Output files from each data type are sorted by the specific workflow
(e.g. Metagenome Assembly, Annotation) that was run and are each
available for download when the sample of interest is selected. Users
must log in with an ORCID account before downloading data.

### *Bulk download*

[![](../_static/images/howto_guides/portal_guide/bulk_download.png)](../_static/images/howto_guides/portal_guide/bulk_download.png)

In addition to the ability to download single output files from samples
run through the NMDC standardized workflows, the NMDC portal allows
users to perform bulk downloads on workflow output files. Once samples
of interest are down-selected through query terms, output files from
each NMDC standardized workflow run on those samples are available as
bulk downloads. Users must be logged in with an ORCID account before
downloading data.

## References

> 1.  Abras C, Maloney-Krichmar, D., Preece, J. 2004. User-Centered
>     Design. In Bainbridge W (ed), Encyclopedia of Human-Computer
>     Interaction. Sage Publications, Thousand Oaks.
> 2.  Preece J, Rogers, Y., & Sharp, H. 2002. Interaction design: Beyond
>     human-computer interaction. John Wiley & Sons, New York, NY.
> 3.  Yilmaz P, Kottmann R, Field D, Knight R, Cole JR, Amaral-Zettler
>     L, Gilbert JA, Karsch-Mizrachi I, Johnston A, Cochrane G, Vaughan
>     R, Hunter C, Park J, Morrison N, Rocca-Serra P, Sterk P, Arumugam
>     M, Bailey M, Baumgartner L, Birren BW, Blaser MJ, Bonazzi V, Booth
>     T, Bork P, Bushman FD, Buttigieg PL, Chain PSG, Charlson E,
>     Costello EK, Huot-Creasy H, Dawyndt P, DeSantis T, Fierer N,
>     Fuhrman JA, Gallery RE, Gevers D, Gibbs RA, Gil IS, Gonzalez A,
>     Gordon JI, Guralnick R, Hankeln W, Highlander S, Hugenholtz P,
>     Jansson J, Kau AL, Kelley ST, Kennedy J, Knights D, Koren O, et
>     al. 2011. Minimum information about a marker gene sequence
>     (MIMARKS) and minimum information about any (x) sequence (MIxS)
>     specifications. Nature Biotechnol. 29:415-420.
> 4.  Taylor CF, Paton NW, Lilley KS, Binz P-A, Julian RK, Jones AR, Zhu
>     W, Apweiler R, Aebersold R, Deutsch EW, Dunn MJ, Heck AJR, Leitner
>     A, Macht M, Mann M, Martens L, Neubert TA, Patterson SD, Ping P,
>     Seymour SL, Souda P, Tsugita A, Vandekerckhove J, Vondriska TM,
>     Whitelegge JP, Wilkins MR, Xenarios I, Yates JR,
>     Hermjakob H. 2007. The minimum information about a proteomics
>     experiment (MIAPE). Nature Biotechnol. 25:887-893.
> 5.  Sansone S-A, Fan T, Goodacre R, Griffin JL, Hardy NW,
>     Kaddurah-Daouk R, Kristal BS, Lindon J, Mendes P, Morrison N,
>     Nikolau B, Robertson D, Sumner LW, Taylor C, van der Werf M, van
>     Ommen B, Fiehn O, Members MSIB. 2007. The Metabolomics Standards
>     Initiative. Nature Biotechnol. 25:846-848.
> 6.  Buttigieg PL, Morrison N, Smith B, Mungall CJ, Lewis SE, Envo Consortium. 2013. The environment ontology: contextualising biological and biomedical entities. J Biomed Semantics 4:1–9.
> 7.  Cooper L, Jaiswal P. 2016. The Plant Ontology: a tool for plant genomics. Methods Mol Biol. 1374:89–114. https://doi.org/10.1007/978-1-4939-3167-5_5.
> 8.  Mungall CJ, Torniai C, Gkoutos GV, et al. 2012. Uberon, an integrative multi-species anatomy ontology. Genome Biol. 13:R5. https://doi.org/10.1186/gb-2012-13-1-r5.
> 9.  Mukherjee S, Stamatis D, Li CT, Ovchinnikova G, Kandimalla M, Handke V, Reddy A, Ivanova N, Woyke T, Eloe-Fadrosh EA, Chen I-MA, Kyrpides NC, Reddy TBK. 2024. Genomes OnLine Database (GOLD) v.10: new features and updates. Nucleic Acids Res. https://doi.org/10.1093/nar/gkae1000.
> 10.  Kanehisa M, Goto S. 2000. KEGG: Kyoto Encyclopedia of Genes and Genomes. Nucleic Acids Res. 28:27–30. https://doi.org/10.1093/nar/28.1.27.
> 11.  Bateman A, Coin L, Durbin R, Finn RD, Hollich V, Griffiths-Jones S, Khanna A, Marshall M, Moxon S, Sonnhammer ELL, Studholme DJ, Yeats C, Eddy SR. 2004. The Pfam protein families database. Nucleic Acids Res. 32:D138–D141. https://doi.org/10.1093/nar/gkh121.
> 12.  Tatusov RL, Galperin MY, Natale DA, Koonin EV. 2000. The COG database: a tool for genome-scale analysis of protein functions and evolution. Nucleic Acids Res. 28:33. https://doi.org/10.1093/nar/28.1.33.
> 13.  The Gene Ontology Consortium. 2019. The Gene Ontology resource: 20 years and still GOing strong. Nucleic Acids Res. 47:D330–D338. https://doi.org/10.1093/nar/gky1055.
