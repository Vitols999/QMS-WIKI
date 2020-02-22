[Prev](Ubuntu-18-HowTo) (Ubuntu-18) | [Home](Home) | [Manual](DocMain) | [Index](AxAdvIndex) | (OSX) [Next](BuildOSX)
- - -

***Table of contents***

* [Compiling and Building QMapShack on Linux Mint 19.x](#compiling-and-building-qmapshack-on-linux-mint-19x)
    * [Install cmake and g++](#install-cmake-and-g)
    * [Install Qt 5.9.5](#install-qt-595)
    * [Install Git and Subversion](#install-git-and-subversion)
    * [Install C-Compiler, Make and other necessary packages](#install-c-compiler-make-and-other-necessary-packages)
    * [Install OpenGL](#install-opengl)
    * [Install GDAL and Proj4](#install-gdal-and-proj4)
    * [Install QuaZip](#install-quazip)
    * [Download and install Routino](#download-and-install-routino)
    * [Download and install QMapShack](#download-and-install-qmapshack)
    * [Run QMapShack](#run-qmapshack)

* * * * * * * * * *
 
# Compiling and Building QMapShack on Linux Mint 19.x

*This page is a translation of the German page [QMapShack & Linux Mint 19.x](https://www.mtb-touring.net/qms/qmapshack-linux-mint-19)*

To compile and build QMS carry out the following steps:

## Install cmake and g++

Run:

`sudo apt-get install cmake g++ cmake-curses-gui`


## Install Qt 5.9.5

Run:

`sudo apt-get install qt5-default qttools5-dev-tools qttools5-dev qttools5-private-dev qtwebengine5-dev libqt5sql5-mysql`

## Install Git and Subversion

Run:

`sudo apt-get install git subversion`

## Install C-Compiler, Make and other necessary packages

Run:

`sudo apt-get install gcc make libalglib-dev libc6-dev zlib1g-dev libbz2-dev libgraphics-magick-perl`


## Install OpenGL

Run:

`sudo apt-get install freeglut3 freeglut3-dev`


## Install GDAL and Proj4

Run:

`sudo add-apt-repository ppa:ubuntugis/ubuntugis-unstable`

`sudo apt-get update`

*Remark:* This adds the UbuntuGIS-unstable PPA (see [ubuntugis-unstable](https://launchpad.net/~ubuntugis/+archive/ubuntu/ubuntugis-unstable))

Run:

`sudo apt-get install gdal-bin libgdal-dev python-gdal libgeo-proj4-perl libproj-dev`

## Install QuaZip

Run:

`sudo apt-get install libquazip5-headers libquazip5-1 libquazip5-dev`

## Download and install Routino

Run:
 
`sudo apt-get install python3-dev`

Run:
 
`svn co http://routino.org/svn/trunk routino`

`cd routino`

`make`

`sudo make install`

**Note: If you see an error message when starting QMapShack stating something like `... routino lib not found ...` you have to modify the file `routino/Makefile.conf`:**

* Find line `prefix=/usr/local` (line 48) and change it to `prefix=/usr` 
* Rerun the 2 Routino building steps.

## Download and install QMapShack

Download QMS development branch from GitHub server:

`git clone https://github.com/Maproom/qmapshack.git QMapShack`

Run:

`cd QMapShack`

`git checkout dev`

`cd ..`

`mkdir build_QMapShack`

`cd build_QMapShack`

Run ccmake:

`ccmake ../QMapShack`

If the `ccmake` run stops, press **`c`** (maybe, several times) and then **`g`**.

After `ccmake` ends run:

`make`

`sudo make install`

## Run QMapShack

Type

`qmapshack`

into a console window and press `Enter`.


- - -
[Prev](Ubuntu-18-HowTo) (Ubuntu-18) | [Home](Home) | [Manual](DocMain) | [Index](AxAdvIndex) | [Top](#) | (OSX) [Next](BuildOSX)
