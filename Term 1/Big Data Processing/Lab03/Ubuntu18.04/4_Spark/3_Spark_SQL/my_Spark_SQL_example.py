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
import pyspark.sql.functions
import pyspark.sql.types
import sys

# ------------------------------------------
# FUNCTION my_main
# ------------------------------------------
def my_spark_sql_job(spark, my_dataset_dir, my_result_dir):
    # 1. We define the Schema of our DF.
    my_schema = pyspark.sql.types.StructType(
        [pyspark.sql.types.StructField("line", pyspark.sql.types.StringType(), True)])

    # 2. Operation C1: Load DataFrame
    inputDF = spark.read.format("csv") \
        .option("delimiter", ";") \
        .option("quote", "") \
        .option("header", "false") \
        .schema(my_schema) \
        .load(my_dataset_dir)

    # 3. Operation T1: split
    sentenceDF = inputDF.withColumn("words_list",
                                    pyspark.sql.functions.split(pyspark.sql.functions.col("line"), " ")
                                    ) \
        .drop("line")

    # 4. Operation T2: explode
    wordsDF = sentenceDF.withColumn("draft_word",
                                    pyspark.sql.functions.explode(pyspark.sql.functions.col("words_list"))
                                    ) \
        .drop("words_list")

    # 5. Operation T3: regexp_replace
    cleanDF = wordsDF.withColumn("clean_word",
                                 pyspark.sql.functions.regexp_replace("draft_word",
                                                                      r'[^a-zA-Z]',
                                                                      ""
                                                                      )
                                 ) \
        .drop("draft_word")

    # 6. Operation T4: lower
    lowerDF = cleanDF.withColumn("word",
                                 pyspark.sql.functions.lower(pyspark.sql.functions.col("clean_word"))
                                 ) \
        .drop("clean_word")

    # 7. Operation T5: GroupBy
    solutionDF = lowerDF.groupBy(["word"]).agg({"word": "count"})

    # 8. Operation A1: We save the results
    solutionDF.write.format("csv") \
        .save(my_result_dir)

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
    spark = pyspark.sql.SparkSession.builder.getOrCreate()
    spark.sparkContext.setLogLevel('WARN')
    print("\n\n\n")

    # 3. We call to our main function
    my_spark_sql_job(spark, my_dataset_dir, my_result_dir)
