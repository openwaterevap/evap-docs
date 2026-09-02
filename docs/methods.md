# Methods

The OWEN modelling workflow integrates daily gridded weather and reservoir property data into the Penman-based Daily Lake Evaporation Model (DLEM),
enabling the simulation of daily evaporation rates at each relevant reservoir.
These rates are then combined with surface area estimates and precipitation data to produce net evaporation rates, volumes, and associated outputs.
The integrated data is stored in a geodatabase for secure storage and easy access via a web interface and API.

<center>

<img src="https://picsur.spatialbytes.work/i/b77c0887-802d-4a3f-bda5-a5ed7d0b204c.jpg" alt="OperEvap Methods" width="600">

</center>


Figure: Conceptual diagram of reservoir evaporation processing pipeline and geodatabase storage and access end points.

## Daily Lake Evaporation Model

Reservoir evaporation estimates produced by this project are based on a daily version of Texas A&M Lake Evaporation Model (DLEM) developed by Zhao and Gao (2019) and Zhao et al. (2024).
DLEM uses a Penman combination equation along with reservoir fetch and heat storage effects represented. DLEM requires input solar radiation, wind speed and direction, air temperature,
vapor pressure deficit, and reservoir area and depth data. Meteorological forcing data is adjusted to over water conditions using wind functions developed by McJannet (2012).

Reservoir heat storage within DLEM is simulated using an equilibrium temperature approach where water column temperature at the current timestep is calculated from water
temperature at the current timestep, equilibrium temperature, and a lag time. The equilibrium temperature is defined as the water temperature at which there is no heat exchange
between air and water. The lag time is a function of reservoir depth. Inclusion of heat storage adjustments improves evaporation estimates in large, deep-water bodies where a
significant amount of radiative energy in the spring goes towards warming the water body rather than fueling evaporation. Conversely, in the fall when the water body is warm and
air temperatures are cool, heat storage can increase evaporation rates. Daily evaporation rate estimates are combined with reservoir surface area information to estimate volumetric losses.

## Weather Forcing Data for DLEM

Weather data used to force DLEM are derived primarily from the [gridMET](https://www.climatologylab.org/gridmet.html) and
[Real-Time Mesoscale Analysis (RTMA)](https://www.nco.ncep.noaa.gov/pmb/products/rtma/) datasets. The specific dataset, configuration,
and temporal coverage of forcing data may vary by project. Consult the relevant database documentation for project-specific details.

The forcing variables include:

- Wind speed and direction
- Air temperature
- Specific humidity
- Atmospheric pressure

## Reservoir Depth, Area, and Volumes

DLEM uses reservoir-depth information to quantify heat storage. Depth data are compiled from various online repositories; when no
site-specific information is available, statistical values are used. Gap-filling routines are applied to address missing data periods.

OWEN combines reservoir surface area with modeled DLEM evaporation rates to estimate volumetric evaporation losses. Net evaporation
is calculated as total evaporation minus precipitation falling on the reservoir surface. 
Details on reservoir depth and surface-area data sources, including gap-filling methods, are available in the database documentation.

## References

```
Abatzoglou, John T. "Development of gridded surface meteorological data for ecological applications and modelling." International Journal of Climatology 33.1 (2013): 121-131.

De Pondeca, Manuel SFV, et al. "The real-time mesoscale analysis at NOAA’s National Centers for Environmental Prediction: current status and development." Weather and Forecasting 26.5 (2011): 593-612.

McJannet, David L., Ian T. Webster, and Freeman J. Cook. "An area-dependent wind function for estimating open water evaporation using land-based meteorological data." Environmental modelling & software 31 (2012): 76-83.

Zhao, Gang, and Huilin Gao. "Estimating reservoir evaporation losses for the United States: Fusing remote sensing and modeling approaches." Remote Sensing of Environment 226 (2019): 109-124.

Zhao, Bingjie, et al. "Developing a general Daily Lake Evaporation Model and demonstrating its application in the state of Texas." Water Resources Research 60.3 (2024): e2023WR036181.
```

