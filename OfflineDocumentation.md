[Prev](BuildOSX) (OSX) | [Home](Home) | [Manual](DocMain) | [Index](AxAdvIndex) | (Getting started) [Next](DocGettingStarted)
- - -

***Table of contents***

* [Using offline documentation](#using-offline-documentation)
    * [Introduction](#introduction)
    * [Installing and using QMS help browser](#installing-and-using-qms-help-browser)
    * [Installing and using local QMS Wiki copy](#installing-and-using-local-qms-wiki-copy)

* * * * * * * * * *
 

_(Valid as of QMapShack version 1.14.1)_

# Using offline documentation

## Introduction

The official source of help for QMapShack (QMS) is the [online QMapShack Wiki on GitHub][QMSWiki]. This Wiki includes help for QMapTool (QMT), too.
The online documentation is also available offline as

* a QMapShack help browser or as
* a local copy (clone) of the QMS Wiki.

The QMS offline help needs access to the Internet only for following links to pages not being part of the QMS Wiki (external links).

Both forms of the offline help have their specific advantages and disadvantages:

| Advantages | Disadvantages |
|------------|---------------|
| __QMS help browser__ | . |
| easy access to table of contents, index, and full-text search | . |
| no extra viewer/browser required for rendering | . |
| installed with QMS but can be downloaded and used without QMS installation | . |
| open with `F1` click from within QMS | . |
| separate comfortable viewer | . | 
| . | no possibility to edit pages |
| __Local Wiki copy__ | . |
| available without QMS installation | . |
| possibility to edit pages | . |
| . | special Markdown viewer or Markdown Internet browser plugin required for rendering pages|
| . | rendering quality depends on Markdown variant used in viewer or browser |
| . | `git` is required for the installation of a local Wiki copy |

_Remark:_ Everything described for QMS is analogously valid for QMapTool (QMT). Some differences are mentioned later on this page.


## Installing and using QMS help browser

* QMS is installed on the computer (preferred way to use the offline help):
    1. Start QMS.
    1. Press `F1` on the keyboard. The QMS help browser pops-up. Use the contents, index, or search tabs to find the help topic of interest.
* QMS can't be installed on the computer:
    1. Go to the [QMS source code repository][HelpSource] and download the files `QMSHelp.qch` and `QMSHelp.qhc` (when having a QMS installation these 2 files can be found in the `doc/html` subdirectory of the QMS installation directory).
    1. Be sure [Qt assistant][QtAssistant] is installed together with Qt and on your path.
    1. To open QMS help run the following command in a console window:
    
             assistant -collectionFile path_to_qmshelp.qhc/QMSHelp.qhc
           
* For QMapTool help replace `qmapshack` in the download link with `qmaptool` and replace `QMS` in the file names with `QMT`.

## Installing and using local QMS Wiki copy

To install and use a local copy of the QMS Wiki carry out the following steps:

1. If not yet available, install [git (tool for access to GitHub revision control system)][GitInstall] and make sure that `git` is found on your path.
1. Create a local directory, say `QMapShack-doc`.
1. Run the following command in a console window to download the Wiki pages to the local computer:

        git clone https://github.com/Maproom/qmapshack.wiki.git QMapShack-doc

1. The Wiki consists of _Markdown_ (`*.md`) and some other files, and to read them you will need some _Markdown_ plugin to your browser. When looking for a Markdown plugin select one that supports _GitHub Flavored Markdown_ (GFM).

     _Example of a plugin for Google Chrome browser:_ [Markdown viewer/Browser extension][MDPlugin].
   
1. Open a Markdown (`MD`) file in the browser with activated Markdown plugin. Good starting pages are `Home.md` and `DocMain.md`. From these pages other help pages can be accessed.
1. The QMapTool part of the Wiki can be found in the `QMapTool` subdirectory. Starting pages are `QMTHome.md` and `QMTDocMain`.

_Remark:_ The files necessary for the QMS/QMT offline help can be created locally when having a local copy of the QMS Wiki. To do so 

* read the information at the top of the file `Makefile.make`,
* install the tools mentioned in this information,
* run the command 

        make VERBOSE=YES -f Makefile.make show
        
  This will create and open the QMS help browser.      

[QMSWiki]: https://github.com/Maproom/qmapshack/wiki "QMS Wiki"
[QtAssistant]: https://doc.qt.io/qt-5/qtassistant-index.html "Qt assistant help"
[GitInstall]: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git "Git installation"
[MDPlugin]: https://chrome.google.com/webstore/detail/markdown-viewer/ckkdlimhmcjmikdlpkmbgfkaikojcbjk "Chrome Markdown plugin"
[HelpSource]: https://github.com/Maproom/qmapshack/tree/dev/src/qmapshack/doc "QMS help source"

- - -
[Prev](BuildOSX) (OSX) | [Home](Home) | [Manual](DocMain) | [Index](AxAdvIndex) | [Top](#) | (Getting started) [Next](DocGettingStarted)
