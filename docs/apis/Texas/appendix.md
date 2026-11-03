# Texas API Appendix

## Available Variables

### Reservoir Variables

The following variables are available for reservoirs, by dataset:

#### RTMA Dataset (Weather Variables)

Weather data before 2016 is derived from the hybrid RTMA-gridMET dataset. See the [Methods](../../methods.md) section for additional details.

| Variable | Description | Units (Metric) | Units (English) |
|----------|-------------|----------------|-----------------|
| pr | Daily Precipitation | mm | in |
| tmmx_c | Daily Maximum Temperature | °C | °F |
| tmmn_c | Daily Minimum Temperature | °C | °F |
| vpd_kpa | Daily Vapor Pressure Deficit | kPa | psi |
| pres | Daily Atmospheric Pressure | Pa | psi |
| vs2m | Daily Wind Speed at 2m | m/s | mph |
| th | Daily Wind Direction | deg | deg |
| srad | Daily Solar Radiation | W/m² | Btu/s/ft² |
| etr | Daily Alfalfa Reference ET | mm | in |
| eto | Daily Grass Reference ET | mm | in |
| sph_kgkg | Daily Specific Humidity | kg/kg | lb/lb |

#### CFS_GRIDMET Dataset (Forecast Weather Variables)

Forecast weather data comes from CFS gridMET (28-day forecasts). The forecast datasets also include `res`, `lem`, and `nete-volume-calcs`, with the same variables as the tables below.

| Variable | Description | Units (Metric) | Units (English) |
|----------|-------------|----------------|-----------------|
| pr | Daily Precipitation | mm | in |
| tmmx_c | Daily Maximum Temperature | °C | °F |
| tmmn_c | Daily Minimum Temperature | °C | °F |
| vpd_kpa | Daily Vapor Pressure Deficit | kPa | psi |
| vs2m | Daily Wind Speed at 2m | m/s | mph |
| srad | Daily Solar Radiation | W/m² | Btu/s/ft² |
| etr | Daily Alfalfa Reference ET | mm | in |
| eto | Daily Grass Reference ET | mm | in |
| th | Daily Wind Direction | deg | deg |
| sph_kgkg | Daily Specific Humidity | kg/kg | lb/lb |
| pres | Daily Atmospheric Pressure | Pa | psi |

#### RES Dataset (Reservoir Physical Variables)

| Variable | Description | Units (Metric) | Units (English) |
|----------|-------------|----------------|-----------------|
| stage_m | Lake Surface Elevation (above mean sea level) | m | ft |
| area_m2 | Lake Surface Area | m² | ft² |
| depth_m | Average Lake Depth | m | ft |

#### LEM Dataset (DLEM Evaporation and Heat Storage Variables)

| Variable | Description | Units (Metric) | Units (English) |
|----------|-------------|----------------|-----------------|
| E_hs | Daily Penman Evaporation with heat storage | mm | in |
| E_nhs | Daily Penman Evaporation without heat storage | mm | in |
| Rn | Net Radiation | MJ/m² | Btu/ft² |
| Tw | Water Temperature at end of day | °C | °F |
| Tw0 | Water Temperature at end of previous day | °C | °F |
| Fetch | Daily Reservoir Fetch based on wind dir and area | -- | -- |
| Lerr | LEM Model Error Flag | -- | -- |

#### NETE-VOLUME-CALCS Dataset (Net Evaporation and Evaporation Volume Variables)

| Variable | Description | Units (Metric) | Units (English) |
|----------|-------------|----------------|-----------------|
| NetE | Net Evaporation (E_hs - pr_mean) | mm | in |
| E_volume | Evaporation Volume (E_hs * area) | m³ | ft³ |
| NetE_volume | Net Evaporation Volume (NetE * area) | m³ | ft³ |

### Pond Evaporation Variables

The pond evaporation endpoints (`/timeseries/daily/point/pond_evaporation/daterange` and `/timeseries/daily/polygon/pond_evaporation/daterange`) return daily gridded evaporation for six representative pond scenarios, in mm (metric) or in (English). Each scenario is a variable named after the pond's depth, area, and volume:

| Variable | Depth | Area | Volume |
|----------|-------|------|--------|
| depth5_area5_volume25 | 5 | 5 | 25 |
| depth5_area25_volume125 | 5 | 25 | 125 |
| depth10_area5_volume50 | 10 | 5 | 50 |
| depth10_area25_volume225 | 10 | 25 | 225 |
| depth10_area100_volume1000 | 10 | 100 | 1000 |
| depth20_area100_volume2000 | 20 | 100 | 2000 |

## HTTP Status Codes

The API may return the following HTTP status codes:

| Status Code | Description |
|-------------|-------------|
| 200 | Successful response |
| 403 | Forbidden (missing or invalid API key) |
| 404 | Not found (resource not found) |
| 422 | Validation error (invalid parameters) |
| 500 | Server error |

## Data Quality Flags

If you request `also_return=qflag`, each value includes a data quality flag:

| Flag | Description |
|------|-------------|
| O | Raw data value from data sites |
| M | Data was not available for this date and is filled with the previous date's value |
| S | Data point is static |
| R | Removed outlier data |

## File Formats

### Shapefile Components

When uploading a shapefile to filter reservoirs by location (`/info/list_RES_NAMES`), the following files are required:

| File Extension | Description |
|----------------|-------------|
| .shp | The main file that stores the geometry |
| .dbf | The database file that stores the attributes |
| .prj | The projection file that stores the coordinate system |
| .shx | The index file that stores the index of the geometry |

## Glossary

| Term | Definition |
|------|------------|
| Evaporation | The process by which water changes from a liquid to a gas or vapor |
| Net Evaporation | The difference between evaporation and precipitation (evaporation minus precipitation) |
| Reservoir | A large natural or artificial lake used as a source of water supply |
| Forecast | A 28-day projection of weather and evaporation for a reservoir |
| NWSLI ID | National Weather Service Location Identifier, convertible to reservoir names with `/info/convert_NWSLI_IDs` |
| Timeseries | A series of data points indexed in time order |
| Metadata | Data that provides information about other data |
| API | Application Programming Interface |
| REST | Representational State Transfer, an architectural style for APIs |
| JSON | JavaScript Object Notation, a lightweight data-interchange format |
| CSV | Comma-Separated Values, a text file format that uses commas to separate values |
| Dataset | A collection of data |
| Variable | A measurable property |
| Units | The standard of measurement |
| Metric | The International System of Units (SI) |
| English | The US Customary Units |
| Quality Flag | An indicator of the quality or reliability of the data |
| Shapefile | A geospatial vector data format for geographic information system software |
