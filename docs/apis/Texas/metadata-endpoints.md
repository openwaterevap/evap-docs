# Metadata Endpoints

The metadata endpoints provide information about the reservoirs and stations available in the API. This metadata includes details such as location, physical characteristics, and other attributes.

## Reservoir Metadata

Retrieves metadata for one or more reservoirs.

=== "Python"

    ```python
    import requests

    url = "https://twdb.dri.edu/metadata/reservoirs"
    headers = {
        "api-key": "YOUR_API_KEY"
    }
    params = {
        "RES_NAMES": "CANYON LAKE, CADDO LAKE",
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

    # Get reservoir metadata
    curl -X GET "https://twdb.dri.edu/metadata/reservoirs?RES_NAMES=CANYON%20LAKE,CADDO%20LAKE&output_format=json" \
         -H "api-key: ${API_KEY}"
    ```

### Parameters

| Parameter     | Type   | Description                                   | Default                 |
| ------------- | ------ | --------------------------------------------- |-------------------------|
| output_format | string | Response format (json or csv)                 | json                    |
| RES_NAMES     | string | One or more reservoir names (comma-separated) | CANYON LAKE, CADDO LAKE |

### Response

Returns a list of dictionaries containing metadata information for the specified reservoirs. 
The metadata includes attributes such as:

- Geographic coordinates (latitude, longitude)
- Physical characteristics (area, depth, etc.)
- Administrative information
- Quality flags (qflag)
- And other attributes

### Notes

Use the `/info/list_RES_NAMES` endpoint to discover available reservoir names.


## Using Metadata in Other Requests

The metadata attributes can be included in timeseries responses by using the `also_return` parameter in timeseries requests. 
For example:

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
        "also_return": "qflag",
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

    # Get timeseries data with metadata attributes
    curl -X GET "https://twdb.dri.edu/timeseries/daily/reservoirs/daterange?RES_NAMES=CANYON%20LAKE&datasets=nete-volume-calcs&variables=NetE,E_volume&start_date=2020-01-01&end_date=2020-01-31&units=metric&also_return=qflag&output_format=json" \
         -H "api-key: ${API_KEY}"
    ```

This is useful for understanding the quality or context of the data returned in timeseries responses.
