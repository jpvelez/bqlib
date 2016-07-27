# bqlib

bqlib is a thin python wrapper over Google's BigQuery service. It allows you to
query BigQuery tables and get the results as python objects, save query results
to tables, views, or csv files, upload csv files to BQ tables, delete tables,
and more.

## Installation

For bqlib to work, it needs to be able to talk to BigQuery. To do that, you
need to install Google Cloud SDK, get access to you GCP projects, install the
and Google API python client (bqlib uses the client under the hood). To do all
this, just follow these instructions: https://cloud.google.com/compute/docs/tutorials/python-guide.
NOTE: Make sure that you add the BigQuery repository you want while running
`gcloud init`.

## API docs

bqlib supports the following API calls:

* `add_bq_dataset(dsname)`: Creates a dataset at a given BQ location
* `add_bq_tbl_from_qry(qry, tbl)`: For a given query (qry), generates a BQ table
  with name (tbl).
* `add_bq_vw_from_qry(qry, vw)`: For a given query (qry), generates a BQ view with
  name (vw).
* `add_bq_tbl_from_csv(file, tbl, schema)`: Uploads a csv (file) to a BQ table with
  name (tbl) using schema (schema).
* `remove_from_bq(obj)`: Removes an object (obj) from BQ repository.
* `query_bq(qry)`: Interactively runs BQ query (qry).
* `output_qry_to_csv(qry, out_file)`: Runs BQ query (qry), then outputs results to csv
  file (out_file).
