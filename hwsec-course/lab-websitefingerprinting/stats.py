import json
import statistics
import os

# 1️⃣ Load the JSON file
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "traces.out")

with open(file_path, "r") as f:
    data = json.load(f)

traces = data["traces"]  # List of lists

# Helper function to compute stats for a list of values
def compute_stats(values, label):
    mean_val = statistics.mean(values)
    median_val = statistics.median(values)
    stdev_val = statistics.stdev(values) if len(values) > 1 else 0
    min_val = min(values)
    max_val = max(values)
    range_val = max_val - min_val

    print(f"\n{label}:")
    print(f"Mean = {mean_val:.3f}")
    print(f"Median = {median_val}")
    print(f"Stdev = {stdev_val:.3f}")
    print(f"Range = {range_val} (min={min_val}, max={max_val})")


# 2️⃣ Per-trace statistics
print("Statistics for each trace:")
for i, trace in enumerate(traces):
    mean_val = statistics.mean(trace)
    median_val = statistics.median(trace)
    stdev_val = statistics.stdev(trace) if len(trace) > 1 else 0
    min_val = min(trace)
    max_val = max(trace)
    range_val = max_val - min_val

    print(
        f"Trace {i+1}: "
        f"mean={mean_val:.3f}, median={median_val}, "
        f"stdev={stdev_val:.3f}, range={range_val}"
    )


# 3️⃣ Group stats: traces 1–4
group1_values = [val for trace in traces[0:4] for val in trace]
compute_stats(group1_values, "Statistics for Traces 1–4")


# 4️⃣ Group stats: traces 5–8
group2_values = [val for trace in traces[4:8] for val in trace]
compute_stats(group2_values, "Statistics for Traces 5–8")


# 5️⃣ Overall stats across all traces
all_values = [val for trace in traces for val in trace]
compute_stats(all_values, "Overall statistics across all traces")
