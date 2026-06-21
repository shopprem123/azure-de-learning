# A list in Python = a single column result set in SQL
pipeline_names = ["ingest_titanic", "ingest_sales", "ingest_customers", "transform_orders"]
row_counts = [891, 45230, 12800, 98000]

# FOR loop = iterating through every row
# SQL : SELECT * FROM pipelines (processes all rows)
# Python : for loop processes one at a time

for pipeline in pipeline_names:
    print(f"Pipeline Found : {pipeline}")

# Loop with index
for i in range (len(pipeline_names)):
    print(f"{pipeline_names[i]:30} processed {row_counts[i]:>8} rows")

# List comprehension -- Pythonic shorthand
# SQL : SELECT pipeline_name FROM pipelines WHERE row_count > 10000
large_pipelines = [pipeline_names[i] for i in range(len(pipeline_names)) if row_counts[i] > 100000]
print(f"\nHigh volume pipelines: {large_pipelines}")

# The most useful pattern for DE: building a list of results 
pipeline_summary = []
for i in range(len(pipeline_names)):
    summary = {
        "name" : pipeline_names [i],
        "rows" : row_counts[i],
        "status" : "high" if row_counts[i] > 50000 else "normal"
    }
    pipeline_summary.append(summary)

print("\nPipeline Summary")
for s in pipeline_summary:
    print(s)