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

    for c in [None, 'uncompressed', 'gzip', 'lzo', 'brotli', 'lz4', 'zstd', 'snappy']:
        try:
            df.write.parquet(f'{c}.parquet', compression=c)
            print(f"- compression={c} ok")
        except Exception as e:
            print(f"- compression={c} exception={e}")

    spark.stop()
