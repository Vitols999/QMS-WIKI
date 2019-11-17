[Prev](BuildWindowsVisualStudio) (Windows with VisualStudio 2017) | [Home](Home) | [Manual](DocMain) | [Index](AxAdvIndex) | (Ubuntu-14.04) [Next](Ubuntu-14.04-HowTo)
- - -

***Table of contents***

* [GDAL support for additional map formats](#gdal-support-for-additional-map-formats)
    * [zlib ](#zlib)
    * [cURL ](#curl)
    * [sqlite ](#sqlite)
    * [Additional binaries needed to compile PROJ.4 version 6](#additional-binaries-needed-to-compile-proj4-version-6)

* * * * * * * * * *
 
# GDAL support for additional map formats
 
!!!!!!!WORK IN PROGRESS Compiling and Building QMapShack for Windows / VS2107 WORK IN PROGRESS!!!!!!!

If you need GDAL support for the WCS, WMS, WMTS, MBTiles formats, then you need to compile GDAL with zlib, cURL and sqlite.

The following instructions show how to provide these dependencies.

Finally don't forget to activate the usage of those libraries in the nmake.opt from GDAL before compiling GDAL.

## zlib 

* download https://zlib.net/zlib1211.zip
* Read zlib-1.2.11\contrib\vstudio\readme.txt
* Build instructions for Visual Studio 2015 (32 bits or 64 bits)
    * Decompress current zlib, including all contrib/* files
    * Open contrib\vstudio\vc14\zlibvc.sln with Microsoft Visual C++ 2015
* as zlib-1.2.11 does not provide a .sln file for VS1017, we have to take the one for VS2015:
*    just let VS2017 convert the sln configuration
* build the zlibvc project (Release, x64)
* create a directory M:\lib2017\zlib
* create a subdirectory bin where you store the zlibwapi.dll created during build
* create a subdirectory include where you copy all the *.h files from the source
* create a subdirectory lib where you store the zlibwapi.lib created during build

## cURL 

* from https://curl.haxx.se/download.html download the latest source, e.g. curl-7.61.0.zip
* read https://curl.haxx.se/docs/install.html how to install curl and libcurl
* read curl-7.61.0\winbuild\BUILD.WINDOWS.txt
* consider to provide zlib as dependency as described in that file
* Open the VS2017 x64 command prompt, navigate to the curl-7.61.0\winbuild directory
```
  nmake /f Makefile.vc mode=dll 
  nmake /f Makefile.vc mode=dll WITH_DEVEL=M:\lib2017\curl_deps WITH_ZLIB=dll
```
* from curl-7.61.0\builds\libcurl-vc-x64-release-dll-zlib-dll-ipv6-sspi-winssl, copy the 3 sub-directories to M:\lib2017\cURL

## sqlite 

* Here we are lazy and don't compile
https://dcravey.wordpress.com/2011/03/21/using-sqlite-in-a-visual-c-application/
* Download the native SQLite DLL from: https://www.sqlite.org/2019/sqlite-dll-win64-x64-3270200.zip
* Create a directory M:\lib2017\sqlite
* Unzip the DLL and DEF files to that directory
* Open a “Visual Studio Command Prompt (2017)” and navigate to your source folder.
* Create an import library using the following command line:
```
LIB /DEF:sqlite3.def
```
* Download https://www.sqlite.org/2019/sqlite-amalgamation-3270200.zip
* Unzip the sqlite3.h header file also to M:\lib2017\sqlite

## Additional binaries needed to compile PROJ.4 version 6

To build [PROJ.4 version 6](https://proj4.org/news.html#release-notes), you need also 
the sqlite executables. See [PROJ.4 Installation instructions](https://proj4.org/install.html?highlight=sqlite#compilation-and-installation-from-source-code)

* Download https://www.sqlite.org/2019/sqlite-tools-win32-x86-3270200.zip
* Unzip the EXE files to the same directory where you placed the DLL and DEF files



- - -
[Prev](BuildWindowsVisualStudio) (Windows with VisualStudio 2017) | [Home](Home) | [Manual](DocMain) | [Index](AxAdvIndex) | [Top](#) | (Ubuntu-14.04) [Next](Ubuntu-14.04-HowTo)
