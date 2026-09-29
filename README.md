# GeoDev Lab Africa — Flood-Risk Mapping in Tandale
A community-focused GIS project identifying flood-exposed residential buildings along the Ng'ombe River in Tandale Ward, Dar es Salaam, Tanzania.

## The Question
Which residential buildings in Tandale Ward fall within 100m, 200m, or 300m of the Ng'ombe River?

## The Answer
45.0% of Tandale's residential buildings (3,434 of 7,629) sit within 300m of the Ng'ombe River, with the highest concentration, 1,287 buildings, in the innermost 100m band. Full results in [month-1-summary.md](month-1-summary.md).

## Overview
- Location: Tandale Ward, Dar es Salaam, Tanzania
- Coordinate System: EPSG:32737 (WGS 84 / UTM Zone 37S)
- Core Datasets: OpenStreetMap via Geofabrik Tanzania, NBS 2022 PHC Ward Shapefiles
- Cohort: GeoDev Lab Africa, Cohort One (2026)

Full data specifications, exact file sizes, and sourcing are documented in [docs/01-project-brief.md](docs/01-project-brief.md).

## Month 1, Week by Week
- [Week 1 — Project Brief](docs/01-project-brief.md): the question, why it matters, and where every dataset comes from
- [Week 2 — Data Notes](docs/02-data-notes.md): what was downloaded, feature counts, columns, and coverage gaps
- [Week 3 — Data Preparation](docs/03-data-preparation.md): CRS choice, reprojection, clipping, and five quality checks
- [Week 4 — Month 1 Summary](month-1-summary.md): the buffer analysis, the map, and the answer above

## Data
Analysis-ready GeoPackages are committed at [data/processed/](data/processed/): ward boundary, river, and building footprints, all clipped to Tandale and reprojected to EPSG:32737. Raw downloads are not committed due to file size (hundreds of MB to ~2 GB); sources and links are in the Week 1 brief.
