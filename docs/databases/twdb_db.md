# Texas Reservoir Evaporation Database & Web Application

> A statewide resource for accessing high-quality, near-real-time reservoir evaporation data for Texas.

---

## Project Overview

### Background

Reservoir evaporation is a critical component of water budgeting and operational planning. However, it is often overlooked or simplified because consistent, accurate evaporation estimates can be difficult to obtain.

Historically, evaporation estimates across Texas have relied on pan evaporation methods, which are known to introduce substantial bias and uncertainty *(Friedrich et al., 2018)*. Recent advances in hydrometeorological modeling and cloud-based data processing now enable the near-real-time production of high-resolution evaporation estimates to support water-management decisions.

### Funding

The Texas Reservoir Evaporation Project was jointly funded by:

- [**Texas Water Development Board (TWDB)**](https://www.twdb.texas.gov/)
- [**U.S. Army Corps of Engineers (USACE)**](https://www.swf.usace.army.mil/)

### Database Description

This project developed a freely accessible, daily reservoir evaporation database for water managers, planners, stakeholders, and the public throughout Texas.

The database provides historical and near-real-time records of:

- **Evaporation rates**
- **Evaporation volumes**
- **Reservoir storage conditions**
- **Meteorological forcing data**

These inputs are integrated to produce the best available estimates of reservoir evaporation for major Texas reservoirs.

In addition to reservoir-specific estimates, the project includes a raster-based **DLEM** application that simulates evaporation under six pond scenarios statewide. These scenarios support planning and development in locations where site-specific reservoir data are unavailable.

---

## Project Objectives

- Produce reservoir-specific simulations of evaporation rates and volumes for major water-supply reservoirs throughout Texas.
- Generate gridded evaporation estimates for six pond scenarios to support statewide planning and development activities.

---

## Applications & Resources

| Resource | Description | Link |
|---|---|---|
| **Texas Reservoir Evaporation API** | Provides programmatic access to evaporation data for reservoirs across Texas. | [Visit API](https://twdb.dri.edu/) |
| **Texas Reservoir Evaporation Web Explorer** | Provides an interactive interface for viewing reservoir evaporation data. | [Open Web Explorer](https://twdb.dri.edu/) |
| **Texas Gridded Reservoir Evaporation** | Provides access to gridded evaporation estimates across the state of Texas. | [View Gridded Data](https://twdb.dri.edu/) |
| **Texas Reservoir Evaporation Forecast** | Provides access to reservoir evaporation forecast data. | [View Forecast Data](https://twdb.dri.edu/) |

---

## Texas Reservoir Data and DLEM Forcings

| Category                           | Data Source | Time Period | Description                                                                                                            | Link                                                                                                 |
|------------------------------------|:-----------:|:---:|------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| Meteorological forcing<sup>1</sup> |   gridMET   | 1980–2015 | gridMET meteorological forcings are adjusted to RTMA using monthly bias-correction factors.                            | [gridMET](https://www.climatologylab.org/gridmet.html)                                               |
| Meteorological forcing<sup>1</sup> |    RTMA     | 2016–present | RTMA data are aggregated from hourly to daily by Climate Engine and used to force DLEM.                                | [Climate Engine RTMA Daily](https://climateengine.org/datasets/climatehydrology/rtma_daily_2500/)    |
| Precipitation                      |   gridMET   | 1980–present | Precipitation and net evaporation estimates are based on gridMET precipitation data.                                   | [gridMET](https://www.climatologylab.org/gridmet.html)                                               |
| Reservoir parameters               |    TWDB     | 1980–present | Reservoir area, volume, and depth are based on on-site observations where available; static values are used elsewhere. | [TWDB Water Data for Texas](https://www.waterdatafortexas.org/)                                      |
| GIS data                           |    TWDB     | — | Reservoir geometry and extent are derived from polygons developed by TWDB.                                             | [TWDB Water Data for Texas](https://www.waterdatafortexas.org/)                                      |
| Forecast Forcings                  | CFS gridMET | — | 28-day forecast forcings are derived from CFS gridMET and adjusted to RTMA using monthly bias-correction factors.      | [Climate Engine CFS gridMET](https://climateengine.org/datasets/forecasts/cfsgridmet_1to4week_4000/) |

<sup>1</sup>Meteorological forcing variables include air temperature, vapor pressure deficit, wind speed and direction, solar radiation, and air pressure. 
For more details on forcing variables, refer to the [Appendix](https://docs.openwaterevap.net/appendix/).