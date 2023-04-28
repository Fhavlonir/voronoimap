library(sf)
library(tidyverse)

affarer <- st_transform(st_read("supermarkets.geojson"), st_crs("EPSG:3006"))
world  <- read_sf("ne_10m_admin_0_countries.shp")
sweden <- st_transform(world[world$NAME == "Sweden",], st_crs("EPSG:3006"))

voronoi <- affarer %>%
        st_geometry() %>%
        st_union() %>%
        st_voronoi(envelope = st_geometry(sweden)) %>%
        st_collection_extract(type="POLYGON") %>%
        st_sf() %>%
        st_intersection(sweden) %>%
        st_join(affarer)

ggplot() +
        geom_sf(data=voronoi, aes(fill=Kedja), alpha=.2, lty=0) +
        scale_fill_manual(values=c('blue', 'green', 'red'))+
        geom_sf(data=sweden, lwd=.1, fill=NA, lty=1)+
        geom_sf(data=affarer, aes(color=Kedja), pch=20, alpha=0.5, size=.2, lwd=0.01)+
        scale_colour_manual(values=c('blue', 'darkgreen', 'red'))
        #labs(fill="Zone")

