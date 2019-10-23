[Prev](Ubuntu-14.04-HowTo) (Compile Instructions for Ubuntu-14.04) | [Home](Home) | [Manual](DocMain) | [Index](AxAdvIndex) | (Create Offline Documentation) [Next](OfflineDocumentation)
- - -
 
***Table of contents***

* [Initial build Routino and QMapShack](#initial-build-routino-and-qmapshack)
    * [Create installation folder](#create-installation-folder)
    * [Installation of needed build packages](#installation-of-needed-build-packages)
    * [Initial build of Routino](#initial-build-of-routino)
        * [Update of Routino when something has changed in future](#update-of-routino-when-something-has-changed-in-future)
    * [Initial build of QMapShack](#initial-build-of-qmapshack)
        * [Update of QMapShack when something has changed in future](#update-of-qmapshack-when-something-has-changed-in-future)
    * [Start QMapShack](#start-qmapshack)
* [Setup development environment](#setup-development-environment)

* * * * * * * * * *
 
This installation guide is based on a fresh new installation of Ubuntu 18.04.


# Initial build Routino and QMapShack

## Create installation folder
Create a installation folder for all QMS data (ex. ~/GPS) 
```
mkdir ~/GPS
cd ~/GPS
```

## Installation of needed build packages
```
sudo apt-get install cmake build-essential subversion mercurial qt5-default qttools5-dev libqt5webkit5-dev qtscript5-dev qttools5-dev-tools libgdal-dev libproj-dev libghc-bzlib-dev libgraphics-magick-perl libquazip5-dev libqt5sql5-mysql gdal-bin qtwebengine5-dev
```

**Remark:**

Starting with version 1.13.0 QMapShack requires PROJ.4 version 5.0.0 or newer. To check the PROJ.4 version installed with the above command run

    pkg-config --modversion proj
    
If necessary, an update of the PROJ.4 version can be done as follows:

* Ensure that SQLite3 is installed on your system.    
* Download the source packages `proj-5.x.0.tar.gz`  (or even `proj-6.0.0.tar.gz`) and `proj-datumgrid-1.8.zip` from the [PROJ.4 download page](https://proj4.org/download.html).
* Follow the [general installation instructions](https://proj4.org/install.html#compilation-and-installation-from-source-code) and the [Autotools installation instructions](https://proj4.org/install.html#autotools).
* To install PROJ.4 at the correct location change to the PROJ.4 source folder and call

        ./configure --prefix=/usr
        make
        sudo make install
        
    

## Initial build of Routino
```
svn co http://routino.org/svn/trunk routino
cd routino
make
sudo make install
cd ..
```
Note: If you see an error message when starting QMapShack stating something like " ... routino lib not found ..." maybe you have to modify Makefile.conf. Change line 48 from prefix=/usr/local to prefix=/usr and rerun the building steps of Routino.

### Update of Routino when something has changed in future
```
cd ~/GPS/routino
svn update
make
sudo make install
cd
```

## Initial build of QMapShack
```
hgit clone https://github.com/Maproom/qmapshack.git QMapShack
mkdir build_QMapShack
cd build_QMapShack
cmake ../QMapShack
make
sudo make install
```

### Update of QMapShack when something has changed in future
```
cd ~/GPS/QMapShack
git pull
cd ../build_QMapShack
make
sudo make install
cd
```

## Start QMapShack
```
qmapshack
```


# Setup development environment
To code at your own you can easily build a development environment by using "QtCreator" for coding. 
```
sudo apt-get install qtcreator 
```

Note:
In QtCreator you can add -jN in Project/Create/Steps/Details/Toolparammeter to speed up the compilation time. -jN specifies the number (N) of jobs to run simultaneously. You can start with -j2 and increase (-j3, -j4, ...) to the value of the optimal compilation speed depending on your CPU.

More information about developing of QMapShack will be found in chapter "Developing QMapShack" beginning [here](DeveloperCodingGuideline) and [here](DeveloperCommitCode).


- - -
[Prev](Ubuntu-14.04-HowTo) (Compile Instructions for Ubuntu-14.04) | [Home](Home) | [Manual](DocMain) | [Index](AxAdvIndex) | [Top](#) | (Create Offline Documentation) [Next](OfflineDocumentation)
