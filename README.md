# Tandale Flood Risk

## The Question

Which residential buildings in Tandale Ward fall within 100m, 200m, or 300m of the Ng'ombe River?

## The Answer

45.0% of Tandale's residential buildings (3,434 of 7,629) sit within 300m of the Ng'ombe River, with the highest concentration, 1,287 buildings, in the innermost 100m band. Full results in [month-1-summary.md](https://github.com/michael-ami/Tandale-flood-risk/blob/main/month-1-summary.md).

## Overview

* Location: Tandale Ward, Dar es Salaam, Tanzania
* Coordinate System: EPSG:32737 (WGS 84 / UTM Zone 37S)
* Core Datasets: OpenStreetMap via Geofabrik Tanzania, NBS 2022 PHC Ward Shapefiles
* Cohort: GeoDev Lab Africa, Cohort One (2026)

Full data specifications, exact file sizes, and sourcing are documented in [docs/01-project-brief.md](https://github.com/michael-ami/Tandale-flood-risk/blob/main/docs/01-project-brief.md).

## Month 1, Week by Week

* [Week 1 — Project Brief](https://github.com/michael-ami/Tandale-flood-risk/blob/main/docs/01-project-brief.md): the question, why it matters, and where every dataset comes from
* [Week 2 — Data Notes](https://github.com/michael-ami/Tandale-flood-risk/blob/main/docs/02-data-notes.md): what was downloaded, feature counts, columns, and coverage gaps
* [Week 3 — Data Preparation](https://github.com/michael-ami/Tandale-flood-risk/blob/main/docs/03-data-preparation.md): CRS choice, reprojection, clipping, and five quality checks
* [Week 4 — Month 1 Summary](https://github.com/michael-ami/Tandale-flood-risk/blob/main/month-1-summary.md): the buffer analysis, the map, and the answer above

## Data

Analysis-ready GeoPackages are committed at [data/processed/](https://github.com/michael-ami/Tandale-flood-risk/blob/main/data/processed): ward boundary, river, and building footprints, all clipped to Tandale and reprojected to EPSG:32737. Raw downloads are not committed due to file size (hundreds of MB to ~2 GB); sources and links are in the Week 1 brief.

## Month 2: Development Environment and Early Python

The same project, now with Python. The work runs with `uv run <file>.py`.

* Week 5: set up Python, VS Code and the terminal. `hello.py` runs.
* Week 6: set up the project with uv and added pandas. `check.py` prints the pandas version.
* Week 7: `analyse.py` reads `wards.csv`, converts each count and classifies each band as large or small.
* Week 8: `inspect_data.py` summarises distance to river and building footprint in my Tandale buildings data (`tandale_buildings.csv`, 7,629 rows, one per building).
* Week 9: `summary.py` splits the inspection into small functions and summarises distance to river and building footprint in my Tandale buildings data.

### Month 2 reflection

The idea that clicked this month is the difference between print and return: print shows a value to a person, while return hands it back so the code can use it. What is still fuzzy for me is dictionaries. I understand that they hold values by name instead of by position, but I still get confused when one is nested inside another, and when I loop over one with `.items()`. My capstone shows that the average building in Tandale is about 365 m from the Ng'ombe River, with the nearest only 0.4 m away and the farthest 916 m, and that the average building footprint is about 77 m². That matches the Month 1 result that a large share of the ward sits close to the river.
