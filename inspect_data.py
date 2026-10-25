# Prediction: count will be 7629 for both columns
import csv

def inspect_column(filename, column):
    with open(filename, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    values = []
    for row in rows:
        raw = row[column].strip()
        if raw == "":
            continue
        values.append(float(raw))
    return {
        "smallest": min(values),
        "largest": max(values),
        "count": len(values),
    }

dist_result = inspect_column("tandale_buildings.csv", "distance_m")
area_result = inspect_column("tandale_buildings.csv", "footprint_m2")

print("Distance to river:", dist_result)
print("Building footprint:", area_result)