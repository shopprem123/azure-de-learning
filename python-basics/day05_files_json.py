import json

# Reading JSON -- this is how you process API responses, ADF run outputs,
# Databricks job results, webhook payloads

with open("sample_pipeline_runs.json","r") as f:
    runs = json.load(f)

print(f"Loaded {len(runs)} pipeline runs")
print(f"First run: {runs[0]}")

# Process the data
total_rows = sum(r["rows_loaded"] for r in runs)
failed_rows = [r for r in runs if r["status"] == "failed"]
success_rate = (len(runs) - len(failed_rows))/len(runs) * 100

print(f"\nSummary:")
print(f" Total rows loaded: {total_rows:,}")
print(f" Failed pipelines: {len(failed_rows)}")
print(f" Success rate: {success_rate:.1f}%")

# Writing JSON output
summary = {
    "run_date" : "2024-01-15",
    "total_pipelines" : len(runs),
    "successful" : len(runs) - len(failed_rows),
    "failed" : len(failed_rows),
    "total_rows_loaded" : total_rows,
    "success_rate_pct" : round(success_rate,1),
    "failures" : [{"pipeline" : r["pipeline"], "duration" : r["duration_seconds"]} for r in failed_rows]
}

with open("pipeline_summary_report.json", "w") as f:
    json.dump(summary, f, indent=2)

print(f"\nReport written to pipeline_summary_report.json")
print(json.dumps(summary, indent = 2))
