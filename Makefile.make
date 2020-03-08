
# makefile to create Qt help packages for QMapShack and QMapTool

# The extension ".make" is used for this file to avoid conflicts with already existing Makefile in same directory!

# Run after setting config parameters inside this script (see below): 
#   `make -f Makefile.make all` (on Windows start in msys shell!)

# To check if configuration is correct: 
#   `make VERBOSE=YES -f Makefile.make check` 

# If configuration parameters are set on command line change to
#   `make PYTHON=name_of_python_executable ... -f Makefile.make ...` 

# Prerequisites:

# - local copy of QMS Wiki (git should work in this copy!)
# - Python 3.6 or better, used Python scripts are not executable and might not have correct shebang lines.
# - Python package "Pillow" version 3.2.1 or better (to install run: `pip install --upgrade Pillow`)
# - Python package "Markdown" version 7.0.0 or better (to install run: `pip install --upgrade Markdown`)
# - qhelpgenerator (from Qt5 installation)
# - (Gnu)make 4.1
# - msys for Windows
# - git

# Supported makefile targets:

#   help:  show help info 
#   check  check if used script and project files can be found
#   clean: delete all HTML and .q* Qt Help files
#   doc:   generate HTML from MD
#   build: generate compressed Qt help files
#   run:   build packages and open QMS help with assistant
#   all:   run clean and build (rebuild all)

# Software versions used with Ubuntu 18.04 for tests:
#   make 4.1
#   Qt5.9.5
#   Python: 3.6.8
#   Qt Collection Generator version 1.0 (Qt 5.9.5)
#   git 2.17.1

# Software versions used with Windows10 for tests:
#   make 4.1
#   Qt5.14.0
#   Python 3.7.6
#   Qt Help generator version 1.0 (Qt 5.14.0) (`qhelpgenerator`, if not available, use deprecated `qcollectiongenerator`)
#   git 2.23.0.windows.1
#   GNU bash, version 3.1.17(1)-release (i686-pc-msys)

# Used files:

# Input files: files relative to main directory of local copy of QMS Wiki:
#     * MakeFile.make: this file
#     * *.qhcp Qt: help collection configuration files
#     * Tools/HTMLMake.py, Tools/QMSQtHelp.py: Python scripts for generating .html and .qhp files 
#     * QMapTool/qmsstyle.css (doesn't appear as dependency in this Makefile!)

# Output files: *.qhc, *.qch Qt help files

# Intermediate files (can be removed): .html files for all Wiki pages used for the help package, .qhp Qt help configuration files

# List of all files used for generating QMS Qt help:

#        A.png
#        Makefile.make
#        QMSAllHelp.qhcp
#        QMSHelp.qhcp
#        QMTHelp.qhcp
#        QMapShack.png
#        QMapTool/qmsstyle.css
#        Tools/HTMLMake.py
#        Tools/QMSQtHelp.py
#        about.txt
#        about_de.txt

#################### Configuration ################################

# set necessary values for the variables PYTHON, HELPGENERATOR, QTDIR (names of the executables and path to qhelpgenerator/qcollectiongenerator)
# all variables can be set on the command line

# use VERBOSE::=YES to display some configuration info when starting the script

# see also comments in HTMLMake.py and QMSQtHelp.py!

# switch to enable output of some info about the script - can be set on command line
VERBOSE ::=

# Example of OS-specific setup:
ifeq ($(OS),Windows_NT)
    QTDIR ::= d:/Qt/5.12.3/5.14.0/msvc2017_64/bin/
    PYTHON ::= python37
    HELPGENERATOR ::= $(QTDIR)qhelpgenerator
else
    QTDIR ::= 
    PYTHON ::= python3

    # qcollectiongenerator is flagged "deprecated" in newer Qt5 versions!
    # "qhelpgenerator" might not be available for older Qt5 versions!
    HELPGENERATOR ::= $(QTDIR)qcollectiongenerator    
endif

##################### End of configuration ###########################

# check existence of executables
res ::= $(shell which $(PYTHON))
ifeq ("$(res)", "")
    $(error Configuration error: can't find $(PYTHON))
endif

res ::= $(shell which $(HELPGENERATOR))
ifeq ("$(res)", "")
    $(error Configuration error: can't find $(HELPGENERATOR))
endif

ifdef VERBOSE
    $(info )
    $(info Configuration info:)
    $(info .   OS:                             $(OS))
    $(info .   Make version:                   $(MAKE_VERSION))
    $(info .   Shell version:                  $(shell sh --version))
    $(info .   Qt5 directory used (QTDIR):     $(QTDIR))
    $(info .   qhelpgenerator (HELPGENERATOR): $(HELPGENERATOR))
    $(info .      version:                     $(shell $(HELPGENERATOR) -v))
    $(info .   Python executable (PYTHON):     $(PYTHON))
    $(info .      version:                     $(shell $(PYTHON) -V))
    $(info .      Markdown:                    $(shell $(PYTHON) -c "import markdown;print(markdown.__version__)"))
    $(info .      PIL/Pillow:                  $(shell $(PYTHON) -c "import PIL;print(PIL.__version__)"))
    $(info .   Git:                            $(shell git --version))
    $(info )
endif
 
# Python scripts used: 
htmmake ::= ./Tools/HTMLMake.py
qmshelp ::= ./Tools/QMSQtHelp.py

# generated intermediate Qt help project files
qtproj  ::= QMSHelp.qhp ./QMapTool/QMTHelp.qhp

############################################### preparation of some file lists

# Wiki directories with images
IMGDIRS ::= ./QMapTool/images ./images

# list of all QMS/QMT image files
IMGS ::= $(foreach imgdir, $(IMGDIRS), $(shell git ls-files $(imgdir)))

# lists of QMT and QMS .md files
qmtsrc ::= $(shell git ls-files ./QMapTool/*.md)
qmssrc ::= $(shell git ls-files ./*.md)

# remove _Sidebar.md from files list - it isn't part of help package, but part of Wiki
qmssrcc ::= $(qmssrc:_Sidebar.md=)

# list of all MD files in QMS and QMT parts
src ::= $(qmssrcc) $(qmtsrc)

# replace .md suffix with .html suffix to get list of .html files belonging to .md files
srchtml ::= $(basename $(src))
srchtml ::= $(addsuffix .html, $(srchtml))

# The Wiki ./Downloads folder consists of text files with various extensions. Some of them belong to the Wiki,
# others not. Without using git information it is difficult to identify those belonging to the Wiki. We just keep
# list of extensions.

# These files must be handled in a special way

# list of all traced by git files in Downloads directory
down ::= $(shell git ls-files ./Downloads)

# list of all .html files belonging to Wiki files in ./Downloads folder
downhtml ::= $(basename $(down))
downhtml ::= $(addsuffix .html, $(downhtml))

# list of all required .html files (coming from .md and from ./Downloads)
tgthtml = $(srchtml) $(downhtml)

usedext ::= $(sort .py .wmts .tms .wcs .vrt)
downext ::= $(sort $(suffix $(down)))

# if next check fails, then this Makefile must be adjusted  in the targets part!
ifdef VERBOSE
    ifneq '$(downext)' '$(usedext)'
        $(info )
        $(info Check of download folder extensions:)
        $(info .    Used extensions:      $(usedext))
        $(info .    Downloads extensions: $(downext))
        $(error Downloads folder extensions different to used ones! Update Makefile rules!)
    else
        $(info )
        $(info Used extensions for ./Downloads folder:)
        $(info .    $(usedext))
        $(info .    Extensions ok.)
    endif
endif

# switch to allow generation of 1 help package for QMS and QMT - set it from command line!
ifdef SHOWALL
    allshow ::= QMSAllHelp.qhc
else
    allshow ::= QMSHelp.qhc  
endif

############################################ start of rules part
.PHONY: clean help all doc build check

# Default rule to display  "help" output 
help:
	$(info )
	$(info Usage:)
	$(info .   make [params] -f Makefile.make [help] # Display this text.)
	$(info .   make [params] -f Makefile.make check  # Check if used script and project files can be found.)	
	$(info .   make [params] -f Makefile.make clean  # Discard all "*.html" and ".q*" Qt help files.)
	$(info .   make [params] -f Makefile.make doc    # Update all outdated "*.html" files from MD files.)
	$(info .   make [params] -f Makefile.make build  # Sanitize all changed ".q*" Qt help project files)
	$(info .   make [params] -f Makefile.make all    # Run clean and build (rebuild all))
	$(info .     [params]:)
	$(info .        VERBOSE=YES:                      show configuration info)
	$(info .        PYTHON|QTDIR|HELPGENERATOR=value: set parameter value)  
	$(info )
    
# check if necessary files can be found (Python scripts and Qt help configuration files)
FILES2CHECK ::= $(htmmake) $(qmshelp) QMSHelp.qhcp QMTHelp.qhcp
    
check: $(FILES2CHECK)
	$(info )
	$(info All checked Python and help project files found.)
	$(info )    
    
$(FILES2CHECK):
	$(info )
	$(error File not found: $@)
    
# remove all HTML files belonging to MD files and all .qhp files
clean:
	$(info )
	$(info Removing intermediate files ...)
	@rm -f $(tgthtml) $(qtproj)

# Rule to update all outdated "*.html" files:
doc: $(tgthtml)

# Rule to create a single ".html" file from its Markdown resp. ./Downloads source file
# (we also have to re-create the ".html" file, should the conversion script change)

# if the list of used extensions in the Downloads folder was changed, then the list of 
# the following targets must be updated!

%.html: %.md $(htmmake)    
	$(PYTHON) $(htmmake) $<

%.html: %.tms $(htmmake)    
	$(PYTHON) $(htmmake) $<
	
%.html: %.vrt $(htmmake)    
	$(PYTHON) $(htmmake) $<

%.html: %.wcs $(htmmake)    
	$(PYTHON) $(htmmake) $<

%.html: %.wmts $(htmmake)    
	$(PYTHON) $(htmmake) $<    
	
%.html: %.py $(htmmake)    
	$(PYTHON) $(htmmake) $<    
    
# generate Qt help project files
%.qhp: $(tgthtml) $(qmshelp) $(IMGS)
	 $(PYTHON) $(qmshelp)
 
# avoid automatic deletion of help configuration files
.SECONDARY: QMSHelp.qhp QMTHelp.qhp

# generate compressed Qt help files for QMS/QMT  
build: QMSHelp.qhc QMTHelp.qhc $(allshow)
     
%Help.qhc: %Help.qhcp %Help.qhp 
	 $(HELPGENERATOR) $< -o $@
     
%Help.qhcp: ;
     
# Show QMS help in Qt assistant     
run: $(allshow)
	$(info )
	$(info Showing help ...)
	$(info )    
	$(QTDIR)assistant -collectionFile $(allshow) &
    
# Rerun everything after cleaning
all: clean build