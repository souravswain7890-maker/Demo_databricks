from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

data = [
    (1, "John", "USA"),
    (2, "Mary", "UK"),
    (3, "Ravi", "India")
]

df = spark.createDataFrame(data, ["id", "name", "country"])

df.show()

print("Customer data loaded successfully")
print("Modified from Databricks Free Edition")