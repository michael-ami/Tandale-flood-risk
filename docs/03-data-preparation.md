# CRS, Reprojection, and Quality Checks

**CRS chosen and why**
Working CRS: EPSG:32737 (WGS 84 / UTM Zone 37S). Chosen because Tandale Ward sits within UTM Zone 37S's coverage, it's a projected system in metres (required for accurate distance buffers and area calculation), and it uses the modern WGS84 datum, matching the OSM source data natively rather than the older Arc 1960 datum used in some Tanzanian government products.

**What was reprojected and clipped**
All three layers (Tandale ward boundary, Ng'ombe River, building footprints) originated in EPSG:4326 (river and buildings from OSM/QuickOSM; boundary from NBS). Each was clipped to the Tandale ward extent, then reprojected to EPSG:32737. Working files saved in `data/processed/`; original downloads untouched in `data/raw/`.

**Five quality checks and results**

1. **CRS confirmation** — verified all three processed layers report EPSG:32737 (confirmed programmatically, not just via QGIS Properties panel).
2. **Area sanity check** — area calculated in the wrong system (EPSG:4326) produced 0.0000954 square degrees, a meaningless number confirming why CRS matters. Recalculated correctly on the EPSG:32737 boundary layer: 1,165,249.76 m² = 1.1652 km². This matches published figures for Tandale (Ramani Huria's mapping report: 1.17 km²; Wikipedia: 1.1 km²) closely — confirming the reprojection is correct.
3. **Feature count check** — boundary = 1, river = 2, buildings = 7,629. Consistent with Week 2 counts; clip did not drop or duplicate features.
4. **Clip completeness check** — verified via bounding box comparison that river (526200.76–527647.87 E, 9248557.41–9249595.27 N) and buildings extents sit fully inside the boundary extent (526020.48–527648.11 E, 9248518.68–9249597.47 N). No layer extends past the study area.
5. **Geometry validity check** — geometry types confirmed unchanged after reprojection: river = MultiLineString, buildings = MultiPolygon, boundary = MultiPolygon. No new nulls introduced by reprojection beyond those already documented in Week 2.

**Problems found and resolution**
- River geometry contains unmapped gaps along the northeast section (documented Week 2) — flagged, not fixed; affects buffer accuracy only in those specific stretches.
- Ward boundary closely follows the Ng'ombe River's course along the north edge — confirmed as a real geographic fact (Ramani Huria's own report states Ng'ombe forms Tandale's boundary with Kijitonyama and Magomeni wards), not a data error.

**Where the analysis-ready file lives**
`data/processed/` — contains `Tandale_Boundary.gpkg`, `Tandale_river_32737.gpkg`, `Tandale_Buildings_32737.gpkg`, all clipped to Tandale and reprojected to EPSG:32737.
