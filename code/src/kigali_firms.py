!pip install osmnx pandas
import osmnx as ox
import pandas as pd
import geopandas as gpd
import folium


place = "Kigali, Rwanda"
tags = {"amenity": True, "shop": True, "office": True}

gdf = ox.features.features_from_place(place, tags)

for col in ["name", "amenity", "shop", "office"]:
    if col not in gdf.columns:
        gdf[col] = None

gdf = gdf[["name", "amenity", "shop", "office", "geometry"]].copy()
gdf = gdf[gdf["geometry"].notnull()]

gdf = gdf[gdf[["amenity", "shop", "office"]].notnull().any(axis=1)]

raw_file = f"drive/MyDrive/kigali_firms_raw.csv"
gdf.to_csv(raw_file, index=False)

df = gdf.drop_duplicates(subset=["name"]).copy()

df["type"] = df["amenity"].fillna(df["shop"]).fillna(df["office"])

firm_types = [
    "bank", "restaurant", "cafe", "bar",
    "pharmacy", "supermarket", "shop"
]

df = df[df["type"].isin(firm_types)]

df = df[["name", "type", "geometry"]]

gdf_proj = df.to_crs(epsg=3857)
centroids = gdf_proj.centroid.to_crs(epsg=4326)

df["lat"] = centroids.y.values
df["lon"] = centroids.x.values

df["activity_score"] = 1

#drop firm names for privacy
df = df.drop(columns=["name"])

clean_file = f"drive/MyDrive/kigali_firms_clean.csv"
df.to_csv(clean_file, index=False)

print("Clean data saved:", clean_file)
print("\nTop categories:")
print(df["type"].value_counts().head(10))

m = folium.Map(location=[-1.95, 30.06], zoom_start=12)

for _, row in df.iterrows():
    if pd.notnull(row["lat"]) and pd.notnull(row["lon"]):
        folium.CircleMarker(
            location=[row["lat"], row["lon"]],
            radius=3
        ).add_to(m)

map_file = f"drive/MyDrive/kigali_firm_map.html"
m.save(map_file)

print("Map saved:", map_file)