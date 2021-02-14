import sys
import os
from datetime import *
from time import *
from pyspark.sql import *
from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.sql.session import SparkSession
from pyspark.sql import SQLContext

sc = SparkContext()
spark = SparkSession(sc)
sqlcont = SQLContext(sc)

empDf = sqlcont.read.json("customers.json")
empDf.show()
empDf.printSchema()

# SQL Queries
empDf.select("company").show()
empDf.filter(empDf['id'] > 8).show()

sc.stop()
