from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

data = [
    (1, "John", "USA"),
    (2, "Mary", "UK"),
    (3, "Ravi", "India")
]

df = spark.createDataFrame(data, ["id", "name", "country"])

df.write.mode("overwrite").format("delta").save("/tmp/customer_data")

print("Customer data loaded successfully")