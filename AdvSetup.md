[Prev](AdvRealtime) (Realtime data) | [Home](Home) | [Manual](DocMain) | [Index](AxAdvIndex) | (Overview of toolbar actions) [Next](AdvToolbarAct)
- - -
 
***Table of contents***

* [Overview of setup and configuration options](#overview-of-setup-and-configuration-options)
    * [General options](#general-options)
        * [Workspace setup](#workspace-setup)
        * [Waypoint icons setup](#waypoint-icons-setup)
        * [Toolbar setup](#toolbar-setup)
    * [Map and DEM setup](#map-and-dem-setup)
        * [Download and install ](#download-and-install)
        * [Map paths](#map-paths)
        * [Map cache path for online maps](#map-cache-path-for-online-maps)
        * [DEM file paths](#dem-file-paths)
        * [Map window display switches (toggles)](#map-window-display-switches-toggles)
        * [Map window display setup](#map-window-display-setup)
        * [Single map display options](#single-map-display-options)
    * [Routing setup](#routing-setup)
        * [Routino database paths](#routino-database-paths)
        * [Routino setup](#routino-setup)
        * [BRouter setup](#brouter-setup)
        * [MapQuest setup](#mapquest-setup)
    * [Further setup and configuration options](#further-setup-and-configuration-options)

* * * * * * * * * *
 
# Overview of setup and configuration options

_Valid from patch version 55d8aa7 (18.11.2017)._

This page gives an overview over the available QMS GUI setup and configuration options. This includes in some cases QMS installation topics, too.

More details of the topics mentioned on this page can be found elsewhere in this [Wiki](DocMain).

## General options

### Workspace setup

* Goto menu  `Workspace - Setup workspace` (__Remark:__ changes made to these options need QMS restart!)

    In the pop-up windows define
  
    * a time interval for automatic project data backup,
    * a listening port for a QMS multi-user environment,
    * how GPS devices should be handled by QMS. If this option is not checked, then GPS devices can't be seen in QMS. Otherwise GPS devices plugged in to the PC can be seen in QMS. For details compare section ["Working with GPS Devices"](DocGisDevices).

* To control the visibility of parts of the workspace goto menu `Window`
    * `Toggle docks:` change visibility of all docked window parts at once.
    * `Toolbar:` change visibility of toolbar.
    * `Maps, Dig.Elev.Model (DEM), Workspace, Database, Routing:` change visibility of single docked window part.
    
### Waypoint icons setup

* Goto menu  `Workspace - Setup waypoint icons`
* In the pop-up windows click the `Open` icon and define a path from which additional user-defined waypoint icons can be loaded


### Toolbar setup

The toolbar allows quick access to important QMS actions.

* Toggle the display of the toolbar with the help of the menu `Window - Toolbar`.
* Configure the toolbar with the help of the menu `Window - Setup toolbar`:
    * Move actions to be included in the toolbar from the left part of the pop-up window to the right part of the window.
    * Move actions not to be included in the toolbar from the right part of the pop-up window to the left of the window.
    * Select the checkbox, if the toolbar should be displayed in the fullscreen mode, too.

## Map and DEM setup

### Download and install 

QMS can render vector maps in the Garmin format and various types of raster and online maps.

* _Vector maps:_ 
    * must have the `gmapsupp.img` container format,
    * only unlocked ones can be used,
    * typical sources:
        * [http://download.freizeitkarte-osm.de/garmin/latest](http://download.freizeitkarte-osm.de/garmin/latest) - select region and correct format.
        * [http://raumbezug.eu/osm-garmin_en.htm](http://raumbezug.eu/osm-garmin_en.htm) - select region and format.
        * an overview of available free vector maps can be found [here](http://wiki.openstreetmap.org/wiki/OSM_Map_On_Garmin/Download).
    * download (and unzip if necessary) the map and save it in some map directory.
* _Raster maps:_ for details see [here](DocFaqMaps).
* _Online maps:_ 
    * [Load file with links to on-line maps](http://www.mtb-touring.net/qms/onlinekarten-einbinden/ "On-line maps"). 
      _Hint:_ Click field `Download online maps`! Result is a downloaded file `Onlinemaps.zip`. 
    * Unpack this file into some map directory.  
    
QMS can use digital elevation data (`DEM` data). Necessary files can be downloaded from

* [https://dds.cr.usgs.gov/srtm/version2_1/SRTM3](https://dds.cr.usgs.gov/srtm/version2_1/SRTM3) or
* [http://viewfinderpanoramas.org/dem3.html](http://viewfinderpanoramas.org/dem3.html).

For more details about the installation of maps and DEM data compare also the [Quick start guide](DocQuickStartEnglish).

### Map paths

* _Assumption:_ Vector, raster maps or links to online maps have been downloaded and installed
* Goto the `Maps` tab (docked window, if not visible, then open it with the menu entry `Window - Maps`)
* Right click in the window to open the context menu
* Select `Setup map paths` (alternatively: select menu `File - Setup map paths`)
* In the pop-up window, add or remove paths with vector or raster maps

### Map cache path for online maps

* Goto the `Maps` tab (docked window, if not visible, then open it with the menu entry `Window - Maps`)
* Right click in the window to open the context menu
* Select `Setup map paths` (alternatively: select menu `File - Setup map paths`)
* In the pop-up window, define a path used for caching online map tiles

### DEM file paths

* _Assumption:_ DEM data has been downloaded and installed.
* Goto the `Dig.Elev.Model (DEM)` tab (docked window, if not visible, then open it with the menu entry `Window - Dig.Elev.Model (DEM)`)
* Right click in the window to open the context menu
* Select `Setup DEM paths` (alternatively: select menu `File - Setup DEM paths`)
* In the pop-up window add or remove paths with digital elevation (DEM) data 


### Map window display switches (toggles)

The following toggles change the layout of all map windows:

* Menu `View - Show scale`: switch on or off display of map scale 
* Menu `View - Show grid`:  switch on or off display of map grid in all map views
* Menu `View - POI text`: switch on or off display of POI names on vector maps
* Menu `View - Map tooltip`: switch on or off tooltip window display of features of the objects under the mouse cursor in a vector map
* Menu `View - Night/Day`: change map display between day and night layout (if supported by map)
* Menu `View - Min./max. track values`: show the minimum and maximum values of the track properties along the track in the map view
* Menu `View - Flip mouse wheel`: change the zoom direction when zooming a map with the mouse wheel
* Menu `View - Ext. profile`: if selected: track profile is shown in a resizable and floating separate window, otherwise in a small and fixed window

### Map window display setup

The following setup options change the layout of all map windows:

* Menu `View - Setup map font`: In the pop-up window select the font and its properties used for text in map objects
* Menu `View - Setup map background`: In the pop-up window select the color of the map background
* Menu `View - Setup units`: In the pop-up window select the length unit (nautical, imperial, metric) and the slope unit (% or °). 
  _Hint:_ Changes may take effect only after a QMS restart
* Menu `View - Setup grid`: 
    * Select the color of the map grid with the help of the palette icon
    * _Expert mode_: Define projection and datum (coordinate system) used for the map grid
    * _Remark:_ Each view has its own settings!
* Menu `View - Setup map view`: 
    * Set the map scales to _Logarithmic_ or _Square_. A change of this option leads to a different zoom behavior of maps 
     (compare section "[Map scale type](AdvMapDetails#map-scale-type)").
    * _Expert mode_: Define projection and datum (coordinate system) used for rendering of maps
    * _Remarks:_ 
        * Each view has its own settings!
        * Projections using lat/lon coordinates are not supported. Don't use Proj.4 settings with `+proj=longlat`!
        
* Menu `View - Setup coord. format`: Select one out of 3 supported geographical coordinate formats

### Single map display options

With the help of these options the user controls the rendering of a single map. For details, see 
section "[Adjustable map properties](AdvMapDetails#adjustable-map-properties)"


## Routing setup

### Routino database paths

* _Assumption:_ Routing databases have been downloaded and installed. For more details compare also the [Quick start guide](DocQuickStartEnglish).
* Goto the `Routing` tab (docked window, if not visible, then open it with the menu entry `Window - Routing`)
* In the combobox on the top of the window, select `Routino (offline)` 
* In the pop-up window, add or remove paths for Routino databases

### Routino setup

* Goto the `Routing` tab (docked window, if not visible, then open it with the menu entry `Window - Routing`)
* In the combobox on the top of the window, select `Routino (offline)` 
* Select 
    * Profile (vehicle type)
    * Language (for routing instructions)
    * Mode (quickest/shortest)
    * Routino database (should cover area under consideration)
    
### BRouter setup

* For general information about the use of BRouter see [here](http://brouter.de/brouter/).
* Goto the `Routing` tab (docked window, if not visible, then open it with the menu entry `Window - Routing`)
* In the combobox on the top of the window, select `BRouter (...)` 
* Be sure the Internet can be accessed
* Click the `Setup` button
* In the pop-up window choose 
    * online (`BRouter-Web (online)`) or offline (`local installation`) routing. _Remark:_ This selection will change the router name shown in the above mentioned combobox.
    * `Expert mode:` if appropriate: enables setting of some additional parameters for off- or online routing. _Recommendation:_ Don't select the expert mode (there is no advantage from changing the given default values)
* _Online router settings (recommended, easier to use, no additional installation step):_ 
    * Click `Next` after selecting online routing
    * In the next window, add or remove available BRouter profiles. Click on a profile name to see a short summary of the profile features.
    * If necessary, change the order of selected profiles
    * Close the profile selection window
* _Offline router settings (requires additional installation step):_
    * Be sure that Java runtime environment is installed on your system
    * Click `Next` after selecting offline routing
    * Select local BRouter installation directory
        * If the installation directory is empty or doesn't exist: click button `Create new BRouter installation` resp. `Create directory and install BRouter there`
        * If a BRouter installation is found in the installation directory: click button `Update existing BRouter installation` and select the version you
          want to install
    * Select Java executable if not automatically found
    * Go to the next window
    * Add or remove available BRouter profiles. Click on a profile name to see a short summary of the profile features.
    * If necessary, change the order of selected profiles
    * Close the profile selection window
    * In the next window, select the tiles (areas) to be used for routing.
        * The tiles (segments) have a size of 5° in each direction
        * The scale of the tile selection window can't be changed, but the window itself can be resized.
        * The tile selection window shows a world map as background.
        * _Recommendation:_ Before starting the BRouter setup define with the help of the context menu `Add area` (resp. `Add waypoint`) a sufficiently large area on the map (resp. a few  waypoints) for which routing data are required. Find this area in the tile selection window by moving the map to this area and then select tiles around it. In the next image a user-defined area covering large parts of Central Europe is shown.
        * The color and the texture of each tile inform about the following tile properties (also shown in an infobox, if the mouse is located on a tile):
             * Routing data available on the server or not.
             * Routing data is locally saved or not.
             * Routing data is outdated and should be updated.
             * Size of data download.
        * The status line in the window informs about the number of up-to-date and outdated tiles, and about. the number of tiles selected for download.    
           
           ![Area overlay](images/DocAdv/BRouterTileSelection.jpg "BRouter tile selection")
           
    * Click `Download` to start the download of routing data for offline use. _Attention:_ Depending on the size of the selected area
      the download duration can be considerable!
    * Close the download window after the end of the download.
    
* Select one of the available routing profiles
* Select, if wanted, an alternative to the original route
* In the case of offline routing, select the `on the fly routing` checkbox, if the next route segment should be calculated
   immediately after selecting the next route point.
    

### MapQuest setup

* Goto the `Routing` tab (docked window, if not visible, then open it with the menu entry `Window - Routing`)
* In the combobox on the top of the window, select `MapQuest (online)` 
* Select 
    * Profile (vehicle type)
    * Language (for routing instructions)
    * Road types to avoid
* _Hint:_ When creating a new track, create first a new route, select - if necessary - `Calculate route` from the route context menu
  and after the route has been completely constructed, convert it to a track with the help of the route context menu.

## Further setup and configuration options

The following list shows some more setup options without detailed description:

* Database import from QLandkarte (menu `Tool - Import database from QLandkarte`)
* VRT Builder for raster maps (menu `Tool - VRT Builder`)
* Routino database creation (menu `Tool - Create Routino database`)

- - -
[Prev](AdvRealtime) (Realtime data) | [Home](Home) | [Manual](DocMain) | [Index](AxAdvIndex) | [Top](#) | (Overview of toolbar actions) [Next](AdvToolbarAct)
