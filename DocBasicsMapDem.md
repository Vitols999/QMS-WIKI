[Prev](DocInstallMapDem) (Install Maps & DEM Data) | [Home](Home) | [Manual](DocMain) | [Index](AxAdvIndex) | (Control maps and DEM files) [Next](DocControlMapDem)
- - -

***Table of contents***

* [Basic knowledge about maps and DEM files](#basic-knowledge-about-maps-and-dem-files)
    * [Map formats](#map-formats)
        * [Vector Maps](#vector-maps)
        * [Raster Maps](#raster-maps)
        * [Online Maps](#online-maps)
        * [DEM Files](#dem-files)
    * [Projection and Scaling](#projection-and-scaling)
    * [GDAL *.vrt Maps](#gdal-vrt-maps)
    * [WMTS Maps](#wmts-maps)
    * [TMS Maps](#tms-maps)
    * [Mapsforge Maps](#mapsforge-maps)

* * * * * * * * * *
 
# Basic knowledge about maps and DEM files

## Map formats

QMapShack supports the following map formats:

### Vector Maps

 Ext.   | Comment
--------|-------------
.img    | Garmin Map Images. This must be the same container files as used on the devices (often named gmapsupp_*.img). Garmin map images consisting of several mapsets (required for older Garmin devices) can be used only if all included mapsets use the same type file. Freely available software tools can be used to find the properties of a map image container and to create map images with just 1 mapset from map image containers with several mapsets. A collection with a \*tdb file and several \*img map tile files won't do.


### Raster Maps

 Ext.   | Comment
--------|-------------
*.vrt   | GDAL Virtual File. This is a wrapper format for all files supported by GDAL. (see details below)
*.jnx   | Garmin Birds Eye.
*.rmap  | CompeGPS Map Container. Just a very reduced feature set is supported. The tile format must be JPEG. The projection can be Mercator or Gauss Krueger 4/3
*.gemf  | [Map file format](https://www.cgtk.co.uk/gemf "Description of GEMF file format") that is mainly used with the mobile phone [Osmdroid app](https://github.com/osmdroid/osmdroid "Osmdroid homepage").

### Online Maps

 Ext.   | Comment
--------|-------------
*.wmts | The WMTS server's WMTSCapabilities.xml sheet renamed to a unique name. (see details below)
*.tms | This is a small XML file to define all data needed to access TMS serves. (see details below)

### DEM Files

 Ext.   | Comment
--------|-------------
*.vrt | GDAL Virtual File. This is a wrapper format for all files supported by GDAL. (see details below)


## Projection and Scaling

The default basic projection used by QMapShack is Mercator. The geographic datum is WGS84. However, you can use maps with different projections and datums as QMapShack will re-project them on-the-fly. The same applies to the scale.
QMapShack uses a fixed logarithmic scale. All maps will be re-scaled to this scale on-the-fly.

It is also possible to change the basic projection via "View->Setup Map Workspace".

## GDAL *.vrt Maps

All raster maps handled by GDAL have to be wrapped by a virtual map. You can do this with _gdalbuildvrt_.
A virtual map can contain one or several map files (you can replace \*.tif with any other extension supported by GDAL, e.g. \*.hgt).

    gdalbuildvrt My_Map_Name.vrt path1/file1.tif path2/file2.tif

If you have a lot of files you can use wildcards:

    gdalbuildvrt My_Map_Name.vrt path1/*.tif

If you use the wacky console of Windows you have to do this in two steps:

    for %f in (*.tif) DO echo %f >> hgt_list.txt
    gdalbuildvrt My_Map_Name.vrt -input_file_list hgt_list.txt

You can define a no data value, too. This is quite useful for DEM data that does not cover a complete rectangular area:

    gdalbuildvrt -vrtnodata 32767  ASTER_GDEM2_Europe.vrt europe/*.tif

**Important:** All files must have the same color mode and the same projection/datum/scaling.

If the files are large it will take a lot of memory and time to display them in the outer zoom levels.
You might consider to use gdaladdo to add overview levels to the files.

    gdaladdo My_Map_Name.vrt 2 4 8 16

This will create a file _My_Map_Name.vrt.ovr_ next to _My_Map_Name.vrt_ containing scaled overviews by factor
_2 4 8 16_.


## WMTS Maps

A Web Map Tile Service (WMTS) is a standard protocol for serving pre-rendered georeferenced map tiles over the Internet (says Wikipedia). The capabilities of a WMTS server are defined in an XML document named WMTSCapabilities.xml. It can be found on the server:

    http://<server_address>/<optional_path>/1.0.0/WMTSCapabilities.xml

For example there is a variety of free worldwide WMTS map from [Arcgis](http://services.arcgisonline.com/arcgis/rest/services). The capability sheet of the topo map can be found at:

    http://services.arcgisonline.com/arcgis/rest/services/World_Topo_Map/MapServer/WMTS/1.0.0/WMTSCapabilities.xml

Or satellite images:

    http://services.arcgisonline.com/arcgis/rest/services/World_Imagery/MapServer/WMTS/1.0.0/WMTSCapabilities.xml

To use the map you download the XML file and rename it, let's say: _World_Topo.wmts_. Move the file into QMapShack's map path and you can use the map on-line.

For some servers, the "capabilities" XML sheet may need some hand tuning (comparing with the above working ones from Arcgis may greatly help in fixing it). For example, there is some detailed info about French IGN WMTS server in the ["maps tips & tricks"](DocMapsTipsOnline) section.

If your WMTS provider needs some custom HTTP headers you can specify them in the XML file :

```xml
<?xml version="1.0" encoding="UTF-8"?>
...
<Capabilities>
...
    <Contents>
        ...
        <RawHeader>
            <Value name="User-Agent">Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0</Value>
        </RawHeader>
        ...
    </Contents>
</Capabilities>
```

## TMS Maps

To access TMS servers you have to define a few properties via XML file.  This is an example for definition file with two layers.

```xml
<TMS>
 <Title>OSM D-Land TK 50</Title>
 <MinZoomLevel>3</MinZoomLevel>
 <MaxZoomLevel>18</MaxZoomLevel>
 <Layer idx="0">
  <Title>Open Topo Map</Title>
  <ServerUrl>http://a.tile.opentopomap.org/%1/%2/%3.png</ServerUrl>
  <MinZoomLevel>3</MinZoomLevel>
  <MaxZoomLevel>11</MaxZoomLevel>
 </Layer>
 <Layer idx="1">
  <Title>Trails</Title>
  <ServerUrl>http://tile.waymarkedtrails.org/hiking/%1/%2/%3.png</ServerUrl>
  <MinZoomLevel>3</MinZoomLevel>
  <MaxZoomLevel>9</MaxZoomLevel>
 </Layer>
 <RawHeader>
   <Value name="User-Agent">Whatever</Value>
 </RawHeader>
 <Copyright>Map data: (c) OpenStreetMap contributors, ODbL | Rendering: (c) OpenTopoMap, CC-BY-SA | Trails by tile.waymarkedtrails.org </Copyright>
</TMS>
```

`<Title>`: This tag is currently of no use and just for backward compatibility to QLandkarte

`<Copyright>`: A copyright notice for the maps displayed.

`<RawHeader>`: An optional list of name/value pairs to be inserted into the HTTP header of the request. Some servers want to see special value here.
Example:

```xml
<RawHeader>
<Value name="User-Agent">Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36</Value>
</RawHeader>
```

`<MinZoomLevel>`: Can be 0..17. 0 is the most detailed level. Below this level tiles from the specified level will be taken and scaled.

`<MaxZoomLevel>`: Can be 1..18. 1 is the most detailed level. Above this level the map will not be drawn.

MinZoomLevel and MaxZoomLevel will be taken as default for the layers. _Note_: zoom level = 18 - map level

`<Layer idx="0">`: Specifies a layer. **idx** gives the order to display layers. 0 is first.

On each layer you can define:

`<Title>`: A name for the layer. If no title is given, "Layer" with the index number is used.

`<ServerUrl>`: This is the servers URL with placeholders. %1 is for the map level (z), %2 for the column (x) and %3 for the row (y). If the URL contains special characters, you have to escape them according to the HTML specification, e.g. `&` becomes `&amp;`

`<MinZoomLevel>`: Override the default MinZoomLevel for this layer. Can be 0..17. 0 is the most detailed level. Below this level tiles from the specified level will be taken and scaled.

`<MaxZoomLevel>`: Override the default MaxZoomLevel for this layer. Can be 1..18. 1 is the most detailed level. Above this level the map will not be drawn.

Next to the normal TMS naming scheme for URLs the URL can be formed by a bit of JavaScript. Here is an example for Microsoft's Bing:

```xml
<TMS>
<Title>Bing</Title>
<Layer idx="0">
<Script><![CDATA[
(
function convert(z1, x1, y1)
{
  serverpart = 0
  serverpart = (serverpart + 1) % 4;
  function encodeQuadTree(zoom, tilex, tiley)
  {
    var tileNum = []
    for (var i = zoom - 1; i >= 0; i--)
    {
      var num = (tilex % 2) | ((tiley % 2) << 1);
      tileNum[i] = new String(num);
      tilex >>= 1;
      tiley >>= 1;
    }
    return tileNum.join("");
  }
  return "http://ecn.t" + serverpart + ".tiles.virtualearth.net/tiles/a" + encodeQuadTree(z1,x1,y1) + ".jpeg?g=1036";
}
)
]]></Script>
</Layer>
<Copyright>Microsoft - Bing</Copyright>
</TMS>
```

Instead of a `<ServerUrl>`: the layer has a `<Script>`: tag with JavaScript code.

## Mapsforge Maps

Whilst QMapShack doesn't support Mapsforge maps (i.e. from [openandromaps.org](https://www.openandromaps.org/)), you can use a local tile server and a TMS file to display the maps nevertheless.

To set up the tile server, you have to download (or clone) the [mapsforgesrv with gradle repository](https://github.com/telemaxx/mapsforgesrv_with_gradle) and copy the contents of the `jars_ready2use` folder to an easily accessible path. You can delete the rest.

Now download some map of interest into any folder that suits you. To conveniently start the tile server create a .cmd file where you copied the contents of `jars_ready2use` and add this as contents:

```cmd
java -jar MapsforgeSrv.jar -m \path\to\map
pause
```

Double-click the .cmd file to start tileserver, you should get something like this as output:

```
MapsforgeSrv - a mapsforge tile server
no port given, using 8080
Map file: baden-wuerttemberg_ML.map
Theme: OSMARENDER
preferredLanguage, using null
2020-01-28 18:50:16.171:INFO::main: Logging initialized @531ms to org.eclipse.je
tty.util.log.StdErrLog
listening on localhost port:8080
2020-01-28 18:50:17.766:INFO:oejs.Server:main: jetty-9.4.25.v20191220; built: 20
19-12-20T17:00:00.294Z; git: a9729c7e7f33a459d2616a8f9e9ba8a90f432e95; jvm 1.8.0
_241-b07
2020-01-28 18:50:17.906:INFO:oejs.AbstractConnector:main: Started ServerConnecto
r@4387b79e{HTTP/1.1,[http/1.1]}{localhost:8080}
2020-01-28 18:50:17.911:INFO:oejs.Server:main: Started @2297ms
```

If this is successful, you can add a TMS file to your QMS map folder with following contents:

```xml
<TMS>
<Layer idx="0">
<Title>Mapname</Title>
<MinZoomLevel>3</MinZoomLevel>
<MaxZoomLevel>15</MaxZoomLevel>
<ServerUrl>http://localhost:8080/%1/%2/%3.png?textScale=1.2&amp;userScale=0.8</ServerUrl>
</Layer>
</TMS>
```

`textScale` scales the size of the text, the `userScale` scales the size of symbols (it should, it probably only does for SVG symbols). Further options are explained on the [git site of the tile server](https://github.com/telemaxx/mapsforgesrv_with_gradle).

If you want to use a different style for the map, you can download any style that does not use style menus. This is since the tile server (as of 28.01.2020) does not support style menus. From openandromaps.org you can download the `Elevate 2 (Mapsforge 0.3)` style. Again, save this file to some convenient folder and edit the contents for your .cmd file to:

```cmd
java -jar MapsforgeSrv.jar -m \path\to\map -t \path\to\style
pause
```

Alternatively, a wrapper script based on above information can make Mapsforge maps available in QMapShack, amongst others OpenAndroMaps maps. In addition, it allows for initially selecting a Mapsforge map and theme and later on switching easily map and theme while QMapShack keeps running. Script _Mapsforge_for_QMapShack.tcl_ is written in Tcl/Tk command language and is executable on Microsoft Windows and Linux operating system. Execution requires Tcl/Tk 8.6 or newer command interpreter to be installed. Tcl/Tk binaries for Microsoft Windows can be downloaded e.g. from [this repository](https://bitbucket.org/tombert/tcltk/downloads/), binaries for Linux are part of distribution and can be installed by corresponding package manager.

Update June 20th, 2020:

* Recent version of Mapsforge tile server is able to serve multiple maps. Thus adjacent maps overlap seamlessly and allow for cross-regional planning. Script has been extended to allow selecting multiple map files.  
* In addition, recent version of Mapsforge tile server now accepts Mapsforge rendertheme version 4 XML files containing styles and overlays. Unfortunately, tile server does not allow selecting a particular style nor enabling/disabling overlays. Instead of that, **all** styles and overlays contained in theme file are rendered. However, separation into different theme files, one file per style, can be derived by removing all unneeded style layers, overlay layers **and** rules from original theme file.

Update July 11th, 2020:

* Recent version of Mapsforge tile server now accepts style and a list of overlays as optional parameters. Script has been extended to allow selecting style and overlays if contained in rendertheme.   

Before using script, some script variables settings (folders, executables, ...) have to be modified to match local installation and environment. These variables are described and set at the beginning of script.

Script gets executed by command:

```cmd
wish Mapsforge_for_QMapShack.tcl
```

Select map(s), theme, style and overlays, press wrapper's _QMapShack_ button to start QMapShack and activate selected map(s) by QMapShack's maps list _Mapsforge_ item. After changing Mapsforge map(s), theme, style or overlays, first press _QMapShack_ button, then right click QMapShack's maps list and force QMapShack to reload maps.

Screenshot:

![Mapsforge_for_QMapShack](https://user-images.githubusercontent.com/62614244/87225215-a38cb700-c38b-11ea-87f0-cf8c30972ad3.png)

Script _Mapsforge_for_QMapShack.tcl_ (as of July 11th, 2020) can be downloaded from [here](https://github.com/Maproom/qmapshack/files/4906862/Mapsforge_for_QMapShack.zip).

*Hint:*

If QMapShack is showing rendered Mapsforge map a little blurred, it may help to

* first open “View -> Setup Map View” and set “Scale” to “Square”  
* then hit “symbol grid” button at upper right corner above and set “Projection” to “World Mercator (OSM)”


- - -
[Prev](DocInstallMapDem) (Install Maps & DEM Data) | [Home](Home) | [Manual](DocMain) | [Index](AxAdvIndex) | [Top](#) | (Control maps and DEM files) [Next](DocControlMapDem)
