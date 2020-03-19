[Prev](ReferenceTool) (Reference tool) | [Home](QMTHome) | [Manual](QMTDocMain) | [Index](QMTAxAdvIndex) | (Color palette tool) [Next](PaletteTool)
- - -

***Table of contents***

* [Grid tool](#grid-tool)
    * [Basic information](#basic-information)
    * [More details](#more-details)
    * [Examples of referencing a map with the grid tool](#examples-of-referencing-a-map-with-the-grid-tool)
        * [Example 1](#example-1)
        * [Example 2](#example-2)

* * * * * * * * * *
 
# Grid tool

## Basic information

The grid tool is an add-on to the [reference tool](ReferenceTool). It is used to reference maps with a grid for which the coordinate system is known.

While in the reference tool manual input of coordinates is required for each reference point, the grid tool needs only a description of the coordinate system
used in the map and the coordinates of just one reference point. 3 other reference points in the grid must be defined by clicking on them in the map.

The grid tool automatically creates additional reference points on the grid in a user-defined area. If necessary, the reference tool can help
to improve the positions of reference points created with the grid tool.

To work with the QMT grid tool proceed as follows (compare the images in the [example section](#examples-of-referencing-a-map-with-the-grid-tool)):

1. Select the menu entry `Window - Shell` to open a shell window (docked window, can be moved on the desktop).
1. Click the `Reference tool` button in the QMT `Tools` window (docked window, can be moved on the desktop).
1. Click the `Open` (`Add map files to list`) icon (![](QMapTool/images/PathBlue.png)) and select a raster map with a grid and known coordinate system for the grid (this means: some
   form of the Proj.4 description of the coordinate system should be known). 
   The raster map is loaded into the QMT map window.
1. Click the grid tool icon (![](QMapTool/images/GridTool.png)) in the reference tool to open the grid tool (docked window, can be moved on the desktop).
1. Zoom the map with the mouse wheel so that 1 complete grid square is displayed in the window (make it as large as reasonable).
1. Click the coordinate system selection icon (![](QMapTool/images/GridWizzard.png))
1. Choose the coordinate system of the grid (coordinate systems may have degree or meter as unit). If the coordinate system is not in the list provided by QMT, then
   check if it can be found in the [list of some additional coordinate systems](EpsgOverview) or in one of the links given there.
1. Get the coordinates of the upper left corner of a grid square (coordinates must match the coordinate system defined in the previous step!).
1. Insert easting/longitude and northing/latitude into their fields. Use meters with easting/northing and degrees with longitude/latitude.
1. Define the horizontal and vertical size (spacing) of the considered grid square with the unit used in the previous point.
1. Select the next (second) radio button.
1. Goto the map and left-click the upper left corner of the grid square. This selects the first reference point (remember: the coordinates of this point 
   have been defined earlier). 
1. Select each of the 3 neighbors in the square in the tool window and click the corresponding grid corners of the map. This defines 3
   additional reference points. The coordinates of these points are calculated from the grid size defined earlier. All reference points up to this step are
   displayed on the map as small orange squares.
1. Click the `Set area` button in the grid tool. A black-framed rectangle appears in the map window (zoom out if not visible!). Within this area
   the tool creates additional grid points (shown as small black points).
1. To change the size of the area click in the square at the upper left or lower right corner of the area frame to fix the mouse to this corner,
   move the mouse to the wanted new location and left click again to fix the corner.
1. Click `Ok` to close the grid tool.
1. In the reference tool there appears now a list of reference points. If necessary, the positions of the reference points can be improved as described in the
   [reference tool](ReferenceTool) section.
1. Proceed with the reference tool as described there.

## More details

* Feel free to use the 4 vertices of an arbitrary grid rectangle. If doing so, the horizontal resp. vertical spacing values should be the length of the horizontal resp. vertical
  edges of the rectangle. This approach can reduce the number of reference points created automatically by the grid tool. 
* Selecting the second radio button in the tool window and clicking `Reset` in the big gray square deletes all reference points (but not the coordinate system definition).
* Clicking the `Reset` button at the button of the tool window deletes the coordinate system definition and the selected reference points.
* Clicking the `Cancel` button closes the grid tool without transferring the referenced points to the reference tool.
* The grid tool can be used repeatedly when referencing a map and even with different coordinate systems. After finishing one run of the grid tool re-open it from
  the reference tool. If necessary, define a new coordinate system in the grid tool. New reference points created in the next grid tool run are appended to the 
  list already existing reference points. This can be useful
  if there are different grid coordinate systems used in one raster map (e.g. grids for 2 different Gauß-Krüger zones covered by the map). The following image 
  illustrates such a situation where the left part of the map belongs to the Gauß-Krüger zone 5, the right one to the zone 6 (look at labels _Ostgrenze, Westgrenze_ marking the
  zone boundary). Pay attention to the fact that in this
  case grid lines are broken (see cyan rectangle for northing and jump in the easting value)!
  
    ![Different grids on map](QMapTool/images/GridChange.jpg "Different grids on 1 map")

## Examples of referencing a map with the grid tool

### Example 1

* Used map: OpenStreetMap displayed in QMS, screen snapshot of center of Addis Abeba, Ethiopia

    ![Used map](QMapTool/images/ETH_Map.jpg "Used map")

* Grid used: EPSG 3857,  WGS 84 / Pseudo-Mercator (selected in QMS/QMT via "World Mercator (OSM) - datum WGS_1984"):

    ![Set grid to World Mercator (OSM) - WGS84](QMapTool/images/ETH_GridSetting.jpg "Set grid to World Mercator (OSM) - WGS84")

    ![Set proj.4 to World Mercator (OSM) - WGS84](QMapTool/images/ETH_GridSetting1.jpg "Set proj.4 to World Mercator (OSM) - WGS84")

* Proj.4 parameters: `+proj=merc +a=6378137 +b=6378137 +lat_ts=0.001 +lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m +nadgrids=@null +no_defs` 
* Open grid tool for referencing
* Upper left grid corner used as first grid point and then then 3 immediate neighbors (orange points in upper left corner)
* Coordinates of first point: Easting: 4312000 (m), Northing: 1009000 (m), horiz./vert. spacing: 1000 (m) (grid unit is km, square size is 1km by 1 km)
* number of reference points added by QMT: 8 (small green squares, returning back to the reference tool all reference points are shown as small black squares)
* no additional refinement of automatically created reference points in the reference tool (precision of obtained reference points seems to be sufficient)

    ![Grid tool](QMapTool/images/ETH_GridTool.jpg "Grid tool")


* Result when displaying referenced map in QMS: differences in grid lines and streets between original OSM map and referenced map practically not visible
  (inside the black frame is the referenced map, outside the original one).

    ![Compare original and referenced map](QMapTool/images/ETH_ReferencedMap.jpg "Compare original and referenced map")
    
### Example 2

* Similar to Example 1
* Grid used: EPSG 4326 (WGS84 geographic)

     ![Set grid to EPSG 4326](QMapTool/images/ETH_ReferenceMap1.jpg "Set grid to EPSG:4326")

* Proj.4 parameters: `+init=epsg:4326`
* Coordinates of first point N9.035°, E38.74 (easting: longitude, northing: latitude, spacing in degrees)
* no additional refinement of automatically created reference points

    ![Grid tool EPSG 4326](QMapTool/images/ETH_GridTool4326.jpg "Grid tool EPSG 4326")
    
- - -
[Prev](ReferenceTool) (Reference tool) | [Home](QMTHome) | [Manual](QMTDocMain) | [Index](QMTAxAdvIndex) | [Top](#) | (Color palette tool) [Next](PaletteTool)
