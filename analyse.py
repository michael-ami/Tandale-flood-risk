with open("wards.csv") as f:
    lines = f.readlines()

for line in lines[1:]:
    parts = line.strip().split(",")
    band = parts[0]
    buildings = int(parts[1])
    if buildings > 1200:
        size = "large"
    else:
        size = "small"
    print(band, "has", buildings, "buildings:", size)