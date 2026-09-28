# Month 1 Summary

**Question, restated:** Which residential buildings in Tandale Ward fall within 100m, 200m, or 500m of the Ng'ombe River?

**Operation run:** A river buffer at three distances (100m, 200m, 500m) in EPSG:32737, then each building was classified by whether its centroid fell within each buffer ring. Buffer + spatial classification was chosen because the question is explicitly framed as distance bands, not a simple in/out flood zone, so a plain intersection wouldn't capture the tiered structure the project needs.

**What I expected:** Given Tandale's small size (1.17 km²) and the river running close to two of its edges rather than through the middle, I expected the 500m buffer might cover a large share of the ward, with 100m being the smallest, tightest band.

**What I got:**
- 0–100m: 1,287 buildings
- 100–200m: 1,090 buildings
- 200–500m: 2,858 buildings
- Beyond 500m: 2,394 buildings
- Total within 500m: 5,235 buildings (68.6% of all 7,629)
- The 500m buffer covers 69.1% of the ward's total area

**What surprised me:** The 500m band doesn't just capture "many" buildings, it captures over two-thirds of the entire ward. Only the southwest corner sits outside it. This means "500m flood-risk zone" is close to describing most of Tandale, not a narrow strip along the water, given how the Ng'ombe runs along the ward's northern and eastern edges rather than through its centre.

A second surprise came from the row-count check itself: my first QGIS run of the distance join returned 7,677 buildings instead of the expected 7,629, a discrepancy that traced back to the river layer's 2 separate line segments. Buildings tied equidistant between both segments were being duplicated by the "Join attributes by nearest" tool. Dissolving the river into a single feature before rejoining fixed it, and the corrected run matched the expected 7,629 exactly. This is a good example of why Step 4's row-count check matters: it caught a real processing error that would otherwise have silently inflated every band's count.

**What data I still need:** The river geometry gaps flagged in Week 2/3 (unmapped breaks in the northeast) mean the buffer along those stretches is incomplete, some buildings near those gaps may be under-classified. I also still need a way to confirm which buildings in the "residential" category are genuinely occupied homes versus vacant or non-residential structures still carrying a generic OSM tag, since that affects how the counts above should be read for public-health prioritisation.



See tandale_flood_risk_map.png for the visual result ![Flood risk map](tandale_flood_risk_map.png) 
