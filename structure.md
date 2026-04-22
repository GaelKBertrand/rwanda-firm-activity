rwanda-nightlights-firm-activity/
├── README.md
├── .gitignore
├── environment.yml                     # (optional) conda environment file
├── data/
│   ├── raw/                            # Raw, immutable data
│   │   ├── osm/                        # OSM extracts (Geofabrik .pbf or .gpkg)
│   │   ├── viirs/                      # VIIRS annual GeoTIFFs (2015–2025)
│   │   ├── sentinel2/                  # Sentinel‑2 derived NDBI caches
│   │   ├── boundaries/                 # Rwanda & Kigali administrative boundaries
│   │   └── surveys/                    # External survey microdata (WBES, Census)
│   ├── processed/                      # Cleaned, merged, analysis‑ready data
│   │   ├── firms_clean.csv
│   │   ├── firms_clustered.csv
│   │   ├── firm_nightlights_panel.csv
│   │   ├── firm_ndbi_cache.csv
│   │   ├── grid_500m.geojson
│   │   ├── grid_panel.csv
│   │   └── validation_sample.csv
│   └── external/                       # Data from third‑party sources (e.g., WBES, NISR, World Bank)
│
├── notebooks/
│   ├── 01_setup_and_gee_auth.ipynb
│   ├── 02_osm_extraction.ipynb
│   ├── 03_viirs_nightlights.ipynb
│   ├── 04_sentinel2_ndbi.ipynb
│   ├── 05_firm_panel_construction.ipynb
│   ├── 06_clustering_and_indices.ipynb
│   ├── 07_grid_analysis.ipynb
│   ├── 08_validation.ipynb
│   └── 09_results_visualization.ipynb
│
├── src/                                # Reusable Python modules
│   ├── __init__.py
│   ├── data_utils.py
│   ├── gee_utils.py
│   ├── spatial_utils.py
│   └── indices.py
│
├── outputs/
│   ├── maps/                           # PNG/PDF maps
│   ├── tables/                         # CSV/LaTeX tables
│   └── figures/                        # Other figures (time series, scatter)
│
├── docs/                               # Research questions, literature notes
│   ├── research_design.pdf
│   └── literature_notes.md
│
└── reports/                            # Final reports drafts
    ├── working_paper.pdf
    └── policy_brief.pdf