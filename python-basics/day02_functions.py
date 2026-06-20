# In SQL you write CASE WHEN every time
# In Python you write a function once and call it many times
# In Informatica you created a reusable Transformation
# In Python you can create a reusable function

def classify_pipeline_status(row_count):
    """Classifies a pipeline run by rows processed."""
    if row_count == 0:
        return "Empty -- investigate source"
    elif row_count < 100:
        return "Low volumn -- check for upstream issues"
    elif row_count < 100000:
        return "Normal"
    else:
        return "High Volume -- monitor cluster performance"
    

# Test it
print(classify_pipeline_status(0))
print(classify_pipeline_status(50))
print(classify_pipeline_status(5000))
print(classify_pipeline_status(1000000))

# Call it on multiple values -- This is row iteration
# SQL processes all rows at once (set-based)
# Python iterates row by row (this distinction matters deeply in PySpark)
daily_counts = [0, 1200, 87000, 4200000, 45]
for count in daily_counts:
    status = classify_pipeline_status(count)
    print(f"Row count {count:>8} -> {status}")

##Mini challenge:

# Write a function called get_medallion_layer(path)
# that returns "bronze", "silver", "gold", or "unknown"
# based on whether the word appears in the path string
# Test: get_medallion_layer("abfss://bronze@storage/dfs.core.windows.net/titanic/")
# Should return: "bronze"

def get_medallion_layer(path):
    # Lower case comparison to avoid case sensitive mismatches
    lower_path = path.lower()

    if "bronze" in lower_path:
        return "bronze"
    elif "silver" in lower_path:
        return "silver"
    elif "gold" in lower_path:
        return "gold"
    else:
        return "unknown"
    
# Testing our path mapping functions
path_1 = "abfss://bronze@storage.dfs.core.windows.net/titanic/"
path_2 = "abfss://silver@storage.dfs.core.windows.net/orders/"
path_3 = "abfss://GOLD@storage.dfs.core.windows.net/analytics/" # Testing capital letters
path_4 = "abfss://landing-zone@storage.dfs.core.windows.net/"

print(f"Path: {path_1} -> Detected Layer {get_medallion_layer(path_1)}")
print(f"Path: {path_2} -> Detected Layer {get_medallion_layer(path_2)}")
print(f"Path: {path_3} -> Detected Layer {get_medallion_layer(path_3)}")
print(f"Path: {path_4} -> Detected Layer {get_medallion_layer(path_4)}")