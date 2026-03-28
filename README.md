# Rwanda Firm Activity

## Overview
This project aims at building a proxy for firm activity and economic intensity using satellite data.

Nightlights are widely used in development economics to:
- estimate economic growth
- detect firm clusters
- proxy for informal sector activity

## Motivation
Firm-level data in developing countries is incomplete or unavailable.
This project explores how satellite data can fill that initial gap.

## Data
- VIIRS Nighttime Lights (NOAA)

## Methods
- Raster data processing
- Normalization of light intensity
- Spatial visualization

## Objective Outputs (evolving)
- Heatmap of economic activity
- Summary statistics of intensity distribution

## Future Extensions (evolving)
- Merge with survey data (EICV)
- Train ML model to predict firm density
- Detect economic shocks over time

### How to run
- pip install -r requirements.txt
- python src/download_data.py
- python src/preprocess.py
- python src/analysis.py
