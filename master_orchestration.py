dbutils.notebook.run("customer_load", 300)
dbutils.notebook.run("customer_report", 300)

print("Pipeline completed successfully")