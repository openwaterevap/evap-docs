# CONUS API Appendix

## Available Variables

### Reservoir Variables

The following variables are available for reservoirs, by dataset:

#### URMA Dataset (Weather Variables)

The CONUS project uses daily weather data from the UnRestricted Mesoscale Analysis (URMA). See the [Methods](../../methods.md) section for additional details.

| Variable | Description | Units (Metric) | Units (English) |
|----------|-------------|----------------|-----------------|
| pr | Daily Precipitation | mm | in |
| tmax | Daily Maximum Temperature | °C | °F |
| tmin | Daily Minimum Temperature | °C | °F |
| vpd | Daily Vapor Pressure Deficit | kPa | psi |
| vs2m | daily 2meter windspeed | m/s | mph |
| srad | Daily Solar Radiation | W/m² | Btu/s/ft² |
| etr | Daily Alfalfa Reference ET | mm/day | in |
| eto | Daily Grass Reference ET | mm/day | in |
| th | Daily Wind Direction | deg | deg |
| sph | Daily Specific Humidity | kg/kg | lb/lb |
| pres | Daily Atmospheric Pressure | Pa | psi |

#### CFS_GRIDMET Dataset (Forecast Weather Variables)

Forecast weather data comes from CFS gridMET (28-day forecasts). The forecast datasets also include `res`, `lem`, and `nete-volume-calcs`, with the same variables as the tables below.

| Variable | Description | Units (Metric) | Units (English) |
|----------|-------------|----------------|-----------------|
| pr | Daily Precipitation | mm | in |
| tmax | Daily Maximum Temperature | °C | °F |
| tmin | Daily Minimum Temperature | °C | °F |
| vpd | Daily Vapor Pressure Deficit | kPa | psi |
| vs2m | daily 2meter windspeed | m/s | mph |
| srad | Daily Solar Radiation | W/m² | Btu/s/ft² |
| etr | Daily Alfalfa Reference ET | mm/day | in |
| eto | Daily Grass Reference ET | mm/day | in |
| th | Daily Wind Direction | deg | deg |
| sph | Daily Specific Humidity | kg/kg | lb/lb |
| pres | Daily Atmospheric Pressure | Pa | psi |

#### RES Dataset (Reservoir Physical Variables)

| Variable | Description | Units (Metric) | Units (English) |
|----------|-------------|----------------|-----------------|
| stage | lake Surface Elevation (above mean sea level) | m | ft |
| area | Lake Surface Area | m² | ft² |
| depth | Average Lake Depth | m | ft |
| tds | Total Desolved Solids | tds | -- |

#### LEM Dataset (DLEM Evaporation and Heat Storage Variables)

| Variable | Description | Units (Metric) | Units (English) |
|----------|-------------|----------------|-----------------|
| evap | Penman Evaporation with heat storage | mm/day | in |
| evap_noheat | Penman Evaporation without heat storage | mm/day | in |
| rn | Net Radiation | MJ/m² per day | Btu/ft² |
| tw | Water Temperature at end of day, celsius | °C | °F |
| tw0 | Water Temperature at previous time step | °C | °F |
| fch | Daily Reservoir Fetch based on wind dir and area | -- | -- |
| ierr | LEM Model Error Flag | -- | -- |

#### NETE-VOLUME-CALCS Dataset (Net Evaporation and Evaporation Volume Variables)

| Variable | Description | Units (Metric) | Units (English) |
|----------|-------------|----------------|-----------------|
| net_evap | Net Evaporation (E_hs - pr_mean) | mm | in |
| evap_volume | Evaporation Volume (E_hs * area) | m³ | ft³ |
| net_evap_volume | Net Evaporation Volume (NetE * area) | m³ | ft³ |

### Station Variables

The following variables are available for stations (`/timeseries/stations/...` endpoints):

| Variable | Description | Units (Metric) | Units (English) |
|----------|-------------|----------------|-----------------|
| ATemp | Air Temperature | °C | °F |
| ATemp_Min | Air Temperature Min | °C | °F |
| ATemp_Max | Air Temperature Max | °C | °F |
| BP | Barometric Pressure | kPa | psi |
| BR | Bowen Ratio | -- | -- |
| Ce | Bulk Transfer Coefficient | -- | -- |
| DO | Dissolved Oxygen, Water, Unfiltered | mg/L | lb/gal |
| DO_percent | Dissolved Oxygen, Water, Unfiltered | percent of saturation | % of saturation |
| EnergyT | Energy Transferred to Lakebed | W/m² | Btu/s/ft² |
| ETo | ETo | mm/day | in/day |
| ETr | ETr | mm/day | in/day |
| evap_1 | Evaporation | mm/day | in/day |
| evap_2 | Evaporation | mm/day | in/day |
| evap_3 | Evaporation | mm/day | in/day |
| evap_4 | Evaporation | mm/day | in/day |
| evap_5 | Evaporation | mm/day | in/day |
| HSEnergyFlux | Heat Storage Energy Flux | W/m² | Btu/s/ft² |
| IncomingSR | Incoming Shortwave Radiation | W/m² | Btu/s/ft² |
| inflow | Inflow | m³/s | ft³/s |
| SurfaceT | Mean Surface Temperatures | °C | °F |
| MO_StabilityL | MOST Stability Length | -- | -- |
| NC_EnergyStored | Net Change in Energy Stored in the Lake | W/m² | Btu/s/ft² |
| NR | Net Radiation | W/m² | Btu/s/ft² |
| NW_AdvectedE | Net Water Advected Energy | W/m² | Btu/s/ft² |
| outflow | Outflow | m³/s | ft³/s |
| PH | PH, Water, Unfiltered, Field | standard units | -- |
| RH | Relative Humidity | % | % |
| SamplingD | Sampling Depth | m | ft |
| SkinTemp | Skin Temperature | °C | °F |
| SpecConduct | Specific Conductance, Water, Unfiltered | microsiemens/cm at 25 degC | uS/in at 25 degC |
| SWin | Swin | W/m² | Btu/s/ft² |
| VP | Vapor Pressure | kPa | psi |
| VPD | VPD | kPa | psi |
| WTemp | Water Temperature | °C | °F |
| WVD | Water Vapor Density | g/m³ | lb/ft³ |
| WD | Wind direction | deg | deg |
| WS | Wind Speed | m/s | mph |
| PofDays | Percentage of days represented | % | % |

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

When uploading a shapefile to filter reservoirs or stations by location (`/info/list_OWEN_NAMES`, `/info/list_STA_NAMES`), the following files are required:

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
| Station | An in-situ monitoring site at or near a reservoir |
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
