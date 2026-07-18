# A dictionary = one row in a result set
# Every JSON object from an API, every pipeline config, every metadata record
# --- in Python it becomes a dictionary

pipeline_config ={
    "name" : "ingest_titanic",
    "source_type" : "http",
    "source_url" : "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv",
    "target_layer" : "bronze",
    "targt_folder" : "titanic",
    "schedule" : "daily",
    "owner" : "data_team"
}

# Access values
print(pipeline_config["name"])
print(pipeline_config.get("onwer", "unknown")) # safe access with default

# Update
pipeline_config["last_run_status"] = "success"
pipeline_config["last_run_rows"] = 891

print(f"Pipeline {pipeline_config["name"]} last ran : {pipeline_config["last_run_status"]}")

# A list of dicts = a full result set
# SQL : SELECT * FROM pipeline_runs
pipeline_runs = [
    {"pipeline" : "ingest_titanic", "status" : "success", "rows" : 891},
    {"pipeline" : "ingest_sales", "status" : "failed", "rows" : 0},
    {"pipeline" : "transform_orders", "status" : "success", "rows" : 45230},
]

# SQL : SELECT * WHERE status = 'failed'
failures = [r for r in pipeline_runs if r["status"] == "failed"]
print(f"\nFailed pipelines: {failures}")

# Error handling -- critical for DE pipelines
# In Informatica, bad rows went to reject files
# In Python: try/except catches error without crashing everything

def safe_cast_to_int(value, field_name):
    """Safely converts a value to integer. Returns None on failure"""
    try:
        return int(value)
    except (ValueError, TypeError) as e:
        print(f"\nWarning: Could not cast {field_name} = '{value}' to int: {e}")
        return None
    
# Test with Good and Bad values
values = ["891", "MISSING", None, "45230", "Not_a_Number"]
for v in values:
    result = safe_cast_to_int(v, "row_count")
    print(f"Input: {str(v):15} -> Output: {result}")