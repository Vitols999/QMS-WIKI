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
*.gemf  | [Map file format](http://www.cgtk.co.uk/gemf "Description of GEMF file format") that is mainly used with the mobile phone [Osmdroid app](https://github.com/osmdroid/osmdroid "Osmdroid homepage").

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

Alternatively, a wrapper script based on above information can make Mapsforge maps available in QMapShack, amongst others OpenAndroMaps maps. In addition, it allows for initially selecting a Mapsforge map and theme and later on switching easily map and theme while QMapShack keeps running. Script _Mapsforge_for_QMapShack.tcl_ is written in Tcl/Tk command language and is executable on Microsoft Windows and Linux operating system. Execution requires Tcl/Tk 8.6 or newer command interpreter to be installed.

Before using script, some script variables settings (folders, executables, ...) have to be modified to match local installation and environment. These variables are described and set at the beginning of script.

Script gets executed by command:

```cmd
wish Mapsforge_for_QMapShack.tcl
```

Select map and theme, press wrapper's _QMapShack_ button to start QMapShack and activate selected map by QMapShack's maps list _Mapsforge_ item. After changing Mapsforge map or theme, first press _QMapShack_ button, then right click QMapShack's maps list and force QMapShack to reload maps.

Code of script _Mapsforge_for_QMapShack.tcl_:

```tcl
# Wrapper to make Mapsforge maps and themes available to QMapShack
# ================================================================

# -- Description of script variables ------------------------------------------
#
# qms_exe
#   Command to run QMapShack executable from command line
#   Either full qualified path of QMapShack executable
#   or name of QMapShack executable if resolved by PATH variable
# tms_folder
#   Folder containing QMapShack (Tile Map Service) online maps with suffix .tms
#   Map file Mapsforge.tms and preset file Mapsforge.ini get stored there.
#   Hence, folder must be writable!
# tiles_folder
#   QMapShack's main folder containing tiles cache subfolders of online maps
#   QMapShack will cache Mapsforge map tiles in subfolder Mapsforge
#   Subfolder has to get cleaned after changing Mapsforge map or theme
# maps_folder
#   Folder recursively searched for Mapsforge map files with suffix .map
# themes_folder
#   Folder recursively searched for Mapsforge theme files with suffix .xml
# java_exe
#   Command to run Java executable from command line
#   Either full qualified path of Java executable
#   or name of Java executable if resolved by PATH variable
# server_jar
#   Full qualified path of local Mapsforge tiles server jar file
#   MapsforgeSrv.jar contained in downloaded folder jars_ready2use
# tcp_port
#   TCP port for communication between Mapsforge tiles server and QMapShack
#   (49152 <= port <= 65535)
# user_scale
#   Resizes the symbols on the map rendered by tiles server
# text_scale
#   Resizes the labels on the map rendered by tiles server
# tile_size
#   Pixels per direction on map, will be resized to 256 pixels on output
#   (Default: 256, i.e. no pixel resizing required)
# transparent
#   "false" ... Tile background should be rendered using a solid color
#   "true"  ... Tile background should be rendered using the PNG transparency
# language
#   Preferred Mapsforge map language
#   (2 character country code "en", "de" etc. or "" for Mapsforge default)
#
# -- End of description -------------------------------------------------------

# -- Begin of variables settings section --------------------------------------
# == Please adjust variables settings to your installation and environment! ===

# Operating system Microsoft Windows variables settings 

if {$tcl_platform(os) == "Windows NT"} {
  set qms_exe       "C:/Program Files/QMapShack/qmapshack.exe"
  set tms_folder    "D:/Data/QMapShack/Onlinemaps"
  set tiles_folder  "D:/Data/QMapShack/Tilescache"
  set maps_folder   "D:/Data/Mapsforge/maps"
  set themes_folder "D:/Data/Mapsforge/themes"
  set java_exe      "java"
  set server_jar    "C:/Program Files/MapsforgeServer/jars_ready2use/MapsforgeSrv.jar"
}

# Operating system Linux variables settings

if {$tcl_platform(os) == "Linux"} {
  set qms_exe       "/usr/local/bin/qmapshack"
  set tms_folder    "~/QMapShack/Onlinemaps"
  set tiles_folder  "~/.QMapShack"
  set maps_folder   "/mnt/hgfs/D/Landkarten/Mapsforge/maps"
  set themes_folder "~/Mapsforge/themes"
  set java_exe      "java"
  set server_jar    "~/MapsforgeServer/jars_ready2use/MapsforgeSrv.jar"
}

# Operating system independent variables settings

set tcp_port      60815
set user_scale    0.75
set text_scale    1.25
set tile_size     256
set transparent   "false"
set language      ""

# -- End of variables settings section ----------------------------------------

# Console window for script debugging on Windows operating system
# Uncomment for debugging purpose only!

# catch {console show}

# Configure toplevel window

wm withdraw .
wm title . "Mapsforge for QMapShack"
wm protocol . WM_DELETE_WINDOW "set action 0"
wm resizable . 0 0
. configure -borderwidth 5
bind Toplevel <Visibility> {update idletasks}

set cwd [pwd]

# Show error message procedure

proc error_message {message exit_return} {
  tk_messageBox -title [wm title .] -type ok -icon error -message $message
  eval $exit_return
} 

# Check if QMapShack already running
# and check operating system

if {$tcl_platform(os) == "Windows NT"} {
  set exe [file tail $qms_exe]
  catch {exec TASKLIST /NH /FO CSV /FI "IMAGENAME eq $exe" \
	 /FI "USERNAME eq $tcl_platform(user)"} result
  set result [split $result ","]
  if {[llength $result] == 5} {
    eval set pid [lindex $result 1]
    error_message "QMapShack already running with process id $pid" exit
  }
} elseif {$tcl_platform(os) == "Linux"} {
  set exe [file tail $qms_exe]
  set rc [catch {exec pgrep -u $tcl_platform(user) $exe} result]
  if {$rc == 0} {
    set pid $result
    error_message "QMapShack already running with process id $pid" exit
  }
} else {
  error_message "Operating system $tcl_platform(os) not supported" exit
}

# Recursively find files procedure

proc find_files {folder pattern} {
  set list [glob -nocomplain -directory $folder -type f $pattern]
  foreach subfolder [glob -nocomplain -directory $folder -type d *] {
    set list [concat $list [find_files $subfolder $pattern]]
  }
  return $list
}

# Get list of available Mapsforge maps

cd $maps_folder
set maps_list [find_files "" "*.map"]
cd $cwd

if {[llength $maps_list] == 0} {
  error_message "No Mapsforge map found" exit
}

# Get list of available Mapsforge themes
# and add (empty) Mapsforge built-in default theme

cd $themes_folder
set themes_list [find_files "" "*.xml"]
lappend themes_list ""
cd $cwd

# Remember previous Mapsforge map and theme from file Mapsforge.ini

namespace eval setting {}
set fd [open "$tms_folder/Mapsforge.ini" a+]
fconfigure $fd -buffering full -buffersize 65536
seek $fd 0
while {[gets $fd line] != -1} {
  set value ""
  if {[scan $line "%\[^.\].%s\t%\[^\t\]" name1 name2 value] != -1} {
    if {$name1 == "setting"} {
      set name ${name1}::${name2}
      set $name $value
    }
  }
}
close $fd

# Header

eval [concat {font create title_font} [font configure TkDefaultFont] \
	{-underline 1 -weight bold}]
label .title -anchor w -text [wm title .] -font title_font
pack .title -expand 1 -fill x

# Mapsforge map selection

label .maps_folder_label -anchor w -text "Mapsforge maps folder:"
entry .maps_folder_entry -textvariable maps_folder -state readonly -width 0
label .maps_list_label -anchor w -text "Mapsforge map:"
ttk::combobox .maps_list_combo -state readonly -takefocus 0 \
	-textvariable setting::map \
	-values [lmap index $maps_list {file rootname $index}]
if {[.maps_list_combo current] < 0} {.maps_list_combo current 0}
foreach widget {.maps_folder_label .maps_folder_entry \
	.maps_list_label .maps_list_combo} {
  pack $widget -expand 1 -fill x
}

# Mapsforge theme selection

label .themes_folder_label -anchor w -text "Mapsforge themes folder:"
entry .themes_folder_entry -textvariable themes_folder -state readonly -width 0
label .themes_list_label -anchor w -text "Mapsforge theme:"
ttk::combobox .themes_list_combo -state readonly -takefocus 0 \
	-textvariable setting::theme \
	-values [lmap index $themes_list {file rootname $index}]
if {[.themes_list_combo current] < 0} {.themes_list_combo current 0}
foreach widget {.themes_folder_label .themes_folder_entry \
	.themes_list_label .themes_list_combo} {
  pack $widget -expand 1 -fill x
}

# Action buttons

frame .buttons
button .buttons.continue -text "QMapShack" -width 12 -command {set action 1}
button .buttons.cancel -text "Finish" -width 12 -command {set action 0}
pack .buttons -ipady 5
pack .buttons.continue .buttons.cancel -side left
bind Button <Return> {%W invoke}

# Hint

append hint "Hint:\n"
append hint "After changing Mapsforge map or theme\n"
append hint "first press QMapShack button above\n"
append hint "then right click QMapShack's maps list\n"
append hint "and force QMapShack to reload maps!\n"
label .hint -text $hint
pack .hint

# Display windows

update idletasks
wm state . normal

# Wait for selection or finish

vwait action
if {$action == 0} {exit}
unset action

# Hide toplevel window

wm state . iconic
update idletasks

# Create Mapsforge.tms file as QMapShack online map

set fd [open "$tms_folder/Mapsforge.tms" w]
puts $fd "<TMS>"
puts $fd "<Layer idx=\"0\">"
puts $fd "<Title>Mapsforge</Title>"
puts $fd "<MinZoomLevel>3</MinZoomLevel>"
puts $fd "<MaxZoomLevel>15</MaxZoomLevel>"
append url "http://localhost:$tcp_port/%1/%2/%3.png"
append url "?textScale=$text_scale"
append url "&amp;userScale=$user_scale"
append url "&amp;transparent=$transparent"
append url "&amp;tileRenderSize=$tile_size"
puts $fd "<ServerUrl>$url</ServerUrl>"
puts $fd "</Layer>"
puts $fd "</TMS>"
close $fd

# Process start procedure

proc process_start {command process} {

  set rc [catch {open "| $command 2>@1" w+} result]
  if {$rc} {
    error_message "$result" return
    after 0 {set action 0}
    return
  }

  namespace eval $process {}
  namespace upvar $process fd fd

  set fd $result
  fconfigure $fd -blocking 0 -buffering line -translation crlf

  append script "if {\[gets $fd line\] >= 0} {puts \$line};"
  append script "if {\[eof $fd\]} {"
  append script "  close $fd;"
  append script "  namespace delete $process;"
  append script "  set ::action 0;"
  append script "}"
  fileevent $fd readable $script

}

# Process stop procedure

proc process_stop {process} {

  if {! [namespace exists $process]} {return}

  namespace upvar $process fd fd
  set pid [pid $fd]
  fileevent $fd readable ""
  close $fd
  namespace delete $process

  if {$::tcl_platform(os) == "Windows NT"} {
    catch {exec TASKKILL /F /PID $pid}
  } elseif {$::tcl_platform(os) == "Linux"} {
    catch {exec kill -SIGTERM $pid}
  }

}

# Mapsforge tiles server start procedure

proc server_start {} {

  lappend command $::java_exe -jar [file normalize $::server_jar]
  lappend command -p $::tcp_port
  set map [lindex $::maps_list [.maps_list_combo current]]
  set map "[file normalize $::maps_folder]/$map"
  lappend command -m $map
  set theme [lindex $::themes_list [.themes_list_combo current]]
  if {$theme != ""} {
    set theme "[file normalize $::themes_folder]/$theme"
    lappend command -t $theme
  }
  if {$::language != ""} {lappend command -l $::language}

  process_start $command server

}

# QMapShack start procedure

proc qms_start {} {

  lappend command $::qms_exe --no-splash --style fusion 

  process_start $command qms

}

# Start Mapsforge tiles server

server_start

# Start QMapShack

qms_start

# Wait for new selection or finish

update idletasks
vwait action

# After changing Mapsforge map or theme:
# Stop tiles server, clear tiles cache folder, restart tiles server

while {$action == 1} {
  unset action
  process_stop server
  catch {file delete -force "$tiles_folder/Mapsforge"}
  server_start
  update idletasks
  wm state . iconic
  vwait action
}
unset action

# Stop Mapsforge tiles server

process_stop server

# Stop QMapShack

process_stop qms

# Delete file Mapsforge.tms and Mapsforge tiles cache folder

catch {file delete -force "$tms_folder/Mapsforge.tms" "$tiles_folder/Mapsforge"}

# Save current Mapsforge map and theme to file Mapsforge.ini

set fd [open "$tms_folder/Mapsforge.ini" a+]
fconfigure $fd -buffering full -buffersize 65536
set get 0
set put 0
while {1} {
  seek $fd $get
  if {[gets $fd line] == -1} {break}
  set get [tell $fd]
  if {[scan $line "%\[^.\].%s" name1 name2] != -1} {
    if {$name1 != "setting"} {
      seek $fd $put
      puts $fd "$line"
      set put [tell $fd]
    }
  }
}
seek $fd $put
foreach name [info vars setting::*] {
  set value [set $name]
  regsub {^::setting::} $name {} name
  puts $fd [format "setting.%s\t%s" $name $value]
}
chan truncate $fd
close $fd

# Done

destroy .

exit
```

- - -
[Prev](DocInstallMapDem) (Install Maps & DEM Data) | [Home](Home) | [Manual](DocMain) | [Index](AxAdvIndex) | [Top](#) | (Control maps and DEM files) [Next](DocControlMapDem)
