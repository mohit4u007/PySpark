# Spark Session
from pyspark.sql import SparkSession

spark = SparkSession.builder \
	.appName("Cluster Execution") \
	.getOrCreate()

# Create a sample data frame
df = spark.range(10)

# Write the data of the data frame
df.write.mode("overwrite").format("csv").option("header", True).save("output/range.csv")