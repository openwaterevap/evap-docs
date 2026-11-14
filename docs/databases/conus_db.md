# CONUS Open Water Evaporation

> Daily, near-real-time evaporation estimates and forecast products for reservoirs and lakes throughout the contiguous United States (CONUS).

!!! warning "Beta / Provisional Data"
    Current estimates are based on static surface area and depth information. Dynamic surface area and depth
    estimates derived from remote sensing workflows are planned for incorporation in 2027. Users should
    interpret estimates with caution and anticipate updates to data values and methodology.

<p align="center">
  <img src="/images/conus_water.png" width="480" alt="CONUS-wide water bodies.">
</p>

## Find the right resource

| Resource                   | Use it to | Access |
|----------------------------|---|---|
| Open Water Web Explorer    | View and compare evaporation, storage, and meteorological data. | [Open Explorer](https://dri-apps.projects.earthengine.app/view/openwaterevap) |
| Open Water Evaporation API | Retrieve data programmatically for analysis and integration. | COMING SOON |

[//]: # (| Evaporation Forecasts | Access 28-day forecast data for supported reservoirs. | [View forecasts]&#40;https://dri-apps.projects.earthengine.app/view/twdb-reservoir-forecast&#41; |)

## What data are available?

The project provides historical and near-real-time records of:

- Evaporation rates and volumes
- Reservoir storage conditions and related physical parameters
- Meteorological forcing data
- Forecast forcing and evaporation products


## About the project

### Why evaporation matters
Evaporation is a major component of a water bodies water budgets and operational planning.
Traditional pan-evaporation approaches can introduce bias and uncertainty
*(Friedrich et al., 2018)*. This project applies hydrometeorological modeling and
cloud-based processing to provide consistent evaporation estimates across the Contiguous United States.

### Project objectives
- Produce water body-specific evaporation rates and volumes for major and minor water bodies throughout CONUS.
- Support water management, planning, analysis, and public access to evaporation data.

### Partners and funding
The CONUS-wide Reservoir Evaporation Project was supported by:

- [National Aeronautics and Space Administration (NASA)](https://www.nasa.gov/)
- [United States Geological Survey (USGS)](https://www.usgs.gov/)

## Data sources and model forcings

Open water evaporation estimates integrate specific meteorological, hydrologic, and geospatial
datasets to provide stakeholders with consistent, high-quality information for their intended use cases and
applications. The following table summarizes the primary datasets used to develop open water evaporation estimates.

[//]: # (See the [project report]&#40;URL&#41; and [methods documentation]&#40;URL&#41; for details.)

| Category                | Source / product                                      | Period | Use in this project                                                 | Link                                                                                              |
|-------------------------|-------------------------------------------------------|---|---------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| Meteorological forcing¹ | URMA                                                  | 1985–present | Provides meteorological forcing variables for evaporation modeling. | [Climate Engine URMA Daily](https://climateengine.org/datasets/climatehydrology/urma_daily_2500/) |
| Precipitation           | PRISM (800m)                                          | 1980–present | Used in precipitation and net-evaporation estimates.                | [PRISM](https://gee-community-catalog.org/projects/prism_daily/)                                  |
| Water body parameters²  | Coming Soon                                           | 1980–present | Provides area, volume, and depth data where available.              | Coming Soon                                                                                       |
| GIS data                | HydroLAKES, GRanD, Reclamation, TWDB, USGS³ | — | Provides water body geometry and extent.                            | Documentation coming soon.                                                                        |

¹ Meteorological forcing variables include air temperature, vapor pressure deficit,
wind speed and direction, solar radiation, and air pressure. See the
[Appendix](https://docs.openwaterevap.net/appendix/) for additional information and definitions.

²Current estimates in the CONUS-wide dataset apply static surface area and depth information derived from the original
polygon data source (e.g. Reclamation, Texas Water Development Board, USGS, and HydroLAKES). To support improved
estimation of water body surface area, volume, and depth at locations lacking monitoring or real-time data, a remote
sensing workflow is under development. It uses Landsat satellite imagery and the
[USGS Dynamic Surface Water Extent algorithm](https://www.usgs.gov/landsat-missions/landsat-dynamic-surface-water-extent-science-products).

³The CONUS-wide dataset blends geometry information from multiple sources to provide spatial coverage throughout CONUS.
Specific sources include Reclamation, Texas Water Development Board, USGS, and HydroLAKES. Before integration,
HydroLAKES polygons were screened and refined to improve linework and more accurately represent the extent of each water
body. Source information for individual polygons is available in the GIS attribute tables.