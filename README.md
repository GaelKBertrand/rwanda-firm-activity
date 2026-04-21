# Rwanda Firm Activity Tracker
 
**Purpose:** Construct firm-level proxies for economic activity using satellite nightlights and OpenStreetMap data

## Overview
This repository demonstrates a reproducible pipeline for:
1. Extracting firm locations from OpenStreetMap for Kigali, Rwanda
2. Downloading and processing VIIRS nightlights data (2022-2023)
3. Performing spatial joins to assign nightlights intensity to each firm
4. Clustering firms geographically using K-means
5. Generating panel data for firm-level analysis

## Key Findings (Preliminary)
- 736 firms identified across 7 business types in Kigali
- 3 distinct geographic clusters with varying nightlights intensity
- Mean nightlights range from 15.3 (Cluster 0) to 38.3 (Cluster 1)

## Data Sources
- VIIRS Nightlights: NOAA/VIIRS/DNB/ANNUAL_V22 (Google Earth Engine)
- Firm Locations: OpenStreetMap (via osmnx)
- Administrative Boundaries: FAO GAUL 2015

## Repository Structure
- OSM_exploration.ipynb   # Main analysis pipeline
- data/
 - raw/                 # Raw VIIRS GeoTIFFs
 - processed/           # Cleaned CSVs and panel data
- outputs/
 - maps/                # Visualizations and interactive maps

## Replication
Run `OSM_exploration.ipynb` in Google Colab with:
- Google Earth Engine authentication
- Google Drive mounted at `/content/drive`