[Prev](DeveloperTranslate) (Add translations) | [Home](Home) | [Manual](DocMain) | [Index](AxAdvIndex) | (Recommendations for editing QMS Wiki pages) [Next](AxMaintainAutoPages)
- - -

***Table of contents***

* [Developing Documentation](#user-content-developing-documentation)
    * [Prerequisites](#user-content-prerequisites)
    * [Remarks about the Markdown language](#user-content-remarks-about-the-markdown-language)
    * [General rules for building GitHub fragment identifiers](#user-content-general-rules-for-building-github-fragment-identifiers)
        * [Preliminaries and recommendations](#user-content-preliminaries-and-recommendations)
        * [General fragment identifier build rules](#user-content-general-fragment-identifier-build-rules)
        * [Differences for Google Chrome fragment identifier build rules](#user-content-differences-for-google-chrome-fragment-identifier-build-rules)
        * [Overview of slugify rules](#user-content-overview-of-slugify-rules)
    * [General recommendations for editing QMS Wiki pages](#user-content-general-recommendations-for-editing-qms-wiki-pages)
    * [QMapShack-specific rules for Markdown use](#user-content-qmapshack-specific-rules-for-markdown-use)
    * [Further recommendations for editing Wiki pages](#user-content-further-recommendations-for-editing-wiki-pages)
    * [Rules for new pages](#user-content-rules-for-new-pages)
    * [Offline editing workflow](#user-content-offline-editing-workflow)

    
* * * * * * * * * *


_(Valid as of QMapShack version 1.14.1)_

 
# Developing Documentation

## Prerequisites

* If you want to contribute to existing pages of the QMapShack (QMS) documentation Wiki at
GitHub, you should have sufficient knowledge of the installation and use of
    * the Markdown language,
    * the `git` tool for accessing the GitHub version control system and for keeping consistent a local copy and the QMS repository on the server.
*   If you want to create new Wiki pages or contribute to the index, then you need some more tools on your PC:
    * the `make` tool for adding some content to Wiki pages and for creating some files,
    * Python (version > 3.5) which is required by some `make` scripts,
    * `awk/gawk` and the `bash` shell which are required by some `make` scripts,
    * a Markdown browser extension.
    
    Windows users may install the [MSYS][MSYS] package which includes `make, awk/gawk`, and a bash shell.

    It is not in the scope of this page to describe in detail the use of the tools mentioned.
    
*   You should be registered at
    [GitHub](https://GitHub.com/ "GitHub registration") and should be logged in when working with the GitHub server.
*   If you want to do more than just correcting a typo (which can also be
    done directly on the
    [GitHub server][WIKI]), you should be working on a
    local copy (a clone) of the QMS GitHub Wiki repository.  

    If you have [git (tool for access to GitHub revision control system)][GitInstall] installed,
    you can clone the QMapShack Wiki by issuing the command

           git clone https://GitHub.com/Maproom/qmapshack.Wiki.git QMapShack-doc
          
    This command copies all Wiki repository files from the GitHub server to the `QMapShack-doc` directory on your PC. Contributing to the QMS Wiki now means that you have 
    
    * to edit one or more of the existing `*.md` files (Markdown files) or to create new ones,
    * to upload (push) the modified files to the QMS Wiki on the GitHub server.
    
    _Remember:_ the language used in the QMS Wiki is English.
    
*   Use an editor that supports UTF-8 encoded files. Any editing must be done with this encoding. Never use Latin-1 or another encoding!

    This is required because the Markdown language implemented on the GitHub server does not pass any HTML entities like for instance `&amp;`, `&ecirc;`, or the equivalent forms for the latter, `&#234;` and `&#x000EA;`, on to the HTML code. Rather, it renders `&amp;` into `&amp;amp;` which will then again be displayed literally as `&amp;` by your browser.  This is not a problem as long as you are only typing English text using 7-bit ASCII characters, even using any of the characters `&<>[]{}`.  But as soon as you are using German umlauts, French accented characters, or even more exotic glyphs, you cannot just use their standard HTML entities but rather **you have to make sure your editor correctly encodes these characters as UTF-8** or they will not be displayed properly.  And, of course, you'll have to know how to tell your editor to insert a UTF-8 character, say `Ê`,  directly into your file.
    
* Be aware that the Wiki pages are used to create a QMS offline help. If you include images in Wiki pages, save them in the Wiki and not elsewhere on the Internet.    

## Remarks about the Markdown language

*   **Documentation** regarding the Markdown language can be found in
    various places:

    *   John Gruber's original
        [Markdown syntax definition](https://daringfireball.net/projects/markdown/syntax "Markdown syntax")
        dating back to 2004.

    *   [GitHub Flavored Markdown Specification][GFM].

    *   Finally, you can look into any of the `*.md` files in the QMS
        repository and at the same time point your browser to the
        corresponding web page at the
        [GitHub server][WIKI]
        to see the effect of a particular Markdown clause.  And if you
        want to see the HTML source of the current page in your browser,
        and your browser happens to be Firefox, just type `Ctrl-u`
        (other browsers may or may not need different handling, but most
        decent browsers will be able to display the HTML source of the
        current page one way or the other).

*   **Important note:** Mind that a Markdown file isn't just a text
    file you're looking at using a browser.  For instance, a Markdown
    file containing the line

         For more information see here: http://x.y.z.com
          
    will result in an HTML file where you cannot even click the URL in
    your browser!  Instead, this line should be written as

         For more information see [here](http://x.y.z.com).

    in Markdown.  In this case, the word `here` will be clickable in
    your browser, taking you to `http://x.y.z.com`.

*   **Fragment identifiers:** This term refers to the optional last part
    of a URL which is separated from the rest using a _hash sign_ (`#`),
    as in `http://x.y.z.com#chapter_1`.  When you click such a URL, the
    part to the left of the hash sign (`http://x.y.z.com`) specifies the
    HTML file to open, while the fragment identifier to the right
    of the hash sign (`chapter_1`) specifies a label defined somewhere
    in the HTML code itself to which your browser then is pointed.

    Using Markdown you cannot directly define labels corresponding to your own fragment
    identifiers but Markdown implicitly defines several labels which you can use in URLs, provided you know them.
    To refer to a label "identifier" defined in the current
    file use something like
  
    **'[text\](#identifier)'**
  
    and to refer to a label in another file in the same
    directory use

    **'[text\](file#identifier)'**

* If a Markdown header line in a GitHub Wiki page completely consists of ASCII characters without any additional Markdown formatting, then a fragment identifier referencing this header line can be built by applying the following rules:

    1. Delete leading and trailing spaces of the header text.
    1. Convert the header text to lowercase.
    1. Remove anything that is not a letter, number, space, underscore, or hyphen.
    1. Replace each space with a hyphen.
    1. Add the prefix `user-content-` (GitHub-specific optional but recommended prefix).     
   
    Thus, the fragment identifier referencing the ASCII header line

            ## My Header: example

    should be
    
            user-content-my-header-example
    * See [here][GeneralRules] for more general fragment identifier rules (also called slugify rules).
    * __Important remarks:__ 
        * The above-mentioned rules hold true only in the case that the text in the header line consists solely of ASCII characters.
          For text with non-ASCII characters, the construction rules for fragment identifiers are more complicated and may depend on the Markdown implementation used.
        * Valid fragment identifiers working in the GitHub Wiki may not work when using them in other Markdown browsers and vice versa.
        * A reliable way to find a fragment identifier for a header is as follows:       
            * Upload (push) the page to the GitHub Wiki and open it there.
            * Go to the HTML source text of the Wiki page (try `CTRL-u` or use context menu!).
            * Find the header text in the HTML source text.
            * Take the value of the HTML `id` attribute as fragment identifier.
            * _Example of source code and fragment identifier for a header with non-ASCII characters:_
            
                Markdown header line with Cyrillic (i.e. non-ASCII) characters:
               
                    ## Cyrillic_text: Загрузка файлов из Интернета
                   
                HTML source code for this text found in GitHub:
               
                    <h2>
                    <a id="user-content-cyrillic_text-Загрузка-файлов-из-Интернета" class="anchor" 
                      href="#cyrillic_text-..."    <=== (...: url-encoded Cyrillic text)
                      aria-hidden="true">
                      ...
                    </a>
                    Cyrillic_text: Загрузка файлов из Интернета
                    </h2>

                GitHub-specific fragment identifier for the given header:  

                    user-content-cyrillic_text-Загрузка-файлов-из-Интернета         

                _Remarks:_ 
                
                * The identifier shown is different from the one used e.g. in Google Chrome for the same header.                    
                * As can be seen in this example, the fragment identifier is the value of the `id` attribute of the anchor (`a`) tag within the header tag (`h2` in the example).

## General rules for building GitHub fragment identifiers

*(These rules are also called **slugify** rules.)*

### Preliminaries and recommendations

* Links from a Markdown Wiki page to HTML pages on the Internet have to follow the normal rules for URLs.    
* Markdown supports links to sections in the same or some other Markdown-formatted page. Markdown links can be built in one of two forms:
    * **[linktext\](filename#fragment "description")**
    * **[linktext\][linkref\]** ===> **[linkref\]: filename#fragment "description"** (reference-style link)
            
    The "filename" part of the link must follow the GitHub Wiki rules for filenames. It must be an ASCII string of letters, underscores, and hyphens without a file extension and without a path.  
            
    In both cases of links, the "description" part is shown as tooltip text when hovering with the mouse over the  link in a Markdown viewer/browser. This part is recommended but can be omitted.
            
    The "#fragment" part of the link is optional and identifies the referenced section of a page.  A Markdown section should be started with a section header line consisting of one or more hash characters ("#") followed by the header text for the section. The "fragment" part is derived from the section header following certain rules. 
            
    Rules found on the Internet for this purpose are quite often formulated under the assumption that the header consists of ASCII characters only, i.e. that the header text is an English text. These rules fail when using arbitrary languages and thus arbitrary Unicode characters in the header. In this case, each Markdown viewer (GitHub Wiki, Google Chrome, VS code, ...) makes use of a separate set of rules without making the rules  explicit. 
            
    The "fragment" part must be equal to the value of the `id` attribute of the referenced section header in the HTML page used to render the Markdown page in a Markdown viewer/browser. Typically, the rules for building the `id` attribute can be found only by trial and error.
            
    Markdown pages written for the QMS documentation must use "fragment" building (slugify) rules suitable for the GitHub Wiki. This may imply that some links to headers with  non-ASCII characters are broken when rendering the Markdown page in a different Markdown viewer. 
            
    QMS documentation is available also in an offline  version. The offline version is built from HTML pages obtained with the help of a special Markdown-to-HTML converter. This converter guarantees that all links to the same or other Wiki pages are correct in the converted page if the rules [described later][GeneralRules] have been applied when building the "fragment" part of a link. 
  
* When defining section headers try to use as many ASCII characters as possible. Try to avoid as many non-ASCII characters as possible. This reduces the likelihood of making errors in link building and increases the likelihood that the links work in different Markdown viewers.
* Don't use Markdown formatting (emphasis, links, images, ...) in header lines. Otherwise, check carefully that   links to such a header work as expected.
* The rules described here are such that as many links as possible work also in Google Chrome. Without this requirement. rules could be formulated in a slightly different form.
* The rules used in the GitHub Wiki are not known in detail and they can't be changed. Thus, links in MD files  (e.g. in the table of contents and elsewhere) **must** have the form required by GitHub. The consequence is that links with  non-ASCII uppercase letters and other non-ASCII Unicode characters fail to work in Chrome. A typical  description of the slugify algorithm (the build rules for fragment identifiers) states: "convert everything to lowercase". This statement is wrong in the case of non-ASCII letters in the GitHub Wiki, it is true in Google Chrome.
* Conversion of MD to HTML for the QMS offline help is under user control. Thus, when converting Markdown links to HTML necessary link adjustments  are possible using preprocessing or postprocessing in the Python Markdown module used for this conversion.          
* Some Markdown-to-HTML converters found on the Internet have considerable weaknesses when handling  special formatting in headers and when handling non-ASCII characters!
* The slugify rules described in the next section should be correct for all languages. *Rules are found by trial and error in the case of non-ASCII characters. Thus, there can be still some failures!*
* The Markdown-to-HTML converter (i.e. the Python script `HTMLMake.py`) used to create HTML pages for the QMS offline help recreates the table of contents (TOC) on top of the page using the Markdown header lines. A Python markdown module extension is used for this purpose. In the case of errors in TOC links in the HTML pages, the `slugify` method used in the converter must be adjusted.
          
### General fragment identifier build rules

1. If the header contains an image link of the form **"!\[some_text\](...)"**, then drop it.
1. If there is an italic Markdown using underscores (`_text_`), then drop the underscores (rule found by trial 
 and error!).
1. Strip leading and trailing whitespace from the header.
1. Replace each whitespace character (Unicode category Cf) with a hyphen.
1. Convert **all ASCII uppercase characters and only those** to lowercase. **Don't change non-ASCII uppercase   letters!** (i.e. change only ASCII letters with Unicode category Lu),
1. Keep unchanged all characters belonging to Unicode categories 
    * Ll (lowercase letters), 
    * Lo (other letters, e.g. º), 
    * Nd (decimal digits, e.g. 019𝟓𝟘), 
    * Nl (Number (letter), e.g. Ⅷⅲ), 
    * Pc (Punctuation (connector), e.g. underscore), 
    * Pd (Punctuation (Dash), e.g. hyphen),  
1. Drop all characters belonging to Unicode categories
    * Cf (Other (format), e.g. ZERO WIDTH SPACE)
    * No (Number (Other), e.g. ²³¾፲₄⑥⑵), 
    * Pe (Punctuation, (Close), e.g. )]), 
    * Pf (Punctuation (Final quote), e.g. »), 
    * Pi (Punctuation (Initial quote), e.g. «), 
    * Po (Punctuation (Other), e.g. !"#%&'*,./:;?@\¡¿), 
    * Ps (Punctuation (Open), e.g \(\[), 
    * Sc (Symbol (Currency), e.g. £₤€₽￥), 
    * Sk (Symbol (Modifier)),
    * Sm (Symbol (Math), e.g. +<=>|→⇔∈), 
    * So (Symbol (Other), e.g. ©™↘⇨⏻►✔✘𝄞👍😁😩🚚)
1. Prepend the prefix `user-content-` to the remaining string.

### Differences for Google Chrome fragment identifier build rules

1. Differences occur only for headers with non-ASCII characters or with special Markdown formatting.
1. Keep only **"some_text"** in the case of an image link of the form **"!\[some_text\](...)"**.
1. Keep unchanged Unicode characters with category "No" (other numbers, e.g. `²³`).
1. Keep unchanged non-ASCII Unicode characters with categories No, Pf, Pi, Po, Sc, Sk, Sm, So (found by trial and error for characters used in the QMS Wiki).
1. Don't prepend the `user-content-` prefix to the link.

### Overview of slugify rules

The following table describes the slugify action to be taken for characters in tested [Unicode categories][UCDcats]:

| Unicode category | GitHub action | Chrome difference | Characters tested |
| ---------| --------- | ------------- | ----------- |
| Cf | drop | - | Unicode ZERO WIDTH SPACE |
| Ll | keep | - | a...zßàáâäçèéêëìíîïñòóôöùúûüýąćčďęěłńňœŕřśšťůźżžавгезийклнортуфяёաենրւև|
| Lo | keep | - | º |
| Lu | if ASCII then to lower, keep others | - | A...ZÀÁÄÇÈÉÊÍÑÓÖÚÜÝĄĆČĎĘĚŁŃŇŘŚŠŤŮŹŻŽАЗИЯԵ|
| Nd | keep | -  | 019𝟓𝟘 |
| Nl | keep | -  | Ⅷⅲ |
| No | drop  | keep  | ²³¾፲₄⑥⑵ |
| Pc | keep | - | _ (underscore) |
| Pd | keep | - | - (hyphen) |
| Pe | drop | - | )] |
| Pf | drop  | keep non-ASCII | » | 
| Pi | drop  | keep non-ASCII | « | 
| Po | drop  | keep non-ASCII | !"#%&'\*,./:;?@\¡¿ |
| Ps | drop | - | ( \[ |
| Sc | drop  | keep non-ASCII|  £₤€₽￥ |
| Sk | drop  | keep non-ASCII |  \`¨ |
| Sm | drop  | keep non-ASCII |  +<=>\|→⇔∈ |
| So | drop  | keep non-ASCII |  ©™↘⇨⏻►✔✘𝄞👍😁😩🚚 |
| Zs | convert to hyphen | - | SPACE |
          
## General recommendations for editing QMS Wiki pages

*Remark: In the examples in this section some backslashes added to escape the Markdown meaning of a few special characters!*

* If you are editing an **already existing** `*.md` file:
    * Leave the navigation bars at the top and bottom of it unchanged.  The top navigation bar looks like

            \[Prev](... | \[Home](... | \[Manual](... | ...
            - - -

        while the bottom navigation bar looks like

            - - -
            \[Prev](... | \[Home](... | \[Manual](... | ...
            
    * Do not use the Markdown directive `\- \- \-` to insert a horizontal rule, that is, a horizontal line running from the left edge of the browser window to the right edge.  This special way of coding a horizontal rule is regarded as part of the navigation bars and will be removed anywhere else in the file when the navigation bars are automatically inserted or updated.  Rather, use the Markdown variants `---` or `\*\*\*`, if you need a horizontal rule somewhere in your Markdown file.
    *   Leave the header and footer line of the table of contents (TOC) at the top of the page unchanged. These lines look like
    
             \*\*\*Table of contents\*\*\*
            
             ...

             \* \* \* \* \* \* \* \* \* \*            
        
    * If necessary, update the links in the table of contents after changes in the section headers.
    
* Be conservative when editing an existing file: try to maintain the general look of the original file.
* You can edit an existing or create a new `*.md` file either online or [offline][EditOffline], the latter being the preferred method. **Online editing is discouraged and should only be used for minor changes like correcting a typo!**

    One reason for discouraging online editing is that it causes the
    GitHub server to use a stereotype `Edited online` commit
    message which doesn't convey any real information as to **why** a
    particular change was made to the Wiki repository.  But keeping
    track of why a change was introduced is one of the benefits of
    maintaining the Wiki as a GitHub repository.  Another
    reason for discouraging online editing is that the GitHub server
    does neither check the contents of your file nor update its
    navigation bars. So either don't use online editing at all or only
    use it for really trivial changes.

    And finally, being able to use your favorite editor at home will
    presumably make life easier for you, should the editing involve
    major searching, mass changes, or cut-and-paste operations.

*   Thoroughly check your edited text, in particular, make sure **you don't
    introduce broken links**.  This checking can, of course, be done
    more easily and more thoroughly offline. Thus, this is just
    another reason for discouraging online editing.

## QMapShack-specific rules for Markdown use

* Use [GFM-compatible Markdown][GFM].
* New files/pages must have ASCII-only filenames.
* All extensions in filenames (`.md` and some others used in the Wiki) must be lowercase.
* The encoding of Wiki pages must be UTF-8. Don't use a different encoding like Latin-1! Don't use editors not supporting UTF-8!
* Use only `ATX`-type section headers, i.e. those initialized by one or more hashes `#`. Don't use setext-type section headers (those with underlining in the next line).
* Each page must have exactly one top-level header, i.e. a line of the form 

        # Header_of_page
        
    Other sections of the page should be subsections of the top-level header (section) and form a tree structure. 
      
* Use a header text only once on a page (i.e. headers on a page must be unique).
* Don't use extra formatting in headers (images, emphasis, links, ...).
* Don't use footnotes (not supported in GitHub Wiki).
* Unordered lists should be labeled with `*` or `-` and not with another character.
* Lists on the top-level must have their label in the leftmost column (no indentation of the label).
* Add a title (a description) to each link, i.e. in a link of the form 

    **!\[text1]\(some_url "description")**

    the **"text1"** and **"description"** parts must be meaningful non-empty strings.
    
* The table of contents of a page must have an entry for each header on the page. The entry must be a link to the header. Edit the table of contents of the page properly and with correct links.
* Save snapshots or images used in Wiki pages in the Wiki itself and not in the cloud or somewhere else on the Internet.
* Limit the size (especially the width) of images. Large images in Markdown/HTML files are automatically scaled by some browsers (so-called "responsive images"). 
  This doesn't hold true for some versions of the Qt help browser used to display the offline QMS help. 
 
## Further recommendations for editing Wiki pages

* Spell-check the text.
* Be aware that the formatting of a Wiki page as seen on the GitHub server and the one seen in some local Markdown browser may be different. Thus, always check formatting on the server as the last editing step.
*   Test carefully, if formatting is correct. If any possible, check the layout with 
    * some Markdown viewer (browser or editor with Markdown extension) _and with_
    * HTML files derived from the modified Markdown files (procedure is described [later][EditOffline] on this page).
    
    Pay special attention to
    
    * correct indentation (lists, images, code, ...),
    * correct use of empty lines,
    * correct rendering of images.
    
* Test if links work correctly. Repeat the test after uploading the page to the QMS repository on the server. When using non-ASCII characters in a header then check carefully, if links to this header work correctly.

* Images for the QMS part of the Wiki have to be located in child directories of the `images` subdirectory. Those for QMT are located in the `QMapTool\images` subdirectory (without further subdirectories).
* The QMapTool (QMT) Wiki part is located in the `QMapTool` subdirectory of the QMS local Wiki directory. 
* Links to images in pages of the QMT Wiki must have the form required by GitHub (the relative path to the image should be `QMapTool/images/`).

    _Example:_
  
    **!\[Input of ...\](QMapTool/images/RefToolCoord.jpg "Input of ...")**
      
* `QMapTool` is the only subfolder with Markdown files. All QMS Markdown files of the Wiki should be 
  located in the root directory (in the example used on this page: `QMapShack-doc`) of the Wiki.
* The GitHub Wiki merges the QMS and QMT part filenames into one large list of filenames without path. 
  This implies, that filenames in the complete Wiki (QMS and QMT) must be unique. To achieve this, some 
  filenames start with a `QMT` prefix. 
* [Offline help for QMS and QMT][HelpOffline] is split into 2 separate packages. In links from the QMS part of the Wiki to the QMT part or vice versa the target address must be an external link to the Wiki on the server (i.e. a link to `https://GitHub.com/Maproom/qmapshack/Wiki/...`. Otherwise, offline help can't handle the link correctly.
* Only files in the root directory and the `QMapTool`, `images`, and `Downloads` subdirectories are used when preparing QMS and QMT offline help. If using additional subdirectories, then the generation of offline help must be adjusted.

## Rules for new pages

*   If the file you want to edit does **not yet exist**, select a
    **blank-free** name for it which **only** consists of **plain upper-
    and lowercase ASCII characters**,
    **digits**, and **underscores** (`_`). Accented characters, umlauts, or other non-ASCII characters are not allowed in filenames for Markdown and other QMS Wiki files. Do your best to mimic the naming scheme used by already existing files.
    
    **Mind that the `.md` extension is mandatory when creating a new  Markdown file offline!**  If you omit the `.md` extension, neither the local scripts nor the GitHub server will recognize your file as a Markdown file.


*   If the file you want to edit does **not yet exist**, create it in the
    sub-directory `playground` of the local Wiki copy.  This way your new file does
    neither disturb others 
    while you are developing the contents of your file nor do other
    people's operations add currently unwanted changes to
    your file which is still in the making.  And you can develop your
    file at your own pace over a longer period of time or also ask
    others to have a look at it before it is _really_ added to the Wiki.
    
    Mind that links in a new QMS Markdown file which point to other QMS Wiki
    files have to be temporarily prefixed with `../` as in

        [Text](../File)

    or they will not be resolvable while you inspect your work online on
    the GitHub server or offline by manually [converting Markdown files to HTML][EditOffline].
    
    For new QMapTool Markdown files, the prefix should be `../QMapTool/`.
    
    Having finished editing move your file to its final location in the Wiki (root directory of local Wiki copy for QMS files, `QMapTool` subdirectory of the root directory for QMT files) and don't forget to remove the extra `../` or `../QMapTool/` link prefix and commit and push your changes to the server repository using the `git` tool.

*   If the file you want to edit does **not yet exist**, do not try to
    manually add to it the navigation bars you see in all the other Wiki
    files because this could cause confusion. Navigation bars will be created [later][Workflow]. Just add the following header and footer lines for a table of contents at the top of the page:
    
        \*\*\*Table of contents***
            
        ...
 
        \* \* \* * * * * * * *           

      (some backslashes added to avoid misinterpretation!)  and add a link to each header line on the page between the header and the footer (compare with an existing Markdown file!).

    The TOC should be followed by the top-level header line.


## Offline editing workflow

* Just open an existing `*.md` file or create a new one as described [above][NewMD] in your favorite UTF-8 capable editor and edit it to your heart's content.

*   If you finally decide to really include your new contributions into the Wiki,
    some more steps are necessary:

    *   Ensure that the GNU tools `make` and `gawk` (implicitly called from `make`) and the Python interpreter can be used.
    *   If your file is saved in the `playground` subdirectory and you followed the recommendations in the section ["Rules for new pages"][NewMD] about prefixing links, then remove all these prefixes, i.e. for QMS files change all strings of the form `]\(\.\./`  to just  `]\(` (inline links, backslashes added to avoid misinterpretation) or from the form `]: ../xxx` to `]: xxx` (reference links)
        else these links will no longer be resolvable after moving the file to its final
        location.

    *   Move your file from the `playground` subdirectory one directory level up in the case of a QMS file and to the sibling subdirectory `QMapTool` in the case of a QMT file.

    *   If your new file isn't reachable via some link occurring in one of
        the other Wiki files, it is dead.  Or at least as good as
        dead.  There is a good chance that nobody ever reads your text.
        So there should always be at least one link to it in the other
        Markdown files. The recommended way is to add a link to the new page at a proper location in the global TOC maintained at the end of the file `DocMain.md`. This will also ensure the correct construction of navigation bars on the page in a later step.
    
    * If you changed the content of the TOC in one of the edited files, then update the global TOC of the Wiki. To do this follow the instructions described [here][TC]. Running the Python script `Tools/CompareIdxToc.py` in the `Tools` directory helps to identify inconsistencies between the global Wiki TOC and the source file `Tools/(QMT)AxData4Index.txt` for the global index.
    
    * Having added new content to the Wiki it is good practice to add some additional index entries to the global Wiki index. To do this follow the instructions described [here][IDX]. Rebuild the global index by running the Python script `Tools/BuildIndex.py` in the `Tools` directory.  

    *   If you are done with editing, run the command

            make nav
            
        from the top-level directory of your Wiki repository.    

        This will update or add the top and bottom navigation bars of each `*.md` file affected.  
        
        Under some circumstances (in particular, when running it for the very first time) the command `make nav` might process more than just the files you changed. However, it should normally not introduce any real changes (not even changes to file modification dates) which aren't caused by your own work.
        
    *   _Optional, but recommended:_ Convert the edited Markdown files to HTML files and check again the formatting with the help of the HTML file. Conversion is done by running the command

            ./Tools/HTMLMake.py your_markdown_file.md
            
        The result of the conversion will be a file `doc/HTML/your_markdown_file.html`. This file is used in the [QMS offline help][HelpOffline].
        
    * Now your edited files are ready for upload (push) to the GitHub server. For this run the following `git` commands from the top-level directory of your Wiki repository:

        * `git status`

            Check the list of file changes to be sent to the server. All your changes must be listed there with their correct locations.

        *  `git commit -a -m "your commit message here"` 
        
            and then 
           
            `git push`
        
            If you don't know the correct usage or the purpose of these commands just run `git commit --help` resp. `git push --help`.

            The last command pushes all changes in Wiki files to the Wiki repository on the server. You might need your GitHub password for this step.
            

[GitInstall]: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git "Git installation"
[GFM]:        https://GitHub.GitHub.com/gfm/ "GitHub Flavored Markdown Specification"
[WIKI]:       https://github.com/Maproom/qmapshack/wiki "QMS Wiki on GitHub"
[MSYS]:       https://www.msys2.org/ "MSYS installation"

[EditOffline]: #offline-editing-workflow "Offline editing"
[General]:     #general-recommendations-for-editing-qms-wiki-pages "General recommendations"
[NewMD]:       #rules-for-new-pages "Rules for new pages"
[Workflow]:    #offline-editing-workflow "Offline editing - workflow"
[IDX]:         AxMaintainIndex "Maintain QMS index"
[TC]:          AxMaintainPageTOC "Maintain QMS TOC"
[HelpOffline]: OfflineDocumentation  "Offline help"

[GeneralRules]: #general-fragment-identifier-build-rules "General fragment identifier build rules"

[UCDcats]:     http://www.fileformat.info/info/unicode/category/index.htm "Unicode categories"

- - -
[Prev](DeveloperTranslate) (Add translations) | [Home](Home) | [Manual](DocMain) | [Index](AxAdvIndex) | [Top](#) | (Recommendations for editing QMS Wiki pages) [Next](AxMaintainAutoPages)
