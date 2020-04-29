#!/usr/bin/env python
# coding: utf-8

# # Convert Markdown to HTML for QMapShack/QMapTool Wiki pages
# 
# Author: W.Thämelt
# 
# This script is based on code taken from the HTMLMake.py script written by R.Woitok. 
# 
# Therefore the name of the script is intentionally the same as the name chosen by R.Woitok.
# But the scripts are stored in different directories.
# 
# Changes have been necessary due to new Python and Markdown versions not 
# compatible with the ones assumed for the original script and also due 
# to some Github-specific and other adjustments. 
# 
# Non-markdown files in the `Downloads` subfolder of the Wiki are converted to 
# markdown files for better rendering.
# 
# The only configuration parameter in this script is `MAXWIDTH`. It is used if 
# an image width is greater than MAXWIDTH. In this case the image is resized to MAXWIDTH 
# when rendered (not all tested browsers support responsive images (for example, 
# Qt assistant version 5.14.0 for Windows 10))
# 
# Markdown reference: https://python-markdown.github.io/reference/
# 

# ## Imports

import re
import sys
import os
import glob

import PIL
from PIL import Image

import markdown
from markdown.extensions import Extension
from markdown.inlinepatterns import SimpleTagPattern
from markdown.preprocessors import Preprocessor
from markdown.postprocessors import Postprocessor

# ## Configuration

MAXWIDTH = 1300                  # if image width > MAXWIDTH, then image is resized to MAXWIDTH when rendered

DIRNAME = os.path.abspath(".")   # folder in which all QMS MD files can be found. Subfolders: QMapTools, Downloads, Tools
                                 # setting depends on current working directory = location of Makefile.make!

HTMLDIR = "doc/html"             # relative path to subdirectory with .html files (root: Wiki root directory)

FILES2CONVERT = (sys.argv[1], )  # convert MD file given on command line
SINGLEFILE = True                # convert just 1 file - don't change or remove, used in another script variant!

# ## HTML header and footer definitions

header = """<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="" xml:lang="">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes" />
  <link rel="stylesheet" type="text/css" href="{reldir}/qmsstyle.css"/>
  <title>{title}</title>

</head>
<body>
"""

footer = """</body>
</html>
"""

# ## Class definitions

# ### class AddHtmlExt
# 
# Define additional markdown extensions for preprocessing MD input files.
# 
# The following actions are carried out:
# 
# * Replace existing TOC in markdown file with tag [TOC] for further processing. 
#   Thus, the TOC in Qt help is always up-to-date.
# * If reference to an image is found and if image is wider than predefined 
#   threshold MAXWIDTH, then add width attribute in markdown form to reference for 
#   further processing within markdown attr_list extension.
# * Github requires that images in the QMapTool\image folder referenced from a 
#   QMapTool MD file have the QMapTool\image folder in the reference. The converted 
#   HTML requires a reference to the "images" subfolder only. Thus, "QMapTool" is 
#   dropped from the image reference.
# * There are some references to non-MD files in QMS MD files. To ensure correct 
#   rendering of these files they are embedded as code during the conversion to an 
#   HTML page (both in the Wiki and in the HTML page the accompanying text is 
#   misleading - it promises falsely the possibility to download). In the HTML/Qt help 
#   case copy the text shown in the browser and save it. The extensions .WMTS, .TMS, .PY 
#   are replaced with .HTML.
# * Remove image references in markdown headers.
# * Github finds MD files in QMapTool folder without reference to this folder. HTML files 
#   need the correct folder name. Thus, the correct folder is added.
# * Ensure, that references to other markdown files get correct HTML extension.

# References to local files in the various "*.md" source files are requ-
# ired by Bitbucket/Github to have NO extension but are required by any browser
# to have an ".html" extension.   Therefore we use  the following addit-
# ional Markdown preprocessor to add ".html" extensions to file names:

class AddHtmlExt(Preprocessor):
    def run(self, InLines):               # content of whole MD file - list of lines!
        OutLines = []                     # To receive the output lines.

        #
        # Regular expression "ReExt" matches both, inline and reference-
        # style, local link definitions  already featuring  an extension
        # (without any dashes) which is again suffixed with an addition-
        # al ".html" extension  (the first parenthesized  sub-expression
        # matches the  beginning  of the link  definition  including the
        # dash-free file name extension, provided this file name extens-
        # ion is suffixed with ".html" and followed by a file name term-
        # inating character, if any,  which is matched by the third par-
        # enthesized sub-expression.  Not allowing dashes in the extens-
        # ion prevents  "Ubuntu-14.04-HowTo"  from being  mistaken for a
        # file name  with extension).   And regular  expression  "ReUrl"
        # simply matches both, inline and reference-style local link de-
        # finitions (the first parenthesized  sub-expression matches the
        # beginning of the link definition  up to but excluding the file
        # name terminating  character,  if any,  which is matched by the
        # third parenthesized sub-expression):

        ReExt = re.compile(r'((^ *\[[^^][^]]*\]:[ \t]+|\]\( *).*\.[^-/ )#]+)\.html([ )#]|$)')
        ReUrl = re.compile(r'((^ *\[[^^][^]]*\]:[ \t]+|\]\( *)[^ :#)]+)([ )#]|$)')

        ReImg = re.compile(r"\]\(#-")        # some MD headers include an image reference.
                                             # the GitHub markdown renderer creates in this case
                                             # a header ID with "-" as the first character.
                                             # This character appears in the TOC of the page, too.
                                             # python-markdown doesn't use this character in the ID
                                             # Thus, it is dropped from TOC links

        ReQMT = re.compile(r'\]\(QMTDocMain "QMapTool documentation"')
                                             # Github finds pages in subdirectories without
                                             # explicit addressing the subdirectory, HTML version needs it.

        ReDownloads = re.compile('((\]\(Downloads/[^\.]+)\.[^\)]+)\)')
                                             # matches link to Downloads folder
            
        ReRefLnk = re.compile('''^(\[[^\]]+\]:)\s+(images/)''')   # matches start of link reference for image
        ReRefLnkQMT = re.compile('''^(\[[^\]]+\]:)\s+(QMapTool/images/)''')   # QMT: matches start of link reference for image

        ReWholeImg = re.compile('(!\\[[^\\]]+\\]\\(([^ \)]+)[^\\)]*\\))')
        # matches img link in: 'aaa ![Grid tool](QMapTool/images/ETH_GridTool.jpg "Grid tool EPSG") ccc'

        ReTOC = re.compile('\*\*\*Table of contents\*\*\*.*\* \* \* \* \* \* \* \* \* \*', re.DOTALL)
                                             # matches whole script-generated TOC in markdown file

                                             # replace markdown TOC with [TOC] marker for further processing
        InLines = ReTOC.sub("\n\n***Table of contents***\n\n[TOC]\n\n", "§§§".join(InLines))
        InLines = InLines.split("§§§")

        for line in InLines:                 # Process whole input file.

            rr = ReWholeImg.search(line)     # add width attribute to image link if large image
            if rr:
                img = "{}\\{}".format(DIRNAME, rr.group(2))

                if os.path.exists(img):      # there are some img links without a correct img name!
                    im = Image.open(img)     # this is no error in markdown file!
                    width, height = im.size
                    if width > MAXWIDTH:
                                             # insert the width info (extended MD syntax!) into markdown link
                        line = ReWholeImg.sub(r'\1{{: width="{}"}}'.format(MAXWIDTH), line)

            rr = ReRefLnk.search(line)
            if rr:
                line = ReRefLnk.sub(r"\1 ../../\2", line)  # adjust reference to link

            rr = ReRefLnkQMT.search(line)                   # adjust reference to link for QMT
            if rr:
                line = ReRefLnk.sub(r"\1 ../../../\2", line)
                
            if "](Downloads/" in line:       # adjust link in case of WMTS;TMS, ... file
                line = ReDownloads.sub(r"\2)", line)  # remove .wmts, .tms, ... extensions

            if "(images/" in line:           # adjust links to images
                line = line.replace("(images/", "(../../images/")
            elif "(QMapTool/images/" in line:
                line = line.replace("(QMapTool/images/", "(../../../QMapTool/images/")
                
            line = ReImg.sub("](#", line)             # drop leading "-" in TOC link

            line = ReQMT.sub('](QMapTool/QMTDocMain "QMapTool documentation"', line)  # Insert subdirectory name

            OutLines.append(ReExt.sub(r'\1\3', ReUrl.sub(r'\1.html\3', line)))

        return OutLines

# ### class HeaderFooterPostprocessor
# 
# Define additional markdown extension
# 
# * Add borders to HTML tables
# * Add header with page title and footer (closing tags) to HTML output

class HeaderFooterPostprocessor(Postprocessor):
    TITLE = "My title"                                               # dummies - overwritten in DoIt
    RELDIR = ""

    def run(self, text):                                             # text = HTML conversion result
        text = text.replace('<table>', '<table border="1">')         # add table borders

        rpng_jpg = re.compile('\.(jpg|png)\.html')                   # remove extra .html extension after .jpg/.png extension
                                                                     # source of this extra extension unknown
        text = rpng_jpg.sub(".\\1", text)
                                                                     # add HTML header and footer to page
        return "{}\n{}\n{}".format(header.format(reldir=self.RELDIR, title=self.TITLE), text, footer)

# ### class FixHtml
# 
# Add user-defined extensions to markdown extension handling

class FixHtml(Extension):

    def extendMarkdown(self, md, md_globals):

        # Insert "AddHtmlExt" preprocessor and "HeaderFooterPostprocessor" postprocessor
        # as markdown extensions
        md.preprocessors.register(AddHtmlExt(md), 'add_html_ext', 500)
        md.postprocessors.register(HeaderFooterPostprocessor(md), "add_header_footer", 1)

        md.inlinePatterns.deregister('entity')
        md.inlinePatterns.deregister('html')
        md.preprocessors.deregister('html_block')

        return

# ### class StrikeThrough
# 
# Is this extension really needed? Does StrikeThrough happen in QMS Wiki MD files?

# Define a Markdown extension  to process the  "~~xxxxx~~"  notation for
# "strike through"  (mind that the regular expression  assigned to vari-
# able "ReDel" must not be compiled, and mind the additional parentheses
# around the first "~~" which cause the text to be striked through to be
# returned by "group(3)",  the place where  "SimpleTagPattern()"  is ex-
# pecting it):

ReDel = r'(~~)(.*?)~~'   # Regular expression matching "strike through".

class StrikeThrough(Extension):
    def extendMarkdown(self, md, md_globals):
        md.inlinePatterns.register(
            SimpleTagPattern(ReDel, 'del'),
            'del',
            200
        )

        return

# ## Function slugify

# Define a "slugify" function which does  the same thing as the standard
# "slugify function built into the  Markdown "toc" extension  and addit-
# ionally adds the Github specific prefix to header line identifiers:

# build MD reference from given string using separator as word separator

r1 = re.compile("[A-Z]+")                     # matches ASCII uppercase
r2 = re.compile("[А-ЯÁÄÉÍÑÓÖÚÜ]")             # matches non-ASCII uppercase - don't change them
r4 = re.compile(r"\!\[[^]]*\]\([^)]*\)\s+")   # include spaces at the end of the link

# Github version working with non-ASCII
def f(matchobj):                              # convert ASCII uppercase to lowercase
    return matchobj.group(0).lower()

def slugify(value, separator):                # variant that handles non-ASCII in GitHub correctly
    value = r4.sub("-", value)                # remove possible image link

    value = re.sub(r'[^0-9a-zа-яßáäéíñóöúü\s-]', '', value, flags=re.IGNORECASE).rstrip()  # drop non-alphabetic characters
    value = r1.sub(f, value)                  # make only ASCII uppercase to lower

    if r2.search(value):                      # non-ASCII uppercase found
        value = "user-content-%s" % value     # use "id" instead of "href" for link target

    return re.sub(r'\s', separator, value).strip()  # replace space with separator ("-")

# ## DoIt

def DoIt():

    md = markdown.Markdown(         # use one instance of this class for conversion of whole list of files
        output_format="xhtml",      # closer to XML than "html5"
        extensions=['markdown.extensions.abbr',
                    'markdown.extensions.def_list',
                    'markdown.extensions.fenced_code',
                    'markdown.extensions.footnotes',
                    'markdown.extensions.sane_lists',
                    'markdown.extensions.tables',
                    'markdown.extensions.toc',
                    'markdown.extensions.attr_list',
                    FixHtml(),                   # extensions defined in this script
                    StrikeThrough(),
                    ],
        extension_configs={'markdown.extensions.toc': {'slugify': slugify},  # !??
                           },
    )

    # convert all files to HTML
    for mdfile in FILES2CONVERT:

        # _Sidebar,md is part of the QMS Wiki, but not used in Qt help
        if "_Sidebar" in mdfile:
            continue

        # set HTML page title to filename
        HeaderFooterPostprocessor.TITLE = os.path.splitext(os.path.basename(mdfile))[0]

        HeaderFooterPostprocessor.RELDIR = "css"        # adjust reference to .css file
        if "Downloads" in mdfile or "QMapTool" in mdfile:
            HeaderFooterPostprocessor.RELDIR = "../css"

        mdinpf = open(mdfile, "r", encoding="utf-8")    # read whole input file
        mdinput = mdinpf.read()
        mdinpf.close()

        if "Downloads\\" in mdfile or "Downloads/" in mdfile:  # this is a WMTS, TMS, ... but not a MD file
            mdinput = "~~~\n{}\n~~~\n".format(mdinput)  # convert whole file content to reasonable markdown

        converted = md.convert(mdinput)                 # convert whole file content to HTML
        md.reset()

        output = "{}/{}.html".format(HTMLDIR, os.path.splitext(mdfile)[0])  # filename of HTML output
        outf = open(output, "w", encoding="utf-8")
        outf.write(converted)                           # save HTML file
        outf.close()

    return

if __name__ == '__main__':
    DoIt()

