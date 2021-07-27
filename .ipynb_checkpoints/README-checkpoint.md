Hello candidate for the SuLab and the WuLab at Scripps Research,

Here is a small programming task for you to complete. This may or may not overlap with your past experience, but there is plenty of documentation online that would help you complete this. This task is representative of the type of project that the person this position would perform, at least initially.

We have prepared a small collection of dataset metadata here: https://www.dropbox.com/s/3c221ucnqlf1uzm/harvard_dataverse.json?dl=0

You should load and index this data file in Elasticsearch. Then, you should create a python web API that provides programmatic access to that data. The API should allow users to query by two methods. First, users should be able to query by a specific dataset identifier as indicated by the '@id' field in the data file (e.g., "https://doi.org/10.11588/data/0HJAJS"). Second, users should be able to query by a specific field in the JSON object (e.g., datasets with "Earth and Environmental Sciences" in the keywords). The output of this web API by either query method should be the matching metadata object(s) in JSON format.

There is also a bonus point if you can achieve:

create a customized mapping file to index metadata objects so that
index "funder.name" field as keyword (if possible, case-insensitive keyword) and allow passing a "facet=funder.name" parameter to the query endpoint to return the facet results on "funder.name".
The rest of fields should still be indexed and searchable as the default behavior



Assumptions:
- only 1 search bar needed (it is not a nested search)
