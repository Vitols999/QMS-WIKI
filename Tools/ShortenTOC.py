#! python3
# -*- coding: utf-8 -*-

# Prepare abbreviated table of contents for use in Wiki sidebar

# Procedure:
#  - read complete TOC
#  - copy only lines with < len(empty) spaces at start of line
#  - remove navbar and modify header line 


empty = " " * 9                                                      # (9) drop lines starting with that many spaces
title = "# Complete table of contents"                               # identify header line
index = "* [Index](AxAdvIndex)"                                      # identify index line to drop subentries

dontcopy = True                                                      # don't copy line if True (used to drop navbar)

toc = r"..\AxAdvToc.md"                                              # complete TOC
otoc = r"d:..\AxAdvTocAbbr.md"                                       # abbreviated TOC


inpf = open(toc, "r", encoding="utf-8")
outf = open(otoc, "w", encoding="utf-8")

for lne in inpf:

    if lne.startswith(empty):                                        # drop line
        continue
        
    elif lne.startswith(title):                                      # modify header
        outf.write("# Table of contents (abbreviated)\n")
        dontcopy = False                                             # start copying from here
        
    elif dontcopy:                                                   # don't copy line
        continue
            
    elif lne.startswith(index):                                      # suppress subentries 
        empty = "    "
        outf.write(lne)
                
    elif lne.startswith("- - -") or lne.startswith("[Prev]"):        # drop navbar lines 
        continue
        
    else:                                                            # copy normal line
        outf.write(lne)    
