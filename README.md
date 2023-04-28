# Voronoimap
Simple scripts with python and R to make a map of closests supermarkets in Sweden, based on OSM data

## Requirements:
- Python
  - Pandas
- R
  - tidyverse
  - sf

## Usage:
- Download OpenStreetMap data as geojson, for instance from https://overpass-turbo.eu/
- Download map shapefile. I used https://www.naturalearthdata.com/downloads/ 10m scale world map
- Run ```python prepare.py```
- Run ```Rscript voronoi.R```
