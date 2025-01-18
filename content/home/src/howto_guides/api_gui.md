# Using the NMDC API Graphical User Interface (GUI)

<!--
   TODO: Delete `.png` files from `content/home/src/_static/images/howto_guides/api_gui`
         that are no longer being referenced by this document.
-->

_Note: This guide was written while using `nmdc-runtime` version `1.2.0`._

## Retrieving Metadata using the ___Find___ and ___Metadata___ API Endpoints

Metadata describing NMDC data (e.g. studies, biosamples, data objects, etc.) may be retrieved with GET requests, using the **[NMDC API Graphical User Interface (GUI)](https://api.microbiomedata.org/docs)**. The API GUI provides a guided user interface for direct access to the NMDC data portal. It allows for:
1. performing highly granular and targeted queries directly. This is especially helpful if a user has a query that may not be supported by the [NMDC Data Portal](https://data.microbiomedata.org/) yet. 
2. interactive exploration of querying capabilities. It provides code snippets that can be used in scripts for programmatic access, i.e. the request `curl` commands and URLs provided in the responses (please see the examples below).

Please note that the endpoints discussed in this documentation were designed for use primarily by NMDC data consumers. For documentation describing other endpoints, primarily those designed for use by NMDC team members, please see the [NMDC Runtime documentation](https://docs.microbiomedata.org/runtime/).

API requests can include various parameters to filter, sort, and organize the requested information. The syntax of the parameters will vary, depending upon whether the API endpoint is a ___find___ endpoint or a ___metadata___ endpoint. ___Find___ endpoints are designed to use more [compact syntax](https://docs.openalex.org/how-to-use-the-api/get-lists-of-entities/filter-entity-lists) (for example, filtering biosamples for those having an "Ecosystem Category" of "Plants" would involve submitting a request containing `ecosystem_category:Plants` to the `GET /biosamples` endpoint). In contrast, ___metadata___ endpoints use [MongoDB-like query syntax](https://www.mongodb.com/docs/manual/tutorial/query-documents/) (e.g. the same filter would look like `{"ecosystem_category": "Plants"}` using the `GET /nmdcshema/{collection_name}` endpoint with `collection_name` set to `biosample_set`).

The following sections are about the ___find___ and ___metadata___ endpoints.

#### ___Find___ Endpoints

The [find endpoints](https://api.microbiomedata.org/docs#/find) are provided with NMDC metadata entities already specified. In other words, there are ___find___ endpoints specific to finding [studies](https://w3id.org/nmdc/Study), other ___find___ endpoints specific to finding [biosamples](https://w3id.org/nmdc/Biosample), ones for finding [data objects](https://w3id.org/nmdc/DataObject/), and ones for finding [planned processes](https://w3id.org/nmdc/PlannedProcess/). 

When preparing to submit an API request to a ___find___ endpoint, we recommend reviewing the parameter options
in that endpoint's section of the [API GUI](https://api.microbiomedata.org/docs). They're all listed in a section called "Find".

Here are some of the ___find___ endpoints that exist today:

![find get studies](../_static/images/howto_guides/api_gui/find_get_studies.png)
The `GET /studies` endpoint is a general purpose way to retrieve NMDC studies based on parameters provided by the user. Studies can be filtered and sorted based on the applicable [Study attributes](https://microbiomedata.github.io/nmdc-schema/Study/). <br/>

![find get studies by study_id](../_static/images/howto_guides/api_gui/find_get_studies_study_id.png)
If the study identifier is known, a study can be retrieved directly using the `GET /studies/{study_id}` endpoint. Note that only one study can be retrieved at a time using this method.<br/>

![find get biosamples](../_static/images/howto_guides/api_gui/find_get_biosamples.png)
The `GET /biosamples` endpoint is a general purpose way to retrieve biosample metadata using user-provided filter and sort criteria. Please see the applicable [Biosample attributes](https://microbiomedata.github.io/nmdc-schema/Biosample/).<br/>

![find get biosamples by sample_id](../_static/images/howto_guides/api_gui/find_get_biosamples_sample_id.png)
If the biosample identifier is known, a biosample can be retrieved directly using the `GET /biosamples/{sample_id}`. Note that only one biosample metadata record can be retrieved at a time using this method.<br/>

![find get data objects](../_static/images/howto_guides/api_gui/find_get_data_objects.png)
To retrieve metadata about NMDC data objects (such as files, records, or omics data) the `GET /data_objects` endpoint may be used along with various parameters. Please see the applicable [Data Object attributes](https://microbiomedata.github.io/nmdc-schema/DataObject).<br/>

![find get data objects by data object_id](../_static/images/howto_guides/api_gui/find_data_objects_data_object_id.png)
If the data object identifier is known, the metadata can be retrieved using the `GET /data_objects/{data_object_id}` endpoint. Note that only one data object metadata record may be retrieved at a time using this method.<br/>

For the latest, complete list of ___find___ endpoints, consult the "Find" section of the [API GUI](https://api.microbiomedata.org/docs).

#### Find endpoint example: Get all studies that have EMSL-related funding

_Note: "EMSL" stands for "Environmental Molecular Sciences Laboratory"._

1. Click on the dropdown arrow to the right side of the **`GET /studies`** endpoint.
   ![find example step 1](../_static/images/howto_guides/api_gui/find_example_step1.png)
2. Click **Try it out** in the upper right of the expanded endpoint box.
   ![find example step 2](../_static/images/howto_guides/api_gui/find_example_step2.png)
3. Enter the query parameters. In this case, we will enter "`funding_sources.search:EMSL`" into the **filter** parameter. The "`.search`" part tells the API you want it to perform a full-text search of `funding_sources` values, to find studies whose `funding_sources` values have the word "EMSL" in them.
4. Click **Execute**.
   ![find example step 3 and step 4](../_static/images/howto_guides/api_gui/find_example_step3and4.png)
5. View the API response body in JSON format. You can download it by clicking the **Download** button at the lower right, or copy the results by clicking the clipboard icon next to it. In this case, two studies were retrieved.
   ![find example step 5](../_static/images/howto_guides/api_gui/find_example_step5.png)<br/>

- Note that an equivalent curl command and request URL are provided as well—complete with the request parameters—in case you want to perform the same request from a command line or script:
  ![find example note](../_static/images/howto_guides/api_gui/find_example_note.png)

#### ___Metadata___ Endpoints

The [metadata endpoints](https://api.microbiomedata.org/docs#/metadata) can be used to get and filter metadata from collection set types (including studies, biosamples, activities, and data objects as discussed in the __find__ section). 

Unlike the compact syntax used in the __find__  endpoints, the syntax for the filter parameter of the metadata endpoints uses [MongoDB-like query syntax](https://www.mongodb.com/docs/manual/tutorial/query-documents/).

When preparing to submit an API request to a ___metadata___ endpoint, we recommend reviewing the parameter options
in that endpoint's section of the [API GUI](https://api.microbiomedata.org/docs). They're all listed in a section called "Metadata".

Here are some of the ___find___ endpoints that exist today:

![metadata get nmdcshema version](../_static/images/howto_guides/api_gui/metadata_get_nmdcschema_version.png)
To view the [NMDC Schema](https://microbiomedata.github.io/nmdc-schema/) version the database is currently using, try executing the `GET /nmdcschema/version` endpoint.<br/>

![metadata get collection stats](../_static/images/howto_guides/api_gui/metadata_get_collection_stats.png)
To get the NMDC Database collection statistics, like the total count of records in a collection or the size of the collection, try executing the `GET /nmdcschema/collection_stats` endpoint.<br/>

![metadata get collection name](../_static/images/howto_guides/api_gui/metadata_get_collection_name.png)
The `GET /nmdcschema/{collection_name}` endpoint is a general purpose way to retrieve metadata about a specified collection given user-provided filter and projection criteria. Please see the [Collection Names](https://microbiomedata.github.io/nmdc-schema/Database/) that may be retrieved. Please note that metadata may only be retrieved about one collection at a time.<br/>

![metadata get doc_id](../_static/images/howto_guides/api_gui/metadata_get_doc_id.png)
If the identifier of the record is known, the `GET /nmdcshema/ids/{doc_id}` can be used to retrieve the specified record. Note that only one identifier may be used at a time, and therefore, only one record may be retrieved at a time using this method.<br/>

![metadata get collection_name doc_id](../_static/images/howto_guides/api_gui/metadata_get_collection_name_doc_id.png)
If both the identifier and the collection name of the desired record is known, the `GET /nmdcschema/{collection_name}/{doc_id}` can be used to retrieve the record. The projection parameter is optionally available for this endpoint to retrieve only desired attributes from a record. Please note that only one record can be retrieved at one time using this method.<br/>

For the latest, complete list of ___metadata___ endpoints, consult the "Metadata" section of the [API GUI](https://api.microbiomedata.org/docs).

#### Metadata endpoint example: Get all the biosamples that are part of the "1000 Soils Research Campaign" study sampled from Colorado

1. Click on the dropdown arrow to the right side of the **`GET /nmdcschema/{collection_name}`** endpoint.
   ![metadata example step1](../_static/images/howto_guides/api_gui/metadata_example_step1.png)
2. Click **Try it out** in the upper right of the expanded endpoint box.
   ![metadata example step2](../_static/images/howto_guides/api_gui/metadata_example_step2.png)
3. In order to enter the parameters, get the identifier for this study by navigating to the [1000 Soils Research Campaign study page](https://data.microbiomedata.org/details/study/nmdc:sty-11-28tm5d36) in the NMDC Data Portal and copying the `ID`.
   ![metadata example step3](../_static/images/howto_guides/api_gui/metadata_example_step3.png)
4. Enter the parameters in the **`GET /nmdcschema/{collection_name}`** endpoint. For this example, we will input `biosample_set` into the **collection_name** parameter and `{"part_of": "nmdc:sty-11-28tm5d36", "geo_loc_name.has_raw_value": {"$regex": "Colorado"}}` into the **filter** parameter. See the [Biosample Class](https://microbiomedata.github.io/nmdc-schema/Biosample/) in the NMDC Schema to view the applicable biosample attributes (slots); for this example, they are `part_of` and `geo_loc_name.has_raw_value`. Note that `$regex` conducts a full text search for the word "Colorado" in the `geo_loc_name.has_raw_value` attribute.
5. Click **Execute**.
   ![metadata example step4](../_static/images/howto_guides/api_gui/metadata_example_step4and5.png)
6. View the results in JSON format, available to download by clicking **Download**; or copy the results by clicking the clipboard icon in the bottom right corner of the response. In this case, two studies were retrieved. Note that the curl and request URL are provided as well.
   ![metadata example step6](../_static/images/howto_guides/api_gui/metadata_example_step6.png)
