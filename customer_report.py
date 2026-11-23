from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

df = spark.read.format("delta").load("/tmp/customer_data")

df.show()

print(f"Total Customers: {df.count()}")