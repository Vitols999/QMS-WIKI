Prev () | [Home](Home) | [Manual](DocMain) | [Index](AxAdvIndex) | () Next
- - -

# Raster IMG

__This is a translation of the Russian [original](http://whiter.brinkster.net/raster_img.shtml) written by (late) Alex Whiter.__

As you know, IMG maps in the Bluechart G2 Vision format can contain raster layers.

This document is an attempt to partially document the meaning of the various fields in the headers of such IMG maps.

The web has several very good sources of information about the IMG format and its individual subblocks.

Here are the main ones:

* [http://wiki.opensTREetmap.org/wiki/OSM_Map_On_Garmin/Format](http://wiki.opensTREetmap.org/wiki/OSM_Map_On_Garmin/Format)
* [http://www.pinns.co.uk/osm/RGN.html](http://www.pinns.co.uk/osm/RGN.html)
* [exploring_img.pdf](exploring_img.pdf)
* `imgformat-1.0.pdf`, which can be downloaded, for example, [here](http://sourceforge.net/projects/garmin-img/files/). 

Unfortunately, these sources do not contain any information about saving raster maps in IMG maps.

Let's try to parse the main header fields of a map using the example file `00355951.GMP`, the smallest map file in terms of volume and number of images of the map of the Isle of Man which is freely available for [download](http://www.garmin.com/uk/maps/isle-of-man-map).

~~~
Offset from     Offset from 
start of file   start of block  Content from 00355951.GMP                          Meaning

0000            GMP + 000       0035 'GARMIN GMP' 0001 07DA 07 15 09 37 3A         GMP block header
0015            GMP + 015       00000000                                           
0019            GMP + 019       000000E8                                           TRE
001D            GMP + 01D       000001F2                                           RGN
0021            GMP + 021       0000027D                                           LBL
0025            GMP + 025       00000000                                           NET
0029            GMP + 029       00000000                                           NOD
002D            GMP + 02D       00000000                                           DEM
0031            GMP + 031       00000000                                           MAR
0035            GMP + 035       'Copyright' ...                                    Copyright

00E8            TRE + 000       00D3 'GARMIN TRE' 0001 07DA 07 15 09 37 3A         TRE block header
00FD            TRE + 015       2693EA FCE8F4 2693CA FCE81A                        Coordinates of map boundary
0109            TRE + 021       00000508 00000020                                  TRE1, level section
0111            TRE + 029       00000486 00000082                                  TRE2, group section
0119            TRE + 031       0000047D 00000009 0003                             TRE3, copyright section
0123            TRE + 03B       00 00 00 00                                        
0127            TRE + 03F       01                                                 Flags
0128            TRE + 040       0014                                               Rendering priority
012A            TRE + 042       10 01 08 24 00 01 00 00                            Flags
0132            TRE + 04A       00000528 00000000 0002 00 00 00 00                 TRE4
0140            TRE + 058       00000528 00000000 0002 00 00 00 00                 TRE5
014E            TRE + 066       00000528 00000000 0003 00 00 00 00                 TRE6
015C            TRE + 074       007E6E07                                           Map ID
0160            TRE + 078       00 00 00 00                                        
0164            TRE + 07C       0000052E 00000020 0004 01 00 00 00                 TRE7, raster layer section
0172            TRE + 08A       00000528 00000006 0003 00 00 02 00 00 00           TRE8
0182            TRE + 09A       1C 72 78 19 89 72 44 BB 1B 72 71 BB 1B 72 71 BB    Map ID hash
0192            TRE + 0AA       00 00 00 00                                        
0196            TRE + 0AE       0000054E 00000000 0000 00 00 00 00                 TRE9
01A4            TRE + 0BC       0000054E 00000000 0001 00 00 00 00                 TRE10
01B2            TRE + 0CA       00 00 00 00 00                                     
01B7            TRE + 0CF       00056E6F                                           Number that matches the name of the map file (0x00056E6F = 00355951)

01BB            TRE + 0D3       'Isle of Man Copyright' ...                        Card name

01F2            RGN + 000       007D 'GARMIN RGN' 0001 07DA 07 15 09 37 3A         RGN block header
0207            RGN + 015       0000054E 00000000                                  RGN1
020F            RGN + 01D       0000054E 000001A4                                  RGN2
0217            RGN + 025       02 00 00 00 00 00 00 00 00 FF 00 00 20 FD FC 03 00  
                                00 00 00 00                                        
022B            RGN + 039       000006F2 00000000                                  RGN3
0233            RGN + 041       00 00 00 00 00 00 00 00 00 3F 00 00 20 FD 0F 00 00  
                                00 00 00 00                                        
0247            RGN + 055       000006F2 00000000                                  RGN4
024F            RGN + 05D       00 00 00 00 00 00 00 00 00 FF 07 00 20 3F F7 3F 00  
                                00 00 00 00                                        
0263            RGN + 071       000006F2 00000070 E3 00 00 00                      RGN5

026F                            000E 000006F2 00000000 00 00 00 00                 RGNEXT

027D            LBL + 000       0200 'GARMIN LBL' 0001 07DA 07 15 09 37 3A         LBL block header
0292            LBL + 015       00000773 000000FB 00 09                            LBL1
029C            LBL + 01F       00000870 00000000 0000 00 00 00 00                 LBL2
02AA            LBL + 02D       00000870 00000000 0006 01 00 00 00                 LBL3
02B8            LBL + 03B       00000870 00000000 0007 01 00 00 80                 LBL4
02c5            LBL + 049       00000870 00000000 0000 00 00 00 00                 LBL5
02D4            LBL + 057       00000870 00000000 00 00 00 00 00                   LBL6
02E1            LBL + 064       00000870 00000000 0000 00 00 00 00                 LBL7
02EF            LBL + 072       00000870 00000000 0003 00 00 00 00                 LBL8
02FD            LBL + 080       00000870 00000000 0006 00 00 00 00                 LBL9
030B            LBL + 08E       00000870 00000000 0004 02 00 00 00                 LBL10
0319            LBL + 09C       00000870 00000000 0003 00 00 00 00 04E4            LBL11
                                07 00 02 80                                        
032D            LBL + 0B0       00000762 00000011                                  LBL12, sorting method description
0335            LBL + 0B8       0000086E 00000000 0000 00 00                       LBL13
0341            LBL + 0C4       00000870 00000000 0000 00 00                       LBL14
034D            LBL + 0D0       00000870 00000000 002E 01 00 00 00                 LBL15
035B            LBL + 0DE       0000086E 00000002 0000 00 00 00 00                 LBL16
0369            LBL + 0EC       00000870 00000000 0000 00 00 00 00                 LBL17
0377            LBL + 0FA       00000870 00000000 0000 00 00 00 00                 LBL18
0385            LBL + 108       00000870 00000000 000C 00 00 00 00                 LBL19
0393            LBL + 116       0000086E 00000000 0003 00 00 00 00                 LBL20
03A1            LBL + 124       00000870 00000000 0000 00 00 00 00                 LBL21
03AF            LBL + 132       00000870 00000000 0000 00 00 00 00                 LBL22
03BD            LBL + 140       00000870 00000000 0000 00 00 00 00                 LBL23
03CB            LBL + 14E       00000870 00000000 0000 00 00                       LBL24
03d7            LBL + 15A       00000870 00000000 0000 00 00 00 00                 LBL25
03E5            LBL + 168       00000870 00000000 0000 00 00 00 00                 LBL26
03F3            LBL + 176       00000870 00000000 0000 00 00 00 00                 LBL27
0401            LBL + 184       00000870 00000008 0004 00 00 00 00                 LBL28, offsets to individual JPEG images relative to LBL29
040F            LBL + 192       00000878 000005C8                                  LBL29, start of image block
0417            LBL + 19A       00000870 00000000 0000 00 00                       LBL30
0423            LBL + 1A6       00000870 00000000 0000 00 00                       LBL31
042F            LBL + 1B2       00000E40 00000000 0000 00 00                       LBL32
043B            LBL + 1BE       00000E40 00000000 0000 00 00                       LBL33
0447            LBL + 1CA       00000870 00000000 0000 00 00 00 00                 LBL34
0455            LBL + 1D8       00000870 00000000 0000 00 00 00 00                 LBL35
0463            LBL + 1E6       0000086E 00000000 0000 00 00                       LBL36
046F            LBL + 1F2       00000878 00000000 0000 00 00 00 00                 LBL37

047D            TRE3            00000C                                             Offsets to lines relative to LBL1
0480                            000032                                             
0483                            000093                                             

0486            TRE2            000000 00 FCE880 269380 8001 0001 0002             Level groups
                                000000 00 FCE880 2693C0 8002 0001 0003             
                                000000 00 FCE880 2693E0 8004 0001 0004             
                                000000 00 FCE880 2693E0 8008 0002 0005             
                                000000 00 FCE888 2693D8 800F 0003 0006             
                                000000 00 FCE888 2693DC 801C 0005 0007             
                                000000 00 FCE886 2693DA 8037 0009 0008             
                                000000 00 FCE887 2693DA 806D 0010                  
                                00 00 00 00                                        
                                
0508            TRE1            87 11 0001                                         Levels
                                06 12 0001                                         
                                05 13 0001                                         
                                04 14 0001                                         
                                03 15 0001                                         
                                02 16 0001                                         
                                01 17 0001                                         
                                00 18 0001                                         
                                
0528            TRE8            130606                                             Parameters of object types. First one: raster tiles.
                                01060D                                             Second one: DATA_BOUNDS.
                                
052E            TRE7            00000000                                           Offset of the descriptions of raster layers relative to RGN2
0532                            0000002E                                           
0536                            0000005C                                           
053A                            0000008A                                           
053E                            000000B8                                           
0542                            000000F3                                           
0546                            00000169                                           
054A                            000001A4                                           

054E            RGN2 + 000      0D 01 FFFE 0000 07 1B 21 F8                        Descriptions of raster layers.
                                06 B3 FFFE 0000 07 1B 21 F8                        Format still unknown.
                                BC 00 00                                           
                                E0 2B 01                                           
                                26940000 FCE90000 2693C000 FCE80000                
                                00000278                                           
057C            RGN2 + 02E      0D 01 FFFD FFFF 07 23 22 78                        
                                06 B3 FFFD FFFF 07 23 22 78                        
                                BC 00 00                                           
                                E0 2B 01                                           
                                2693E000 FCE90000 2693C000 FCE82000                
                                0000278                                            
05AA            RGN2 + 05C      0D 01 FFFA FFFF 07 05 80 0F                        
                                06 B3 FFFA FFFF 07 05 80 0F                        
                                BC 00 00                                           
                                E0 2B 01                                           
                                2693F000 FCE8F000 2693D000 FCE82000                
                                0000278                                            
05D8            RGN2 + 08A      0D 01 FFF2 FFFE 07 09 98 5E                        
                                06 B3 FFF2 FFFE 07 09 98 5E                        
                                BC 00 00                                           
                                E0 2B 01                                           
                                2693E800 FCE8F000 2693C800 FCE81800                
                                0000278                                            
0606            RGN2 + 0B8      0D 01 FFE5 FFFC 07 2B 42 F8                        
                                06 B3 FFE5 FFFC 07 2B 42 F8                        
                                DE 00 00                                           
                                E0 2B 00                                           
                                2693E800 FCE8F400 2693CC00 FCE81C00                
                                00000350                                           
0641            RGN2 + 0F3      0D 01 FFCB FFF9 07 33 04 DE                        
                                0D 01 FFCB FFF8 07 33 23 78                        
                                06 B3 FFCB FFF9 07 33 04 DE                        
                                DE 00 00                                           
                                E0 2B 00                                           
                                2693EA00 FCE8F400 2693CA00 FCE81C00                
                                00000350                                           
                                06 B3 FFCB FFF8 07 33 23 78                        
                                DE 00 00                                           
                                E0 2B 00                                           
                                2693EA00 FCE8F400 2693CA00 FCE81C00                
                                00000350                                           
                                06 33 FFCB FFF9 07 33 04 DE                        
                                BC 00 00                                           
                                06 33 FFCB FFF8 07 33 23 78                        
                                BC 00 00                                           
06B7            RGN2 + 169      0D 01 FF94 FFF1 07 3B 19 FC                        
                                06 B3 FF94 FFF1 07 3B 19 FC                        
                                DE 00 00                                           
                                E0 2B 00                                           
                                2693E900 FCE8F400 2693CB00 FCE81B00                
                                00000350                                           
                                06 33 FF94 FFF1 07 3B 19 FC                        
                                BC 00 00                                           
                                
06F2            RGN5            DF 14 06 02 20 0B                                  Not yet known
                                00 06 00 02 05 02                                  
                                00 01 00 00 00 02 01 00 00 00                      
                                09 01 00 00 00 09 04 00 00 00                      
                                09 07 00 00 00 09 36 00 00 00                      
                                09 6C 00 00 00 09 D9 00 00 00                      
                                03 00 00 00 00 03 00 00 00 00 00                   
                                03 00 00 00 00 03 00 00 00 00 00                   
                                03 00 00 00 00 03 00 00 00 00 00                   
                                03 00 00 00 00 03 00 00 00 00 00                   
                                02 00 00 00 0F 00 00 00                            
                                0D 00 00 00 1B 00 00 00                            
                                1E 00 00 00                                        
                                
0762            LBL12           'Western Europeean' 00                             

0773            LBL1 + 000      00 'Raster Map' 00                                 
077F            LBL1 + 00C      'GARMIN LTD' ...                                   
07A5            LBL1 + 032      'Reproduced with permission' ...                   
0806            LBL1 + 093      'Crown Coyright' ...                               
082F                            'OSGB_OS_N54143149W4533473-27M.JPG' 00             
0851                            'IOM_N54249345W4353571-3M.JPG' 00                  

086E            LBL16           00 00                                              

0870            LBL28           00000000                                           Offsets to images relative to LBL29
0874                            00000350                                           

0878            LBL29 + 000     Jpeg 000                                           Images themselves
0BC8            LBL29 + 350     Jpeg 001                                           
~~~

In order to make your own raster IMG, it remains "only" to figure out the structure of the areas TRE8, RGN2 and RGN5.

Some information about the RGN2 format is available in the document `exploring_img.pdf`.

Apparently, type `E0` is used for drawing a raster image. For example, consider this fragment from `RGN2 + 169`:

    E0 2B 00
    2693E900 FCE8F400 2693CB00 FCE81B00
    00000350

Here `2B` in some way defines the number of bits that is used to encode the JPEG sequence number in table `LBL29`.
In the considered `00355951.GMP` there are only 2 images, and here, one byte is enough to index the images.
And, say, in the subfile `00263430.GMP` of the `Lake District.img` map as many as 896 images are saved. Type `E0` is followed by code `25`, and two bytes are already used for indexing images.

Further, `2693E900 FCE8F400 2693CB00 FCE81B00` are, obviously, the coordinates of the image, 32 bytes for each of the coordinates.

`00000350` - the size of the block with the image.

That's all for now. I hope that this file will be updated with information on not yet explored areas.
If you have comments or additions, please write to the [(late) author](a.whiter@yandex.ru).

Last modification: 15 Mar 2017


_Translator's notes:_

* Some of the links on this page (and its Russian original) are broken.
* Some internal links on this page had to be removed due to Markdown formatting limitations. If  necessary, compare with [original page](http://whiter.brinkster.net/raster_img.shtml).
* More information about the author can be found [here](https://www.naviboard.de/thread/64138-alex-whiter-gestorben/?postID=517042#post517042) (in German) and [here](https://www.gpspower.net/forum-announcements/359499-vale-alexwhiter.html).

- - -
Prev () | [Home](Home) | [Manual](DocMain) | [Index](AxAdvIndex) | [Top](#) | () Next
