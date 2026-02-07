import json
import statistics
import os

# 1️⃣ Load the JSON file

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "traces.out")

with open(file_path, "r") as f:
    data = json.load(f)

traces = data["traces"]  # This is a list of lists of numbers

# 2️⃣ Compute mean and median for each trace
print("Mean and Median for each trace:")
for i, trace in enumerate(traces):
    mean_val = statistics.mean(trace)
    median_val = statistics.median(trace)
    print(f"Trace {i+1}: mean = {mean_val:.3f}, median = {median_val}")

# 3️⃣ Compute overall mean and median across all traces
all_values = [val for trace in traces for val in trace]  # Flatten all traces
overall_mean = statistics.mean(all_values)
overall_median = statistics.median(all_values)
print("\nOverall statistics across all traces:")
print(f"Overall mean = {overall_mean:.3f}, Overall median = {overall_median}")
