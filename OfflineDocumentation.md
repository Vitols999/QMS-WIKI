[Prev](Ubuntu-18-HowTo) (Compile Instructions for Ubuntu-18) | [Home](Home) | [Manual](DocMain) | [Index](AxAdvIndex) | (Getting started) [Next](DocGettingStarted)
- - -

***Attention: This page describes features tested only with the Bitbucket Wiki!***

# Using Offline Documentation

The online _QMapShack_ documentation (which you are probably just reading)
is also available as offline documentation in the [QMSgithub wiki](https://github.com/Maproom/qmapshack)  If you
have _GIT_ installed, you can clone the _QMapShack_ wiki by issuing
the command

        git clone https://github.com/Maproom/qmapshack.wiki.git QMapShack-doc

The wiki consists of _Markdown_ (`*.md`) files, and to read
them you will either need some _Markdown_ plugin for your browser or
you'll need to create `*.html` input files for your browser from the
`*.md` files as described below.

## Prerequisites

To create the `*.html` files from the corresponding `*.md` files you
will need:

* _Python_ 2.7 or better.

* _Python_'s _Markdown_ module version 2.6.6 or better plus the
  following standard _Markdown_ extensions:

     * _Abbreviations_[^1]
     * _Definition Lists_[^1]
     * _Fenced Code Blocks_[^1]
     * _Footnotes_[^1]
     * _Sane Lists_
     * _Table of Contents_
     * _Tables_[^1]
     * _WikiLinks_

    Installation instructions for _Markdown_ and its aforementioned
    extensions are for instance available
    [here](https://python-markdown.github.io/install/).

* _GNU_ `make`.  The makefile provided for maintaining the offline
  documentation uses "simply expanded variables" (defined via "`::=`",
  as introduced by the Posix standard in 2012)[^2]

[^1]: These extensions are sub-extensions included in _Python_'s
_Markdown_ _Extra_ extension.  Since these are the only sub-extensions
of the _Extra_ extension which are supported by the Bitbucket server,
these are also the only extensions of the _Extra_ extension used by the
conversion script.

[^2]: If your version of `make` can't handle "`::=`" and you can't find
or install another one, simply replace all occurrences of "`::=`" in file
`Makefile` in the documentation directory with "`=`".  In this makefile
using "simply expanded variables" (defined via the "`::=`" assignment)
rather than "recursively expanded variables" (defined via the normal
"`=`" assignment) is just a matter of efficiency: referencing variables
assigned with "`::=`" will burn less CPU cycles but in the case at hand
will not produce different results in any way ("`::=`" is the type of
variable assignment we are used from normal programming languages, while
"`=`" behaves more like a function definition).

## Building the `*.html` files

Change into the `QMapShack-doc` directory containing the offline documentation
and issue the commands


```
#!bash
cd QMapShack-doc
make doc
_YourBrowser_ DocMain.html
```

This will create any new and update all outdated `*.html` files before
it opens your browser at the main documentation page.  If you plan to
frequently reference the offline documentation, you might consider
creating a command alias from the last command line above by executing

>    alias qms-doc='_YourBrowser_ /_absolute_/_path_/_to_/doc/DocMain.html'[^3]

[^3]:  Under _Cygwin_ you should instead use

>    alias qms-doc="_YourBrowser_ $(cygpath -w /_absolute_/_path_/_to_/doc/DocMain.html)"

because in that case the argument passed to your browser must be interpretable as a Windows path.




///Footnotes Go Here///
- - -
[Prev](Ubuntu-18-HowTo) (Compile Instructions for Ubuntu-18) | [Home](Home) | [Manual](DocMain) | [Index](AxAdvIndex) | [Top](#) | (Getting started) [Next](DocGettingStarted)
