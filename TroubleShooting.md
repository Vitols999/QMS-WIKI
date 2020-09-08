[Prev](DocFaqMaps) (Maps) | [Home](Home) | [Manual](DocMain) | [Index](AxAdvIndex) | (Reporting a bug) [Next](ReportBugs)
- - -

***Table of contents***

* [Troubleshooting](#troubleshooting)
    * [Create a backtrace of a crash on Linux](#create-a-backtrace-of-a-crash-on-linux)
    * [Limitations of QMapShack for Windows, short: QMS](#limitations-of-qmapshack-for-windows-short-qms)
        * [Qt comes without SSL support](#qt-comes-without-ssl-support)
        * [GDAL comes without curl support](#gdal-comes-without-curl-support)
        * [GDAL comes without support for exotic formats](#gdal-comes-without-support-for-exotic-formats)

* * * * * * * * * *
 
# Troubleshooting

Since the 13-Oct-2015 development version, you can start qmapshack
with the commandline option "-f".
Then a logfile `org.qlandkarte.QMapShack.log` will be created in
the system's temporary folder.
On a Windows installation this temporary folder is
`C:\Users\your_user_name\AppData\Local\Temp`.
This logfile may give additional insight to the root cause of the trouble.

More details about restarting QMS after a data or configuration error are given in section ["What to do if QMS doesn't start"][QMSRestart].

[QMSRestart]: DocFaqConfig#what-to-do-if-qms-doesnt-start "What to do if QMS doesn't start"


## Create a backtrace of a crash on Linux

If QMapShack crashes on Linux the best you can do to help development is to send a backtrace. A backtrace is a log of the last code lines executed before the crash. Usually this contains enough hints to fix the problem fast.

To create a backtrace you have to compile QMapShack as debug version yourself. Have a look at [the getting started chapter of the wiki](DocGetQMapShack) for basic instructions.

When you do the step:


```bash
ccmake ../QMapShack
```

Change the variable CMAKE_BUILD_TYPE to *Debug*. Now start the build process with

```bash
make
```

No need to do a "make install". To create a backtrace you have to start QMapShack with the GDB debugger:

```bash
gdb bin/qmapshack
```
At gdb's commandline prompt enter 'r' to run QMapShack. Now you can provoke the crash. After the crash enter 'bt' on gdb's commandline. This will output the backtrace. Copy the lines and attach them to your bug report.



## Limitations of QMapShack for Windows, short: QMS

To limit the build and maintenance effort, the Windows binary packages
for QMS come with a restricted set of 3rd party libraries.
In particular the timely maintenance of security related libraries would
either put an unmanageable burden on your QMS Windows maintainer or add
an incalculable risk to the users (imagine what could happen if I package
a SSL library where severe bugs such as Heartbleed are not yet fixed).
Due to this limitation certain kinds of maps - in particular online maps -
will not work.

Below those restrictions are summarized and  possible workarounds are
described. Please be aware that those workarounds are on the sole risk
of the users - I cannot take responsibility in which situations they work
or not.

### Qt comes without SSL support

Qt5 binaries are delivered without SSL support due to legal restrictions in
some countries. See [qt-5-ssl](https://doc.qt.io/qt-5/ssl.html).
This may hinder some kinds of web maps (TMS, WMTS) to be downloaded properly.
As a workaround you could download the and compatible Windows SSL package
and copy the 2 DLLs libeay32.dll and ssleay32.dll to QMS home directory.
The DLLs from the following 2 sources have been reported to work:
[indy](https://indy.fulgan.com/SSL/) (download latest file `openssl-x.y.z-x64_86-win64.zip`) or
[gisinternals](https://www.gisinternals.com/query.html?content=filelist&file=release-1800-x64-gdal-1-11-4-mapserver-6-4-3.zip).
Please judge by yourself whether those sources are trustable for you and
whether they fit to your actual installation.

### GDAL comes without curl support

The default GDAL libraries come without curl support.
This may hinder some kinds of web maps to be downloaded properly.
As a workaround you could download GDAL binaries from
[gisinternals](http://download.gisinternals.com/sdk/downloads/release-1800-x64-gdal-1-11-4-mapserver-6-4-3.zip)
and then brute-force-copy the complete "bin" subdirectory including
subdirectories to the QMS home directory.

### GDAL comes without support for exotic formats

Some raster map formats (e.g. wavelet based) are not supported by the default
GDAL installation. The reasons may be various (licenses, dependencies, ...).
A possible workaround is the same as to add curl support: use the GDAL binaries
from [gisinternals](https://gisinternals.com/).

Proposals for extending the standard GDAL distribution for Windows with some additional plugins that support more raster map formats can be found
on the ["Tips & tricks for raster maps"](DocMapsTipsRasterDEM) page. 

- - -
[Prev](DocFaqMaps) (Maps) | [Home](Home) | [Manual](DocMain) | [Index](AxAdvIndex) | [Top](#) | (Reporting a bug) [Next](ReportBugs)
