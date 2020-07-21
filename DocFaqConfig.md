[Prev](DocFaq) (Frequently Asked Questions) | [Home](Home) | [Manual](DocMain) | [Index](AxAdvIndex) | (Use of issue templates) [Next](DocFaqProjectSite)
- - -

***Table of contents***

* [Frequently Asked Questions - Configuring and running QMapShack](#frequently-asked-questions---configuring-and-running-qmapshack)
    * [Can I run several QMS instances at the same time?](#can-i-run-several-qms-instances-at-the-same-time)
    * [Why does QMS ask for authorization on start-up (Ubuntu version)](#why-does-qms-ask-for-authorization-on-start-up-ubuntu-version)
    * [User-relevant QMapShack directories (Windows version)](#user-relevant-qmapshack-directories-windows-version)
    * [How to change the GUI language?](#how-to-change-the-gui-language)
    * [Where does QMS save setup, configuration, and other information?](#where-does-qms-save-setup-configuration-and-other-information)
    * [What to do if QMS doesn't start?](#what-to-do-if-qms-doesnt-start)


* * * * * * * * * *
 
 
# Frequently Asked Questions - Configuring and running QMapShack

## Can I run several QMS instances at the same time?


_Valid from patch version aa576e2 (22.02.2017)._ 

No. QMS saves workspace information in the file `workspace.db`. There is only one such
file. If this file would be used by several QMS instances at the same time, then the 
QMS workspace data behavior would be unpredictable.

If an attempt is made to start a second QMS instance, then the file parameters of this call are transferred to the first QMS instance
and the files are loaded there silently.

## Why does QMS ask for authorization on start-up (Ubuntu version)

When starting QMS with Ubuntu 18.04 it may happen that a user authorization/authentication is required.

The reason for this is, that QMapShack probes all block devices for GPS devices by mounting them, analyzing their file structure and unmounting them again. This is also done for devices containing the system, as there is no known way to distinguish them from a GPS device. Usually, the unmount for system drives is expected to fail. Most likely, some Ubuntu window managers interfere and ask for authorization.  

The following approach for avoiding this authorization was recommended in the [QMS issue tracker](https://github.com/Maproom/qmapshack/issues/156):

* Open the file 

        /usr/share/polkit-1/actions/org.freedesktop.UDisks2.policy
      
    in an editor.
    
* Locate the definition of the action 

        org.freedesktop.udisks2.filesystem-unmount-others
      
    which starts with the line 

        <action id="org.freedesktop.udisks2.filesystem-unmount-others">
    
* Locate the end of this action at the line `</action>`.
* Replace the line 

        <allow_active>auth_admin_keep</allow_active> 
    
    located 2 lines before the end of the action by the line 
  
        <allow_active>yes</allow_active> 

* Do not forget to back up original file!

## User-relevant QMapShack directories (Windows version)

* Directories relative to location of `qmapshack.exe`:
    * `.\translations`: language files
    * `.\routino-xml`: routino configuration files including `profiles.xml`
* Other directories:
    * `c:\Users\your_user_name\AppData\Local\Temp\org.qlandkarte.QMapShack.log`: logfile written if commandline option
      `-f` is used
    * `c:\Users\your_user_name\.QMapShack`: tile caches for online maps (default, can be changed by the user)
    * `c:\Users\your_user_name\.config\QLandkarte\workspace.db`: backup of last used workspace - used for rebuilding the last workspace when QMapShack is restarted

## How to change the GUI language?

The language used in the QMapShack user interface (GUI) is defined using the following rules:

* If the language of the operating system is a language supported by QMS, then this language is used as the default GUI language.
* Languages available in QMS are:
    * English 
    * Catalan (ca)    
    * Czech  (cs)    
    * Dutch (nl)    
    * French (fr)    
    * German (de)
    * Italian (it) 
    * Russian (ru)
    * Spanish (es)
 
* If the language of the operating system is not supported by QMS, then English is used as the QMS GUI language.
* The user can change the GUI language with the help of these steps:
    * Find the abbreviation of the operating system language (the so-called locale, e.g. `hu` for Hungarian).
    * Find in the QMS installation directory or its subdirectories the language files `qmapshack_*.qm` 
      (Windows: go to subdirectory `translations`).
    * Select one of the supported languages (e.g. `de` for German).
    * Copy the file `qmapshack_de.qm` to `qmapshack_hu.qm`.
    * After the next start of QMS the GUI language will be the selected language (German in the example).
    * _Remarks:_ 
        * The (default) English language file is `qmapshack.qm`, not `qmapshack_en.qm`! 
        * Both the locale (en, de, fr, ...) and the language file used with its full path can be  found in the [QMS logfile (debug output)](DocCmdOptions "Use of QMS logfile"). Check for lines of the form
    
                 2017-01-31 13:24:30.594 [debug] locale "de"    
                 2017-01-31 13:24:30.594 [debug] "using file 'c:...\\translations/qmapshack_de.qm' for translations."
     
            If the language of the operating system is not supported by QMS than these lines have the form
     
                 2017-01-31 13:26:00.785 [debug] locale "de"
                 2017-01-31 13:26:00.785 [warning] "no file found for translations 'c:...\\translations/qmapshack_de' (using default)."
                 
* When running QMS under Windows the GUI language can be changed by starting QMS with a batch file of the form:
    
        set LANG=de
        qmapshack.exe
      
    In this example German will be used as GUI language even if the Windows system language is different.    
    
## Where does QMS save setup, configuration, and other information?

The following list gives an overview of the locations used for saving setup, configuration, and some other information.

* **Logfile (`org.qlandkarte.QMapShack.log`)**
    * *Purpose:* Provide various information about QMS run
    * *Commandline:* `qmapshack.exe -f`
    * *Location (Windows):* `c:\Users\user_name\AppData\Local\Temp\`
    * *Location (Linux):* `/tmp/`
* **Console debug output (Linux only)**
    * *Purpose:* Provide various information about QMS run (same information as in logfile)
    * *Commandline:* `qmapshack.exe -d`
    * *Location (Linux):* output on console
* **`workspace.db`**
    * *Purpose:* Save various information for restoring QMS workspace at restart. Proprietary file structure.
    * *Location (Windows):* `c:\Users\user_name\.config\QLandkarte\`
    * *Location (Linux):* `~/.config/QLandkarte/` 
* **INI file**
    * *Purpose:* Save most of the QMS setup and configuration information in a usual INI file structure
    * *Commandline:* `qmapshack.exe -c my_inifile.ini`
    * *Location (Windows):* defined with INI file name, if necessary, `my_inifile.ini` should include complete path
    * *Location (Linux):* defined with INI file name, if necessary, `my_inifile.ini` should include complete path
* **Registry (Windows only)** 
    * *Purpose:* Save most of the QMS setup and configuration information in a structure similar to the one used in QMS INI file. Registry is used, if no INI file is given on commandline.
    * *Location (Windows):* `HKCU\Software\QLandkarte\QMapShack`
* **`QMapShack.conf` (Linux only)**
    * *Purpose:* Save most of the QMS setup and configuration information in a usual INI file structure. File is used, if no QMS INI file is given on commandline.
    * *Location (Linux):* `~/.config/QLandkarte/`
* **User-defined waypoint icons**
    * *Purpose:* Default path for adding user-defined waypoint icons (user can change this path!) 
    * *Location (Windows):* `c:\Users\user_name\.config\QLandkarte\WaypointIcons\`
    * *Location (Linux):* `~/.config/QLandkarte/WaypointIcons/` 
    
*Remark:*

* The commandline parameters `-f` and `-d` for Linux can be used simultaneously. In this case, debug output is written to the logfile and to the console.

 
## What to do if QMS doesn't start?

*(Find details and locations of files mentioned in this section [here][SetupFiles])*

1. Search in the list of running processes (task manager!) for a still running QMS process. If yes, kill it. Restart QMS.
1. Start QMS from commandline using `qmapshack.exe -f`. A logfile is written. Check this logfile for error messages and try to avoid these errors.
1. If no `qmapshack.exe` process is running: Back up  
    * `workspace.db`, 
    * INI file (if used), 
    * QMS part of registry (Windows users only. Use text format!) or  `~/.config/QLandkarte/QMapShack.conf` (Linux users)
1. Remove one after the other `workspace.db` (workspace isn't re-established), INI file **and also**  QMS part of registry resp. `QMapShack.conf` (QMS restarted without any previous setup and configuration data) and try to restart QMS after each step
1. If QMS restart was successful, shutdown QMS and repeat step 3 with different filenames (saves new clean setup!)
1. If QMS restart was successful: Restore `workspace.db` from first backup in step 3 and restart QMS again. In case of success: old QMS workspace is restored. If restart fails, `workspace.db` can be broken and workspace can't be recovered. Remove `workspace.db` again.
1. If QMS was successfully restarted, redefine essential parts of setup and configuration. _Hint:_ Open the INI file, the registry or the `QMapShack.conf` file saved in step 3 to get some information about the last QMS setup and configuration.


[SetupFiles]: #where-does-qms-save-setup-configuration-and-other-information "Save setup info"
  


- - -
[Prev](DocFaq) (Frequently Asked Questions) | [Home](Home) | [Manual](DocMain) | [Index](AxAdvIndex) | [Top](#) | (Use of issue templates) [Next](DocFaqProjectSite)
