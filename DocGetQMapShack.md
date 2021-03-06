[Prev](DocMain) (Manual) | [Home](Home) | [Manual](DocMain) | [Index](AxAdvIndex) | (Windows with VisualStudio 2013) [Next](BuildWindowsVisualStudio2013)
- - -

***Table of contents***

* [Install QMapShack](#install-qmapshack)
    * [Windows](#windows)
    * [OS X](#os-x)
    * [Linux](#linux)
        * [From distribution's package system](#from-distributions-package-system)
        * [From Source](#from-source)
            * [Prerequisites](#prerequisites)
            * [Obtaining the Source](#obtaining-the-source)
            * [Compiling and Installing](#compiling-and-installing)

* * * * * * * * * *
 
# Install QMapShack

## Windows

For 64-bit Windows there is a binary installer available [in the download section](https://github.com/Maproom/qmapshack/releases).
There is also an outdated version for 32 bit Windows. To get up-to-date 32 bit binaries it needs someone maintaining it.

**Hint:** *Never use non-ASCII characters in installation directory names (limitation due to external packages used by QMapShack)!*

If you want to compile QMapShack for Windows have a look at ["Compiling and Building QMapShack for Windows"](BuildWindowsVisualStudio) in the source tree.

## OS X

A binary bundle is available [in the download section](https://github.com/Maproom/qmapshack/releases).
The binary is build with compatibility for Mac OS X 10.14 and later. 

The application can also be installed through cask (homebrew addition).
Installing homebrew and cask, if not already done:

    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    brew install caskroom/cask/brew-cask

Installing QMapShack (latest provided version):

    brew cask install qmapshack

Update QMapShack to the latest version:

    brew cask install qmapshack --force
    
Additional instructions about how to install can be found [here](BuildOSX)    

## Linux

**Check out your distribution's package system. Probably there is a binary package already.**


### From distribution's package system

Many distributions come with a prebuilt version of QMapShack.

Installing via official repository is the preferred way of installing QMapShack.
Below a (non-exhaustive) list of Linux Distributions shipping QMapShack:

* [Debian](https://packages.debian.org/testing/qmapshack)
* [Ubuntu](https://packages.ubuntu.com/xenial/qmapshack)
* [OpenSUSE](https://software.opensuse.org/package/qmapshack)
* [Downloads for Linux (deb, eopkg, rpm, txz, xz, zst) from pkgs.org](https://pkgs.org/download/qmapshack)

Refer to your distribution's manual on how to install packages using the package system.

### From Source

#### Prerequisites

To compile QMapShack, you need to have installed:

* [Qt5](https://www.qt.io/) (at least 5.8)
* [GDAL](https://gdal.org/)
* [Proj4](https://github.com/OSGeo/PROJ/wiki)
* [Routino](http://www.routino.org/) (at least 3.1)
* [QuaZip](http://quazip.sourceforge.net/index.html)
* CMake/Make
* a C++ compiler (supporting C++11)

Prefer installing those dependencies via the distribution's package system.
You also need to **install the development packages** in order to build QMapShack

Additional instructions about how to install can be found

* [here](Ubuntu-14.04-HowTo) for Ubuntu-14-04,
* [here](Ubuntu-HowTo) for Ubuntu-18 and Ubuntu 20,
* [here](BuildLinuxMint19) for Linux Mint 19.

#### Obtaining the Source

The **latest stable release** [can be downloaded here](https://github.com/Maproom/qmapshack/releases).
You have to download and unpack the \*tar.gz files.


Keep in mind: **_The cutting edge may be less stable and/or contain bugs_**

Clone the QMapShack repo into a folder QMapShack by executing:

    git clone https://github.com/Maproom/qmapshack.git QMapShack

To update the code to the cutting edge change to the folder `QMapShack` and execute:

    git pull
   

#### Compiling and Installing

Create a new directory `build_QMapShack` parallel to the source directory (if it does not yet exist)

    mkdir build_QMapShack

And run:

    cd build_QMapShack
    cmake ../QMapShack
    make


And install the application with:

    sudo make install

- - -
[Prev](DocMain) (Manual) | [Home](Home) | [Manual](DocMain) | [Index](AxAdvIndex) | [Top](#) | (Windows with VisualStudio 2013) [Next](BuildWindowsVisualStudio2013)
