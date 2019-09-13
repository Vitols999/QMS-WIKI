[Prev](DocControlMapDem) (Control maps and DEM files) | [Home](Home) | [Manual](DocMain) | [Index](AxAdvIndex) | (Working with Projects) [Next](DocWorkingWithProjects)
- - -
[TOC]
- - -

# Sources of QMapShack-compatible maps and elevation data

This page provides information about sources for

* maps in various formats (online, vector, raster) and
* elevation data (DEM data) in various formats (SRTM, online).

The information is ordered by regions and based on contributions of QMS users to this Wiki. Information for smaller regions is given only, if it is not yet available as part of a larger region. 

Please, feel free to add your favorite map and elevation data sources to this page.

## World

Maps listed in the following table cover the whole world.

| Title | Source | Type | Characteristics | More details |
|:-------------|:--------|:------|:---------|:--------------|
| Google map | file `Google.tms` in [package online.zip](http://www.mtb-touring.net/?ddownload=5012) | online, raster | 4 map layers can be selected: Google Hybrid, Google (street), Google Sat(ellite) Map, Google Terrain Map. |  |
| Bing map | file `Bing.tms` in [package online.zip](http://www.mtb-touring.net/?ddownload=5012) | online, satellite | worldwide satellite map |  |
| Lambertus map | [Free maps for Garmin brand GPS devices](http://garmin.openstreetmap.nl) | offline, vector | The server offers the possibility to select user-defined  regions of the world and download offline vector maps based on OpenStreetMap data in the Garmin container format. Follow the instructions on the given page. Several map types and TYP files can be selected, too. After being informed that the download is ready, download the file `osm_generic_gmapsupp.zip`, unpack it and rename file `gmapsupp.img` to `your_favorite_name_for the_region.img`. |  |
| Raumbezug map | [OpenStreetMap-Data for Garmin GPS devices](http://raumbezug.eu/osm-garmin_en.htm) | offline, vector | select continent, country, and use `gmapsupp.img` format |  |
| OpenStreetMap | [OSM Map On Garmin](https://wiki.openstreetmap.org/wiki/OSM_Map_On_Garmin/Download) | offline, vector | list with vast range of offline vector maps for different regions of the world and for different activities. If the map can be downloaded in the `gmapsupp.img` format (look for this term!), then the map can be used with QMS. | |
| BBBike download server | [bbbike.org (OSM, Garmin format)](https://download.bbbike.org/) | offline, vector | select your range, choose Garmin output | other output formats not supported in QMS!|
| OpenStreetMap | file `OpenStreetMap.tms` in [package online.zip](http://www.mtb-touring.net/?ddownload=5012) | online, raster created from vector data | worldwide street map labeled in local languages | |
| World satellite map | file `WorldSat.wmts` in [package online.zip](http://www.mtb-touring.net/?ddownload=5012) | online, raster created from vector data| worldwide satellite map | |
| World topo map | file `WorldTopo.wmts` in [package online.zip](http://www.mtb-touring.net/?ddownload=5012) | online, raster created from vector data| worldwide topo map |  |
| OpenStreetMap public transportation map| file `OSM OePNV.tms` in [package online.zip](http://www.mtb-touring.net/?ddownload=5012) | online, raster created from vector data | public transportation networks | |
| Railway overlay| file `OpenRailwayMap.tms` in [package online.zip](http://www.mtb-touring.net/?ddownload=5012) | online, raster created from vector data | railway networks overlay, 3 layers for infrastructure, max. speeds, and signaling |  |
| Outdoor tracks overlay| file `Waymarkedtrails.tms` in [package online.zip](http://www.mtb-touring.net/?ddownload=5012) | online, raster created from vector data | 6 layers with tracks for in-line skating, mountain biking, cycling, horse riding, hiking, and winter sports  | |
| OpenStreetMap public GPS traces| file `OSM_GPS-traces.tms` in [package online.zip](http://www.mtb-touring.net/?ddownload=5012) | online, raster created from vector data | They are just GPS-registered traces. They do not ensure that there is a trail, but sometimes they can reveal trails that have not yet been drawn on OSM maps. Overlay it on a basemap. |  |
|  Soviet and U.S. military maps | [http://loadmap.net](http://loadmap.net) | offline, raster | server for a wide variety of raster maps covering large parts of the world. Among them are various kinds of Russian army and topographic maps, but also maps of the U.S. army map service. Maps are useful for regions where other maps with more recent data are not available. The legend of Russian maps is Russian. | [Russian army maps](DocMapsTipsRasterDEM#markdown-header-russian-army-maps) |
| Hill-shading overlay | file `Hillshading.tms` in [package online.zip](http://www.mtb-touring.net/?ddownload=5012) | online, raster created from vector data| map overlay for hill-shading | |
| Strava heatmap | file `Strava.tms` in [package online.zip](http://www.mtb-touring.net/?ddownload=5012) | online, raster created from vector data| 2 overlay layers showing frequency of hiking and cycling track use |  |
| **Elevation (DEM) data** |
| ViewFinder | [ViewFinder](http://viewfinderpanoramas.org/dem3.html) | offline | select data precision and region | |
| SRTM | [SRTM](https://dds.cr.usgs.gov/srtm/version2_1/SRTM3/)  | offline | select data precision and region |  |
| Worldwide online DEM | [World-wide online DEM](Downloads/World_Online_SRTM900.wcs) | online | save the WCS file shown in the link and activate it. _Remark for Windows users:_ needs special supplementary [installation](DocMapsTipsRasterDEM#markdown-header-dem-data-from-wcs-web-coverage-service-servers). | |

Some more maps can be found in the [package online.zip](http://www.mtb-touring.net/?ddownload=5012) maintained by Emi (www.mtb-touring.net).

## Europe and European regions

| Country/Region | Source | Type | Characteristics | More details |
|:-------------|:--------|:------|:---------|:--------------|
| **Europe** | 
| Leisure map | [Leisure map](http://download.freizeitkarte-osm.de/garmin/latest) | offline, vector | select country or region and use `gmapsupp.img` format |  |
| OpenTopoMap contour line overlay | [European online DEM](Downloads/Europe_Online_DEM25.vrt) | online | save the VRT file shown in the link and activate it | [here](DocMapsTipsRasterDEM#markdown-header-european-dem-data) |
| European online DEM | [OpenTopoMap contour line overlay](http://garmin.opentopomap.org/#download) | offline, vector | select your region and download the file in the Garmin format. The downloaded file contains both a base map and a contour line overlay map in the `gmapsupp.img` format. |  |
| Alps| file `Alpenkarte.tms` in [package online.zip](http://www.mtb-touring.net/?ddownload=5012) | online, raster created from vector data | covers the whole Alps region, 2 layers for summer and winter |   |
| Austria | file `BasemapAT.wmts` in [package online.zip](http://www.mtb-touring.net/?ddownload=5012) | online, raster | 5 different layers including street map and orthofotos |  |
| Czech Republic | file `MTBMapCZ.tms` in [package online.zip](http://www.mtb-touring.net/?ddownload=5012) | online, raster | mountain bike and cycle tracks for Czech Republic and large parts of __Europe__. | If map doesn't load, try to replace server URL with __http://tile.mtbmap.cz:81/mtbmap_tiles/%1/%2/%3.png__ |
| France | [TMS file for France](Downloads/BRGM.tms) | online, raster | save the TMS file shown in the link and activate it. Street map from Bureau de Recherches Géologiques et Minières. Covers parts of neighboring countries. | [here](DocMapsTipsOnline#markdown-header-use-wms-server-as-tms-server)|
| **Germany** |
| TopPlus-Web-Open Germany | [TopPlus-Web-Open Germany](http://sgx.geodatenzentrum.de/wmts_topplus_web_open/1.0.0/WMTSCapabilities.xml) | online, raster | download the file in the link and change extension of downloaded file to `wmts`. Map of Germany, __includes worldwide overview map__ (available scales/details vary from region to region, house numbers for Germany)! | |
| TMS file for North Rhine-Westphalia | [TMS file for North Rhine-Westphalia](Downloads/NRW.tms) | online, raster | save the TMS file shown in the link and activate it. North Rhine-Westphalia street map. | [here](DocMapsTipsOnline#markdown-header-use-wms-server-as-tms-server) |
| eoportal Thuringia | [Geoportal Thuringia](http://www.geoportal-th.de/de-de/Downloadbereiche/Download-Offene-Geodaten-Th%C3%BCringen) | offline, raster | access to georeferenced topo maps and orthofotos | |
| Great Britain | [OS Opendata](http://www.the-thorns.org.uk/mapping/help/ukgarmin.html) | offline, vector| save the link, unzip it, rename and activate the gmapsupp.img. Detailed topo map.  | [here](http://www.the-thorns.org.uk/mapping/help/ukgarmin.html) |
| Italy | [TMS file for Italy](Downloads/ItalyGeoPortale.tms) | online, raster created from vector data| save the TMS file shown in the link and activate it. Italy topo map.  | [here](DocMapsTipsOnline#markdown-header-use-arcgis-server-as-tms-server) |
| Poland | [Hike routes](http://mapaszlakow.eu/Gdynia.html/wmts) | online, raster | download file in link and change extension of downloaded file to `wmts`. Hike routes in Poland | |
| Norway | file `Norway Topo 50.tms` in [package online.zip](http://www.mtb-touring.net/?ddownload=5012) | online, raster created from vector data| Norway topo map |   |
| **Spain** |
| . | file `ESP_ IGN_Topografico.tms` in [package ESP\_IGN\_QMS\_onlinemaps.zip](https://www.dropbox.com/s/sfzxdehmdqfs784/ESP_IGN_QMS_onlinemaps.zip?dl=0) | online, raster | Spain topo map | |
| . | file `ESP_IGN_Ortofoto.tms` in [package ESP\_IGN\_QMS\_onlinemaps.zip](https://www.dropbox.com/s/sfzxdehmdqfs784/ESP_IGN_QMS_onlinemaps.zip?dl=0) | online, raster | Spain orthofotos |  | 
| . | file `ESP\_IGN\_MDT25.wcs` in [package QMS\_onlineDEM\_WCS.zip](https://drive.google.com/open?id=1CLzw4SH62BtgLJ7ZeUgT9SFQh1lh3Dbn) | online DEM| place the `.wcs` file in your DEM path and activate it  | [here](DocMapsTipsRasterDEM#markdown-header-online-dem-data)  |

_Remarks:_

* The [webpage](http://www.geodatenzentrum.de/geodaten/gdz_rahmen.gdz_div?gdz_spr=deu&gdz_akt_zeile=5&gdz_anz_zeile=1&gdz_unt_zeile=0&gdz_user_id=0) of the German _Bundesamt für Kartographie und Geodäsie_ has links to various forms of online and offline maps for Germany. Equivalent institutions for German counties offer similar services.
* Some more maps and detailed DEMs for Spain can be found in the packages [ESP\_IGN\_QMS\_onlinemaps.zip](https://www.dropbox.com/s/sfzxdehmdqfs784/ESP_IGN_QMS_onlinemaps.zip?dl=0) and [QMS\_onlineDEM\_WCS.zip](https://drive.google.com/open?id=1CLzw4SH62BtgLJ7ZeUgT9SFQh1lh3Dbn)  provided by [Mitxel](https://sourceforge.net/p/qlandkartegt/mailman/message/35951444/). You can also have a look at the [list of maps and resources in Mendiak spanish forum.](https://www.mendiak.net/viewtopic.php?f=529&t=59020).


## Other regions

| Country/Region | Source | Type | Characteristics | More details |
|:-------------|:--------|:------|:---------|:--------------|
| New Zealand | [TMS file for New Zealand](Downloads/NZ.tms) | online, raster created from vector data| save the TMS file shown in the link and activate it. New Zealand topo map. | [here](DocMapsTipsOnline#markdown-header-tms-configuration-for-new-zealand-topo-maps) |
| New Zealand | [TMS file for New Zealand](Downloads/NewZealand_Orho_Topo50.tms) | online, raster| save the TMS file shown in the link and activate it. New Zealand orthographic and topographic map (2 layers). |  |

## Short summary of map and DEM use

A short introduction to the use of maps and DEM data in QMS is given in the QMS GUI at the first start of this software. More details can be found in the following sections of this Wiki:

* [Basic knowledge about maps and DEM files](DocBasicsMapDem)
* [Map and DEM setup](AdvSetup#markdown-header-map-and-dem-setup)
* [Tips & tricks for online maps](DocMapsTipsOnline)
* [Tips & tricks for raster maps, vector maps, and elevation data](DocMapsTipsRasterDEM)
* [Supported raster map formats](DocFaqMaps#markdown-header-which-raster-map-formats-are-supported)
* [Details of map use](AdvMapDetails)


To activate maps or elevation data proceed as follows (compare [Map and DEM setup](AdvSetup#markdown-header-map-and-dem-setup)):

* Put the map/elevation data file in a map/DEM path.
* Go to the docked Maps/DEM window.
* Setup the paths using the context menu of the docked window.
* Activate the map/DEM data using the context menu of the docked window.
* _Hint:_ Typically, maps are rendered only at a limited number of zoom levels. To see the rendered map, try to zoom in or out!

## Overview of supported map formats

### Offline maps

* __Vector maps__. Support of maps in the Garmin `gmapsupp.img` container format.
* __Raster maps__.
    * __VRT__. With the help of this wrapper format QMS supports all raster formats that can be handled by GDAL:
        
        * A non exhaustive list: __TIFF, MBTiles, MAP, GeoPDF, ECW\*,MrSID\*__...
        * Supported formats depends on your GDAL installation. For a complete list call `gdalinfo --formats`
        * Support for __ECW__ and __MrSID__ formats needs supplementary [installation](DocMapsTipsRasterDEM#markdown-header-ecw-mbtiles-and-mrsid-maps).
        
    * __RMAP__. CompeGPS Map Container. Just a very reduced feature set is supported.
    * __JNX__. Garmin Birds Eye maps.
    * __GEMF__. Map format mainly used with the mobile phone Osmdroid app.
    
### Online map services

* __TMS__. Tile service. Direct QMS support.
* __WMTS__. Tile service. Direct QMS support of limited number of format variants. Some WMTS services can be accessed via a [TMS service](DocMapsTipsOnline#markdown-header-use-wmts-server-as-tms-server). WMTS services mentioned on this page are supported by QMS.
* (__WMS__). When using this service map tiles have to be created, therefore it is slower than a tile service. WMS is broadly available. No direct QMS support. Some WMS services can be accessed via a [TMS service](DocMapsTipsOnline#markdown-header-use-wms-server-as-tms-server). WMS services mentioned on this page are supported by QMS.

- - -
[Prev](DocControlMapDem) (Control maps and DEM files) | [Home](Home) | [Manual](DocMain) | [Index](AxAdvIndex) | [Top](#) | (Working with Projects) [Next](DocWorkingWithProjects)
