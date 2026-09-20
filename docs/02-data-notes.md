# Data Notes

## Tandale Ward Boundary
- Source: NBS 2022 PHC Ward Shapefiles — https://www.nbs.go.tz/statistics/topic/gis
- Downloaded: 14/09/2026
- 1 feature, polygon (MultiPolygon)
- Columns: administrative hierarchy fields (region, district, council, constituency, division, ward) plus Shape_Leng and Shape_Area
- No nulls
- Confirmed correct: reg_name = Dar es Salaam, dist_name/counc_name = Kinondoni, ward_name = Tandale
- CRS: EPSG:32737 (WGS 84 / UTM Zone 37S)

## River, extracted via QuickOSM
- Query: waterway=river, within Tandale boundary extent
- Extracted: 14/09/2026
- 2 features, Line (MultiLineString)
- Columns: fid, full_id, osm_id, osm_type, waterway, tunnel, layer, covered, bridge:structure, bridge, name
- Only `name` populated: "Ng'ombe" / "Mto Ng'ombe" — all other tag columns NULL
- **Coverage gap:** river geometry has multiple unmapped breaks along the northeast section, closely following the ward boundary. Buffer results across these gap stretches will undercount buildings, since no river geometry exists there to measure distance from.
- CRS: EPSG:32737 (WGS 84 / UTM Zone 37S)

## Buildings, extracted via QuickOSM
- Query: building=*, within Tandale boundary extent (initial query overshot the boundary; clipped afterward)
- Extracted: 14/09/2026
- 7,629 features, Polygon (MultiPolygon)
- Columns: extensive OSM building tags (building, operator:type, roof:shape, roof:material, capacity:persons, etc.)
- Heavy nulls across specialized tags; only `building` itself is consistently populated, with values including residential, public, yes, commercial, and combined tags (e.g. "commercial;residential")
- Coverage: visually dense and consistent across the ward, including directly along the river edge. One open, building-free patch in the ward interior confirmed as a playground — not a residential coverage gap.
- Residential classification will require filtering the `building` column, excluding non-residential values (school, hospital, commercial, mosque, church, public), rather than relying on a single clean "residential" tag
- CRS: EPSG:32737 (WGS 84 / UTM Zone 37S)
