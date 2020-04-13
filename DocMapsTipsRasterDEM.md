[Prev](DocMapsTipsOnline) (Tips & tricks for online maps) | [Home](Home) | [Manual](DocMain) | [Index](AxAdvIndex) | (Data handling) [Next](AdvDataHandling)
- - -

***Table of contents***

* [Tips & tricks for raster maps, vector maps, and elevation data](#tips--tricks-for-raster-maps-vector-maps-and-elevation-data)
    * [Raster maps](#raster-maps)
        * [Russian army maps](#russian-army-maps)
        * [ECW, MBTILES and MrSID maps](#ecw-mbtiles-and-mrsid-maps)
            * [Add ECW plugin](#add-ecw-plugin)
            * [Add MrSID plugin](#add-mrsid-plugin)
            * [Updating QMS after install plugins](#updating-qms-after-install-plugins)
            * [Remarks on proprietary map formats](#remarks-on-proprietary-map-formats)
    * [Elevation data](#elevation-data)
        * [Contour lines](#contour-lines)
            * [Contour line vector map in Garmin IMG format](#contour-line-vector-map-in-garmin-img-format)
            * [Raster contour line layer](#raster-contour-line-layer)
        * [Online DEM data](#online-dem-data)
            * [DEM data from WCS (Web Coverage Service) servers](#dem-data-from-wcs-web-coverage-service-servers)
            * [European DEM data ](#european-dem-data)
    * [Vector maps for Linux systems](#vector-maps-for-linux-systems)
        * [Script](#script)
        * [Configuration](#configuration)

* * * * * * * * * *
 
# Tips & tricks for raster maps, vector maps, and elevation data

## Raster maps

### Russian army maps

[http://loadmap.net](http://loadmap.net) is a server for a wide variety of raster maps covering large parts of the world. 
Among them are various kinds of Russian army and topographic maps,
but also maps of the U.S. army map service.

Some of the maps are georeferenced with reference information in various formats. Quite often the `OziExplorer map file` format is used to keep the reference information.
A major disadvantage of such maps is a border that overlaps neighboring maps. 

To make raster maps from this source available in QMapShack the [QMapTool](https://github.com/Maproom/qmapshack/releases) can be used to reference and to cut unreferenced 
raster maps.

Referenced maps in the OziExplorer format can be prepared for QMS as follows:

* Assume the map was downloaded as `rastermap.gif` with reference information in `rastermap.map`.
* Move these 2 files into a QMS map directory.
* Use `gdalwarp` (to be found in the QMS installation directory for Windows) to convert the map to a georeferenced TIF file:

        gdalwarp rastermap.map rastermap.tif
    
* Open QMapTool (if `qmaptool.exe` is on the `PATH`, then it can be opened from QMS by choosing the menu entry `Tool - Start QMapTool`).
* Use the QMapTool to cut the map to the necessary shape. For details compare the [QMapTool documentation](https://github.com/Maproom/qmapshack/wiki/CutTool).
  The result is a new file `rastermap_cut.tif` in the QMS map directory.
* Open QMapShack and select the menu entry `Tool - VRT Builder`.  
* Insert `rastermap_cut.tif` as source file name, insert a target file name and select the creation of overviews for better rendering of the map. 
* Click the `Start` button in the tool.
* Activate the new map in QMapShack.

### ECW, MBTILES and MrSID maps

_(Updated for QMS 1.12.3  2019-02-10)_

MBTiles is a file format for storing map tiles in a single file. It is, technically, a SQLite database and my contain raster as well as vector data. Starting at QMS 1.12.0 the QMS Windows installer includes support for MBTiles files with raster data. 

ECW stands for **E**nhanced **C**ompression **W**avelet and is a proprietary wavelet compression image format optimized for aerial and satellite imagery. The lossy compression format efficiently compresses very large images with fine alternating contrast while retaining their visual quality.

MrSID stands for **M**ulti**r**esolution **S**eamless **I**mage **D**atabase. It is a file format (with filename extension .sid) for encoding of georeferenced raster graphics, such as orthophotos.

Both ECW and MrSID need some special preparation of the installed QMapShack package as described below for Windows10 64-bit systems (the approach for Linux-type systems should be similar but was not tested).

* This procedure is valid for __QMS 1.12.3__ and newer versions compiled with __GDAL 2.4__ and MSVC2017, therefore links provided pointing to `GISInternals` installers are suitable for these versions. The GISInternals installers will add some plugins to the GDAL package. 
* Previously installed ECW, MrSID, or MBTiles plugins  for  QMapshack versions prior to 1.12.3 WON'T work with newer versions. So, you have to update the plugins:
    * if you are updating from QMS 1.12.0 or newer, simply install the new plugin overwritting the old one and it will work.
    * if you are updating from a version prior to 1.12.0 and you had installed some of the plugins, is highly recommended to make a CLEAN INSTALLATION of QMS 1.12.3 or newer to get rid of files that you  had added to the root folder of QMS and no longer have utility, and then install the correct plugins as explained below.
* Pay attention to the fact that the GISinternals installers _DO NOT ASK_ for an installation path. They always write to `C:\Program Files\GDAL` (or something similar depending on your system language). Therefore, if you already have a GDAL version installed at that location for other purposes, you should rename this folder (e.g. to `GDALBAK`) before running the installers in order to preserve the old installation. Once the task is done you can delete the GDAL folder created by GISinternals installers and rename back the original GDAL folder.
* (_OPTIONAL_) You would like to make a copy of the original QMapShack root folder (e.g. to `QMapShack-BAK`). In this way you can run QMS from the folder with plugins installed, or you can run  the original one from the BAK folder without plugins. Your configuration remains the same for both of them and you could easily turn back, if you don't like the changes. 


#### Add ECW plugin

1. Download and execute this [ECW plugin installer](http://download.gisinternals.com/sdk/downloads/release-1911-x64-gdal-2-4-0-mapserver-7-2-1/gdal-204-1911-x64-ecw-33.msi) from GISinternals.
1. Go to the folder where the plugin has been installed, typically `C:\Program Files\GDAL`.
1. Copy the `gdalplugins` and `license` folders to the QMS root folder, typically `C:\Program Files\QMapShack`.
1. Copy `libecwj2.dll` to the QMS root folder.

#### Add MrSID plugin

1. Download and execute this [MrSid plugin installer](http://download.gisinternals.com/sdk/downloads/release-1911-x64-gdal-2-4-0-mapserver-7-2-1/gdal-204-1911-x64-mrsid.msi) from  GISinternals.
1. Go to the folder where the plugin has been installed, typically `C:\Program Files\GDAL`.
1. Copy the `gdalplugins` and `license` folders to the QMS root folder, typically `C:\Program Files\QMapShack`.
1. Copy  the 3 files `lti_dsdk_9.5.dll, lti_lidar_dsdk_1.1.dll, tbb.dll` to the QMS root folder.

#### Updating QMS after install plugins

* When you upgrade QMapShack from 1.12.3 to a newer version the ECW and MrSID plugins remain intact, nothing else needs to be done.

#### Remarks on proprietary map formats

* This procedure requires that the user agrees to the GISInternals terms of use when installing the plugins.
* The procedure respects the QMS folder structure created by the QMS installer.
* There is no need to set any path to the `gdalplugins` folder, so you can start QMS as usual.
* Before using the discussed raster map formats, VRT files have to be created with the help of the QMS VRT builder for each (or for all) required map files. Put the VRT file in a QMS maps path, reload the maps in QMS, and activate the map. 
* MrSID files can be rather big. Rendering them in QMS can be a time-consuming operation.
* MrSID plugin might fail depending on your Windows system installation. It seems that adding a convenient `tbb.dll` in the QMS root folder would solve the problem. [See issue #129 at GISInternals](https://github.com/gisinternals/buildsystem/issues/129). 
* Depending on the Windows 10 system installation an error message from GDAL might be shown informing that the file `ogr_MSSQLSpatial.dll` can't be found. The reason for this error is a missing Microsoft `sqlncli11.dll`. To resolve this error download the [installation package](https://www.microsoft.com/en-us/download/details.aspx?id=50402) for this DLL file from the Microsoft server and install it. After this additional installation step, the error doesn't occur anymore.



## Elevation data

The standard way of using elevation data in QMS is to download this data and save it locally (for details see [Install Maps & DEM](DocInstallMapDem)).

In this section 2 more possibilities to use elevation data in QMS are presented:

* use of contour lines in Garmin map files,
* use of online elevation data.

### Contour lines

There are two ways to add a transparent contour line layer to your map view:

* add proper vector maps in Garmin IMG format,
* add raster map with transparent contour line tiles. 

#### Contour line vector map in Garmin IMG format

Some maps for Garmin devices provide a separate `gmapsupp.img` file with contour lines. Add this file to your QMS map directory and use it as contour line overlay in a map view. Change transparency of the contour line map, if necessary.

Some sources for vector contour line maps in this format are:

* [OpenTopoMap](http://garmin.opentopomap.org/#download): Select your region and download the file in the Garmin format. The downloaded file contains both a base map and a contour line map in the `gmapsupp.img` format.
* [BBBike](https://extract.bbbike.org/?lang=en): allows to create a contour line file for a custom area.
    * Follow the instructions shown on the linked page,
    * select as output format `SRTM World Contours Garmin (40m)`,
    * after rendering the map in QMS, use the slider of the map in the QMS maps window to change transparency (opacity).
* [Velomap](https://www.velomap.org): download the .exe file and chose "install a separate contour lines only map" during the installation process. Follow the instructions in the files `information for Linux_or_QlandkarteGT_users.txt` and `readme_english.txt` in the velomap installation directory to get the required `gmapsupp.img` file.

#### Raster contour line layer

Some TMS tile servers provide contour line only layers. To use such a layer in QMS, add a TMS file to your map directory. 

Here is a sample TMS file for the contour line layer from [OpenSnowMap](http://www.opensnowmap.org) 
(download from [here](Downloads/OpenSnow_Contours.tms)):


```xml
<TMS>
 <Title>OpenSnowMap Contour Lines</Title>
 <MinZoomLevel>1</MinZoomLevel>
 <MaxZoomLevel>1024</MaxZoomLevel>
 <Layer idx="0">
     <ServerUrl>http://www.opensnowmap.org/opensnowmap-overlay/%1/%2/%3.png</ServerUrl>
 </Layer>
 <Copyright>Openstreetmap contributors | Rendering: www.opensnowmap.org | DEM: ASTER GDEM is a product of METI and NASA
SRTM V4.1 from CGIAR-CSI EU-DEM: Produced using Copernicus data and information funded by the European Union </Copyright>
</TMS>

```

Another sources for transparent contour line tiles is the OpenMapServer from GIScience at Heidelberg University with the URL
  
        <ServerUrl>http://129.206.74.245:8006/tms_il.ashx?x=%2&amp;y=%3&amp;z=%1</ServerUrl>


### Online DEM data

Downloading and preparing DEM data for offline use can be a time-consuming process that requires quite a lot of memory. In some cases it is therefore easier to avoid the preparation of DEM data for some regions and to use instead online elevation data.

#### DEM data from WCS (Web Coverage Service) servers


QMS can obtain online DEM data using a .WCS file that contains the necessary parameters to access a WCS server. 

You can get .wcs files contributed by users ([here](DocMapDemSources)) and you can also create them by yourself as described below

_Usage:_

Place the `.WCS` file in the QMS DEM path and activate it. WCS files are shown at the docked DEM window with this icon  ![WCS](images/DocBasicsMapDem/MimeDemWCS.png "WCS icon") 

The first time you load the new online elevation data it will take a while to load the data. The status line remains quiet, be patient! Once the WCS is connected the QMS status line will show the elevation and slope data on the fly, and if you don't ask to hill-shade or colorize large areas, it will run smoothly.

The use of online elevation data is complementary to the use of local DEM files. If you are using intensively hill-shading or coloring slopes, you would like to have local DEMs.

Online elevation data is useful when:

* you want to view regions outside of your usual mountain area and you don't have its DEM data,
* you  want to draw (or filter) a track with a high elevation accuracy and you don't want to find and download tons of files that you will never use again (e.g. downloading a 5m accuracy DEM for the whole of Spain would be crazy)

In these cases online elevation data work just fine. Some WCS are faster than others, you must try to find the limits, but don't ask QMS to hill-shade the whole Pyrenees with a 5m accuracy elevation on your screen. Of course, the user is required to have a brain.


_Create a basic WCS file:_

* Create a text file following this example and save it in your DEM folder with the extension .wcs (e.g. `ESP_IGN-MDT25.wcs`):

             <WCS_GDAL>
               <ServiceURL>http://www.ign.es/wcs/mdt?</ServiceURL>
               <CoverageName>mdt:Elevacion25830_25</CoverageName>
               <Version>1.0.0</Version>
             </WCS_GDAL>

* You  have to replace the values between the labels according to the WCS you want, where
    * the _ServiceURL_ node defines the URL of the service without parameters,
    * the _CoverageName_ node is the identifier for the elevation dataset (in simple words the layer),
    * the _Version_ is the WCS version that is used in the communication. If you don't know the version, try the default value 1.0.0 (read remarks about versions below).
* The given example can be used to get online elevation data from the Spanish IGN server.
* The URL of the WCS and the coverage names are usually provided  by authorities and data providers on their web sites. If you only know the WCS URL, you can try to get the   available coverage names by requesting the capabilities file in a web browser. (e.g.:  `http://www.example.com/example?request=Getcapabilities`).


_Remarks:_

* Depending on the Windows 10 system installation an error message from GDAL might be shown informing that the file `ogr_MSSQLSpatial.dll` can't be found. The reason for this error is a missing Microsoft `sqlncli11.dll`. To resolve this error download the [installation package](https://www.microsoft.com/en-us/download/details.aspx?id=50402) for this DLL file from the Microsoft server and install it (click red `Download` button, select the file `ENU\x64\sqlnclimsi`, and click the `Next` button to start the download). After this additional installation step, the error doesn't occur anymore.
* WCS version 2.0.1 is supported only starting with GDAL 2.3 which might not be installed on your system (QMS 1.12.0 for Windows is currently compiled with GDAL 2.3). Anyway, you can try to write the WCS file with default version 1.0.0 and usually it will run.
* The first time you use a basic WCS file GDAL will query the WCS server and then it will re-write your basic WCS file converting it into a longer one with more parameters. Advanced users can edit and tune this longer WCS file to choose some parameters when available (e.g. the DEM format: ASCII, Geotiff,... or the SRS).
* A complete example WCS file can be downloaded [here](Downloads/ESP_IGN-MDT25.wcs).

#### European DEM data 

Online DEM data for Europe can be obtained with the help of the following VRT file (download from [here](Downloads/Europe_Online_DEM25.vrt)):

~~~
<VRTDataset rasterXSize="288000" rasterYSize="180000">
  <SRS>GEOGCS["ETRS89",DATUM["European_Terrestrial_Reference_System_1989",SPHEROID["GRS 1980",6378137,298.257222101,AUTHORITY["EPSG","7019"]],TOWGS84[0,0,0,0,0,0,0],AUTHORITY["EPSG","6258"]],PRIMEM["Greenwich",0,AUTHORITY["EPSG","8901"]],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]],AUTHORITY["EPSG","4258"]]</SRS>
  <GeoTransform> -3.5000000000000000e+01,  2.7777777777777734e-04,  0.0000000000000000e+00,  7.5000000000000000e+01,  0.0000000000000000e+00, -2.7777777777777734e-04</GeoTransform>
  <VRTRasterBand dataType="Float32" band="1">
    <NoDataValue>nan</NoDataValue>
    <ColorInterp>Gray</ColorInterp>
    <ComplexSource>
      <SourceFilename relativeToVRT="0">/vsicurl/http://published-files.eea.europa.eu/eudem/entr_r_4258_1_arcsec_gsgrda-eudem-dem-europe_2012_rev1/eudem_dem_4258_europe.tif</SourceFilename>
      <SourceBand>1</SourceBand>
      <SourceProperties RasterXSize="288000" RasterYSize="180000" DataType="Float32" BlockXSize="256" BlockYSize="256" />
      <SrcRect xOff="0" yOff="0" xSize="288000" ySize="180000" />
      <DstRect xOff="0" yOff="0" xSize="288000" ySize="180000" />
      <NODATA>nan</NODATA>
    </ComplexSource>
  </VRTRasterBand>
</VRTDataset> 
~~~

_Usage:_

Place the downloaded `Europe_Online_DEM25.vrt` file in the QMS DEM path and activate it at the docked DEM window.
Take in mind that this is a DSM ([Digital Surface Model](https://en.wikipedia.org/wiki/Digital_elevation_model)).

## Vector maps for Linux systems

In order to use vector maps within QMS you need to create a gmapsupp.img`` file from the map tiles (if not yet available). 

The popular openmtbmap.org and velomap.org maps as well as some other ones come without such container files.

For Windows user, there is an integrated batch file, which will do all necessary steps; so this section is for Linux users. More information on this topic you may find 
[here](https://openmtbmap.org/de/tutorials/mkgmap/).

In Linux, please check, if the package `p7zip-full` is installed – we need it to unpack the .exe file. Open the console and execute *sudo apt-get install p7zip-full* . We need 
[Mkgmap](http://www.mkgmap.org.uk/), too. Also Java is required.

1. Download openmtbmap-ALPS and the latest version of mkgmap
1. Create a folder like ~/openmtbmap_alps and unzip your downloaded version
1. Open the .exe file and extract all files called 6528xxxx.img (maptiles) and 7528xxxx (contour lines), and a typ file (the layout of the map). For this sample we choose *widealp.TYP* 

The folder should now contain all map tiles, the contour lines, the layout file and the extracted files from mkgmap.

Now start your console, browse to your folder and copy the following code: 


```bash
java  -Xmx2048M -jar mkgmap.jar --index --family-id=6528 --description="openmtbmap_alps" --series-name="openmtbmap_alps" --family-name="openmtbmap_alps" --product-id=1 --gmapsupp 6*.img 7*.img widealp.TYP
```

Then press <Enter> and a gmapsupp.img will be created, which you can easily rename to opentmtbmap_alps.img. Now copy this file onto your GPS unit and in your QMapShack maps folder as well.

If you would like do it with some other layout, simply replace the *.TYP (f.e. easyalps.TYP). 
If you prefer another country, be careful: all 6x.img and 7x.img must be from the particular openmtbmap country file! Also don't forget to replace the --family-id with the one from your country.

This is really a quick way, to integrate your favorite openmtbmaps or velomaps into QMapShack.

If you prefer a GUI: you can still use QLandkarteGT for creating gmapsupp.img, too. 

Links (with further information and some tutorials):

* [openmtbmap.org](https://openmtbmap.org/)
* [velomap.org](https://velomap.org/)
* [Mkgmap](http://www.mkgmap.org.uk/)

### Script

If you want to update your maps regularly, you might consider using the script below.
The script requires the following tools to be installed:

* `wget` (downloading)
* `7z` (extraction)
* `mkgmap` (creation of gmapsupp.img)

### Configuration

The script below is configured to download the OpenMTBMap for Bavaria, convert it to `OpenMTBMap_<date>.img` using traddby.TYP and move it to `~/.qmapshack_maps/`.

If this does not match your requirements, you will need to adopt the values *FILESRC*, *IMGFMT*, *QMSMAPDIR* and *TYPE*:

* *FILESRC*: [Navigate here](http://ftp5.gwdg.de/pub/misc/openstreetmap/openmtbmap/odbl/), find the file you want to download and write the URL to *FILESRC*

* *IMGFMT*: Name of the resulting file, see `man 1 date`

* *QMSMAPDIR*: Path to your QMS-Map folder (`~` will not work, use `${HOME}` instead)

Depending on your system's configuration you will need to change *MKGMAP* to allow proper execution of `mkgmap` (see section above).


```bash
#! /bin/sh

# set -vx

# configuration

# Bavaria
FILESRC="http://ftp5.gwdg.de/pub/misc/openstreetmap/openmtbmap/odbl/germany/mtbbayern.exe"

# Baden Württemberg
# FILESRC="http://ftp5.gwdg.de/pub/misc/openstreetmap/openmtbmap/odbl/germany/mtbbaden-wuerttemberg.exe"

# Germany
# for whatever reason 7z does not finish extracting mtbgermany.exe, but there is a linux version for germany
# FILESRC="http://ftp5.gwdg.de/pub/misc/openstreetmap/openmtbmap/odbl/mtbgermanylinux.7z"

# Alps
# FILESRC="http://ftp5.gwdg.de/pub/misc/openstreetmap/openmtbmap/odbl/mtbalps.exe"

# Bremen (small, good for testing)
# FILESRC="http://ftp5.gwdg.de/pub/misc/openstreetmap/openmtbmap/odbl/germany/mtbbremen.exe"

TYPE="trad"
QMSMAPDIR="${HOME}/.QMapShack/Karten/IMG"
MKGMAP="mkgmap"

# code starts here, no changes below here required

error_check() {
	if [ $1 != 0 ]; then
		echo ${red}ERROR${NC}
		exit 1
	else
		echo ${green}OK${NC}
	fi
}

tool_check() {
	which $1 2>&1 1>/dev/null
	if [ $? != 0 ]; then
		echo ${red}ERROR: $1 missing${NC}
		exit 1
	fi
}

red="\033[0;31m"
green="\033[0;32m"
NC="\033[0m"

TMP=`mktemp`
if [ ! -f "${TMP}" ]; then
	echo ${red}ERROR: failed to get temp. file${NC}
	exit 1
fi

tool_check "wget"
tool_check "7z"
${MKGMAP} >/dev/null 2>&1
if [ $? != 0 ]; then
	echo ${red}ERROR: mkgmap can\'t be executed${NC}
	echo ${red}ERROR: make sure MKGMAP is set properly in script configuration${NC}
	exit 1
fi

echo -n " * Downloading... "
wget -q -O "$TMP" "$FILESRC"
error_check $?

echo -n " * Decompressing... "
7z e -o"${TMP}_" ${TMP} >/dev/null

# This is needed to extract the map code (e.g. by for Bavaria or bw for baden-wuerttemberg)
TYPE_FILE=$(basename ${TMP}_/${TYPE}*.TYP)
tmp=${TYPE_FILE#${TYPE}}
REGION=${tmp%\.TYP}
IMGFMT="%Y-%m-%d__${REGION}_OpenMTBMap.img"

error_check $?

FILETIME=`stat -c %Y ${TMP}`
echo $FILETIME
IMGFILE=`date -d@${FILETIME} +"${IMGFMT}"`

echo -n " * Building ${IMGFILE}... "
cd "${TMP}_"
FID=`ls -x 7*.img | head -1 | cut -c1-4`
${MKGMAP} --show-profiles=1 --product-id=1 --family-id=${FID} --index --gmapsupp 6*.img 7*.img ${TYPE_FILE} >/dev/null
error_check $?

echo -n " * Moving gmapsupp.img to ${QMSMAPDIR}... "
mv "${TMP}_/gmapsupp.img" "${QMSMAPDIR}/${IMGFILE}"
error_check $?

echo -n " * Cleanup... "
rm -rf "${TMP}" "${TMP}_"
error_check $?
```

- - -
[Prev](DocMapsTipsOnline) (Tips & tricks for online maps) | [Home](Home) | [Manual](DocMain) | [Index](AxAdvIndex) | [Top](#) | (Data handling) [Next](AdvDataHandling)
