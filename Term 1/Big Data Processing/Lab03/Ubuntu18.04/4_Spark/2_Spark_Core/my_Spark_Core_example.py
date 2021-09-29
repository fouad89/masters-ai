#!/usr/local/bin/python3.8
#
# --------------------------------------------------------
#
# PYTHON PROGRAM DEFINITION
#
# The knowledge a computer has of Python can be specified in 3 levels:
# (1) Prelude knowledge --> The computer has it by default.
# (2) Borrowed knowledge --> The computer gets this knowledge from 3rd party libraries defined by others
#                            (but imported by us in this program).
# (3) Generated knowledge --> The computer gets this knowledge from the new functions defined by us in this program.
#
# When launching in a terminal the command:
# user:~$ python3 this_file.py
# our computer first processes this PYTHON PROGRAM DEFINITION section of the file.
# On it, our computer enhances its Python knowledge from levels (2) and (3) with the imports and new functions
# defined in the program. However, it still does not execute anything.
#
# --------------------------------------------------------

# ------------------------------------------
# IMPORTS
# ------------------------------------------
import pyspark
import sys
import re

# ------------------------------------------
# FUNCTION my_spark_core_job
# ------------------------------------------
def my_spark_core_job(sc, my_dataset_dir, my_result_dir):
    # 1. Operation C1: textFile
    inputRDD = sc.textFile(my_dataset_dir)

    # 2. Operation T1: flatMap
    all_wordsRDD = inputRDD.flatMap(lambda line: line.split(" "))

    # 3. Operation T2: map
    clean_wordsRDD = all_wordsRDD.map(lambda w: (re.sub(r"[^a-zA-Z]", "", w).lower(), 1))

    # 4. Operation T3: reduceByKey
    solutionRDD = clean_wordsRDD.reduceByKey(lambda x, y: x + y)

    # 5. Operation A1: saveAsTextFile
    solutionRDD.saveAsTextFile(my_result_dir)

# --------------------------------------------------------
#
# PYTHON PROGRAM EXECUTION
#
# Once our computer has finished processing the PYTHON PROGRAM DEFINITION section its knowledge is set.
# Now its time to apply this knowledge.
#
# When launching in a terminal the command:
# user:~$ python3 this_file.py
# our computer finally processes this PYTHON PROGRAM EXECUTION section, which:
# (i) Specifies the function F to be executed.
# (ii) Define any input parameter such this function F has to be called with.
#
# --------------------------------------------------------
if __name__ == '__main__':
    # 1. We use as many input arguments as needed, either hard-coded or passed by console
    my_dataset_dir = "/FileStore/tables/my_dataset"
    my_result_dir = "/FileStore/tables/my_result/"

    if (len(sys.argv) > 1):
       my_dataset_dir = sys.argv[1]
       my_result_dir = sys.argv[2]

    # 2. We configure the Spark Context
    sc = pyspark.SparkContext.getOrCreate()
    sc.setLogLevel('WARN')
    print("\n\n\n")

    # 3. We call to our main function
    my_spark_core_job(sc, my_dataset_dir, my_result_dir)
