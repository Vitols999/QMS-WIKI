[Prev](DocMain) (Manual) | [Home](Home) | [Manual](DocMain) | [Index](AxAdvIndex) | (Compile Instructions for Windows with VisualStudio 2013) [Next](BuildWindowsVisualStudio2013)
- - -
[TOC]
- - -

# Install QMapShack

## Windows

For 64 bit Windows there is a binary installer available [in the download section](https://bitbucket.org/maproom/qmapshack/downloads).
There is also an outdated version for 32 bit Windows. To get up-to-date 32 bit binaries it needs someone maintaining it.

If you want to compile QMapShack for Windows have a look at ["Compiling and Building QMapShack for Windows"](BuildWindowsVisualStudio) in the source tree.

## OS X

A binary bundle is available [in the download section](https://bitbucket.org/maproom/qmapshack/downloads).
The binary is build with compatibility for Mac OS X 10.5 (Leopard) and later. The build is done with the Xcode 7.0.1 and tested on OS-X 10.10.5 (Yosemite) and partly on OS-X 10.11 (El Capitan).

The application can also be installed through cask (homebrew addition).
Installing homebrew and cask, if not already done:

    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    brew install caskroom/cask/brew-cask

Installing QMapShack (latest provided version):

    brew cask install qmapshack

Update QMapShack to the latest version:

    brew cask install qmapshack --force

## Linux

**Check out your distribution's package system. Probably there is a binary package already.**


### From distribution's package system

Many distributions come with a prebuilt version of QMapShack.

Installing via official repository is the preferred way of installing QMapShack.
Below a (non-exhaustive) list of Linux Distributions shipping QMapShack:

* [Debian](https://packages.debian.org/testing/qmapshack)
* [Ubuntu](http://packages.ubuntu.com/xenial/qmapshack)
* [OpenSUSE](https://software.opensuse.org/package/qmapshack)
* [Arch](https://aur.archlinux.org/packages/qmapshack-hg/)
* [Fedora](https://admin.fedoraproject.org/pkgdb/package/rpms/qmapshack/)

Refer to your distribution's manual on how to install packages using the package system.

### From Source

#### Prerequisites

To compile QMapShack, you need to have installed:

* [Qt5](https://www.qt.io/) (at least 5.8)
* [GDAL](http://www.gdal.org/)
* [Proj4](https://github.com/OSGeo/proj.4/wiki)
* [Routino](http://www.routino.org/) (at least 3.1)
* [QuaZip](http://quazip.sourceforge.net/index.html)
* CMake/Make
* a C++ compiler (supporting C++11)

Prefer installing those dependencies via the distribution's package system.
You also need to **install the development packages** in order to build QMapShack

[Click here](Ubuntu-14.04-HowTo) for additional instructions about how to install on Ubuntu 14.04.

#### Obtaining the Source

The **latest stable release** [can be downloaded here](https://bitbucket.org/maproom/qmapshack/downloads).
You have to download and unpack the \*tar.gz files.

If you want to use the cutting edge you need _Mercurial_ to access the repository.
A GUI for _Mercurial_ is [TortoiseHg](http://tortoisehg.bitbucket.org/).

Keep in mind: **_The cutting edge may be less stable and/or contain bugs_**

Clone the QMapShack repo into a folder QMapShack by executing:

    hg clone https://bitbucket.org/maproom/qmapshack QMapShack

To update the code to the cutting edge change to the folder `QMapShack` and execute:

    hg pull
    hg update

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
[Prev](DocMain) (Manual) | [Home](Home) | [Manual](DocMain) | [Index](AxAdvIndex) | [Top](#) | (Compile Instructions for Windows with VisualStudio 2013) [Next](BuildWindowsVisualStudio2013)
