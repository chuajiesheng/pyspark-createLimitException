import logging
import os
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession

if __name__ == '__main__':
    spark = SparkSession.builder.appName('test').getOrCreate()

    sc = spark.sparkContext
    sc.setLogLevel("DEBUG")

    df = spark.read.load('sample.csv', format="csv", sep=",", inferSchema="true", header="true")
    print('- lines', df.count())

    df.write.partitionBy('name').format('parquet').save('hello.parquet')
    spark.stop()
