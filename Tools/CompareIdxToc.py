#!python3
# -*- coding: utf-8 -*-

# Find inconsistencies between the TOC in AxAdvToc.md and AxData4Index.txt

# W.Thämelt, 17.02.2020: add handling of of QMapTool files

import difflib
import re

cfg = {"QMS": {}, "QMT": {}}

# configuration for QMS part
cfg["QMS"] = {
"tocfile": r"../AxAdvToc.md",            # complete TOC file 
"idxfile": r"AxData4Index.txt",            # raw index file
}

# configuration for QMT part
cfg["QMT"] = {
"tocfile": r"../QMapTool/QMTAxAdvToc.md",            # complete TOC file 
"idxfile": r"QMTAxData4Index.txt",            # raw index file
}

r2 = re.compile("^[-+]*\s*$")  # result lines of diff with "+" or "-" in first position and empty in the rest

r3 = re.compile("^\s*\*\s+\[")  # TOC line in AxAdvToc & AxData4Index (line starts with "*")

r4 =  re.compile(               # find page name in link: " * [TMS Maps](DocBasicsMapDem#markdown-header-tms-maps)" ==> DocBasicsMapDem 

               """[^\]]+        # several characters not equal to ]
                  \]\(          # followed by ](
                  ([^#]+)"""    # followed by several characters not equal to #, referenced as group
                 , re.VERBOSE)  

ExceptionList = ("AxAdvIndex",         # pages in this list have subsections not maintained in AxData4Index.txt
                 "QMTAxAdvIndex",
                )

def gen_toclines(inpfile):      # find TOC lines in input files - generator used as a filter

    for lne in inpfile:     
      if r3.search(lne) and r4.search(lne).group(1) not in ExceptionList: # skip non-TOC lines and those belonging to a file in exception list
        yield lne.strip()

for pkg in cfg.keys():
    tocfile = cfg[pkg]["tocfile"]
    idxfile = cfg[pkg]["idxfile"]

    oidxfile = open(idxfile, encoding="utf-8")
    otocfile = open(tocfile, encoding="utf-8")
        
    # Differ requires lists    
    idxtoc = list(gen_toclines(oidxfile))
    toctoc = list(gen_toclines(otocfile))

    d = difflib.Differ()
    res = d.compare(idxtoc, toctoc)        # carry out a diff

    for r in res:
      if not r2.search(r) and r[0] != " ": # find important (+ or -) diff lines
         if not "* [Installing QMapShack]" in r and \
            not "* [Using QMapShack]" in r      and \
            not "* [Quickstart" in r:      # these lines are there for hierarchy reasons only!
            
           rr = r.encode(encoding="ASCII", errors="xmlcharrefreplace").decode(encoding="utf-8")
           print(rr)    
     
    print("\nEnd of {} run.".format(pkg))
