[Prev](OverviewTool) (Overview tool) | [Home](QMTHome) | [Manual](QMTDocMain) | [Index](QMTAxAdvIndex) | (Reference tool) [Next](ReferenceTool)
- - -

***Table of contents***

* [Cutting maps](#markdown-header-cutting-maps)
    * [Basic information](#markdown-header-basic-information)
        * [More details   ](#markdown-header-more-details)
    * [Example: Cutting of Russian military maps](#markdown-header-example-cutting-of-russian-military-maps)

* * * * * * * * * *
 
# Cutting maps

With the help of the cut tool the user can cut off (crop) unwanted parts at the edges of a raster map (e.g. map descriptions). Do this a polygon (a mask) has to be defined.
The map area within this polygon (and in the map) is kept as new map area, the area outside the polygon is removed from the map. Technically, this is done by 
making the outside part of the map image transparent. As a consequence, only the transparency information in the map image (the alpha channel values) and not the image 
size itself is changed. Thus, cutting a map is without influence on existing reference points for the map.

In the following image the map area (without content, only grid lines drawn for better visibility) is delimited by a black rectangular frame. The cut polygon is defined
with the help of 6 points (vertices), 4 of them outside the map area. The shaded area within the map is cut off from the map (is made transparent).

![Cut map with polygon](QMapTool/images/CutPolygon.jpg "Cut map with polygon")

## Basic information

To cut a map proceed as follows:

1. Select the menu entry `Window - Shell` to open the QMT shell window (docked window, can be moved on the desktop).
1. Click the `Cut map` button in the QMT `Tools` window to open the cut tool.
1. Click the `Open` (`Add map files to list`) icon (![](QMapTool/images/PathBlue.png)) and select a raster map. The raster map is loaded into the QMT map window.
1. Click the `Add point to mask` icon (![](QMapTool/images/RefAdd.png)). The map cursor now is a cross-hair one.
1. Move the mouse cursor to the first polygon point as precisely as possible (use the mouse wheel to zoom map!) and left-click to fix the point.
1. Move the mouse to the next polygon point and fix it with a left click. Continue until the polygon mask has the wanted shape. _Remark:_ Starting with the third
   point the cut polygon is visible as an area.
1. Click the `Start` button to cut the map. The file name of the new map file gets an additional suffix (default: `_cut`). 
1. The shell window (if activated) shows the used GDAL commands and the progress of the operation.

The following image shows the complete cut tool with a map and a mask which removes the non-map parts of the printed map.

![Cut tool](QMapTool/images/CutMap.jpg "Cut tool")

An advantage of the use of cut maps is that several neighboring ones can be rendered smoothly as demonstrated in the following image:

![Maps cut and joined](QMapTool/images/JoinMaps.jpg "Maps cut and joined")

### More details   

In addition to the basic steps described in the previous section some more actions can be carried out in the cut tool:

Icon | Tooltip | Comment
-----|---------|--------
![](QMapTool/images/DeleteOne.png) | Remove selected (map) file from the list | 
![](QMapTool/images/DeleteMultiple.png) | Clear complete list of map files | 
![](QMapTool/images/Reload.png) | Reload the currently selected map | 
![](QMapTool/images/MoveArrow.png) | Move the map and zoom | Zoom with mouse wheel. |
![](QMapTool/images/RefAdd.png) | Add point to mask | Left-click on polygon edge (selected edge is in red color), move mouse to new location, left-click again to fix the new point. 
![](QMapTool/images/RefMove.png) | Move points of mask | Reposition misplaced mask point. Left-click the mask point in the map, move it to new location, left-click again to fix it.
![](QMapTool/images/RefDel.png) | Remove point from mask | Left-click on a mask point in the map to remove the point.
![](QMapTool/images/RefDelAll.png) | Remove complete cut mask | Requires additional confirmation of deletion of whole mask.
![](QMapTool/images/LoadShape.png) | Load reference points from shape file | Load previously defined cut mask from file.
![](QMapTool/images/SaveShape.png) | Save reference points into shape file | Save cut mask for future use.



_Remarks:_ 

* It is possible to open several map files and to define cut masks for each of these files. If the checkbox `For all files` at the bottom of the tool is checked, then the 
  cutting is carried out for each of the loaded map files.
* The `Create overviews ...` option is available in 4 QMT tools (cut tool, overview tool, reference tool, palette tool). This is necessary because there is no fixed order of
  using these tools. When one of these tools calls GDAL for some operation, then GDAL doesn't read the overview information contained in the raster map file. Thus, overview 
  information should be recreated after such a GDAL operation and this is supported in each of the tools.
* Raster maps can have a considerable size. To get quickly a precise cut mask the following approach can help:
    * Zoom out to display the complete map.
    * Build a first cut mask on the complete map. Iteratively refine this map as described in the next steps.
    * Select the `Move points` icon (or also the `Add point` icon).
    * Locate the mouse near a cut point and zoom in so that the cut point remains visible.
    * Move the cut point on this zoom level to its precise location.
    * Repeat the previous step for each cut point.
* The cut tool can be used for referenced and unreferenced maps. When using it with a referenced map, a warning of the form

        Warning 1: the source raster dataset has a SRS, but the cutline features not.  
        We assume that the cutline coordinates are expressed in the destination SRS.
        If not, cutline results may be incorrect.

  might be shown. In this case check if the output file is correctly cut.
  
## Example: Cutting of Russian military maps

[http://loadmap.net](http://loadmap.net) is a server for a wide variety of raster maps covering large parts of the world. 
Among them are various kinds of Russian army and topographic maps.

These maps have a large boundary for map metadata information.

Typically, Russian military maps are georeferenced with reference information provided in the OziExplorer MAP format. 

Using a text editor and the information from the MAP file it is easy to cut such maps with QMT. Follow these steps for downloading and cutting a map:

* Select a map on [http://loadmap.net](http://loadmap.net).
* When downloading the selected map, 2 files are offered: a GIF and a MAP file. Download both files and put them into some directory.
* As an example the files `001m--m36--(1989).gif`, `001m--m36--(1989).map` will be used in this discussion
* _First approach:_ 
    * Open the MAP file in a text editor and find the lines labeled `MMPXY` near the bottom of the file.
    * In the example these lines are
    
            MMPXY,1,219,86
            MMPXY,2,3466,90
            MMPXY,3,3598,3594
            MMPXY,4,74,3591
        
        (meaning of the lines: pixel coordinates of the 4 corners of the map area in the GIF file).
    * Add the first line of this block once again at the end of the block.
    * Convert this block with the editor to
    
            id,WKT
            1,"POLYGON((219 86, 3466 90, 3598 3594, 74 3591, 219 86))"
        
    * Save these 2 lines to a new file with filename `001m--m36--(1989)_1.shp`.
    * Start QMT and open the cut map tool in QMT.
    * Load `001m--m36--(1989).gif` into the cut tool.
    * Select the `Load cut mask from shape file` icon in the toolbar and load the file `001m--m36--(1989)_1.shp`.
    * The map window shows now a cut mask with cut points in the 4 corners of the map area as shown in the next image:
    
         ![Using shape file](QMapTool/images/CutMask.jpg "Use of a cut mask")
      
         If necessary, improve the cut mask manually as described on this page.
    * Click `Start` to create a new map file which will be displayed without the boundary area (boundary area is now transparent).

* _Second approach (more precise):_
    * Carefully checking the cut mask obtained in the first approach makes the weakness of this map obvious: there is still some part of
      the boundary not cut from the map:
      
         ![Inaccurate cut mask](QMapTool/images/CutMask1.jpg "Inaccurate cut mask")
      
    * Open the MAP file in a text editor and find the lines labeled `POINT` near the top of the file.
    * In the example the lines are
      
            Point01,xy,  219,   86,in, deg,  52,  0.0000,N,  30,  0.0000,E, grid,   ,           ,           ,N
            Point02,xy, 1842,  121,in, deg,  52,  0.0000,N,  33,  0.0000,E, grid,   ,           ,           ,N
            Point03,xy, 3466,   90,in, deg,  52,  0.0000,N,  36,  0.0000,E, grid,   ,           ,           ,N
            Point04,xy,  147, 1839,in, deg,  50,  0.0000,N,  30,  0.0000,E, grid,   ,           ,           ,N
            Point05,xy, 1839, 1873,in, deg,  50,  0.0000,N,  33,  0.0000,E, grid,   ,           ,           ,N
            Point06,xy, 3533, 1842,in, deg,  50,  0.0000,N,  36,  0.0000,E, grid,   ,           ,           ,N
            Point07,xy,   74, 3591,in, deg,  48,  0.0000,N,  30,  0.0000,E, grid,   ,           ,           ,N
            Point08,xy, 1835, 3629,in, deg,  48,  0.0000,N,  33,  0.0000,E, grid,   ,           ,           ,N
            Point09,xy, 3598, 3594,in, deg,  48,  0.0000,N,  36,  0.0000,E, grid,   ,           ,           ,N

        (use only lines where values are filled in!). Meaning of the lines: pixel in the map image and its geographical coordinate.
    * Reorder these lines to get      

            Point01,xy,  219,   86,in, deg,  52,  0.0000,N,  30,  0.0000,E, grid,   ,           ,           ,N
            Point02,xy, 1842,  121,in, deg,  52,  0.0000,N,  33,  0.0000,E, grid,   ,           ,           ,N
            Point03,xy, 3466,   90,in, deg,  52,  0.0000,N,  36,  0.0000,E, grid,   ,           ,           ,N
            Point06,xy, 3533, 1842,in, deg,  50,  0.0000,N,  36,  0.0000,E, grid,   ,           ,           ,N
            Point09,xy, 3598, 3594,in, deg,  48,  0.0000,N,  36,  0.0000,E, grid,   ,           ,           ,N
            Point08,xy, 1835, 3629,in, deg,  48,  0.0000,N,  33,  0.0000,E, grid,   ,           ,           ,N         
            Point07,xy,   74, 3591,in, deg,  48,  0.0000,N,  30,  0.0000,E, grid,   ,           ,           ,N
            Point04,xy,  147, 1839,in, deg,  50,  0.0000,N,  30,  0.0000,E, grid,   ,           ,           ,N
            Point01,xy,  219,   86,in, deg,  52,  0.0000,N,  30,  0.0000,E, grid,   ,           ,           ,N
          
        Add the first line of the block again at the end. Understand the shape generated by the geographical coordinates on a map (polygon!) 
        to understand the order! `Point05` would be in the middle of the map. This line is dropped. 
    * Convert this block with the editor to
    
            id,WKT
            1,"POLYGON((219 86, 1842 121, 3466 90, 3533 1842, 3598 3594, 1835 3629, 74 3591, 147 1839, 219 86))"
        
    * Save these 2 lines to a new file with filename `001m--m36--(1989)_2.shp`.
    * Start QMT and open the cut map tool in QMT.
    * Load `001m--m36--(1989).gif` into the cut tool.
    * Select the `Load cut mask from shape file` icon in the toolbar and load the file `001m--m36--(1989)_2.shp`.
    * The map window shows now a cut mask with 8 cut points (4 points in the corners, 4 points in the middle of the 4 edges of the map). 
    
        ![Using shape file](QMapTool/images/CutMask2.jpg "Use of a more precise cut mask")
      
        This mask is more precise than the one obtained in the first approach. If necessary, improve the cut mask manually as described on this page.
        
    * Click `Start` to create a new map file which is displayed without the boundary area.
      
      
      
          
          
    
    
    
        



- - -
[Prev](OverviewTool) (Overview tool) | [Home](QMTHome) | [Manual](QMTDocMain) | [Index](QMTAxAdvIndex) | [Top](#) | (Reference tool) [Next](ReferenceTool)
