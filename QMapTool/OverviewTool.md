[Prev](InstallSetup) (Installation and setup) | [Home](QMTHome) | [Manual](QMTDocMain) | [Index](QMTAxAdvIndex) | (Cut tool) [Next](CutTool)
- - -
[TOC]
- - -

# The overview tool

Raster map files can have a considerable size. Loading and rendering them on different zoom levels can therefore take some time. The overview tool helps to add
overview maps on different zoom levels to a given map file. Overviews are reduced views of the input image for display at a lower 
resolution. These overviews are smaller and thus loaded and rendered much quicker than the original map. 
If the map with overviews is used
with QMapShack, then the map is rendered on more (or even all) zoom levels (due to the heavy computational load huge maps without overviews are rendered in QMS
only on reasonable zoom levels).

Overviews can be included within the map image file itself or can be built as secondary external files.

## Basic information

To add map overviews proceed as follows:

1. Select the menu entry `Window - Shell` to open the QMT shell window (docked window, can be moved on the desktop).
1. Click the `Add overviews` button in the QMT `Tools` window  to open the overview tool.
1. Click the `Open` (`Add map files to list`) icon (![](QMapTool/images/PathBlue.png)) and select a raster map. The raster map is loaded into the QMT map window.
1. Select up to 6 zoom levels for which overviews should be created. _Remark:_ The selected value is used as reduction factor for the original image size.
1. Select the `Overview as external file` checkbox (the overview file has an additional `OVR` extension added to the map file name, this file is a multipage TIFF file, 
   its pages can be checked/rendered in an image viewer). 
1. Click the `Start` button to create the overview file.
1. The shell window (if activated) shows the used GDAL commands and the progress of the operation.


![Overview tool](QMapTool/images/OverviewTool.jpg "Overview tool")

_Remark:_ In the 3 other QMT tools (cut tool, overview tool, reference tool) a `Create overviews ...` option is available. This is necessary because there is no fixed order of
  using these tools. When one of these tools calls GDAL for some operation, then GDAL doesn't read the overview information contained in the raster map file. Thus, overview 
  information should be recreated after such a GDAL operation and this is supported in each of the tools.

## More details   

* In addition to the basic steps described in the previous section some more actions with maps can be carried out in the overview tool:

    | Icon | Tooltip |
    |------|---------|
    | ![](QMapTool/images/DeleteOne.png) | Remove selected (map) file from the list |
    | ![](QMapTool/images/DeleteMultiple.png) | Clear complete list of map files | 
    | ![](QMapTool/images/Reload.png) | Reload the currently selected map | 

* If the `Remove` checkbox is selected, then the overviews are removed from the map file.
* It is possible to open several map files. If the checkbox `For all files` at the bottom of the tool is checked, then the required action (create or remove overview)
  is carried out for each of the loaded map files.
* A call to the `gdalinfo` tool of the GDAL package (on Windows installed together with QMT) reveals if a raster map file includes overviews:


        gdalinfo.exe ETH_AA.png
        
        Driver: PNG/Portable Network Graphics
        Files: d:\GPS\Maps\ETH_AA.png
               d:\GPS\Maps\ETH_AA.png.ovr
        Size is 1920, 1080
        Coordinate System is ''
        Image Structure Metadata:
          INTERLEAVE=PIXEL
        Corner Coordinates:
        Upper Left  (    0.0,    0.0)
        Lower Left  (    0.0, 1080.0)
        Upper Right ( 1920.0,    0.0)
        Lower Right ( 1920.0, 1080.0)
        Center      (  960.0,  540.0)
        Band 1 Block=1920x1 Type=Byte, ColorInterp=Red
          Overviews: 960x540, 480x270
        Band 2 Block=1920x1 Type=Byte, ColorInterp=Green
          Overviews: 960x540, 480x270
        Band 3 Block=1920x1 Type=Byte, ColorInterp=Blue
          Overviews: 960x540, 480x270

  
    This result shows:
    
    * An overview file `ETH_AA.png.ovr` is attached to the given input file `ETH_AA.png`.
    * The original image size is 1920 x 1080.
    * There are 2 overview levels with image sizes 960 x 540 and 480 x 270 (used overwiew levels: 2 and 4).
  
- - -
[Prev](InstallSetup) (Installation and setup) | [Home](QMTHome) | [Manual](QMTDocMain) | [Index](QMTAxAdvIndex) | [Top](#) | (Cut tool) [Next](CutTool)
