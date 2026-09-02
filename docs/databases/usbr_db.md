# Reclamation Reservoir Evaporation

> Daily, near-real-time evaporation estimates and forecast products for Reclamation reservoirs.

[//]: # ([Explore reservoir data]&#40;https://twdb.dri.edu/&#41; · [Access the API]&#40;https://twdb.dri.edu/&#41;)

## Data Access

| Resource | Use it to | Access |
|---|---|---|
| Reservoir Web Explorer | View and compare reservoir evaporation, storage, and meteorological data. | [Open Explorer](https://dri-apps.projects.earthengine.app/view/bor-reservoir-evaporation) |
| Reservoir Evaporation API | Retrieve data programmatically for analysis and integration. | [View API documentation](https://operevap.dri.edu/docs) |



## What data are available?

The project provides historical and near-real-time records of:

- Evaporation rates and volumes
- Reservoir storage conditions and related physical parameters
- Meteorological forcing data



## About the project

### Why evaporation matters
Evaporation is a major component of reservoir water budgets and operational planning.
Traditional pan-evaporation approaches can introduce bias and uncertainty
*(Friedrich et al., 2018)*. This project applies hydrometeorological modeling and
cloud-based processing to provide consistent evaporation estimates for Reclamation reservoirs.
Reclamation DLEM estimates are being explored for potential integration in modeling and forecasting
workflows. Data is considered provisional and not in operational use at this time. 

See the [project report](URL) for more details.

### Project objectives
- Produce reservoir-specific evaporation rates and volumes for Reclamation reservoirs.
- Assess differences between legacy and new rates to inform potential adoption in Reclamation decision-making.
- Support water management, planning, analysis, and public access to evaporation data.

### Partners and funding
The Reclamation Reservoir Evaporation Project was developed in partnership with Reclamation Technical Service Center (TSC)
and funded by:

- [United States Bureaue of Reclamation (Reclamation)](https://www.usbr.gov/)

## Data sources and model forcings

Reservoir evaporation estimates integrate specific meteorological, hydrologic, and geospatial
datasets to provide stakeholders with consistent, high-quality information for their intended use cases and
applications. The following table summarizes the primary datasets used to develop reservoir evaporation estimates for 
Reclamation reservoirs.


| Category | Source / product | Period | Use in this project | Link                                                                                              |
|---|------------------|---:|---|---------------------------------------------------------------------------------------------------|
| Meteorological forcing¹ | gridMET          | 1980–2015 | Bias-corrected to align with RTMA and used to force DLEM. | [gridMET](https://www.climatologylab.org/gridmet.html)                                            |
| Meteorological forcing¹ | RTMA             | 2016–present | Aggregated from hourly to daily and used to force DLEM. | [Climate Engine RTMA Daily](https://climateengine.org/datasets/climatehydrology/rtma_daily_2500/) |
| Precipitation | gridMET          | 1980–present | Used in precipitation and net-evaporation estimates. | [gridMET](https://www.climatologylab.org/gridmet.html)                                            |
| Reservoir parameters | TWDB             | 1980–present | Provides reservoir area, volume, and depth data where available. | [USBR RISE and others²](https://data.usbr.gov/rise-api)                                           |
| GIS data | Reclamation      | — | Provides reservoir geometry and extent. | [RISE](https://data.usbr.gov/catalog/6406/item/72729)                                             |

¹ Meteorological forcing variables include air temperature, vapor pressure deficit,
wind speed and direction, solar radiation, and air pressure. See the
[Appendix](https://docs.openwaterevap.net/appendix/) for definitions.ls on forcing variables, refer to the [Appendix](https://docs.openwaterevap.net/appendix/).


² Reservoir elevation information is gathered from multiple sources including Reclamation’s Hydromet, United States Geological Survey (USGS) National Water Information System (NWIS),
Reclamation Information Sharing Environment (RISE), and the California Data Exchange Center (CDEC). Elevaiton information is combined with Area-Elevation-Capacity curves to 
estimate both surface area and average depth. Locations without accessible data use static values for depth and area. 