# API Overview

Each OWEN project (Texas, Reclamation, and CONUS) has its own Reservoir Evaporation API. The APIs share the same structure, but the endpoints they offer differ by project.

## Key differences

| | Texas | Reclamation | CONUS                                                    |
|---|---|---|----------------------------------------------------------|
| Base URL | [https://twdb.dri.edu](https://twdb.dri.edu) | [https://operevap.dri.edu](https://operevap.dri.edu) | [https://nasa-revap.dri.edu](https://nasa-revap.dri.edu) |
| Reservoir name parameter | `RES_NAMES` | `RES_NAMES` | `OWEN_NAMES`                                             |
| Stations | No | Yes | Yes                                                      |
| Forecasts | Yes | No | Yes                                                      |
| Gridded pond evaporation | Yes | No | No                                                       |
| Documentation | [Getting Started](Texas/getting-started.md) | [Getting Started](Reclamation/getting-started.md) | [Getting Started](CONUS/getting-started.md)              |

Each project requires its own API key. See the Authentication page for [Texas](Texas/authentication.md), [Reclamation](Reclamation/authentication.md), or [CONUS](CONUS/authentication.md).

## Endpoint availability

| Endpoint | Texas | Reclamation | CONUS |
|---|:---:|:---:|:---:|
| `GET /auth/request_key` | ✓ | ✓ | ✓ |
| `GET /info/list_datasets`, `/info/list_variables`, `/info/list_dates` | ✓ | ✓ | ✓ |
| `GET /info/list_forecast_datasets`, `/info/list_forecast_variables`, `/info/list_forecast_dates` | ✓ | – | ✓ |
| `POST /info/list_RES_NAMES` | ✓ | ✓ | – |
| `POST /info/list_OWEN_NAMES` | – | – | ✓ |
| `GET /info/convert_NWSLI_IDs` | ✓ | – | – |
| `POST /info/list_STA_NAMES` | – | ✓ | ✓ |
| `GET /info/list_station_variables`, `/info/list_station_dates` | – | ✓ | – |
| `GET /info/list_stations_variables`, `/info/list_stations_dates` | – | – | ✓ |
| `GET /metadata/reservoirs` | ✓ | ✓ | ✓ |
| `GET /metadata/stations` | – | ✓ | ✓ |
| `GET /timeseries/daily/reservoirs/daterange`, `/timeseries/daily/reservoirs/date` | ✓ | ✓ | ✓ |
| `GET /timeseries/forecast/daily/reservoirs/daterange`, `/timeseries/forecast/daily/reservoirs/date` | ✓ | – | ✓ |
| `GET /timeseries/stations/daterange`, `/timeseries/stations/date` | – | ✓ | ✓ |
| `GET /timeseries/daily/point/pond_evaporation/daterange` | ✓ | – | – |
| `GET /timeseries/daily/polygon/pond_evaporation/daterange` | ✓ | – | – |

!!! note
    The station variable and date endpoints are named `list_station_*` on the Reclamation API and `list_stations_*` on the CONUS API.
