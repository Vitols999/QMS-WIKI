#!/usr/bin/env python
# coding: utf-8

# # Generate Qt help configuration files for QMapShack and QMapTool
# 
# Author: W.Thämelt

#     
#     

# ## Workflow for preparing Qt help for QMS/QMT
# 
# 1. Be sure, local copy of QMS wiki is up-to-date (including the TOC and index files, git should work on this copy)
# 1. Be sure, files for preparing Qt help (Makefile.make, HTMLMake.py, QMSQtHelp.py, qmsstyle.css, QMS/THelp.qhcp) 
#    are up-to-date and at correct location.
# 1. Be sure, configuration in Makefile.make is up-to date. Check it with
#    `make VERBOSE=YES -f Makefile.make check`.
# 1. In case of changes in the Wiki directory structure check and update the configuration files    
#    QMSHelp.qhcp, QMTHelp.qhcp.
# 1. Run `make -f Makefile.make build` 
# 1. Check the new help packages using Qt assistant or QMS 
#    (run `make -f Makefile.make show` or `assistant.exe -collectionFile path_to/QMSHelp.qhc`, 
#    pay attention to the contents of the cache used by assistant - layout and content at start depends on cache!)
# 
# * __Schematic flow of operations in Makefile.make:__
# 
# ~~~                                          
# 
#       HTMLMake.py .md/.wmts./...                 image files       
#            ||             ||                          ||       
#            ||             ||                          ||             
#            ||             ||                          ||       
#            ||             \/                          ||
#            ==========> |      |                       ||          
#         doc ---------- |.html | <=== clean            ||   
#                        |      |        ||             ||
#                           ||           ||             ||             
#                           ||           ||             ||             
#                           ||           ||             ||        
#                           ||           \/             ||         
#                            ======>  |     | <==========            
#         QMSQtHelp.py ============>  |.qhp |                              
#                                     |     |                             
#                                        ||
#                                        ||
#                                        \/
#         .qhcp =================> |.qch/.qhc | ---- build
#         qhelpgenerator ========> |          |
#                                        ||
#                                        ||
#                                        ||
#                                        \/
#         assistant --------------- show help ------ show             
# ~~~
# 
# * __Used additional directory structure in local Wiki copy:__
# 
# ~~~
# 
# root (*.qhcp, *.qhp, Makefile.make) 
#       |
#       --- doc (some general files used) 
#            |
#            --- qms (QMSHelp.qhc/qch)                                 
#            |
#            --- qmt (QMTHelp.qhc/qch)
#            |
#            --- html (.html)
#                 |
#                 --- css (CSS file)
#                 |
#                 --- QMapTool (.html for QMT)
#                 |
#                 --- Downloads (.html for Downloads/*.wmts, ...)                
# ~~~  
# 
# * The intermediate .html files are included in the global `.gitignore` file. 
#   Thus, they are not pushed to the server.
# 
# 

# ## Prerequisites and some bottlenecks
# 
# The following assumptions about the local copy of the QMS/QMT wiki are assumed to hold true 
# for successfully preparing Qt help:
# 
# * All extensions for filenames must be lowercase.
# * The QMT wiki part is located in the `QMapTool` subfolder of the QMS local wiki folder. 
#   Images for QMT wiki files are located in `QMapTool/images` (without further subfolders).
# * Links to images in MD pages of the QMT wiki have the form required by Github.
# * `QMapTool` is the only subfolder with MD files. All QMS MD files of the wiki should be 
#   located in the root directory of the wiki.
# * Large images in HTML/MD files are automatically scaled by some browsers ("responsive images"). 
#   This doesn't hold true for the Qt help `assistant` coming with Qt5.14.0 for Windows. 
#   Therefore, images having a width exceeding a certain  threshold get an additional 
#   width attribute to force the Qt help browser to resize the image. 
# * The TOC of a Qt help page is built with the help of the TOC extension in the 
#   markdown package when converting .md to .html files.
# * The contents tree of Qt help is built from `AxAdvToc.md` and `QMapTool/QMTAxAdvToc.md`.
# * The index part of Qt help is built from `AxAdvIndex.md` and `QMapTool/QMTAxAdvIndex.md`. 
# * If the formats used in the index resp. TOC markdown files is changed, then this script 
#   must be adjusted to the new format.
# * The wiki subfolder `Downloads` contains only non-MD files. For use in Qt help they are 
#   converted to HTML files. The texts that accompany these links promise a direct download 
#   possibility. This possibility is, most likely, even not available in the original wiki. 
#   To get the contents of these files, copy the content from the browser window and save it.
# * The Github wiki merges the QMS and QMT part filenames into one large list of filenames. 
#   This implies, that filenames in the complete Wiki must be unique. To achieve this, some 
#   filenames start with a `QMT` prefix.
# * Qt help for QMS and QMT is split into 2 separate packages. References/links from one part 
#   to the other should use a reference to `https://github.com/Maproom/qmapshack/wiki/...`.
# * Images for the QMS part are located in child folders of the `images` folder.
# * Only files in the root directory and the `QMapTool`, `images`, and `Downloads` are used when preparing Qt help.

# ## Imports

import re
import os
import sys

import xml.etree.ElementTree as ET

# ## Configuration

# define maximum number of levels in TOC (= TOCDEPTH//4)
TOCDEPTH = 12

QMSBASEDIR = os.getcwd()                      # location of local copy of QMS wiki

HTMLDIR = "doc/html"                          # branch in the Wiki for .html files

# Wiki TOC and Index files used for preparing Qt help
QMSTOCFILE = r"AxAdvToc.md"
QMSIDXFILE = r"AxAdvIndex.md"

# QMapTool
QMTBASEDIR = r"{}/QMapTool".format(QMSBASEDIR)
QMTTOCFILE = r"QMTAxAdvToc.md"
QMTIDXFILE = r"QMTAxAdvIndex.md"

# ## Template of qhp file

QHP = """<?xml version="1.0" encoding="UTF-8"?>
<QtHelpProject version="1.0">
    <namespace>{pkg}</namespace>
    <virtualFolder>doc</virtualFolder>
    <customFilter name="{pkg}Application 1.0">
        <filterAttribute>{pkg}App</filterAttribute>
        <filterAttribute>1.0</filterAttribute>
    </customFilter>
    <filterSection>
        <filterAttribute>{pkg}App</filterAttribute>
        <filterAttribute>1.0</filterAttribute>
        <toc>
           <section title="{toptitle}">
           </section>
        </toc>
        <keywords></keywords>
        <files>
            <file>{cssdir}/qmsstyle.css</file>
            <file>{htmldir}/{qmtswtch}*.html</file>
            {extrafiles}
            <file>{qmtswtch}images/*.*</file>
        </files>
    </filterSection>
</QtHelpProject>
"""

# ## Regular expressions

r1 = re.compile("^#+\s")
# matches:      ## Advanced usage

r2 = re.compile(r"^(\s*)\*\s+\[*([^\]]+)\]*(\(([^\)]+)\))*")
# matches:      * [Widgets Overview](DocGisTemplates#widgets-overview)
#               * Installing QMapShack

r3 = re.compile("^((\s*)\*)")
# matches "    *" at start of line

r4 = re.compile("\* !.+\[__([^_]+)__\]\(([^ ]+)")
# matches * ![UK flag](images/DocGettingStarted/FlagUk.jpg)  [__Quick start__](DocQuickStartEnglish "English quickstart description")

r5 = re.compile("\*\*([^\*]+)\*\*")
# matches    **Active project, create new data**

r6 = re.compile("(:|⊞)\s+\[[^\]]+\]\(([^ ]+)")
# matches:
#  :  [Active projects](AdvProjActions#active-projects "Active projects")
#  :  [Edit items with multiple points](DocGisItemsEditMultiple "Edit items with multiple points") ⊞ \
#     [Edit line](DocGisItemsEditMultiple#edit-line "Edit line") ⊞ \
#     [View / Edit Details](DocGisItemsArea#view--edit-details "View / Edit Details")

# ## class QHPMaker
# 
# This class is used for the QMS and the QMT help configuration file creation.

class QHPMaker():

    # these subdirectories are only used in QMS - drop them for QMT
    ExtraFiles = """<file>{}/Downloads/*.html</file>""".format(HTMLDIR)

    def __init__(self,
                 pkg="QMS",                    # used package: QMS or QMT
                 toptitle="QMapShack manual",  # top title in help content tree
                 basedir=QMSBASEDIR,           # folder for MD files
                 idxfile=QMSIDXFILE,           # index MD filename without path
                 tocfile=QMSTOCFILE,           # TOC MD filename without path
                 ):

        self.basedir = basedir
        self.pkg = pkg

        self.CSSDir = "{}/css".format(HTMLDIR)
        self.QMTSWTCH = ""

        if pkg != "QMS":                       # QMT: remove extra file directories used for QMS
            self.ExtraFiles = ""
            self.QMTSWTCH = "QMapTool/"

        # read TOC file
        inpf = open("{}/{}".format(self.basedir, tocfile), "r", encoding="utf-8")
        self.toclnes = inpf.readlines()
        inpf.close()

        # read index file
        inpf = open("{}/{}".format(self.basedir, idxfile), "r", encoding="utf-8")
        self.idxlnes = inpf.readlines()
        inpf.close()

        # open QHP file template for further handling, insert first QMS/QMT parameters
        self.root = ET.fromstring(QHP.format(pkg=pkg, toptitle=toptitle, extrafiles=self.ExtraFiles,
                                             cssdir=self.CSSDir, htmldir=HTMLDIR, qmtswtch=self.QMTSWTCH))

        self.FindXMLTOC()    # find TOC entries for qhp file
        self.FindXMLIDX()    # find keyword/index entries for qhp file (none for QMT)
        self.FindXMLFiles()  # find all image subfolders for files part of qhp file
                             # QMT part needs special adjustments!

        # save qhp file
        ET.ElementTree(element=self.root).write("{}Help.qhp".format(pkg),
                                                encoding="utf-8",
                                                xml_declaration=True)

        return

# ### method FindXMLTOC

def FindXMLTOC(self):         # build TOC entries for Qt help (= section part in .qhp)

    # all TOC sections are children of main section (QMS or QMT manual)
    toc = self.root.findall("./filterSection/toc/section")
    toc = toc[0]

    nodestack = [toc, ]       # list of nodes with current successors

    TOCSWTCH = True           # make changes depending on this switch only once

    for lne in self.toclnes:
        if "AxAdvToc#appendix" in lne:
            continue

        rr = r1.search(lne)           # line with chapter/section definion in MD (## ...)
        if rr:
            lne = r1.sub("* ", lne)   # replace "## ..." with "*..." (top level TOC entries)

        else:
            rr = r3.search(lne)       # this is a TOC line
            if rr:
                rr1 = r4.search(lne)  # this is a special quickstart line
                if rr1:               # remove icon in front of link in this line
                    lne = "* [{}]({})".format(*rr1.groups())
                if len(rr.group(2)) > TOCDEPTH:  # level of TOC entry too large, drop entry
                    continue
                else:                 # move entry to next hierarchy level in TOC
                    lne = r3.sub("    {}".format(rr.group(1)), lne)

            else:                     # not a TOC line
                continue

        rr = r2.search(lne)           # now, find link in TOC line
        if rr:                        # remove links to single letter in index
            if rr.group(4) and "AxAdvIndex#" in rr.group(4):
                continue

            currident = len(rr.group(1)) // 4      # current indentation level of TOC entry

            parentnode = nodestack[currident]      # entry gets this parent node
            nodestack = nodestack[:currident + 1]  # remove all children of this parent

            # activate TOC entries for QuickStarts
            title = rr.group(2).strip()
            if TOCSWTCH and title == "Complete table of contents":
                title = "Quick start guides"       # rename top level entry in case of QMS
                TOCSWTCH = False

                if "QMapTool" in self.basedir:     # QMT doesn't have Quickstarts, thus, skip the renaming
                    continue

            newsect = ET.SubElement(parentnode, "section")  # insert TOC als new child to parent

            newsect.set("title", title)
            if rr.group(4):                         # some TOC entries are without a reference to a file
                splits = rr.group(4).split("#")
                ref = "{}/{}{}.html".format(HTMLDIR, self.QMTSWTCH, splits[0])   # insert the html extension at the correct location
                if len(splits) == 2:
                    ref = "{}#{}".format(ref, splits[1])
                newsect.set("ref", ref)
            else:                                   # now page referenced - show blank page
                newsect.set("ref", "about:blank")
            nodestack.append(newsect)               # finally, insert new node into the node tree
        continue

    return

QHPMaker.FindXMLTOC = FindXMLTOC  # insert function is method into QHPMaker

# ### method FindXMLIDX

def FindXMLIDX(self):     # build index entries for Qt help (= keywords part)

    keyword = self.root.findall("./filterSection/keywords")
    keyword = keyword[0]

    for lne in self.idxlnes:
        rr = r5.search(lne)           # line with index entry
        if rr:
            kwdname = rr.group(1)
            continue

        rlist = r6.findall(lne)       # get list of all links for index entry
        for x, lnk in rlist:
            # lnk = rr.group(1)

            newkwd = ET.SubElement(keyword, "keyword")
            newkwd.set("name", kwdname)  # add name and id attributes to keyword tag
            newkwd.set("id", kwdname)    # if set, then keyword doesn't appear in the index

            splits = lnk.split("#")      # insert the html extension at the correct location
            ref = "{}/{}{}.html".format(HTMLDIR, self.QMTSWTCH, splits[0])
            if len(splits) == 2:
                ref = "{}#{}".format(ref, splits[1])

            newkwd.set("ref", ref)

            continue
    return

QHPMaker.FindXMLIDX = FindXMLIDX

# ### method FindXMLFiles

def FindXMLFiles(self):   # build files part for Qt help .qhp configuration file

    files = self.root.findall("./filterSection/files")
    files = files[0]

    # find all subfolders of image folder and add them to files part of qhp file
    imgdirs = (x for x in os.listdir("{}/images".format(self.basedir)) if os.path.isdir("{}/images/{}".format(self.basedir, x)))

    for imgdir in imgdirs:
        newfile = ET.SubElement(files, "file")
        newfile.text = r"images/{}/*.*".format(imgdir)

    return

QHPMaker.FindXMLFiles = FindXMLFiles

# ## DoIt

if __name__ == '__main__':

    # prepare QMS Qt help configuration file
    QHPMaker(pkg="QMS",
             toptitle="QMapShack manual",
             basedir=QMSBASEDIR,
             idxfile=QMSIDXFILE,
             tocfile=QMSTOCFILE,)

    # prepare QMT help configuration file
    QHPMaker(pkg="QMT",
             toptitle="QMapTool manual",
             basedir=QMTBASEDIR,
             idxfile=QMTIDXFILE,
             tocfile=QMTTOCFILE,)

