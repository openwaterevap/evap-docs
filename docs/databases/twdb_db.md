# Texas Reservoir Evaporation

> Daily, near-real-time evaporation estimates and forecast products for Texas reservoirs.

| | |
|:---:|:---:|
| ![Texas Water Development Board logo](../images/twdb_logo.jpg){ width="240" } | ![U.S. Army Corps of Engineers logo](../images/usace_logo.png){ width="160" } |


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
The Texas Reservoir Evaporation Project was jointly funded by:

- [Texas Water Development Board (TWDB)](https://www.twdb.texas.gov/)
- [U.S. Army Corps of Engineers (USACE)](https://www.swf.usace.army.mil/)

## Data sources and model forcings

Reservoir evaporation estimates integrate specific meteorological, hydrologic, and geospatial
datasets to provide stakeholders with consistent, high-quality information for their intended use cases and
applications. The following table summarizes the primary datasets used to develop reservoir evaporation estimates for the
State of Texas.
See the [project report](URL) and [methods documentation](URL) for details.

| Category | Source / product | Period | Use in this project | Link |
|---|---|---:|---|---|
| Meteorological forcing¹ | gridMET | 1980–2015 | Bias-corrected to align with RTMA and used to force DLEM. | [gridMET](https://www.climatologylab.org/gridmet.html) |
| Meteorological forcing¹ | RTMA | 2016–present | Aggregated from hourly to daily and used to force DLEM. | [Climate Engine RTMA Daily](https://climateengine.org/datasets/climatehydrology/rtma_daily_2500/) |
| Precipitation | gridMET | 1980–present | Used in precipitation and net-evaporation estimates. | [gridMET](https://www.climatologylab.org/gridmet.html) |
| Reservoir parameters | TWDB | 1980–present | Provides reservoir area, volume, and depth data where available. | [Water Data for Texas](https://www.waterdatafortexas.org/) |
| GIS data | TWDB | — | Provides reservoir geometry and extent. | [Water Data for Texas](https://www.waterdatafortexas.org/) |
| Forecast forcings | CFS gridMET | — | Provides 28-day forecast forcings, bias-corrected to RTMA. | [Climate Engine CFS gridMET](https://climateengine.org/datasets/forecasts/cfsgridmet_1to4week_4000/) |

¹ Meteorological forcing variables include air temperature, vapor pressure deficit,
wind speed and direction, solar radiation, and air pressure. See the
[Appendix](https://docs.openwaterevap.net/appendix/) for definitions.ls on forcing variables, refer to the [Appendix](https://docs.openwaterevap.net/appendix/).