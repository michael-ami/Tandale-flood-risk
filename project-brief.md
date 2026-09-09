# Project Brief: Flood-Risk Exposure in Tandale Ward

## 1. The Question
Which residential buildings in Tandale Ward fall within 100m, 200m, or 500m of the Msimbazi River?

## 2. Why It Matters
Buildings closest to the Msimbazi River flood first and worst when the rains come. A distance-based flood-risk zone gives disaster-management and public-health teams a simple, defensible way to rank which residential clusters need inspection, sanitation outreach, or evacuation planning before the next heavy rainfall.

## 3. The Data I Need

- Msimbazi River Centerline: line geometry marking the river's course through Tandale, used to measure distance buffers.
- Residential Building Footprints: building polygons within Tandale Ward, filtered down to residential using an exclusion rule (drop school/hospital/commercial/mosque/church tags, keep the rest).
- Tandale Ward Boundary: administrative polygon used to clip the river and buildings to this ward only.

## 4. Where Each Dataset Comes From

- River Centerline: OpenStreetMap via Geofabrik Tanzania — [download.geofabrik.de/africa/tanzania.html](download.geofabrik.de/africa/tanzania.html) — Format: .osm.pbf (672 MB) or .shp.zip (1.8 GB) for the full Tanzania extract; negligible once clipped to Tandale.
- Building Footprints: OpenStreetMap via Geofabrik Tanzania — [download.geofabrik.de/africa/tanzania.html](download.geofabrik.de/africa/tanzania.html)  — Format: .osm.pbf (672 MB) or .shp.zip (1.8 GB) for the full Tanzania extract; a few MB after clipping to Tandale.
- Ward Boundary: NBS 2022 PHC Ward Shapefiles — [nbs.go.tz/statistics/topic/gis](nbs.go.tz/statistics/topic/gis) — Format: Shapefile (.zip). Exact size: 58.01 MB.

## 5. What I Will Build
An interactive dashboard where a field officer switches between three river-distance bands — 100m, 200m, and 500m — and gets back a ranked, exportable list of residential buildings inside the selected zone: building ID, rough location, distance from river.
