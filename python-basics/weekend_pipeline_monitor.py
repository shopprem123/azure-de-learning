import json

def load_runs(filepath):
    """Loads pipeline run data from a JSON file"""
    with open(filepath,"r") as f:
        return json.load(f)
    
def summarise_by_status(runs):
    """Groups runs by status and calculates counts and avg duration"""
    summary = {}
    for run in runs:
        status  = run["status"]
        if status not in summary:
            summary[status] = {"count": 0, "total_duration": 0, "pipelines": []}
        summary[status]["count"] += 1
        summary[status]["total_duration"] += run["duration_seconds"]
        summary[status]["pipelines"].append(run["pipeline"])

    for status in summary:
        count = summary[status]["count"]
        summary[status]["avg_duration_seconds"] = round (
            summary[status]["total_duration"] / count, 1
        )
    return summary

def find_slow_pipelines(runs, threshold_seconds=120):
    """Identifies pipelines exceeding a duration threshold"""
    return [
        {"pipeline": r["pipeline"], "duration":r["duration_seconds"]}
        for r in runs
        if r["duration_seconds"] > threshold_seconds
    ]

def generate_report(runs):
    status_summary = summarise_by_status(runs)
    slow_pipelines = find_slow_pipelines(runs)

    report = {
        "report_generated": "2024-01-15",
        "total_runs": len(runs),
        "by_status": status_summary,
        "health": "DEGRADED" if any(r["status"] == "failed" for r in runs) else "HEALTHY"
    }

    with open("monitoring_report.json", "w") as f:
        json.dump(report, f, indent=2)

    # Console output
    print("=" * 50)
    print("PIPELINE MONITORING REPORT")
    print("=" * 50)
    print(f"Total runs: {report['total_runs']}")
    print(f"Health: {report['health']}")
    print()
    for status, data in status_summary.items():
        print(f"{status.upper():10} {data['count']} runs | avg {data['avg_duration_seconds']}s")
    if slow_pipelines:
        print(f"\nSlow Pipelines: {[p['pipeline'] for p in slow_pipelines]}")
    print("\nFull report saved to monitoring_report.json")

if __name__ == "__main__":
    runs = load_runs("sample_pipeline_runs.json")
    generate_report(runs)