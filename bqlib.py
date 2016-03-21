import subprocess
import csv
import sys

def run_subprocess(cmd):
	p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True)
	output = p.stdout.read()
	print output

def add_bq_dataset(dsname):
	mycmd = "bq mk -d --data_location=EU %s" % (dsname)
	print "Creating dataset " + dsname + " with " + mycmd
	run_subprocess(mycmd)
		
def add_bq_tbl_from_qry(qry, tbl):
	mycmd = "bq query --allow_large_results --replace --destination_table="+tbl + " \"" + qry + "\""
	print "For tbl " + tbl + " calling " + mycmd
	run_subprocess(mycmd)

def add_bq_vw_from_qry(qry, vw):
	mycmd = "bq mk --view=\"" + qry + "\" -f " + vw
	print "For view " + vw + " calling " + mycmd
	run_subprocess(mycmd)

def add_bq_tbl_from_csv(file, tbl, schema):
	mycmd = "bq load --encoding=UTF-8 --source_format=CSV \"" + tbl + "\" \"" + file + "\" \"" + schema + "\""	
	print "For tbl " + tbl + " calling " + mycmd
	run_subprocess(mycmd)

def remove_from_bq(obj):
	mycmd = "bq rm -f %s" % (obj)	
	print "For obj " + obj + " calling " + mycmd
	run_subprocess(mycmd)
	
def query_bq(qry):
	encoding = 'utf-8'	  # specify the encoding of the CSV data
	mycmd="bq query --max_rows=1000000000 --format=csv \"%s\"" % (qry)
	#print "Sending a query to subprocess:", mycmd
	sys.stderr.write("Sending a query to subprocess:", mycmd,"\n")
	p2 = subprocess.Popen(mycmd, stdout=subprocess.PIPE, shell=True, stderr=subprocess.STDOUT)
	output = p2.communicate()[0].decode(encoding)
	edits = csv.reader(output.splitlines(), delimiter=",")
	rownum=1
	rownames=None
	header_found=True
	for row in edits:
		if not header_found:
			if rownum==1:
				if row[0].endswith("Error processing job"):
					print row[0]
					for rw in edits:
						print ' '.join(rw)
					return
				else:
					rownames=row
					rownum=rownum+1
			else:
				yield(dict(zip(rownames,row)))
				rownum=rownum+1
		if len(row)==1 and row[0].find("Current status: DONE") > 0:
			header_found=False

def output_csv(query,out_file):
	rows = query_bq(query)
	rowcount=1
	fieldnames=list()
	outfile_handle = open(out_file,"wb")
	csvwriter=None
	for item in rows:
		if rowcount==1:
			fieldnames=item.keys()
			csvwriter=csv.DictWriter(outfile_handle, fieldnames=fieldnames)
			csvwriter.writerow(dict((fn,fn) for fn in fieldnames))
		csvwriter.writerow(item)
		rowcount=rowcount+1
	outfile_handle.close()