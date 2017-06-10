# Data Engineering Test

The task is to transform a poorly formatted TSV file into a properly formatted, machine-readable TSV file. The file does not explicitly adhere to the TSV format, so GitHub and existing data tools cannot accurately parse the file.

### Instructions

Your task is to write a simple script to transform the broken TSV into a properly-formatted tab-separated values (TSV) file that can be read by any standard CSV/TSV parser. The resulting file should have the
following properties:

* Each row contains the same number of fields
* Fields are separated by tabs `\t`
* Fields that contain reserved characters (e.g. `\t`, `\r`, `\n`) are quoted
* The file is UTF-8 encoded (`data.tsv` is UTF-16LE encoded)

Scripts should be written in Python. The solution does *not*
need to be generic enough to apply to similar issues in other files; your algorithm can be designed specifically for this
data set. Extra points are awarded for resource-efficient and scalable solutions.

To take the test, please complete the following steps:

1. Fork this repository
2. Write a Python script to convert data into a parseable file, adhering to guidelines in the previous section.
3. Create a table in Redshift and write the results to it. Credentials will be emailed to you separately. Save the query used to do this.
4. Write a query that can run efficiently to check the emails column in the first table you created, write the domain names that appear more than once to a second table, and include the counts for each one. This query should operate regardless of whether or not the second table has already been created, and should only give the current count (i.e. old values are not preserved if the query is re-run).
5. Commit the Python script, all queries, and a copy of the properly-formatted TSV to the root directory of the repository.
6. Email an archive of your files to jake@gravitybrands.com. In this email, include an explanation as to any oddities found in the data that might indicate problems beyond poorly-formatted files.

### Bonus (optional)

For bonus points, ambitious candidates can parallelize their algorithm. A parallelizable implementation will
have the following properties:

* Given an arbitrary byte `position` and `length`, the algorithm cleans a portion of the full data set and produces
  a unique TSV output file.
* Concatenating the outputs of multiple processes should result in a well-formed TSV file containing no duplicates

*It's important to note that the arbitrary `position` may not necessarily be the start of a new line.*
