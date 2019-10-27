[Prev](BuildWindowsVisualStudio2013) (Compile Instructions for Windows with VisualStudio 2013) | [Home](Home) | [Manual](DocMain) | [Index](AxAdvIndex) | (Compile Instructions for Ubuntu-14.04) [Next](Ubuntu-14.04-HowTo)
- - -

***Table of contents***

* [Compiling and Building QMapShack for Windows](#compiling-and-building-qmapshack-for-windows)
    * [Foreword](#foreword)
    * [General remarks](#general-remarks)
    * [Required tools for building and installing](#required-tools-for-building-and-installing)
    * [Compile instructions](#compile-instructions)
        * [C0.) Install Microsoft Visual Studio 2017 (short: VS2017)](#c0-install-microsoft-visual-studio-2017-short-vs2017)
        * [C1.) Compile the GDAL library, http://www.gdal.org/](#c1-compile-the-gdal-library-httpwwwgdalorg)
        * [C2.) Compile the PROJ library http://trac.osgeo.org/proj/](#c2-compile-the-proj-library-httptracosgeoorgproj)
            * [C2.1.) - for QMapShack before version 1.13.0](#c21---for-qmapshack-before-version-1130)
            * [C2.2.) - for QMapShack from version V1.13.0](#c22---for-qmapshack-from-version-v1130)
        * [C3.) Compile the routino library http://www.routino.org](#c3-compile-the-routino-library-httpwwwroutinoorg)
        * [C4.) Install Qt5.11 or above http://qt-project.org](#c4-install-qt511-or-above-httpqt-projectorg)
        * [C5.) Compile the QuaZip library https://stachenov.github.io/quazip/](#c5-compile-the-quazip-library-httpsstachenovgithubioquazip)
        * [C6.) Compile the jpeg library http://www.ijg.org/](#c6-compile-the-jpeg-library-httpwwwijgorg)
        * [C7.) Get the QMapShack source from the repository, e.g.](#c7-get-the-qmapshack-source-from-the-repository-eg)
        * [C8.) Start the CMake GUI (you did install CMake before, didn't you)](#c8-start-the-cmake-gui-you-did-install-cmake-before-didnt-you)
        * [C9.) Open the generated build\QMapShack.sln with VS2017](#c9-open-the-generated-buildqmapshacksln-with-vs2017)
    * [Creating a Windows binary installer](#creating-a-windows-binary-installer)
        * [I1.) Download the VC redistributable installer](#i1-download-the-vc-redistributable-installer)
        * [I2.) [Optional] Download libmysql.dll from mariadb](#i2-optional-download-libmysqldll-from-mariadb)
        * [I3.) [Optional] Build libraries libeay32.dll and ssleay32.dll](#i3-optional-build-libraries-libeay32dll-and-ssleay32dll)
        * [I4.) Copy all required files to intermediate directory](#i4-copy-all-required-files-to-intermediate-directory)
        * [I5.) Create the installer with NSIS(3.0b1)](#i5-create-the-installer-with-nsis30b1)
    * [TroubleShooting](#troubleshooting)
    * [Debugging with VS2013 !!!TODO Update for VS2017!!!](#debugging-with-vs2013-todo-update-for-vs2017)
        * [D1.) Set the solution configuration type to "RelWithDebInfo"](#d1-set-the-solution-configuration-type-to-relwithdebinfo)
        * [D2.) Right-click on the "qmapshack" project and open the "Properties" dialog](#d2-right-click-on-the-qmapshack-project-and-open-the-properties-dialog)
        * [D3.) Compile](#d3-compile)
        * [D4.) Run/Debug preparations](#d4-rundebug-preparations)
        * [D5.) Run/Debug](#d5-rundebug)

* * * * * * * * * *
 
# Compiling and Building QMapShack for Windows

Since QMapShack Release 1.12.0, Microsoft Visual Studio 2017 (VS2017) is needed to build QMapShack for Windows

For earlier releases, have a look at [BuildWindowsVisualStudio2013](BuildWindowsVisualStudio2013)

## Foreword

The following description explains how the QMapShack windows binaries provided for download at https://github.com/Maproom/qmapshack/releases are created.

I try to keep a balance between providing a complete but still reasonably compact description.
So, depending on the setup of your development machine (e.g. language settings) you might have to make some adaptations which may not be described here in full detail.
So please be prepared for some improvisation, e.g. when adapting path names or resolving start menu entries.

Of course, there might be other ways to create windows binaries, e.g. with other compiler tool chains. If you succeed, you are encouraged to create a build description on a separate Wiki page.


## General remarks

QMapShack for Windows (short: QMS) is build with Visual Studio 2017 as _64bit_ application.

- Ensure to have the 64bit option selected in all build steps.
- Currently, no _32bit_ version is officially supported.
  It should still be possible to build a 32bit version using analogous steps.
  But you might have problems with memory limitations on large maps and you will be on your own when it comes to bug fixing.

Throughout this description, the directory M:\lib2017 will be used for compiled libraries. Of course you can choose a different path according the set-up of your PC.

Note: You don't have to buy Visual Studio 2017. The free-of-charge Visual Studio 2017 Community-Edition works, too.

## Required tools for building and installing

- Microsoft Visual Studio 2017 (short: VS2017)
- CMake 3.15 or later, available at http://www.cmake.org/
- Qt5.11 or later from http://qt-project.org/downloads
- The mingw64 toolchain (http://mingw-w64.org) is needed to compile the routino library.
  For installation, follow the instructions at the beginning of the build_routino.bat which you can find in \msvc_64 directory
- NSIS, available at http://nsis.sourceforge.net/Main_Page
  only required if you want to create the installer

## Compile instructions

### C0.) Install Microsoft Visual Studio 2017 (short: VS2017)
Download the VS2017 installer from https://docs.microsoft.com/en-us/visualstudio/releasenotes/vs2017-relnotes
The free-of-charge Visual Studio 2017 Community-Edition is sufficient.

Install at least the "workload" packages for

  - Desktop Development with C++
  - Universal Windows Platform including?! the latest Windows 10 SDK (e.g. 10.0.16299.0)



### C1.) Compile the GDAL library, http://www.gdal.org/
Build instructions inspired by
  http://trac.osgeo.org/gdal/wiki/BuildingOnWindows,
  http://dominoc925.blogspot.de/2013/03/build-64-bit-gdal-for-windows.html

If you need support for formats such as WCS, WMS, WMTS, MBTiles: see 
[Compile the GDAL library with additional formats](BuildWindowsGdalWithAdditionalFormats)

- Download the source code of the version 2.3.1 (or latest)
  from http://trac.osgeo.org/gdal/wiki/DownloadSource or http://download.osgeo.org/gdal/ and unzip
- Create a file nmake.local next to nmake.opt, with the following lines,
  according to your build environment [my settings are given as example]
  
        #nmake.local - is included by nmake.opt

        #1. GENERAL switches to build gdal 2.3.1 with VS2017

        #1.1 MSVC_VER=1910 corresponds to Visual Studio 2017
        MSVC_VER=1910

        #1.2 GDAL_HOME specifies where the build results will be stored
        # NOTE: try to avoid path names with spaces and non-ASCII characters and in case of trouble try without quotes
        GDAL_HOME = "M:\lib2017\gdal"

        #1.3 Build for x64!
        WIN64=YES

        #2. OPTIONAL specific switches to use sqlite and CURL, thus enabling WCS, WMS, WMTS, MBTiles formats

        #2.1 SQLite Libraries
        SQLITE_INC=-IM:\lib2017\sqlite
        SQLITE_LIB=M:\lib2017\sqlite\sqlite3.lib

        #2.2 cURL
        CURL_DIR=M:\lib2017\cURL
        CURL_INC = -I$(CURL_DIR)/include
        CURL_LIB = $(CURL_DIR)/lib/libcurl.lib wsock32.lib wldap32.lib winmm.lib

        #2.3 zLIB
        ZLIB_EXTERNAL_LIB = 1
        ZLIB_INC = -IM:\lib2017\zlib\include
        ZLIB_LIB = M:\lib2017\zlib\lib\zlibwapi.lib


- On the Windows Desktop:
  select Start | All Programs | Visual Studio 2017 | VS 2017 x64 Native Tools Command Prompt.
- in the command prompt:
  change directory to the extracted GDAL source code root folder
~~~~
  nmake /f makefile.vc
  nmake /f makefile.vc devinstall
~~~~

### C2.) Compile the PROJ library http://trac.osgeo.org/proj/

#### C2.1.) - for QMapShack before version 1.13.0

(_compare_ [https://bitbucket.org/maproom/qmapshack/commits/c3f51f1bb46c8ec25b3ec02daa4b21251df01b76](https://bitbucket.org/maproom/qmapshack/commits/c3f51f1bb46c8ec25b3ec02daa4b21251df01b76))

- Download the source code of the version 5.1 (or latest)
  from http://trac.osgeo.org/proj/ and unzip it
- In nmake.opt, adapt the following lines,
  according to your build environment [my settings are given as example]
~~~~
  INSTDIR=M:\lib2017\PROJ
~~~~
- On the Windows Desktop:
  select Start | All Programs | Visual Studio 2017 | VS 2017 x64 Native Tools Command Prompt.
- in the command prompt:
  change directory to the extracted PROJ4 source code root folder:
~~~~
  nmake /f makefile.vc
  nmake /f makefile.vc install-all
~~~~

#### C2.2.) - for QMapShack from version V1.13.0

(_compare_ [https://bitbucket.org/maproom/qmapshack/commits/c3f51f1bb46c8ec25b3ec02daa4b21251df01b76](https://bitbucket.org/maproom/qmapshack/commits/c3f51f1bb46c8ec25b3ec02daa4b21251df01b76))

- Download the source code of the version 6.0 (or latest)
  from https://proj4.org/ and unzip it
- Have a look at the [installation instructions](https://proj4.org/install.html#cmake)
- Have a look at the README
    - It tells you that you have to use CMAKE to create the VS2017 solution files
    - And it tells you that you need sqlite3 *both during the build process and during runtime*
- Thus ensure that you have sqlite3 available as described in [Compile the GDAL library with additional formats](BuildWindowsGdalWithAdditionalFormats)

CMAKE configuration:

- select BUILD_LIBPROJ_SHARED (tick the box / set to TRUE/YES)
- set CMAKE_INSTALL_PREFIX to a directory where you want the files to be installed.
    - E.g. to `M:\lib2017\PROJ`
    - This directly needs also to be set in QMS copyfiles.bat as the root of files to be copied
- set all the parameters related to SQLITE with meaningful values
    - EXE_SQLITE3 must be the full file path to sqlite3.exe
    - SQLITE3_INCLUDE_DIR must be the path to the sqlite files folder
    - SQLITE3_LIBRARY must be the full file path to sqlite3.lib


- Configure
- Generate
- Open Project
- In VS20017 first run ALL_BUILD, then run INSTALL



### C3.) Compile the routino library http://www.routino.org
- Get the latest version from the SVN trunk http://www.routino.org/download/
~~~~
  svn co http://routino.org/svn/trunk routino
~~~~
Note: you might have to install TortoiseSVN or any other svn client

- Adapt, use and follow instructions found in build_routino.bat
  which you can find in \msvc_64 directory of your QMS source directory
- It may be necessary to switch off antivirus software before compilation (Avast has been reported to block compilation by one user)

### C4.) Install Qt5.11 or above http://qt-project.org
- Download the Qt5 Windows Online Installer from http://qt-project.org/downloads and run it
    - Install the MSVC 2017 64-bit component
    - Install the Qt WebEngine component

Notes: 

- QMS as of August 2018 or later needs at least Qt5.8. The Windows build has initially be tested with Qt 5.11.1 so far. Since February 2019, Qt 5.12.1 is used.
- If you prefer offline installation you can choose the right package in OFFLINE INSTALLERS section of that page

### C5.) Compile the QuaZip library https://stachenov.github.io/quazip/
- Get the latest version from the github download page https://github.com/stachenov/quazip/releases
- unzip the file
- Start the CMake GUI (you did install CMake before, didn't you)
- Enter the path to the source directory (where you unzipped the sources to)
- Enter the path where you want to build the quazip-library (should be a new directory)
- Select "Visual Studio 15 2017 Win64" and "Use default native compilers"
- add these two entries before running configure:
~~~~
CMAKE_PREFIX_PATH C:/Qt5/5.12.1/msvc2017_64    <-- this path has to match the actual Qt-installation
ZLIB_INCLUDE_DIRS C:/Qt5/5.12.1/msvc2017_64/include/QtZlib 
~~~~
- click 'configure'
  - verify no 'NOTFOUND' entries remain
- click 'generate'
- click 'open project' --> this opens the configured project in Visual studio

- in Visual Studio select the solution configuration type 'Release' or 'RelWithDebInfo' (must match the configuration used to build QMS)
- Right-Click on the ALL_BUILD project and select build to start the compilation
- the last step created subdirectories 'Release' resp. 'RelWithDebInfo' in the quazip-build-directory. Within this directory the new build quazip5.dll and lib are to be found.
- quazip-headerfiles are to be found in quazip-source-directory, subdirectory 'quazip'
- create a new directory to collect quazip binaries and includes, e.g.
~~~~
  M:\lib2017\QUAZIP
~~~~
- In that directory, create a sub-directory 'include' and there copy the quazip header files 
- In that directory, create a sub-directory 'lib' and there copy the quazip5.dll and lib files 

### C6.) Compile the jpeg library http://www.ijg.org/
Note: libjpeg is needed for qmt_map2jnx. Other parts of QMapshack may use the jpeg libraries included in Qt or GDAL.
- Get the latest version of the source code as .zip file from http://www.ijg.org/
~~~~
  http://www.ijg.org/files/jpegsr9c.zip
~~~~

- Unzip the source. You will get the directory jpeg-9c
- Read file install.txt concerning the build instructions for "Microsoft Windows, Visual Studio 2017 (v15):"
- Adapt the file makejvcx.v15 for using VS2107 instead of VS2015 not needed:
  property PlatformToolset (line 80) is already correctly set to v141
  See [PlatformToolset](https://blogs.msdn.microsoft.com/vcblog/2016/02/24/stuck-on-an-older-toolset-version-move-to-visual-studio-2015-without-upgrading-your-toolset/) for some background.
- On the Windows Desktop:
  select Start | All Programs | Visual Studio 2017 | VS 2017 x64 Native Tools Command Prompt.
- in the command prompt:
  change directory to the extracted jpeg source code root folder:
~~~~
  NMAKE /f makefile.vs  setup-v15
~~~~
- Open the solution file jpeg.sln
- Open the configuration manager (click on the list box filled with "Win32"
- create a new project platform x64 by cloning from Win32
- now build the project for x64 - Release
- create a directory structure for the header files and the resulting library, e.g.
~
  M:\lib2017\JPEG\include
  M:\lib2017\JPEG\lib
~
  - copy the files jconfig.h, jmorecfg.h, jpeglib.h to the include directory
  - copy the file jpeg.lib to the lib directory

### C7.) Get the QMapShack source from the repository, e.g.
~~~~
   git clone https://github.com/Maproom/qmapshack.git
~~~~
Note: you might have to install 
[git for Windows](https://git-scm.com/download/win), 
[TortoiseGit](https://tortoisegit.org/)
or any other [git client](https://git-scm.com/downloads).

If you want to develop for QMapshack, have a look at [DeveloperCommitCode](https://github.com/Maproom/qmapshack/wiki/DeveloperCommitCode).

### C8.) Start the CMake GUI (you did install CMake before, didn't you)
- Enter the path to the source directory (which has been created by cloning the git repository in the previous step)
- Enter the path where you want to build the binaries (should be a new directory)
- Select "Visual Studio 15 2017 Win64" and "Use default native compilers"
- Configure
    - In the first run there will be errors.
    - Now enter the directories where you have installed Qt5, GDAL,
      PROJ.4, routino and quazip, JPEG to the respective variables.
    - in addition to the usual defines for QUAZIP you may have to specify the path where zlib.h is being found. Zlib is being shipped with Qt5 but is not included within the cmake-find-files Qt does provide. (set QUAZIP_ZLIB_INCLUDE_DIR to e.g. C:/Qt/5.11.1/msvc2017_64/include/QtZlib)
    - Only change the UPDATE_TRANSLATIONS option in you know what you are doing. See the [DeveloperTranslate Wiki page](DeveloperTranslate) for details.
    - After that, Configure again.
    - Notes: 
        - In case that you only get some warnings, you anyway can try to GENERATE.
        - There appears an `ALGLIB` branch in the CMake GUI configuration data (easily visible if `grouped` checkbox is selected). This branch may have red background and shows the 2 entries `ALGLIB_INCLUDE_DIR` and `ALGLIB_LIBRARY`. Don't insert values here. After configuration there pops-up the message `Could not find ALGLIB using internal code.` When using this configuration a project `alg` is added to the project list in VisualStudio. Building the `ALL_BUILD` project compiles the project `alg`, too. If proper values are assigned to the 2 `ALGLIB` configuration entries, then there is no such `alg` project in the VS project list and `alglib` should be compiled separately.


- Generate

### C9.) Open the generated build\QMapShack.sln with VS2017
Hint: Click on the "Open Project" button in the CMake GUI or double-click on the build\QMapShack.sln in Windows Explorer

- Change solution configuration type to "Release"
- Set the qmapshack project as start project by right-clicking and selecting "Set as StartUp Project" (may not be necessary)
- Right-Click on the ALL_BUILD project and select build to start the compilation


## Creating a Windows binary installer

### I1.) Download the VC redistributable installer
  from https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads
Note: in case the redistributable files are already installed in your system,
this step is not necessary.

### I2.) [Optional] Download libmysql.dll from mariadb
  Download mariadb-10.1.34-winx64.zip (large file - ca 260MB) from
  https://downloads.mariadb.org/mariadb/10.1.34/ and extract libmysql.dll.
  Or copy libmysql.dll from an existing QMS installation
  This library is only needed at runtime for mysql/mariadb support

  Note: If you don't download/copy it, you have to comment out the respective
  lines in the copyfiles.bat and QMapShack_Installer.nsi scripts which are described
  in the next steps.

### I3.) [Optional] Build libraries libeay32.dll and ssleay32.dll

(For OpenSSL source look [here](https://www.openssl.org/source/)).

Qt5 binaries are delivered without SSL support due to legal restrictions in
some countries. See [qt-5-ssl](http://doc.qt.io/qt-5/ssl.html).
This may hinder some kinds of web maps (TMS, WMTS) to be downloaded properly.

For SSL support, the 2 DLLs libeay32.dll and ssleay32.dll from [OpenSSL](https://www.openssl.org/source/) are needed.

If you made it until here, it should not be too difficult for you to build them from source

* Download the latest source of OpenSSL 1.0.2 from [here](https://www.openssl.org/source/)
* Follow the steps from [INSTALL.W64](https://github.com/openssl/openssl/blob/OpenSSL_1_0_2-stable/INSTALL.W64) to build libeay32.dll and ssleay32.dll
* Adapt copyfiles.bat (step I.3) and QMapShack_Installer.nsi (step I.4) to deploy libeay32.dll and ssleay32.dll to the directory where QMapShack is installed.

Note: If you don't want to compile these libraries, you can also copy them from an existing QMS installation.


### I4.) Copy all required files to intermediate directory
-  Edit the file copyfiles.bat which you can find in \msvc_64 directory of
  your QMS source directory and adapt the directories
    - where you have installed Qt5
    - where your self compiled binaries of routino, GDAL and PROJ4 are
    - where the runtime libraries from mingw/msys are
    - where the libmysql.dll is
    - Path to the build directory which you have specified in the CMake GUI
-  Execute the copyfiles.bat
- The copyfiles.bat script will create a new directory "Files" which has
  exactly the same content as the final installation directory created
  by the NSIS installer will have.
- QMapShack does not have any dependencies out of its own installation
  directory. So instead of creating an NSIS installer in the next step
  you could just copy this directory to an other machine for a quick deployment
- [optional] Test whether the deployment is complete:
  double-click on Files/qmapshack.exe
  ==> QMapShack should start up and be fully operational without any restrictions

### I5.) Create the installer with NSIS(3.0b1)
- Run the QMapShack_Installer.nsi script e.g via right click on script file
  and choosing "Compile NSIS Script" from contextual menu.

Note: there also are the options to run the script on command prompt with
commandline version(makensis.exe).
Or you can start windows version (makensisw.exe) to run the script.

## TroubleShooting
If QMapShack does not behave as you expect, please have a look at the [TroubleShooting Wiki Page](TroubleShooting). If this does not help you to understand the problem, you can try to dig deeper by debugging as described in the next section.


## Debugging with VS2013 !!!TODO Update for VS2017!!!

For bug fixing you might want to run QMapShack with the VS2017 debugger.
This requires some additional configuration

### D1.) Set the solution configuration type to "RelWithDebInfo"
Note: you would expect the solution configuration "Debug" to be used.
But with "Debug" you will get a crash in pj_init_plus() shortly after
start as described in
http://stackoverflow.com/questions/19197791/projapi-gis-library-heap-overflow
The reason for this problem is currently unknown. Any help is welcome.

### D2.) Right-click on the "qmapshack" project and open the "Properties" dialog
- In C/C++->Optimization: deactivate optimization (/Od)
- In Debugging->Environment set the path such that all required .dll's are found
  (see http://stackoverflow.com/questions/2119539/visual-studio-how-to-set-path-to-dll)
  The path depends on where you have installed/compiled Qt5, gdal, proj.4, routino
  In my case this is
~~~~
  PATH=%PATH%;M:\lib2017\gdal\bin;M:\lib2017\PROJ\bin;M:\src\routino_pkg\lib;C:\Qt5\5.11.1\msvc2017_64\bin
~~~~

### D3.) Compile
- Right-Click on the ALL_BUILD project and select build to start the compilation

### D4.) Run/Debug preparations
Now you can in principle run QMapShack with the VS2017 debugger:
step through, inspect variables, see the debug output

But QMapShack expects some configuration files for gdal and routino in the
directory where it's executable is placed.
If those files are not there, you will get some strange error messages such as
"the specified XML file is not found" at startup and the functionality for
map/coordinate transformations will be limited.

The easiest way to provide these files is to copy the whole content of the
Files directory created by copyfiles.bat as described in step I2)
_except the qmapshack.exe_ to the directory where you RelWithDebInfo executable
has been created (build\bin\RelWithDebInfo).

Note: If you really copy all those files, then you can skip the step to set the
PATH as described in step D2). Alternatively you can set the path as described and
only copy all those configuration files and resources (i.e. all files which are
not .dll's + all directories)

### D5.) Run/Debug
Congratulations: all preparations finished.
Now you can _really_ start debugging!
Right click on "qmapshack" project and select Debug -> Start new instance

- - -
[Prev](BuildWindowsVisualStudio2013) (Compile Instructions for Windows with VisualStudio 2013) | [Home](Home) | [Manual](DocMain) | [Index](AxAdvIndex) | [Top](#) | (Compile Instructions for Ubuntu-14.04) [Next](Ubuntu-14.04-HowTo)
