# Timeseries Endpoints

The timeseries endpoints provide access to time-based data for reservoirs. 
These endpoints are divided into two categories:

1. Timeseries data
2. Forecast timeseries data

Each category has endpoints for retrieving data over a date range or for a single date.

## Reservoir Timeseries Data (Date Range)

Retrieves timeseries data for one or more reservoirs over a specified date range.

=== "Python"

    ```python
    import requests

    url = "https://twdb.dri.edu/timeseries/daily/reservoirs/daterange"
    headers = {
        "api-key": "YOUR_API_KEY"
    }
    params = {
        "RES_NAMES": "CANYON LAKE",
        "datasets": "nete-volume-calcs",
        "variables": "NetE,E_volume",
        "start_date": "2020-01-01",
        "end_date": "2020-01-31",
        "units": "metric",
        "output_format": "json"
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    print(data)
    ```

=== "cURL"

    ```sh
    # Set your API key
    API_KEY="YOUR_API_KEY"

    # Get reservoir timeseries data
    curl -X GET "https://twdb.dri.edu/timeseries/daily/reservoirs/daterange?RES_NAMES=CANYON%20LAKE&datasets=nete-volume-calcs&variables=NetE,E_volume&start_date=2020-01-01&end_date=2020-01-31&units=metric&output_format=json" \
         -H "api-key: ${API_KEY}"
    ```

### Parameters

| Parameter     | Type   | Description                                           | Default                                                                                                                                                                 |
| ------------- | ------ | ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| RES_NAMES     | string | One or more reservoir names (comma-separated)         |                                                                                                                                                  |
| datasets      | string | One or more datasets (comma-separated)                | rtma, res, lem, nete-volume-calcs                                                                                                                                       |
| variables     | string | One or more variables (comma-separated)               | pr, tmmx_c, tmmn_c, vpd_kpa, vs2m, srad, etr, eto, th, sph_kgkg, pres_pa, stage_m, area_m2, depth_m, E_hs, E_nhs, Rn, Tw, Tw0, Fetch, Lerr, NetE, E_volume, NetE_volume |
| units         | string | Units for returned data (english or metric)           | metric                                                                                                                                                                  |
| start_date    | string | Start date (yyyy-mm-dd)                               | 2020-01-01                                                                                                                                                              |
| end_date      | string | End date (yyyy-mm-dd)                                 | 2020-01-31                                                                                                                                                              |
| also_return   | string | Additional metadata attributes to include in response |                                                                                                                                                                         |
| output_format | string | Response format (json or csv)                         | json                                                                                                                                                                    |

### Response

Returns a list of dictionaries containing timeseries data for the specified reservoirs, datasets, variables, and date range.

### Notes

- Use the `/info/list_RES_NAMES` endpoint to discover available reservoir names.
- Use the `/info/list_variables` endpoint to discover available variables for each dataset.
- Use the `/info/list_dates` endpoint to discover the valid date range for each dataset and variable.


## Reservoir Forecast Timeseries Data (Date Range)

Retrieves forecast timeseries data for one or more reservoirs over a specified date range.

=== "Python"

    ```python
    import requests

    url = "https://twdb.dri.edu/timeseries/forecast/daily/reservoirs/daterange"
    headers = {
        "api-key": "YOUR_API_KEY"
    }
    params = {
        "RES_NAMES": "CANYON LAKE",
        "datasets": "nete-volume-calcs",
        "variables": "NetE,E_volume",
        "start_date": "2026-10-01",
        "end_date": "2026-10-10",
        "units": "metric",
        "output_format": "json"
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    print(data)
    ```

=== "cURL"

    ```sh
    # Set your API key
    API_KEY="YOUR_API_KEY"

    # Get reservoir timeseries data
    curl -X GET "https://twdb.dri.edu/timeseries/forecast/daily/reservoirs/daterange?RES_NAMES=CANYON%20LAKE&datasets=nete-volume-calcs&variables=NetE,E_volume&start_date=2020-01-01&end_date=2020-01-31&units=metric&output_format=json" \
         -H "api-key: ${API_KEY}"
    ```

### Parameters

| Parameter     | Type   | Description                                           | Default                                                                                                                                                                |
| ------------- | ------ | ----------------------------------------------------- |------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RES_NAMES     | string | One or more reservoir names (comma-separated)         |                                                                                                                                                                        |
| datasets      | string | One or more datasets (comma-separated)                | cfs_gridmet, res, lem, nete-volume-calcs                                                                                                                               |
| variables     | string | One or more variables (comma-separated)               | pr, tmmx_c, tmmn_c, vpd_kpa, vs2m, srad, etr, eto, th, sph_kgkg, pres_pa, stage_m, area_m2, depth_m, E_hs, E_nhs, Rn, Tw, Tw0, Fetch, Lerr, NetE, E_volume, NetE_volume |
| units         | string | Units for returned data (english or metric)           | metric                                                                                                                                                                 |
| start_date    | string | Start date (yyyy-mm-dd)                               | 2020-01-01                                                                                                                                                             |
| end_date      | string | End date (yyyy-mm-dd)                                 | 2020-01-31                                                                                                                                                             |
| also_return   | string | Additional metadata attributes to include in response |                                                                                                                                                                        |
| output_format | string | Response format (json or csv)                         | json                                                                                                                                                                   |

### Response

Returns a list of dictionaries containing timeseries data for the specified reservoirs, datasets, variables, and date range.

### Notes

- Use the `/info/list_RES_NAMES` endpoint to discover available reservoir names.
- Use the `/info/list_variables` endpoint to discover available variables for each dataset.
- Use the `/info/list_dates` endpoint to discover the valid date range for each dataset and variable.

## Reservoir Timeseries Data (Single Date)

Retrieves timeseries data for all reservoirs on a single date.

=== "Python"

    ```python
    import requests

    url = "https://twdb.dri.edu/timeseries/daily/reservoirs/date"
    headers = {
        "api-key": "YOUR_API_KEY"
    }
    params = {
        "datasets": "nete-volume-calcs",
        "variables": "NetE,E_volume",
        "date": "2020-01-01",
        "units": "metric",
        "output_format": "json"
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    print(data)
    ```

=== "cURL"

    ```sh
    # Set your API key
    API_KEY="YOUR_API_KEY"

    # Get reservoir data for a single date
    curl -X GET "https://twdb.dri.edu/timeseries/daily/reservoirs/date?datasets=nete-volume-calcs&variables=NetE,E_volume&date=2020-01-01&units=metric&output_format=json" \
         -H "api-key: ${API_KEY}"
    ```

### Parameters

| Parameter     | Type   | Description                                           | Default                                                                                                                                                                 |
| ------------- | ------ | ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| datasets      | string | One or more datasets (comma-separated)                | rtma, res, lem, nete-volume-calcs                                                                                                                                       |
| variables     | string | One or more variables (comma-separated)               | pr, tmmx_c, tmmn_c, vpd_kpa, vs2m, srad, etr, eto, th, sph_kgkg, pres_pa, stage_m, area_m2, depth_m, E_hs, E_nhs, Rn, Tw, Tw0, Fetch, Lerr, NetE, E_volume, NetE_volume |
| units         | string | Units for returned data (english or metric)           | metric                                                                                                                                                                  |
| date          | string | Date (yyyy-mm-dd)                                     | 2020-01-01                                                                                                                                                              |
| also_return   | string | Additional metadata attributes to include in response |                                                                                                                                                                         |
| output_format | string | Response format (json or csv)                         | json                                                                                                                                                                    |

### Response

Returns a list of dictionaries containing timeseries data for all reservoirs for the specified datasets, variables, and date.

## Reservoir Forecast Timeseries Data (Single Date)

Retrieves forecast timeseries data for all reservoirs on a single date.

=== "Python"

    ```python
    import requests

    url = "https://twdb.dri.edu/timeseries/forecast/daily/reservoirs/date"
    headers = {
        "api-key": "YOUR_API_KEY"
    }
    params = {
        "datasets": "nete-volume-calcs",
        "variables": "NetE,E_volume",
        "date": "2026-10-15",
        "units": "metric",
        "output_format": "json"
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    print(data)
    ```

=== "cURL"

    ```sh
    # Set your API key
    API_KEY="YOUR_API_KEY"

    # Get reservoir data for a single date
    curl -X GET "https://twdb.dri.edu/timeseries/forecast/daily/reservoirs/date?datasets=nete-volume-calcs&variables=NetE,E_volume&date=2020-01-01&units=metric&output_format=json" \
         -H "api-key: ${API_KEY}"
    ```

### Parameters

| Parameter     | Type   | Description                                           | Default                                                                                                                                                                 |
| ------------- | ------ | ----------------------------------------------------- |-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| datasets      | string | One or more datasets (comma-separated)                | cfs_gridmet, res, lem, nete-volume-calcs                                                                                                                                |
| variables     | string | One or more variables (comma-separated)               | pr, tmmx_c, tmmn_c, vpd_kpa, vs2m, srad, etr, eto, th, sph_kgkg, pres_pa, stage_m, area_m2, depth_m, E_hs, E_nhs, Rn, Tw, Tw0, Fetch, Lerr, NetE, E_volume, NetE_volume |
| units         | string | Units for returned data (english or metric)           | metric                                                                                                                                                                  |
| date          | string | Date (yyyy-mm-dd)                                     | 2020-01-01                                                                                                                                                              |
| also_return   | string | Additional metadata attributes to include in response |                                                                                                                                                                         |
| output_format | string | Response format (json or csv)                         | json                                                                                                                                                                    |

### Response

Returns a list of dictionaries containing timeseries data for all reservoirs for the specified datasets, variables, and date.

## Pond Evaporation Point Timeseries Data (Date Range)

Retrieves timeseries data for one point over a specified date range.

=== "Python"

    ```python
    import requests

    url = "https://twdb.dri.edu/timeseries/daily/point/pond_devaporation/daterange"
    headers = {
        "api-key": "YOUR_API_KEY"
    }
    params = {
        "latitude": "30.325",
        "longitude": "-95.325",
        "units": "metric",
        "start_date": "2020-01-01",
        "end_date": "2020-01-31",
        "output_format": "json"
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    print(data)
    ```

=== "cURL"

    ```sh
    # Set your API key
    API_KEY="YOUR_API_KEY"

    # Get reservoir timeseries data
    curl -X GET "https://twdb.dri.edu/timeseries/daily/point/pond_devaporation/daterange?latitude=30.325&longitude=-95.325&units=metric&start_date=2020-01-01&end_date=2020-01-31&output_format=json" \
         -H "api-key: ${API_KEY}"
    ```

### Parameters

| Parameter     | Type   | Description                                           | Default                                                                                                                                                                 |
|---------------| ------ |-------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| latitude      | string | latitude                                              | 30.325                                                                                                                                                                  |
| longitude     | string | longitude                                             | -95.325                                                                                                                                       |
| units         | string | Units for returned data (english or metric)           | metric                                                                                                                                                                  |
| start_date    | string | Start date (yyyy-mm-dd)                               | 2020-01-01                                                                                                                                                              |
| end_date      | string | End date (yyyy-mm-dd)                                 | 2020-01-31                                                                                                                                                              |
| output_format | string | Response format (json or csv)                         | json                                                                                                                                                                    |

### Response

Returns a list of dictionaries containing timeseries data for the specified location, and date range.

## Pond Evaporation Polygon Timeseries Data (Date Range)

Retrieves timeseries data for one Polygon over a specified date range.

=== "Python"

    ```python
    import requests

    url = "https://twdb.dri.edu/timeseries/daily/polygon/pond_devaporation/daterange"
    headers = {
        "api-key": "YOUR_API_KEY"
    }
    params = {
        "polygon_coordinates": "[[-102.0, 30.0], [-102.0, 30.2], [-101.9, 30.0], [-101.9, 30.2], [-102.0, 30.00]]",
        "units": "metric",
        "start_date": "2020-01-01",
        "end_date": "2020-01-31",
        "output_format": "json"
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    print(data)
    ```

=== "cURL"

    ```sh
    # Set your API key
    API_KEY="YOUR_API_KEY"

    # Get reservoir timeseries data
    curl -X GET "https://twdb.dri.edu/timeseries/daily/polygon/pond_devaporation/daterange?%5B%5B-102.0%2C%2030.0%5D%2C%20%5B-102.0%2C%2030.2%5D%2C%20%5B-101.9%2C%2030.0%5D%2C%20%5B-101.9%2C%2030.2%5D%2C%20%5B-102.0%2C%2030.00%5D%5D&units=metric&start_date=2020-01-01&end_date=2020-01-31&output_format=json" \
         -H "api-key: ${API_KEY}"
    ```

### Parameters

| Parameter           | Type   | Description                                 | Default                                                                                                                                                           |
|---------------------| ------ |---------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| polygon_coordinates | string | list of lat, lon coordinates                | [[-102.0, 30.0], [-102.0, 30.2], [-101.9, 30.0], [-101.9, 30.2], [-102.0, 30.00]]                                                                                                                                                                  |
| units               | string | Units for returned data (english or metric) | metric                                                                                                                                                            |
| start_date          | string | Start date (yyyy-mm-dd)                     | 2020-01-01                                                                                                                                                        |
| end_date            | string | End date (yyyy-mm-dd)                       | 2020-01-31                                                                                                                                                        |
| output_format       | string | Response format (json or csv)               | json                                                                                                                                                              |

### Response

Returns a list of dictionaries containing timeseries data for the specified polygon, and date range.
