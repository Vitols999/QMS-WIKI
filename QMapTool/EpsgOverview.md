[Prev](PaletteTool) (Color palette tool) | [Home](QMTHome) | [Manual](QMTDocMain) | [Index](QMTAxAdvIndex) | (Main menu overview) [Next](QMTAxMenuStructure)
- - -

# Properties of some commonly used coordinate systems

QMapTool (QMT) offers a list of predefined coordinate systems for referencing raster maps. This list is taken from the GDAL sources. Some commonly used coordinate systems
(especially some used in Germany) are not contained in this list. The purpose of this page is to provide basic information
about some of these coordinate systems. The Proj.4 settings can then be used directly in the QMT reference tool.

The information collected on this page is taken from the following sources:

* [epsg.io](https://epsg.io)
* [EPSG Geodetic Parameter Registry](http://www.epsg-registry.org)

and from files in the `nad` subdirectory of the [Proj.4](http://proj4.org/download.html#current-release) source distribution.

For a known EPSG code its features can be obtained by calling

    testepsg epsg:9999
    
where `testepsg.exe` is located in the `bin` subdirectory of the GDAL package or in the QMapTool/QMapShack installation path for Windows OS and where `9999` is
the EPSG code.

__Attention:__ This list shows some coordinate systems that use lat/lon coordinates (those using `+proj=longlat` and labeled _"Geographic"_, too). 
Although these coordinate systems are not supported
in the setup of maps in QMapShack they can be used within QMapTool.

__EPSG 4326: WGS84, geographic__

* __Unit:__ degree
* __Geodetic CRS:__ WGS 84
* __Datum:__ World Geodetic System 1984
* __Ellipsoid:__ WGS 84
* __Prime meridian:__ Greenwich 
* __Area of use:__ World
* __Alias names:__ 
* __Comments:__ 
* __Proj.4:__ `+proj=longlat +datum=WGS84 +no_defs`

__EPSG 4178: Pulkovo 42/83 (Krassowski), geographic__

* __Unit:__ degree
* __Geodetic CRS:__ Pulkovo 1942(83)
* __Datum:__ Pulkovo 1942(83)
* __Prime meridian:__ Greenwich
* __Ellipsoid:__ Krassowsky 1940
* __Area:__ Onshore Bulgaria, Czech Republic, Germany (former GDR), Hungary and Slovakia
* __Alias names:__ Pulkovo 1942(83)
* __Comments:__ In Brandenburg replaced by ETRS89. In Sachsen and Thuringen replaced by RD83 and PD83 which for practical purposes may be considered to be the same as DHDN. 
* __Proj.4:__ `+proj=longlat +ellps=krass +towgs84=26,-121,-78,0,0,0,0 +no_defs`

**EPSG 4258: ETRS 89 (GRS80), geographic**

* __Unit:__ degree
* __Geodetic CRS:__ ETRS89
* __Datum:__  European Terrestrial Reference System 1989
* __Prime meridian:__ Greenwich
* __Ellipsoid:__ GRS80
* __Area:__ Europe
* __Alias names:__ 
* __Comments:__  
* __Proj.4:__  `+proj=longlat +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +no_defs`

**EPSG 4314: DHDN**

* __Unit:__ degree
* __Geodetic CRS:__ DHDN
* __Datum:__ DHDN
* __Prime meridian:__ Greenwich
* __Ellipsoid:__ Bessel 1841
* __Area:__ Germany
* __Alias names:__ 
* __Comments:__  used by EPSG:5678 DHDN / 3-degree Gauss-Kruger zone 4 (E-N) (map) and similar systems
* __Proj.4:__ `+proj=longlat +datum=potsdam +no_defs`

    also:

              +proj=longlat +ellps=bessel +towgs84=598.1,73.7,418.2,0.202,0.045,-2.455,6.7 +no_defs 

**EPSG 4745: RD83**

* __Unit:__ degree
* __Geodetic CRS:__ 
* __Datum:__ Rauenberg 83
* __Prime meridian:__ Greenwich 
* __Ellipsoid:__ Bessel
* __Area:__ Sachsen
* __Alias names:__ 
* __Comments:__  same as DHDN
* __Proj.4:__  `+proj=longlat +ellps=bessel +no_defs`

**EPSG 4746: PD83**

* __Unit:__ degree
* __Geodetic CRS:__ 
* __Datum:__ Potsdam 83
* __Prime meridian:__ Greenwich
* __Ellipsoid:__ Bessel 1841
* __Area:__ Thüringen
* __Alias names:__ 
* __Comments:__  same as DHDN
* __Proj.4:__  `+proj=longlat +ellps=bessel +no_defs`
                                  
**EPSG 5678: DHDN / 3-degree Gauss-Kruger zone 4 (E-N)**

* __Unit:__ meter
* __Geodetic CRS:__ DHDN
* __Datum:__ DHDN
* __Prime meridian:__ Greenwich
* __Ellipsoid:__ Bessel 1841
* __Area:__ Germany
* __Alias names:__ DHDN / 3GK zone 4  
* __Comments:__  10° 30' - 13° 30', used in German Meßtischblatt, Einheitsblatt 1:100000, ...
* __Proj.4:__  `+proj=tmerc +lat_0=0 +lon_0=12 +k=1 +x_0=4500000 +y_0=0 +ellps=bessel +towgs84=598.1,73.7,418.2,0.202,0.045,-2.455,6.7 +units=m +no_defs`

**EPSG: 5679: DHDN / 3-degree Gauss-Kruger zone 5 (E-N)**

* __Unit:__ meter
* __Geodetic CRS:__ DHDN
* __Datum:__ DHDN
* __Prime meridian:__ Greenwich
* __Ellipsoid:__ Bessel 1841 (EPSG::7004)
* __Area:__ Germany
* __Alias names:__ DHDN / 3GK zone 5
* __Comments:__ 13° 30' - 16° 30'
* __Proj.4:__  `+proj=tmerc +lat_0=0 +lon_0=15 +k=1 +x_0=5500000 +y_0=0 +ellps=bessel +towgs84=598.1,73.7,418.2,0.202,0.045,-2.455,6.7 +units=m +no_defs`
                
**EPSG 32632: WGS 84 / UTM zone 32N**

* __Unit:__ meter
* __Geodetic CRS:__ WGS84
* __Datum:__ WGS84
* __Prime meridian:__ Greenwich
* __Ellipsoid:__ WGS84
* __Area:__ 6° - 12° E 
* __Alias names:__ 
* __Comments:__ 6° strips. Zone counting starts at 177° W
* __Prj.4:__  `+proj=utm +zone=32 +datum=WGS84 +units=m +no_defs`

**EPSG 2398: Pulkovo 1942(83) / 3-degree Gauss-Kruger zone 4**

* __Unit:__ meter
* __Geodetic CRS:__ 
* __Datum:__ Pulkovo 1942/83
* __Prime meridian:__ 
* __Ellipsoid:__ Krassowski 1940
* __Area:__ Czech Republic - west of 13°30'E. Germany - states of former East Germany onshore - between 10°30'E and 13°30'E - Brandenburg; 
  Mecklenburg-Vorpommern; Sachsen; Sachsen-Anhalt; Thuringen.
* __Alias names:__ 
* __Comments:__  
* __Proj.4:__  `+proj=tmerc +lat_0=0 +lon_0=12 +k=1 +x_0=4500000 +y_0=0 +ellps=krass +towgs84=26,-121,-78,0,0,0,0 +units=m +no_defs`
         
**EPSG 3857: WGS 84 / Pseudo-Mercator**

* __Unit:__ meter
* __Geodetic CRS:__ WGS84
* __Datum:__ WGS84
* __Prime meridian:__ Greenwich
* __Ellipsoid:__ WGS84
* __Area:__ World
* __Alias names:__ 
* __Comments:__  Web Mercator, Google Web Mercator, Spherical Mercator, WGS 84 Web Mercator or WGS 84/Pseudo-Mercator is 
  the de facto standard for Web mapping applications. It is used by virtually all major 
  online map providers, including Google Maps, Bing Maps, OpenStreetMap, Mapquest, Esri, Mapbox, and many others. 
  Similar: EPSG 3785. 
  
    Choose World Mercator (OSM) projection and WGS84 datum in QMS/QMT to get this coordinate system.
    
* __Proj.4:__  `+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m +nadgrids=@null +wktext  +no_defs`

**EPSG 3395: WGS 84 / World Mercator**

* __Unit:__ meter
* __Geodetic CRS:__ WGS84
* __Datum:__ WGS84
* __Prime meridian:__ Greenwich
* __Ellipsoid:__ WGS84
* __Area:__ World
* __Alias names:__ 
* __Comments:__ Euro-centric view of world excluding polar areas. Choose Mercator projection and WGS84 datum in QMS/QMT to get this coordinate system.
    
* __Proj.4:__  `+proj=merc +a=6378137.0000 +b=6356752.3142 +towgs84=0,0,0,0,0,0,0,0 +units=m  +no_defs`

    or also:
    
    `+proj=merc +lon_0=0 +k=1 +x_0=0 +y_0=0 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs` 
    
    `+proj=merc +lon_0=0 +k=1 +x_0=0 +y_0=0 +datum=WGS84 +units=m +no_defs`

    (for explicit ellipsoid description see [here.](https://en.wikipedia.org/wiki/GRS_80))

                
- - -
[Prev](PaletteTool) (Color palette tool) | [Home](QMTHome) | [Manual](QMTDocMain) | [Index](QMTAxAdvIndex) | [Top](#) | (Main menu overview) [Next](QMTAxMenuStructure)
