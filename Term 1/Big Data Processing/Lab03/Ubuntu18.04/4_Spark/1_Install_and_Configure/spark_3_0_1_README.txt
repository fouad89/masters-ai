----------------------------------------------------------------------------

 SPARK 3.0.1 INSTALLATION

----------------------------------------------------------------------------

In this section we discuss how to install Spark 3.0.1.

We download "spark-3.0.1-bin-hadoop3.2.tgz" from https://spark.apache.org/downloads.html, Version 3.0.1. 
We open a terminal in the folder where the file "spark-3.0.1-bin-hadoop3.2.tgz" is downloaded.

---------------------------------------------------------
TERMINAL
---------------------------------------------------------
(1) $ wget https://downloads.apache.org/spark/spark-3.0.1/spark-3.0.1-bin-hadoop3.2.tgz
---------------------------------------------------------
(2) $ tar -xzvf spark-3.0.1-bin-hadoop3.2.tgz
---------------------------------------------------------
(3) $ sudo mv spark-3.0.1-bin-hadoop3.2 /usr/local/spark
---------------------------------------------------------
(4) $ python3.8 -m pip install pyspark
---------------------------------------------------------
(5) $ sudo gedit ~/.bashrc
---------------------------------------------------------
Add the following lines:
export PATH=... :/usr/local/spark/bin/
export PYSPARK_PYTHON=/usr/local/bin/python3.8
export PYSPARK_DRIVER_PYTHON=/usr/local/bin/python3.8
---------------------------------------------------------
(6) $ spark-submit --version
---------------------------------------------------------

Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /___/ .__/\_,_/_/ /_/\_\   version 3.0.1
      /_/
                        
Using Scala version 2.12.10, OpenJDK 64-Bit Server VM, 11.0.8
Branch HEAD
Compiled by user ubuntu on 2020-08-28T08:58:35Z
Revision 2b147c4cd50da32fe2b4167f97c8142102a0510d
Url https://gitbox.apache.org/repos/asf/spark.git
Type --help for more information.




