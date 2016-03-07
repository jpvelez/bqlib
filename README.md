# bqlib #

This repository has the needed processes to interface with BigQuery
via Python. Before any processes can be run, the installation process
must be completed.

## Installation ##

First, you need to enable Google Cloud SDK and Python API access
following the instructions (see <https://cloud.google.com/compute/docs/tutorials/python-guide>).
Make sure that you add the BQ repository while running ```gcloud init```.

Lastly, run these commands in the bqlib directory:

```
export dir=`python -m site --user-site`
mkdir -p $dir
cp bqlib.py $dir
```

## Included Subprocesses ##

* add_bq_dataset(dsname): Creates a dataset at a given BQ location
* add_bq_tbl_from_qry(qry,tbl): For a given query (qry), generates a BQ table with
  name (tbl).
* add_bq_vw_from_qry(qry,vw): For a given query (qry), generates a BQ view with
  name (vw).
* add_bq_tbl_from_csv(file,tbl,schema): Uploads a csv (file) to a BQ table with
  name (tbl) using schema (schema).
* remove_from_bq(obj): Removes an object (obj) from BQ repository.
* query_bq(qry): Interactively runs BQ query (qry).
* output_qry_to_csv(qry,out_file): Runs BQ query (qry), then outputs results to csv
  file (out_file).