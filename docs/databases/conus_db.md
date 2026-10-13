# CONUS Reservoir and Lake Evaporation

> Daily, near-real-time evaporation estimates and forecast products for reservoirs and lakes throughout the contiguous United States (CONUS).

[//]: # (| | |)

[//]: # (|:---:|:---:|)

[//]: # (| ![Texas Water Development Board logo]&#40;../images/twdb_logo.jpg&#41;{ width="240" } | ![U.S. Army Corps of Engineers logo]&#40;../images/usace_logo.png&#41;{ width="160" } |)

## Find the right resource

| Resource | Use it to | Access |
|---|---|---|
| Reservoir Web Explorer | View and compare reservoir evaporation, storage, and meteorological data. | [Open Explorer](https://dri-apps.projects.earthengine.app/view/twdb-reservoir-evaporation) |
| Reservoir Evaporation API | Retrieve data programmatically for analysis and integration. | [View API documentation](https://twdb.dri.edu/docs) |
| Gridded Evaporation | Access statewide estimates for six representative pond scenarios. | [View gridded data](https://dri-apps.projects.earthengine.app/view/twdb-raster-lake-evaporation) |
| Evaporation Forecasts | Access 28-day forecast data for supported reservoirs. | [View forecasts](https://dri-apps.projects.earthengine.app/view/twdb-reservoir-forecast) |

## What data are available?

The project provides historical and near-real-time records of:

- Evaporation rates and volumes
- Reservoir storage conditions and related physical parameters
- Meteorological forcing data
- Forecast forcing and evaporation products


## About the project

### Why evaporation matters
Evaporation is a major component of reservoir water budgets and operational planning.
Traditional pan-evaporation approaches can introduce bias and uncertainty
*(Friedrich et al., 2018)*. This project applies hydrometeorological modeling and
cloud-based processing to provide consistent evaporation estimates across Texas.

### Project objectives
- Produce reservoir-specific evaporation rates and volumes for major Texas
  water-supply reservoirs.
- Provide statewide gridded evaporation estimates for six pond scenarios.
- Support water management, planning, analysis, and public access to evaporation data.

### Partners and funding
The CONUS-wide Reservoir Evaporation Project was supported by: 

- [National Aeronautics and Space Administration (NASA)](https://www.twdb.texas.gov/)
- [U.S. Army Corps of Engineers (USACE)](https://www.swf.usace.army.mil/)

## Data sources and model forcings

Reservoir evaporation estimates integrate specific meteorological, hydrologic, and geospatial
datasets to provide stakeholders with consistent, high-quality information for their intended use cases and
applications. The following table summarizes the primary datasets used to develop reservoir evaporation estimates.
See the [project report](URL) and [methods documentation](URL) for details.

| Category | Source / product                     |       Period | Use in this project                                              | Link                                                                                                 |
|---|--------------------------------------|-------------:|------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| Meteorological forcing¹ | URMA                                 |    1980–1985 | Bias-corrected to align with RTMA and used to force DLEM.        | [gridMET](https://climateengine.org/datasets/climatehydrology/urma_daily_2500/)                      |
| Meteorological forcing¹ | URMA                                 | 1985–present | URMA b.                                                          | [Climate Engine RTMA Daily](https://climateengine.org/datasets/climatehydrology/rtma_daily_2500/)    |
| Precipitation | PRISM (800m)                         | 1980–present | Used in precipitation and net-evaporation estimates.             | [PRISM](https://gee-community-catalog.org/projects/prism_daily/)                                                 |
| Reservoir parameters | TWDB                                 | 1980–present | Provides reservoir area, volume, and depth data where available. | [Water Data for Texas](https://www.waterdatafortexas.org/)                                           |
| GIS data | Reclamation, TWDB, USGS, Hydrolakes² |            — | Provides reservoir geometry and extent.                          |                                          |
| Forecast forcings | CFS gridMET                          |            — | Provides 28-day forecast forcings, bias-corrected to URMA.       | [Climate Engine CFS gridMET](https://climateengine.org/datasets/forecasts/cfsgridmet_1to4week_4000/) |

¹ Meteorological forcing variables include air temperature, vapor pressure deficit,
wind speed and direction, solar radiation, and air pressure. See the
[Appendix](https://docs.openwaterevap.net/appendix/) for additional information and definitions.

²The CONUS-wide dataset blends geometry information from multiple sources to provide spatial coverage throughout CONUS.
Specific sources include Reclamation, Texas Water Development Board, USGS, and HydroLAKES. Before integration,
HydroLAKES polygons were screened and refined to improve linework and more accurately represent the extent of each water
body. Source information for individual polygons is available in the GIS attribute tables.

