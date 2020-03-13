[Prev](CutTool) (Cut tool) | [Home](QMTHome) | [Manual](QMTDocMain) | [Index](QMTAxAdvIndex) | (Grid tool) [Next](GridTool)
- - -

***Table of contents***

* [Referencing maps](#markdown-header-referencing-maps)
    * [Reference tool](#markdown-header-reference-tool)
        * [Basic information](#markdown-header-basic-information)
        * [More details   ](#markdown-header-more-details)
    * [Example: Referencing of Russian military maps](#markdown-header-example-referencing-of-russian-military-maps)

* * * * * * * * * *
 
# Referencing maps

Raster maps are typically obtained by scanning maps or collecting aerial photographs and satellite images. They are saved as image files in
common formats such as TIF, JPG, PNG (QMT can handle all image formats for which GDAL provides a driver, a list can be obtained by calling `gdalinfo --formats`,
prefer the TIFF format). 

(Geo-)referencing a raster map means 

* to add reference points to the map that link known raster positions to known positions in map coordinates,
* to save the georeferencing information when the referencing is satisfactory (output format, for instance, GeoTIFF).

QMT's reference tool provides an easy way to reference raster maps.

## Reference tool

### Basic information

To work with the QMT reference tool proceed as follows:

1. Select the menu entry `Window - Shell` to open the QMT shell window (docked window, can be moved on the desktop).
1. Find more than 3 reference points in the raster map with known WGS84 lat/lon coordinates. _Remark:_ An easy way to get reference points with coordinates is to use a 
   map (e.g. OpenStreetMap) in QMS.
1. Click the `Reference tool` button in the QMT `Tools` window (docked window, can be moved on the desktop).
1. Click the `Open` (`Add map files to list`) icon (![](QMapTool/images/PathBlue.png)) and select a raster map. The raster map is loaded into the QMT map window.
1. Click the `Add reference point` icon (![](QMapTool/images/RefAdd.png)). The map cursor now is a cross-hair one.
1. Move the mouse cursor on each of the known reference points as precisely as possible (use mouse wheel to zoom map!) and left-click to fix the reference point.
1. Insert the WGS84 coordinates of the reference point into the pop-up window. The input format is shown as soon as input is started. A small black square is shown
   at the reference point in the map. The coordinates and the pixel location of the reference point are inserted into the list of reference points in the tool window.

     ![Input of WGS84 coordinates](QMapTool/images/RefToolCoord.jpg "Input of WGS84 coordinates")

     _Remark:_ An easy way to get reference points into QMT is to use QMS. Find some reference point which is on the raster map and on the
     QMS map as well. Right click the QMS map at the reference point location to get a context menu and then click `Copy position`. This copies the current position to
     the clipboard. Now, goto to the QMT window and add the reference point. When being asked for the coordinates simply press `CTRL-V` to insert the coordinates
     found in QMS.
     
1. Click the `Start projection wizard` icon (![](QMapTool/images/GridWizzard.png)) and select the coordinate system for the output of referenced data. An example is shown in the next image.

     ![Select output coordinates](QMapTool/images/RefToolOutCoord.jpg "Select output coordinates")

1. Leave defaults for other settings.
1. Click the `Start` button to get a referenced image file and a VRT file in the directory of the original raster map. The shell window displays the GDAL commands run.

    ![Reference tool with referenced map](QMapTool/images/RefTool.jpg "Reference tool with referenced map")

### More details   

In addition to the basic steps described in the previous section some more actions with maps and reference points can be carried out in the reference tool:

Icon | Tooltip | Comment
-----|---------|--------
![](QMapTool/images/DeleteOne.png) | Remove selected (map) file from the list | Reference points are deleted, too.
![](QMapTool/images/DeleteMultiple.png) | Clear complete list of map files | Reference points are deleted, too.
![](QMapTool/images/Reload.png) | Reload the currently selected map | Reference points aren't changed.
![](QMapTool/images/MoveArrow.png) | Move the map and zoom | Zoom with mouse wheel.
![](QMapTool/images/RefAdd.png) | Add reference point | Move mouse to wanted point, left-click and insert coordinates into the coordinate definition window.
![](QMapTool/images/RefMove.png) | Move reference point | Reposition misplaced reference point. A selected reference point either in the list or in the map changes the square color to red. Left-click the reference point in the map, move it to new location and left-click again to fix it.
![](QMapTool/images/RefDel.png) | Remove single reference point | A selected reference point either in the list or in the map changes the square color to red. Left-click in the map to remove it.
![](QMapTool/images/RefMoveAuto.png) | Move reference point with automode. This will pick-up (move the mouse to) the next point after you moved a reference point. | Press `b` or `n` on the keyboard to jump to the previous or next reference point in the list.
![](QMapTool/images/RefDelAll.png) | Remove all reference points | Requires additional confirmation of deletion.
![](QMapTool/images/GridTool.png) | Switch to the [grid tool](GridTool) | Reference tool add-on for fast creation of reference points if map has known grid.
![](QMapTool/images/LoadGcp.png) | Load reference points from GCP file | Load previously defined and saved reference points from file.
![](QMapTool/images/SaveGcp.png) | Save reference points into GCP file | Save reference points for future use.
![](QMapTool/images/Sort.png) | Sort list of reference points |

* If the field labeled `Embed result into *.vrt file` is not checked, then the above mentioned VRT file (needed for displaying the map in QMS) is not 
  created. _Remark:_ Leave the checkbox selected, if the referenced map should be used in QMS.
  
* It is possible to open several map files and to reference each of these maps. If the checkbox `For all files` at the bottom of the tool is checked, then the 
  referencing is carried out for each of the loaded map files.
  
  
_Remark:_ the `Create overviews ...` option is available in 4 QMT tools (cut tool, overview tool, reference tool, palette tool). This is necessary because there is no fixed order of
    using these tools. When one of these tools calls GDAL for some operation, then GDAL doesn't read the overview information contained in the raster map file. Thus, overview 
    information should be recreated after such a GDAL operation and this is supported in each of the tools.

## Example: Referencing of Russian military maps

[http://loadmap.net](http://loadmap.net) is a server for a wide variety of raster maps covering large parts of the world. 
Among them are various kinds of Russian army and topographic maps.

These maps have a large boundary for map metadata information.

Typically, Russian military maps are georeferenced with reference information provided in the OziExplorer MAP format. As a rule, the Krassowski ellipsoid 
(epsg 4284, Pulkovo 1942)
is used in the MAP file for lat/lon coordinates. In this example it is assumed that the differences between these coordinates and the WGS84 lat/lon coordinates
used in the reference tool can be neglected.

Using a text editor and the information from the MAP file it is easy [to cut](CutTool#markdown-header-example-cutting-of-russian-military-maps) 
and reference such maps with QMT. Follow these steps for downloading and referencing a (cut) map:

* Select a map on [http://loadmap.net](http://loadmap.net).
* When downloading the selected map, 2 files are offered: a GIF and a MAP file. Download both files and put them into some directory.
* As an example the files `001m--m36--(1989).gif`, `001m--m36--(1989).map` will be used in this discussion.
* Open the MAP file in a text editor and find the lines labeled `POINT` near the top of the file.
* Assume the MAP file has non-zero values in the latitude and longitude columns of the line labeled `Point01` (the other case is described at the end of this subsection).
* In the example these lines are
      
        Point01,xy,  219,   86,in, deg,  52,  0.0000,N,  30,  0.0000,E, grid,   ,           ,           ,N
        Point02,xy, 1842,  121,in, deg,  52,  0.0000,N,  33,  0.0000,E, grid,   ,           ,           ,N
        Point03,xy, 3466,   90,in, deg,  52,  0.0000,N,  36,  0.0000,E, grid,   ,           ,           ,N
        Point04,xy,  147, 1839,in, deg,  50,  0.0000,N,  30,  0.0000,E, grid,   ,           ,           ,N
        Point05,xy, 1839, 1873,in, deg,  50,  0.0000,N,  33,  0.0000,E, grid,   ,           ,           ,N
        Point06,xy, 3533, 1842,in, deg,  50,  0.0000,N,  36,  0.0000,E, grid,   ,           ,           ,N
        Point07,xy,   74, 3591,in, deg,  48,  0.0000,N,  30,  0.0000,E, grid,   ,           ,           ,N
        Point08,xy, 1835, 3629,in, deg,  48,  0.0000,N,  33,  0.0000,E, grid,   ,           ,           ,N
        Point09,xy, 3598, 3594,in, deg,  48,  0.0000,N,  36,  0.0000,E, grid,   ,           ,           ,N

    (use only lines where values are filled in!) 

* Convert this block with the editor to
    
        #V1.0 
        #gcpproj: +proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs 
        -gcp 219 86 52.00000000 30.00000000
        -gcp 1842 121 52.00000000 33.00000000
        -gcp 3466 90 52.00000000 36.00000000
        -gcp 147 1839 50.00000000 30.00000000
        -gcp 1839 1873 50.00000000 33.00000000
        -gcp 3533 1842 50.00000000 36.00000000
        -gcp 74 3591 48.00000000 30.00000000
        -gcp 1835 3629 48.00000000 33.00000000
        -gcp 3598 3594 48.00000000 36.00000000

    _Remark:_ In the above block the fractional part of the geographical coordinates is obtained by dividing the seconds part of the geographical coordinate 60!

* Save these lines to a new file with filename `001m--m36--(1989).gcp`.
* Start QMT and open the reference map tool in QMT.
* Load `001m--m36--(1989).gif` into the reference tool (_hint:_ a map file previously cut with the cut tool can be used here, too). 
* Select the `Load reference points from GCP file` icon in the toolbar and load the file `001m--m36--(1989).gcp`.
* The map window shows now 9 reference points (4 points in the corners, 4 points in the middle of the 4 edges of the map, 1 in the center of the map). 
    
     ![Using GCP file](QMapTool/images/RefToolGCP.jpg "Use of GCP file")
      
    If necessary, improve reference points manually as described on this page.
    
* Define final map projection.  
* Click `Start` to create a new referenced map file.

For some MAP files the described procedure may fail because there are no latitude/longitude coordinates in the `Point` lines.
In this case the described procedure for creating the GCP output file should be changed slightly as follows:

* Find lines labeled `MMPXY` and `MMPLL` near the end of the MAP file.
* An example of such lines is

        MMPXY,1,5,180
        MMPXY,2,4068,162
        MMPXY,3,4091,3915
        MMPXY,4,16,3933
        MMPLL,1,39.25,44.0
        MMPLL,2,39.5,44.0
        MMPLL,3,39.5,43.8333333333
        MMPLL,4,39.25,43.8333333333
        
* The `MMPXY,i` lines gives the values for the first two fields (pixel coordinates) in the new output line.
* The corresponding `MMPLL,i` lines gives the longitude and latitude coordinates for the new output line.
* Build for each such pair a new line of the form

        -gcp 5 180 44.0 39.25
        
    (for the example `i = 1` was used, pay attention that the output order is latitude - longitude!).
  
* Proceed as described in the first part of this subsection. 
  

   
    
- - -
[Prev](CutTool) (Cut tool) | [Home](QMTHome) | [Manual](QMTDocMain) | [Index](QMTAxAdvIndex) | [Top](#) | (Grid tool) [Next](GridTool)
