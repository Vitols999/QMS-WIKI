#! python3
# -*- coding: utf-8 -*-


# Add or update TOC to all Wiki pages

# Author: W. Thämelt, 23.10.2019

################################################################

# Assumptions & restrictions:
# ---------------------------

# - a TOC is added only to pages with a navbar
# - a header line should have its "#" prefixes starting in column 1
# - header lines should be unique within a Wiki page
# - header lines should be on 1 line
# - the TOC starts with the special line "***Table of contents***"
# - the TOC ends with the special line "* * * * * * * * * *"
# - the TOC should be located immediately after the navbar
# - filenames in the complete Wiki including QMapTool should be unique
#
# - There seems to be issues in Github Wiki when handling anchors for non-ASCII languages.
#   Proof: open TestAnchors.md in GitHub Wiki, move to Russian header, select link and
#          open in new tab ===> fails. ASCII headers don>'t fail!
#   Therefore, only pages with English text get a TOC.
#
# - There are differences in anchor building between different markdown renderers.
#   This holds true for headers without strange formats.
#   Thus, everything must be checked in the browser with the Github Wiki.
# - In a local copy of the Wiki local links may fail due to differences in the
#   anchor constructions rules used. This happens if in a header occur uppercase
#   non-ASCII letters (more exactly: German, Spanish, or Russian ones).
# - If other languages than the mentioned ones are included in the Wiki, then the list of respective
#   non-ASCII characters has to be updated.

################################################################

import os
import re
import unicodedata
import fnmatch

rheader = re.compile(r"(#+)\s*([^#]+)")       # mask for MD header line

# mask for finding and deleting image links in section headers
# matches:   ## ![EditDetails](images/DocGisItemsWpt/EditDetails.png) View / Edit Details
r4 = re.compile(r"\!\[[^]]*\]\([^)]*\)\s+")   # include spaces at the end of the link
r1 = re.compile("[A-Z]+")                     # matches ASCII uppercase
r2 = re.compile("[А-ЯÁÄÉÍÑÓÖÚÜ]")             # matches non-ASCII uppercase - don't change them

WIKIDIR = ".."                               # script is located in Tools subdirectory!
filemask = "*.md"

MAXHDRLVL = 6                                 # maximum header level used in TOC

# no TOC inserted into the following pages:
MDWithoutTOC = ("DocMain.md", "AxAdvIndex.md", "AxAdvToc.md", "Home.md", "AxAdvTocAbbr.md",
                "AxGlossary.md", "AxHotkeys.md", "AxWikiImages.md",
                "QMTDocMain.md", "QMTAxAdvIndex.md", "QMTAxAdvToc.md", "QMTHome.md",
                )

MDWithoutTOC = tuple(r"%s" % x.lower() for x in MDWithoutTOC) # necessary for comparisons

################################################################

# find each MD file
def gen_find(filepat, top):
    # filepat: pattern of files to find
    # top: folder where search for files is started

    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, filepat):
            yield os.path.join(path, name)

################################################################

# build MD reference from given string using separator as word separator

# Github version working with non-ASCII   
def f(matchobj):                               # convert ASCII uppercase to lowercase
    return matchobj.group(0).lower()
    
def slugify1(value, separator):  # variant handling non-ASCII in GitHub correctly
    value = re.sub(r'[^0-9a-zа-яßáäéíñóöúü\s-]', '', value, flags=re.IGNORECASE).rstrip() # drop non-alphabetic characters
    value = r1.sub(f, value)                    # make only ASCII uppercase to lower
  
    if r2.search(value):                       # non-ASCII uppercase found
        value = "user-content-%s" % value      # use "id" instead of "href" for link target
  
    return re.sub(r'\s', separator, value).strip() # replace space with separator ("-")
  
################################################################
def FindTOC4Page(mdfile):                          # find existing TOC in file

    if os.path.basename(mdfile).lower() in MDWithoutTOC: # these files are left without TOC
        return "PageWithoutTOC"
        
    inpf = open(mdfile, "r", encoding="utf-8")

    toc = []

    lines = inpf.readlines()
    
    if (lines[0].startswith("[Prev]") or lines[0].startswith("Prev")) and \
        lines[1].startswith("- - -"):                     # page has navbar        

        tocfound = False
        firstidx = False                                  # index of TOC header line
        lastidx = False                                   # index of TOC footer line
        
        for i, lne in enumerate(lines[2:]):
            if lne[:-1] == "***Table of contents***":     # TOC header found
                tocfound = True
                toc.append(lne[:-1])
                firstidx = i+2                            # save index of header line for later update
                
            elif tocfound and lne[:-1] != "* * * * * * * * * *": # normal TOC line found
                toc.append(lne[:-1])
                
            elif lne[:-1] == "* * * * * * * * * *":       # TOC footer found
                toc.append(lne[:-1])
                lastidx = i+3                             # save index of footer line for later update
                return [toc, firstidx, lastidx]
                
            else:                                         # line not related to TOC
                continue
                
        return [toc, firstidx, lastidx]                   # existing TOC with index for header and footer lines
                   
    else:                                                 # pages without navbar don't get TOC (e.g. _sidebar.md)
        return "PageWithoutTOC"

################################################################
def BuildTOC4Page(mdfile):                        # build actual TOC for given file
    inpf = open(mdfile, "r", encoding="utf-8")

    toc = ["***Table of contents***", "", ]       # TOC header

    for lne in inpf:                              # try to find TOC in file

        rr = rheader.match(lne)
   
        if rr:                                    # TOC header found in file
        
            hdr = rr.group(2)                     # header text
            hdr = r4.sub("-", hdr)                # remove possible image link

            anchor = slugify1(hdr, "-")            # build Github anchor
            spacer = "    " * (len(rr.group(1)) - 1) # find necessary indentation for TOC output list
            
            if hdr.startswith("-"):               # drop superfluous "-" as first character
                hdr = hdr[1:]

            if MAXHDRLVL >= len(rr.group(1)) - 1: # avoid too may header levels
                toc.append("%s* [%s](#%s)" % (spacer, hdr[:-1], anchor)) # add 1 TOC line  
        
    toc.append("")    
    toc.append("* * * * * * * * * *")             # add footer to TOC
    
    inpf.close()
    
    return toc                                    # used for comparison with existing TOC in file

################################################################
def UpdateTOC4Page(mdfile, toc0, toc):                  # insert or update TOC in file

    inpf = open(mdfile, "r", encoding="utf-8")
    lines = inpf.readlines()                            # read complete file
    inpf.close()
    
    if toc0[1:] == [False, False]:                      # file without TOC
    
        toc0[1:] = [2, 3]                                # split lines in file here
       
        lines[toc0[1]:toc0[2]] = [" \n"] + ["%s\n" % x for x in toc] + [" \n"] # insert new TOC at proper location and add newlines
       
    else:                                               # file with TOC
        lines[toc0[1]:toc0[2]] = ["%s\n" % x for x in toc] # replace TOC with updated one

    outf = open(mdfile, "w", encoding="utf-8")        # output of updated page - old one is overwritten!
    
    for lne in lines:
        outf.write(lne)
        
    outf.close()
    return
    
################################################################
def HandlePage(mdfile):                                  # decide how to handle TOC in file

    toc0 = FindTOC4Page(mdfile)                          # check if TOC already exists in file

    if toc0 == "PageWithoutTOC":                         # page doesn't need a TOC
        print("Page left without TOC: ", mdfile)
        
    elif toc0[1:] == [False, False]:                     # page does not yet have a TOC
        print("Page with missing TOC:", mdfile)
        
        toc = BuildTOC4Page(mdfile)                      # build necessary TOC for page
        
        UpdateTOC4Page(mdfile, toc0, toc)                # and insert it into page
        
    else:                                                # page has TOC

        toc = BuildTOC4Page(mdfile)                      # build actual TOC for page
 
        if toc == toc0[0]:                               # compare actual with existing TOC
            print("TOC on page ok.        ", mdfile)     # if equal - nothing to do
            
        else:                                            # existing TOC needs update - do it
            print("TOC updated:           ", mdfile)
            UpdateTOC4Page(mdfile, toc0, toc)    

    return
      
################################################################      

if __name__ == '__main__':

    mdfiles = gen_find(filemask, WIKIDIR)             # find all *.md files

    for mdfile in mdfiles:                            # insert or update TOC in all MD files
        HandlePage(mdfile)
    
    print("\nEnd of run.")

    