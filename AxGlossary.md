[Prev](AxAdvToc) (Complete table of contents) | [Home](Home) | [Manual](DocMain) | [Index](AxAdvIndex) | (Index) [Next](AxAdvIndex)
- - -

# Glossary

**Activity**
: Means of motion (pedestrian, bicycle, car, ...) for part (range) of a track.

**Active project**
: A single project in the workspace into which newly created GIS objects are saved.

**BRouter**
: Router application for finding a route between two points using the topographical data from OpenStreetMap. The router can

* handle different routing profiles,  
* use elevation data,
* calculate alternative routes,
* process no-go areas and lines,
* work online and offline.
  
**DEM**
: Abbreviation for **D**igital **E**levation **M**odel. DEM data provides elevation data for maps.
  QMapShack can handle this data from different sources with the help of _VRT_ files that describe the properties of
  the downloaded elevation data.

**Diary**
: See __Roadbook__.

**Douglas-Peuker filter**
: A track filter for smoothing recorded tracks and for removing superfluous trackpoints from a track.

**EPSG code**
: A 4- or 5-digits code which identifies a geodetic coordinate system or its components (projection, datum). 

**Filter**
: See __Track filter__.

**GDAL**
: Abbreviation for **G**eospatial **D**ata **A**bstraction **L**ibrary. Library for handling raster and vector geospatial data formats.

**GIS data**
: Abbreviation for **G**eographic **I**nformation **S**ystems data.  This data includes all tracks, routes and
  waypoints used in QMapShack.

**gmapsupp.img**
: Typical file name and at the same time term for describing widely used container format for Garmin-style vector maps.

**Line**
: See __Polyline__.

**Map cache**
: Special storage location where map data is saved temporarily in a format suitable for fast reloading. One of the
advantages of the map cache is that cached online map tiles can be displayed immediately instead of waiting for the online
map server.

**Map view**
: A window where different types of maps and where tracks, routes and waypoints are displayed and handled.

**Maps window/tab**
: Window/tab in QMapShack where the user can define and activate the vector, raster or online maps for a map view.

** No-go area**
: An area that can't be crossed by a route or a track. In QMS no-go areas can be created from normal areas. The BRouter routing engine can process no-go areas.

** No-go line**
: A line that can't be crossed by a route or a track. In QMS no-go lines can be created from routes or tracks. The BRouter routing engine can process no-go lines.

**Planetsplitter**
: Part of the Routino offline router package. Planetsplitter creates an efficient routing database from OpenStreetMap data.

**Polyline**
: Also denoted as _Line_ or _GIS item with multiple points_. A series of connected straight line intervals linking
given points. Tracks, routes, and area boundaries are polylines.

**Roadbook**
: Also denoted as "_Diary_". A tabular overview of all data in a project.

**Routing method**
: The method used for creating automatically intermediate subpoints of a track or route between 2 consecutive given
  waypoints.

**Routino database**
: Preprocessed form of OpenStreetMap routing data for use with Routino router.

**Routino**
: Offline router application for finding a route between two points using the topographical data from
[OpenStreetMap](https://www.OpenStreetMap.org/). To optimize the routing a custom database format is used.

**Slope at geographical location**
: Value of the steepest ascent or descent at a given geographical location calculated from DEM data. It informs about the steepest ascent resp. descent in the terrain
around a given location.
Measured in degrees. Always nonnegative values. Displayed in the QMS status line
or as adjustable elevation property in a map.

**Slope of terrain (terrain slope)**
: Slope at geographical location of a trackpoint. Can be attached with the help of the `Calculate terrain slope` track filter to trackpoints. 
Can be displayed in a graph in the track edit window. Terrain slope and track slope are to different features of a trackpoint!

**Slope of track**
: Calculated from the elevation difference and the distance between 2 successive waypoints. It informs about the ascent or descent along the track.
It can have positive values (for ascent) and negative values (for descent).
Measured in degrees. Can be displayed in a graph in the track edit window.

**Terrain slope**
: See __Slope of terrain__.

**TMS**
: Abbreviation for **T**ile **M**ap **S**ervice. A **TMS** file provides access to cartographic maps
  on special map servers.

**Track details dialog**
: Also denoted as "_Track edit window_". Window that displays various information about a track and that allows editing
of some track data.

**Track edit mode**
: Special state of a track in which trackpoints can be edited. To do this a copy of the track is created. The user carries out the editing
  (add, move, delete of points, assign activity, ...) on this copy and at the end he decides whether to save the changes to the original or
  to a new track, or if he wants to abort editing.

**Track edit window**
: See __Track details dialog__.

**Track filter**
: Tool to manipulate a track in a predefined way. QMS supports track filters for elevation, timestamps, splitting tracks and
  others.

**Track range**
: A sequence of trackpoints of a track which can be handled separately (copy, assign activity, hide,
  delete, recalculate,...).

**Track segment**
: Each track consists of an ordered list of one or more track segments. A track segment consists of an ordered
  list of trackpoints.
  When combining (joining) tracks in QMS, the track segments of all selected tracks are combined.

**Track subpoint**
: When creating a track the user creates with the help of mouse clicks (ordinary) trackpoints. Depending on the selected
  routing method
  additional trackpoints can be added automatically by the routing algorithm. These additional trackpoints are
  called _subpoints_.

**Trackpoint, hidden**
: Trackpoints in a track which are not displayed in a map view and not used in the calculation of global track data
  (length, ascent, ...).

**VRT Builder**
: QMapShack tool for building VRT files from other data such as elevation data or raster maps. This tool calls the
`gdalbuildvrt` tool of the GDAL package.

**VRT**
: The __VRT__ file format is a format used for describing virtual geospatial data composed from various
  other geospatial data such as elevation data. QMapShack can use elevation data if it is provided as VRT file.
  _Warning:_ VRT files use relative path names to point to other files. Never move them to another location!

**Waypoint, attached to track**
: A waypoint that is at the same time a trackpoint of a track. With the help of waypoints attached to a track the user
  can define track legs for which the roadbook of the track gives additional information.

**WMTS**
: Abbreviation for **W**eb **M**ap **T**ile **S**ervice. A __WMTS__ file provides access to cartographic maps
  on special map servers.

**Workspace**
: The part of the user interface (GUI) where the user can work with projects and their data (waypoints, tracks, routes).


- - -
[Prev](AxAdvToc) (Complete table of contents) | [Home](Home) | [Manual](DocMain) | [Index](AxAdvIndex) | [Top](#) | (Index) [Next](AxAdvIndex)
