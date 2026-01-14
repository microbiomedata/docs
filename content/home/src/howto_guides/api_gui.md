# Using the NMDC API Graphical User Interface (GUI)

> Note: This guide was written with respect to NMDC API version `2.13.0`.

## Retrieving metadata using "Metadata access" API endpoints

Metadata describing NMDC data (e.g. studies, biosamples, data objects, etc.) may be retrieved with GET requests, using the [NMDC API Graphical User Interface (GUI)](https://api.microbiomedata.org/docs). The API GUI provides a guided user interface for direct access to NMDC metadata. People can use it to:

1. perform granular, targeted queries. This is especially helpful if a user has a query that may not be supported by the [NMDC Data Portal](https://data.microbiomedata.org/) yet.
2. learn about querying capabilities. It provides code snippets that can be used in scripts for programmatic access, i.e. the request `curl` commands and URLs provided in the responses (please see the examples below).

The API endpoints are organized into five groups:

1. **Metadata access** - Retrieve and manage metadata
2. **Workflow management** - Manage workflows and their execution
3. **Persistent identifiers** - Mint and manage persistent identifiers
4. **User accounts** - Create and manage user accounts
5. **System administration** - Retrieve system information

Please note that the endpoints discussed in this document were designed for use primarily by NMDC data consumers. For documentation describing other endpoints, primarily those designed for use by NMDC team members, please see the [NMDC Runtime documentation](https://docs.microbiomedata.org/runtime/).

API requests can include parameters to filter, sort, and organize the requested information. The _Metadata access_ section contains endpoints using different query syntax approaches. Some endpoints use [compact syntax](https://docs.openalex.org/how-to-use-the-api/get-lists-of-entities/filter-entity-lists) (for example, filtering biosamples for those having an "Ecosystem Category" of "Plants" would involve submitting a request containing `ecosystem_category:Plants` to the `GET /biosamples` endpoint). Other endpoints use [MongoDB-like query syntax](https://www.mongodb.com/docs/manual/tutorial/query-documents/) (for example, the same filter would look like `{"ecosystem_category": "Plants"}` using the `GET /nmdcschema/{collection_name}` endpoint with `collection_name` set to `biosample_set`).

The following sections describe endpoints in the _Metadata access_ groups.

### Endpoints with compact syntax

The _Metadata access_ section contains several endpoints that are dedicated to finding metadata
of a specific type. There are endpoints specific to finding [studies](https://w3id.org/nmdc/Study),
others specific to finding [biosamples](https://w3id.org/nmdc/Biosample), others for
finding [data objects](https://w3id.org/nmdc/DataObject/), and still others for
finding [planned processes](https://w3id.org/nmdc/PlannedProcess/).

When preparing to submit an API request to one of these endpoints, we recommend reviewing the
parameter options displayed in the endpoint's collapsible section on
the [API GUI](https://api.microbiomedata.org/docs).

Here are some of these endpoints that exist today:

- ![find get studies](../_static/images/howto_guides/api_gui/find_get_studies.png)
  The `GET /studies` endpoint is a general purpose way to retrieve NMDC studies based on parameters provided by the user. Studies can be filtered based on attributes of a Study, which are listed in the [NMDC Schema documentation](https://microbiomedata.github.io/nmdc-schema/Study/).
- ![find get studies by study_id](../_static/images/howto_guides/api_gui/find_get_studies_study_id.png)
  If you already know the study's `id` value, you can get just that one study by using the `GET /studies/{study_id}` endpoint.
- ![find get biosamples](../_static/images/howto_guides/api_gui/find_get_biosamples.png)
  The `GET /biosamples` endpoint is a general purpose way to retrieve biosample metadata using user-provided filter criteria. You can filter based upon the applicable [Biosample attributes](https://microbiomedata.github.io/nmdc-schema/Biosample/).
- ![find get biosamples by sample_id](../_static/images/howto_guides/api_gui/find_get_biosamples_sample_id.png)
  If you already know the biosample's `id` value, you can get just that one biosample by using the `GET /biosamples/{sample_id}`.
- ![find get data objects](../_static/images/howto_guides/api_gui/find_get_data_objects.png)
  To retrieve metadata about NMDC data objects (such as files, records, or omics data) the `GET /data_objects` endpoint may be used along with various parameters. You can filter based upon the applicable [Data Object attributes](https://microbiomedata.github.io/nmdc-schema/DataObject).
- ![find get data objects by data object_id](../_static/images/howto_guides/api_gui/find_data_objects_data_object_id.png)
  If you already know the data object's `id` value, you can get just that one data object metadata record by using the `GET /data_objects/{data_object_id}` endpoint.

For the latest, complete list of these endpoints, consult the "Metadata access" section of the [API GUI](https://api.microbiomedata.org/docs).

### Compact syntax endpoint example: Get all studies that have EMSL-related funding

_Note: "EMSL" stands for "Environmental Molecular Sciences Laboratory"._

1. Click on the dropdown arrow to the right side of the **`GET /studies`** endpoint.
   ![find example step 1](../_static/images/howto_guides/api_gui/find_example_step1.png)
2. Click **Try it out** in the upper right of the expanded endpoint box.
   ![find example step 2](../_static/images/howto_guides/api_gui/find_example_step2.png)
3. Enter the query parameters. In this case, we will enter "`funding_sources.search:EMSL`" into the **filter** parameter. The "`.search`" part tells the API you want it to perform a full-text search of `funding_sources` values, to find studies whose `funding_sources` values have the word "EMSL" in them.
4. Click **Execute**.
   ![find example step 3 and step 4](../_static/images/howto_guides/api_gui/find_example_step3and4.png)
5. View the API response body in JSON format. You can download it by clicking the **Download** button at the lower right, or copy the results by clicking the clipboard icon next to it. In this case, two studies were retrieved.
   ![find example step 5](../_static/images/howto_guides/api_gui/find_example_step5.png)

Note that an equivalent curl command and request URL are provided as well—complete with the request parameters—in case you want to perform the same request from a command line or script:

![find example note](../_static/images/howto_guides/api_gui/find_example_note.png)

### Endpoints with MongoDB-like query syntax

These [endpoints](https://api.microbiomedata.org/docs#/Metadata%20access) can be used to get and filter metadata from _collections_ (e.g. studies—which are in the `study_set` collection; biosamples—which are in the `biosample_set` collection; and data objects—which are in the `data_object_set` collection).

Unlike the compact syntax described above, the syntax for the filter parameter of these endpoints uses a [MongoDB-like query syntax](https://www.mongodb.com/docs/manual/tutorial/query-documents/).

When preparing to submit an API request to one of these endpoints, we recommend reviewing the
parameter options displayed in the endpoint's collapsible section on
the [API GUI](https://api.microbiomedata.org/docs).

Here are some of these endpoints that exist today:

- ![metadata get collection name](../_static/images/howto_guides/api_gui/metadata_get_collection_name.png)
  The `GET /nmdcschema/{collection_name}` endpoint is a general purpose way to retrieve NMDC metadata from a specific collection, given user-provided filter and projection criteria. Please see the [Collection Names](https://microbiomedata.github.io/nmdc-schema/Database/) that may be retrieved. Please note that metadata may only be retrieved about one collection at a time.
- ![metadata get doc_id](../_static/images/howto_guides/api_gui/metadata_get_doc_id.png)
  If you already know the `id` value of the metadata record (i.e. document) you want to retrieve, you can use the `GET /nmdcschema/ids/{doc_id}` to retrieve that record.
- ![metadata get collection_name doc_id](../_static/images/howto_guides/api_gui/metadata_get_collection_name_doc_id.png)
  If both the identifier and the collection name of the desired record is known, the `GET /nmdcschema/{collection_name}/{doc_id}` can be used to retrieve the record. The projection parameter is optionally available for this endpoint to retrieve only specific attributes from a record (e.g. to get only the _name_ of a study, rather than the _entire_ study).

### MongoDB-like query syntax endpoint example: Get all the biosamples that are part of the "1000 Soils Research Campaign" study sampled from Colorado

1. Click on the dropdown arrow to the right side of the **`GET /nmdcschema/{collection_name}`** endpoint.
   ![metadata example step1](../_static/images/howto_guides/api_gui/metadata_example_step1.png)
2. Click **Try it out** in the upper right of the expanded endpoint box.
   ![metadata example step2](../_static/images/howto_guides/api_gui/metadata_example_step2.png)
3. In order to enter the parameters, get the identifier for this study by navigating to the [1000 Soils Research Campaign study page](https://data.microbiomedata.org/details/study/nmdc:sty-11-28tm5d36) in the NMDC Data Portal and copying the study's `ID` value.
   ![metadata example step3](../_static/images/howto_guides/api_gui/metadata_example_step3.png)
4. Enter the parameters in the **`GET /nmdcschema/{collection_name}`** endpoint. For this example, we will input `biosample_set` into the **collection_name** parameter and `{"part_of": "nmdc:sty-11-28tm5d36", "geo_loc_name.has_raw_value": {"$regex": "Colorado"}}` into the **filter** parameter. See the [Biosample Class](https://microbiomedata.github.io/nmdc-schema/Biosample/) in the NMDC Schema to view the applicable biosample attributes (slots); for this example, they are `part_of` and `geo_loc_name.has_raw_value`. Note that `$regex` conducts a full text search for the word "Colorado" in the `geo_loc_name.has_raw_value` attribute.
5. Click **Execute**.
   ![metadata example step4](../_static/images/howto_guides/api_gui/metadata_example_step4and5.png)
6. View the results in JSON format, available to download by clicking **Download**; or copy the results by clicking the clipboard icon in the bottom right corner of the response. In this case, two studies were retrieved. Note that the curl and request URL are provided as well.
   ![metadata example step6](../_static/images/howto_guides/api_gui/metadata_example_step6.png)

## Retrieving metadata using a "Private" API endpoint

### "Public" versus "Private" API endpoints

The previous section was about some API endpoints that people could access without being logged into the NMDC API GUI.
People sometimes refer to endpoints like that as "public" API endpoints.

In contrast, this next section will be
about API endpoints that people can only access when they are logged into the NMDC API GUI. People sometimes refer to
API endpoints like these as "private" API endpoints.

We'll be using those terms—"public" and "private"—that way,
in this section.

### Logging into the NMDC API GUI

Here's how you can log into the NMDC API GUI:

1. Visit the [NMDC API GUI](https://api.microbiomedata.org/docs) in your web browser if you aren't already there.
   > Notice that the padlock icon on the "Authorize" button is _open_, which signifies that you [aren't](https://github.com/swagger-api/swagger-ui/issues/3322#issuecomment-321312974) currently logged
   > into the NMDC API.
2. Near the top of the page (above the endpoint sections), click the "Authorize" button.
   > A modal dialog will appear with available authorization options.
3. In the authorization modal, scroll down and click the "Login with ORCID" link.
   > The "Sign in to ORCID" page will appear in a new window or tab.
4. On the "Sign in to ORCID" page, enter and submit your ORCID credentials.
   > After successful authentication, the window will close and you'll return to the API GUI.
   > The padlock icon on the "Authorize" button will be _closed_, signifying that you are logged _into_ the NMDC API.

At this point, you are logged into the NMDC API GUI.

### Accessing a "private" API endpoint

**Now that you are logged into the NMDC API GUI**, you can use the NMDC API GUI to access "private" API endpoints.

Here's how you can access a "private" API endpoint:

1. Visit the [NMDC API GUI](https://api.microbiomedata.org/docs) in your web browser if you aren't already there.
2. Confirm the "Authorize" button has a _closed_ padlock icon on it, indicating that you are logged in.
3. Scroll down to the _Metadata access_ group of API endpoints.
4. Click the `POST /queries:run` section (which has a padlock icon next to it) to expand it.
5. Click the "Try it out" button next to the "Parameters" heading.
6. Populate the "Request body" field with the following JSON snippet:
   ```json
   {
        "find": "study_set",
        "filter": {"ecosystem_category": "Aquatic"}
   }
   ```
7. Click the "Execute" button.
   > The NMDC API GUI will send an HTTP request to the NMDC API and display the response from the NMDC API.
   >
   > Notice that the "Curl" command includes an `Authorization` header that contains your access token. If you were
   > making the API request via your command line instead of via the NMDC API GUI, you could include that same header
   > in order to access "private" API endpoints.
8. View the API response body in the "Response body" section.
   > The API response body is a JSON object having several properties, including `ok` and `cursor`. The `cursor` property
contains an object having a `firstBatch` property, which contains the array of results that met
the filter criteria that was specified in the API request. In this case, it contains all studies having
an `ecosystem_category` value of "`Aquatic`".
