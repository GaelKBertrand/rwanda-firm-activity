# Rwanda Firm Activity Tracker
 
**Purpose:** Construct firm-level proxies for economic activity using satellite nightlights and OpenStreetMap data

# Measuring Commercial Informality in Kigali Using OpenStreetMap and Satellite Data

**Status:** Research in Progress

---

## Introduction

This project constructs a spatially explicit, time‑varying measure of commercial informality in Kigali, Rwanda. By combining **OpenStreetMap (OSM)** – which is a biased and incomplete map of formal businesses – with **VIIRS nightlights** and **Sentinel‑2 NDBI** (built‑up index), once can infer areas where economic activity is high but formal firm representation is low. The output is a 500m grid‑level panel dataset (2015–2024) containing satellite‑derived economic intensity, OSM firm counts, expected firm counts (using Poisson regression), and a coverage ratio. The informality signal is validated against the **World Bank Enterprise Survey** and a manual sample of grid cells. 
This work provides a low‑cost, replicable tool for monitoring commercial development hot nodes and targeting policy interventions in data‑poor urban environments.

---

## Questions

1. **Primary:** To what extent does OpenStreetMap under‑represent commercial activity in Kigali, and where is this under‑representation most severe?  
2. **Secondary:** How has the spatial pattern of satellite‑derived economic activity (nightlights + NDBI) evolved in Kigali from 2015 to 2024?  
3. **Tertiary:** Can we identify distinct commercial clusters based on the co‑location of formal activity (OSM) and satellite‑inferred informal activity?

---

## Conceptual Framework

- **Economic Geography:** Formal firms (licensed, larger, more visible) are more likely to appear in OSM. Informal firms (small vendors, home‑based workshops, unregistered small shops) are underrepresented.  
- **Satellite Proxies:** VIIRS nightlights correlate with electricity consumption and nighttime economic activity. Sentinel‑2 NDBI (Normalized Difference Built‑up Index) captures daytime built‑up density. Together they can provide a signal of **total economic presence** independent of official registration.  
- **Informality as a Residual:** In areas where satellite activity is high but OSM firm count is low, one can infer a larger informal sector presence. This is a spatial indicator, not an absolute count.

---

## Data Sources

| Data | Source | Access | Temporal Coverage |
|------|--------|--------|-------------------|
| OpenStreetMap (OSM) | Geofabrik Rwanda extract | Public download | Snapshot 2026 (static) |
| VIIRS Nightlights | NOAA / Google Earth Engine | Public (GEE) | Annual 2015–2025 |
| Sentinel‑2 NDBI | Copernicus / Google Earth Engine | Public (GEE) | Annual 2015–2024 |
| Rwanda Administrative Boundaries | FAO GAUL / GADM | Public | Static |
| World Bank Enterprise Survey 2019 | World Bank Microdata Catalog | Free registration | Cross‑section (2019) |
| Rwanda Establishment Census 2023 | NISR Microdata Catalog | Request access | Cross‑section (2023) |
| Manual Validation Sample | Google Maps / field visits | Self‑collected | 2026 |

---

## Methodology Overview

### Phase 1: Setup 
- Set up directory structure and environment.  
- Download and prepare administrative boundaries.

### Phase 2: OSM Firm Extraction
- Use `osmnx` or Geofabrik extract to obtain **all economic‑related points** (amenity, shop, office, craft, industrial, tourism, etc.).  
- Clean, deduplicate, and save.

### Phase 3: Satellite Data Processing
- **VIIRS:** Export annual mean composites clipped to Rwanda using Google Earth Engine.  
- **Sentinel‑2 NDBI:** Compute annual median NDBI for each firm (250m buffer) or each grid cell; cache results.

### Phase 4: Firm‑Level Panel & Clustering
- Merge firm locations with yearly nightlights and NDBI to create a panel.  
- Compute PCA‑based **Satellite‑Derived Economic Intensity** (PC1 of nightlights + NDBI).  
- Cluster firms using PC1, coverage ratio, and geographic coordinates.

### Phase 5: Grid‑Based Analysis (500m)
- Create a 500m grid covering Kigali city.  
- For each cell and year, extract mean nightlights, mean NDBI, and count of OSM firms.  
- Run Poisson regression: `OSM_firms ~ nightlights + NDBI` → expected firms, residual.  
- Compute **Coverage Ratio** = OSM / (expected + 0.1).  
- Negative residuals indicate candidate informal zones or high informality commercial zones in Kigali.

### Phase 6: Validation
- **WBES 2019:** Spatially joining surveyed firms to grid and regress survey firm count on informality residual.  
- **Manual Sample:** Stratified random sample of 50–60 cells; count visible businesses via Google Maps; correlate with satellite indices.  
- **Literature Calibration:** Use published OSM coverage rates (40% in informal, 85% in formal areas) to estimate true firm counts.

### Phase 7: Synthesis & Reporting
- Maps, time‑series plots, and regression tables.  
- Final dataset output

---

## Repository Structure

- **rwanda-nightlights-firm-activity/**
  - **app/** - folder of a future dashboard ui for easy visuals and data interaction
  - **code/** 
    - `ipynb notebooks/` – Jupyter notebooks for each pipeline stage
    - `src/` – Reusable Python modules
    - `stata/` – Reproducible STATA analysis do files
  - **data/**
    - `external/` – Third‑party survey data
    - `raw/` – Immutable original data
    - `processed/` – Cleaned, analysis‑ready data
  - **docs/** – Research design and literature notes
  - **outputs/**
    - `maps/` – HTML/PNG/PDF maps
    - `tables/` – CSV/LaTeX tables
    - `figures/` – Other figures
  - **reports/** – Final reports / briefs
  - `.gitignore`
  - `LICENSE-CODE` – MIT License for code
  - `LICENSE-DATA` – CC BY 4.0 License for data/outputs
  - `README.md` 
  - `REQUIREMENTS.TXT` 
  - `structure.md` 
   
   