[Prev](QMTDocMain) (Manual) | [Home](QMTHome) | [Manual](QMTDocMain) | [Index](QMTAxAdvIndex) | (Overview tool) [Next](OverviewTool)
- - -

***Table of contents***

* [Installation and Setup](#installation-and-setup)
    * [Installation ](#installation)
        * [Windows](#windows)
        * [Linux ](#linux)
    * [Running](#running)
        * [List of command-line options](#list-of-command-line-options)
    * [Setup](#setup)

* * * * * * * * * *
 
# Installation and Setup

## Installation 

### Windows

For 64-bit Windows use the [QMapShack installer binary](https://github.com/Maproom/qmapshack/releases) which installs QMapTool, too.

The Windows installer makes the following changes to environment variables:

* add the installation path to the `PATH` variable,
* set the environment variable `GDAL_DATA` to the `data` subdirectory of the installation directory (contains various `GDAL` files),
* set the environment variable `PROJ_LIB` to the `share` subdirectory of the installation directory (contains various `Proj.4` configuration files).

32-bit Windows systems are not supported.

### Linux 

Download, unpack and compile the [latest stable release from the download page](https://github.com/Maproom/qmapshack/releases). 

To compile QMapTool, you need to have installed:

* [Qt5](https://www.qt.io/) (at least 5.4)
* [GDAL](http://www.gdal.org/)
* [Proj4](https://github.com/OSGeo/proj.4/wiki)
* CMake/Make
* a C++ compiler (supporting C++11)

Prefer installing those dependencies via the distribution's package system.
You also need to **install the development packages** in order to build QMapTool.
 

## Running

To run QMapTool start `qmaptool.exe` in the selected installation path.

Windows users can go to the start menu and select `QMapShack - QMapTool` (remember: QMapTool was installed together with QMapShack!).

After starting QMapTool, the initial user interface is shown:

![QMT initial layout](QMapTool/images/QMTLayout.jpg "QMT initial layout")


### List of command-line options

The following options are available when starting QMT from the command-line:

| Switch | Parameter  | Comment                                        |
|:------:|:----------:|------------------------------------------------|
|*-f*    |            | enable debug output and write it to the file *%TEMP%\org.qlandkarte.QMapTool.log* (Windows only). |
|*-c*    |*<filename>*| read/write the configuration from/to a configuration file.|

If you start the application without the *-c* option the configuration will be stored wherever your system stores application configurations 
otherwise it is stored in *<filename>* at the end of a QMapTool run.

_Remark for Windows users:_

There is no default configuration file. Instead, the default configuration is saved in the registry branch
`HKCU\Software\QLandkarte\QMapTool`.

If the configuration file does not yet exist, then QMapTool is started with its default layout (configuration) shown at the top of this page and the 
configuration is written to the file at the end of the QMapTool run.

The configuration file keeps information about the

* setup of the user interface,
* setup of each of the available tools,
* user-defined setup values.

Configuration files are standard INI files and can be edited (be careful!).

The *-c* option is pretty handy if you start QMapTool from a memory stick and want to take your
configuration with you.


## Setup

QMapTool needs some setup to run properly. The user should carry out the following setup steps before working with QMT:

1. Select the menu item `Setup - Ext.tools` and fill in the requested paths to the GDAL package (QMT is trying to find these paths automatically):

    ![Setup of external tools](QMapTool/images/SetupExternals.jpg "Setup of external tools")
    
   _Remarks:_

   * The first 4 settings are related to GDAL tools used in QMT.
   * The last setting points to an auxiliary executable created in the QMT compiler run.
   * All the executables used in this setup are distributed with the Windows installer and are located in the QMT installation path.
    
1. Select the menu item `Setup - Setup units` and select your unit (Nautical, imperial, or metric).
1. Select the menu item `Setup - Setup coord.format` and select your favorite coordinate format.
1. Until you know how to work with QMT leave the menu entry `Setup - Show tool help` selected (this displays quite a few useful help texts for the
   available tools).
1. Select the menu entry `Window - Shell` if you want to see the progress of calls to the GDAL tools in a shell window (recommended - you can see the end of
   longer calculations).
   
   
    
- - -
[Prev](QMTDocMain) (Manual) | [Home](QMTHome) | [Manual](QMTDocMain) | [Index](QMTAxAdvIndex) | [Top](#) | (Overview tool) [Next](OverviewTool)
