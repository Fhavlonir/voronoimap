import geopandas as gpd

gdf = gpd.read_file('export.geojson')
gdf = gdf[gdf['amenity']!='restaurant']
gdf['Kedja'] = gdf['name'].str.lower().apply(lambda x: 'ICA' if 'ica' in str(x) else 'Coop' if 'coop' in str(x) or 'konsum' in str(x) else 'Axfood' if 'tempo' in str(x) or 'matöppet' in str(x) or 'hemköp' in str(x) or 'willys' in str(x) or 'willy:s' in str(x) or "handlar'n" in str(x) or 'handlarn' in str(x) or 'city gross' in str(x) else None )
gdf['Kedja2'] = gdf['brand'].str.lower().apply(lambda x: 'ICA' if 'ica' in str(x) else 'Coop' if 'coop' in str(x) or 'konsum' in str(x) else 'Axfood' if 'tempo' in str(x) or 'matöppet' in str(x) or 'hemköp' in str(x) or 'willys' in str(x) or 'willy:s' in str(x) or "handlar'n" in str(x) or 'handlarn' in str(x) or 'city gross' in str(x) else None )
gdf['Kedja'] = gdf['Kedja'].fillna(gdf['Kedja2'])
gdf['geometry'] = gdf['geometry'].centroid

gdf[['name', 'Kedja', 'geometry']].to_file('supermarkets.geojson')
