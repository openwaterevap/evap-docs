# Info Endpoints

The Info/Help endpoints provide information about the available data in the API, including datasets, variables, reservoirs, stations, and date ranges. These endpoints are useful for discovering what data is available and how to access it.

## List Date Range

Lists the minimum and maximum dates available for a dataset and variable.

=== "Python"

    ```python
    import requests

    url = "https://twdb.dri.edu/info/list_dates"
    headers = {
        "api-key": "YOUR_API_KEY"
    }
    params = {
        "output_format": "json",  # or "csv"
        "dataset": "nete-volume-calcs",
        "variable": "NetE"
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    print(data)
    ```

=== "cURL"

    ```sh
    # Set your API key
    API_KEY="YOUR_API_KEY"

    # Get date range for a dataset and variable
    curl -X GET "https://twdb.dri.edu/info/list_dates?output_format=json&dataset=nete-volume-calcs&variable=NetE" \
         -H "api-key: ${API_KEY}"
    ```

### Parameters

| Parameter     | Type   | Description                                      | Default           |
| ------------- | ------ | ------------------------------------------------ | ----------------- |
| output_format | string | Response format (json or csv)                    | json              |
| dataset       | string | Dataset name (rtma, res, lem, nete-volume-calcs) | nete-volume-calcs |
| variable      | string | Variable name (see list_variables endpoint)      | NetE              |

### Response

Returns a list containing the start date and end date for the specified dataset and variable.


## List Forecast Date Range

Lists the minimum and maximum dates available for a dataset and variable.

=== "Python"

    ```python
    import requests

    url = "https://twdb.dri.edu/info/list_forecast_dates"
    headers = {
        "api-key": "YOUR_API_KEY"
    }
    params = {
        "output_format": "json",  # or "csv"
        "dataset": "nete-volume-calcs",
        "variable": "NetE"
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    print(data)
    ```

=== "cURL"

    ```sh
    # Set your API key
    API_KEY="YOUR_API_KEY"

    # Get date range for a dataset and variable
    curl -X GET "https://twdb.dri.edu/info/list_forecast_dates?output_format=json&dataset=nete-volume-calcs&variable=NetE" \
         -H "api-key: ${API_KEY}"
    ```

### Parameters

| Parameter     | Type   | Description                                      | Default           |
| ------------- | ------ | ------------------------------------------------ | ----------------- |
| output_format | string | Response format (json or csv)                    | json              |
| dataset       | string | Dataset name (rtma, res, lem, nete-volume-calcs) | nete-volume-calcs |
| variable      | string | Variable name (see list_variables endpoint)      | NetE              |

### Response

Returns a list containing the start date and end date for the specified dataset and variable.


## List Reservoir Names

Lists available reservoir IDs (RES_NAME) that can be used in other API requests.

=== "Python"

    ```python
    import requests

    url = "https://twdb.dri.edu/info/list_RES_NAMES"
    headers = {
        "api-key": "YOUR_API_KEY"
    }
    params = {
        "output_format": "json"  # or "csv"
    }

    # Without shapefile
    response = requests.post(url, headers=headers, params=params)
    data = response.json()
    print(data)

    # With shapefile (if needed)
    files = {
        'shapefile_shp': open('your_shapefile.shp', 'rb'),
        'shapefile_dbf': open('your_shapefile.dbf', 'rb'),
        'shapefile_prj': open('your_shapefile.prj', 'rb'),
        'shapefile_shx': open('your_shapefile.shx', 'rb')
    }

    response = requests.post(url, headers=headers, params=params, files=files)
    data = response.json()
    print(data)
    ```

=== "cURL"

    ```sh
    # Set your API key
    API_KEY="YOUR_API_KEY"

    # Get reservoir names without shapefile
    curl -X POST "https://twdb.dri.edu/info/list_RES_NAMES?output_format=json" \
         -H "api-key: ${API_KEY}"

    # Get reservoir names with shapefile (if needed)
    curl -X POST "https://twdb.dri.edu/info/list_RES_NAMES?output_format=json" \
         -H "api-key: ${API_KEY}" \
         -F "shapefile_shp=@your_shapefile.shp" \
         -F "shapefile_dbf=@your_shapefile.dbf" \
         -F "shapefile_prj=@your_shapefile.prj" \
         -F "shapefile_shx=@your_shapefile.shx"
    ```

### Parameters

| Parameter     | Type   | Description                                         | Default |
| ------------- | ------ | --------------------------------------------------- | ------- |
| output_format | string | Response format (json or csv)                       | json    |
| shapefile_shp | file   | Optional .shp file to filter reservoirs by location |         |
| shapefile_dbf | file   | Optional .dbf file to filter reservoirs by location |         |
| shapefile_prj | file   | Optional .prj file to filter reservoirs by location |         |
| shapefile_shx | file   | Optional .shx file to filter reservoirs by location |         |

### Response

Returns a list of reservoir names that can be used as the `RES_NAMES` parameter in metadata and timeseries API requests.

### Notes

If shapefiles are uploaded, only reservoirs within the shapefile bounds will be returned.


## Convert NWSLI IDs

Converts NWSLI_IDs to RES_NAMES, for use as RES_NAMES parameter in API requests.

=== "Python"

    ```python
    import requests

    url = "https://twdb.dri.edu/info/convert_NWSLI_IDs"
    headers = {
        "api-key": "YOUR_API_KEY"
    }
    params = {
        "output_format": "json"  # or "csv",
        "NWSLI_IDs": "PLCT2, DDET2"  # One or more reservoir names (comma-separated)
    }

    response = requests.post(url, headers=headers, params=params)
    data = response.json()
    print(data)
    ```

=== "cURL"

    ```sh
    # Set your API key
    API_KEY="YOUR_API_KEY"

    # Get reservoir names without shapefile
    curl -X POST "https://twdb.dri.edu/info/convert_NWSLI_IDsS?output_format=json&NWSLI_IDs=PLCT2,DDET2" \
         -H "api-key: ${API_KEY}"
    ```

### Parameters

| Parameter     | Type   | Description                                         | Default |
| ------------- | ------ | --------------------------------------------------- | ------- |
| output_format | string | Response format (json or csv)                       | json    |
| NWSLI_IDs     | string | One or more reservoir names (comma-separated)       |         |


### Response

Returns a list of reservoir names that can be used as the `RES_NAMES` parameter in metadata and timeseries API requests.


## List Available Datasets

Lists all available non-forecast datasets in the API.

=== "Python"

    ```python
    import requests

    url = "https://twdb.dri.edu/info/list_datasets"
    headers = {
        "api-key": "YOUR_API_KEY"
    }
    params = {
        "output_format": "json"  # or "csv"
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    print(data)
    ```

=== "cURL"

    ```sh
    # Set your API key
    API_KEY="YOUR_API_KEY"

    # Get available datasets
    curl -X GET "https://twdb.dri.edu/info/list_datasets?output_format=json" \
         -H "api-key: ${API_KEY}"
    ```

### Parameters

| Parameter     | Type   | Description                   | Default |
| ------------- | ------ | ----------------------------- | ------- |
| output_format | string | Response format (json or csv) | json    |

### Response

Returns a list of dataset names that can be used as the `dataset` parameter in other API requests.

## List Available Forecast Datasets

Lists all available forecast datasets in the API.

=== "Python"

    ```python
    import requests

    url = "https://twdb.dri.edu/info/list_forecast_datasets"
    headers = {
        "api-key": "YOUR_API_KEY"
    }
    params = {
        "output_format": "json"  # or "csv"
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    print(data)
    ```

=== "cURL"

    ```sh
    # Set your API key
    API_KEY="YOUR_API_KEY"

    # Get available datasets
    curl -X GET "https://twdb.dri.edu/info/list_forecast_datasets?output_format=json" \
         -H "api-key: ${API_KEY}"
    ```

### Parameters

| Parameter     | Type   | Description                   | Default |
| ------------- | ------ | ----------------------------- | ------- |
| output_format | string | Response format (json or csv) | json    |

### Response

Returns a list of dataset names that can be used as the `dataset` parameter in other API requests.

## List Available Variables

Lists available variables for a specified dataset.

=== "Python"

    ```python
    import requests

    url = "https://twdb.dri.edu/info/list_variables"
    headers = {
        "api-key": "YOUR_API_KEY"
    }
    params = {
        "output_format": "json",  # or "csv"
        "dataset": "nete-volume-calcs"  # Dataset name
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    print(data)
    ```

=== "cURL"

    ```sh
    # Set your API key
    API_KEY="YOUR_API_KEY"

    # Get available variables for a dataset
    curl -X GET "https://twdb.dri.edu/info/list_variables?output_format=json&dataset=nete-volume-calcs" \
         -H "api-key: ${API_KEY}"
    ```

### Parameters

| Parameter     | Type   | Description                                      | Default           |
| ------------- | ------ | ------------------------------------------------ | ----------------- |
| output_format | string | Response format (json or csv)                    | json              |
| dataset       | string | Dataset name (rtma, res, lem, nete-volume-calcs) | nete-volume-calcs |

### Response

Returns a list of dictionaries containing variable information. The `api_name` field in each dictionary can be used as the `variable` parameter in other API requests.


## List Available Forecast Variables

Lists available variables for a specified forecast dataset.

=== "Python"

    ```python
    import requests

    url = "https://twdb.dri.edu/info/list_forecast_variables"
    headers = {
        "api-key": "YOUR_API_KEY"
    }
    params = {
        "output_format": "json",  # or "csv"
        "dataset": "nete-volume-calcs"  # Dataset name
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    print(data)
    ```

=== "cURL"

    ```sh
    # Set your API key
    API_KEY="YOUR_API_KEY"

    # Get available variables for a dataset
    curl -X GET "https://twdb.dri.edu/info/list_forecast_variables?output_format=json&dataset=nete-volume-calcs" \
         -H "api-key: ${API_KEY}"
    ```

### Parameters

| Parameter     | Type   | Description                                      | Default           |
| ------------- | ------ | ------------------------------------------------ | ----------------- |
| output_format | string | Response format (json or csv)                    | json              |
| dataset       | string | Dataset name (rtma, res, lem, nete-volume-calcs) | nete-volume-calcs |

### Response

Returns a list of dictionaries containing variable information. 
The `api_name` field in each dictionary can be used as the `variable` parameter in other API requests.

