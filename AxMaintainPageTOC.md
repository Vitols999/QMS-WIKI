[Prev](AxMaintainIndex) (Maintaining the QMS Wiki Index) | [Home](Home) | [Manual](DocMain) | [Index](AxAdvIndex) | (Discussion of extended activity system) [Next](DocActivityPlanning)
- - -

***Table of contents***

* [Manage Table Of Content on Wiki pages](#manage-table-of-content-on-wiki-pages)
    * [The `AddToc.py` script](#the-addtocpy-script)
        * [Purpose of the script](#purpose-of-the-script)
        * [Running the script](#running-the-script)
        * [Using the script in a client-side hook](#using-the-script-in-a-client-side-hook)
        * [Limitations of the script](#limitations-of-the-script)
        * [Used anchor building (slugify) method](#used-anchor-building-slugify-method)
    * [Differences in rendering TOC's ](#differences-in-rendering-tocs)

* * * * * * * * * *
 

# Manage Table Of Content on Wiki pages

The Markdown language for Bitbucket supported a `[TOC]` macro which created and updated automatically a table of content (**TOC**) on each Wiki page.

There is no known way to do the same with GitHub Markdown.

For obvious reasons, GitHub doesn't allow to execute arbitrary code on their servers as part of server-side Git hooks. 

Thus, the easiest way to create and update TOC's on Wiki pages is to use a client-side script on a local copy of the remote Wiki. This approach is similar to the handling of navigation bars for Wiki pages and it has the same disadvantages:

* If a Wiki page is edited on the server, then the TOC may get out of sync.
* If a Wiki page is edited locally, then the user *should* run a script to handle necessary updates of the pages TOC. This can be automated with a client-side Git hook, but this hook needs special manual installation by each local user.

## The `AddToc.py` script

### Purpose of the script

This script finds all pages/MD files in the Wiki and adds or updates the table of contents to those files which have a navigation bar. There is a list of MD files (exception list) that don't get a TOC.

### Running the script

* Ensure Python is installed on your computer (no additional modules required).
* Run first `git pull` before locally editing Wiki pages or running the script so that the Wiki on the server and its local copy are in sync.
* After finishing with edit open a command window, change to the `Tools` subdirectory of the local copy of the Wiki and run the script `AddTOC.py` located in this subdirectory.
* `stdout` (output to the command window) informs about actions carried out by the script on the Wiki pages. There are 3 possible types of output messages:
    * `Page left without TOC:  ..\file.md`   - no TOC added to this file, file is in special exclusion list
    * `TOC on page ok.         ..\file.md`   - file has valid TOC, no change to the file
    * `TOC updated:            ..\file.md`   - file has been changed and has got updated (or new) TOC


### Using the script in a client-side hook

The script can be started automatically during a `git commit` when defining a client-side hook. To configure the hook put a file with the name `pre-commit` into the `hook` subdirectory of the local Wiki copy with the following content:

~~~
python ./Tools/AddToc.py
git add -u 
exit 0
~~~

**Prerequisite:** Python must be installed.

**Warning:** The hook script always exits with exit code 0. If by some reason `AddToc.py` fails to run as expected, then the user should - if necessary - remove the change made by `git add -u`.

### Limitations of the script

The following limitations hold true for the script and the handled MD files:

* Supported Wiki languages are English, German, Spanish, and Russian. If other languages than the mentioned ones are included into the Wiki, then the list of non-ASCII alphabetic characters has to be updated in the the script.
* Filenames in the complete Wiki including QMapTool should be unique
* Restrictions for header lines in Wiki pages:
    * only atx-like headers are handled (those with one or more "#" at the begin of a line)
    * a header line should have its "#" prefixes starting in column 1
    * header lines should be unique within a Wiki page
    * header lines should be on 1 line
* Code blocks can be delimited by **```** or by **~~~**. No mixture of both allowed    
* Supported and tested header line formats include the following ones:
    * `C1.) Compile the GDAL library, http://www.gdal.org/` (special characters and link)
    * `The _Markdown_ Language` (italics)
    * `The ``markdown`` language in action` (code)
    * `![EditDetails](images/icons/EditDetails.png) View / Edit Details` (image link)  
     *Remark:* If `EditDetails` appears in front of `View / Edit Details`, then referenced image file is not found and instead of the image there appears the supplied image title.
    * `Only lowercase German non-ASCII: Lüdenscheid` (works with Google Chrome browser, too)
    * `Spanish and German characters: Äáäéíñóöúü` (works in GitHub, not with Chrome)
    * `Загрузка файлов из Интернета`  (doesn't work with Chrome)
    * `Cyrillic text Mixed with Other text: Загрузка файлов из Интернета` (doesn't work with Chrome)
* The TOC in a Wiki page starts with a special line that consists of the word `Table of contents` included into the label `***`.
* The TOC in a Wiki page ends with a special line that consist of 10 `*` characters separated by spaces.
* The TOC in a Wiki page is located immediately after the navbar on top of the Wiki page
* The TOC shouldn't be changed manually
* A TOC is inserted into a Wiki page only 
    * if there is a navbar on top of the page and
    * if the file is not included in the special exclusion list of the script.

### Used anchor building (slugify) method

For handling non-ASCII header lines in GitHub correctly the usual method for anchor/link building (the so-called slugify method) was modified. It consists of the following essential steps:

* Open MD file and find all header lines (lines starting with 1 or more "#" characters).
* If there is an image link in the header line, replace it with "-".
* Remove all characters not in the list `0-9a-zа-яßáäéíñóöúü\s-` (list consists of all digits, alphabetic characters of used languages, whitespace and "-").
* Convert all ASCII characters to lowercase.
* If uppercase non-ASCII characters are in the remaining string then add the prefix `user-content-` to the string.
* Replace whitespace with "-".



## Differences in rendering TOC's 

Markdown files (Wiki pages) can be rendered using various rendering engines: GitHub, BitBucket, Google Chrome with markdown extension, ...

These rendering engines are using different rules for link/anchor building in the case of non-ASCII header lines. The given script creates TOC's for rendering in GitHub. TOC links for header lines with non-ASCII characters might be broken when using different rendering engines. 

[Here](https://johnmacfarlane.net/babelmark2/?text=%5BGo+to+the+anchor%5D(%23i-have-an-anchor)%0A%0A%23+%D0%9E%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%8B%D0%B5+%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B8+QMS) you can see some of the rendering differences.

- - -
[Prev](AxMaintainIndex) (Maintaining the QMS Wiki Index) | [Home](Home) | [Manual](DocMain) | [Index](AxAdvIndex) | [Top](#) | (Discussion of extended activity system) [Next](DocActivityPlanning)
