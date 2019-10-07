# Activity Brainstorming

See [QMS #39](https://github.com/Maproom/qmapshack/issues/39)

These are all activities (V1.13.2). They are also kind of a category. 
Let's collect sub-activities for each of them

## Foot     = 100

    * Foot
    * Running
        - Running 1 - Road or Track 
        - Running 2 - Path
        - Running 3 - Difficult path
        - Running 4 - Off path, rocky terrain
        - Running 5 - You need hands
    * Hiking
        - Hiking 1 - Road or Track 
        - Hiking 2 - Path
        - Hiking 3 - Difficult path
        - Hiking 4 - Off path, rocky terrain
        - Hiking 5 - You need hands
    * Trekking
    * Mountaineering
    * Orienteering
    * Climbing

## Cycle    = 200

    * Cycle
    * Road bike
    * Trekking
    * MTB
        * XC
        * Downhill

## Bike     = 300

    * Bike

## Car      = 400

    * Car

## Cable    = 500

    * Cable

## Swim     = 600

    * Swim

## Ship     = 700

    * Ship
    * Sailing ship
    * Windsurfing
    * Kitesurfing
    * Motorboat
    * Ferry
    * Kayak
    * Canoe
  

## Aero     = 800

    * Aero
    * Gliding
    * Paragliding
    * Parachute
    * Helicopter
    * Small plane
    * Jet

## Ski      = 900

    * Ski
    * Snow shoe
    * Cross-country skiing
    * Downhill skiing
    * Ski tour

## Public Transport    = 1000    (formerly Train)

    * Public Transport
    * Train
    * Bus

## REMARKS and REFERENCES
### Hiking
We have *at least* these references:
 *  **DAV scale** ( [German, sektion 1.6.3 und 1.7.1](https://www.alpenverein.at/portal_wAssets/docs/berg-aktiv/wege_touren/wegehandbuch_digital.pdf) )
*  **SAC scale** ([German](https://www.sac-cas.ch/fileadmin/Ausbildung_und_Wissen/Tourenplanung/Schwierigkeitsskala/Wanderskala-SAC.pdf), [French](https://www.sac-cas.ch/fileadmin/Ausbildung_und_Wissen/Tourenplanung/Schwierigkeitsskala/Cotation-CAS-des-randonnees.pdf) ) 
*  **MIDE** ( [Spanish, view section 'Desplazamiento' pag.7/11](http://montanasegura.com/MIDE/manualMIDE.pdf) )...

The DAV document is more related to how paths have to been marked on the terrain and only makes 3 divisions, the lower one talks about easy paths and the top one talk about alpine skills. I would stick to SAC and MIDE schema with 5 levels (so DAV schema of 3 levels + valley tracks would be inside). 

SAC and MIDE are not *exactly* the same, but their respective descriptions for levels 1-5 are very close.  In both them  level 5 talks about passages where you use your hands, but not real climbing. SAC have a level 6, but involves solid experience with alpine techniques, so it is no hiking.

So for QMS we can use:
- Hiking 1 
- Hiking 2
- (...) to Hiking 5

OSM is following SAC scale for labelling paths, but in QMS I would avoid the explicit reference to SAC nor MIDE, so everyone will feel comfortable with numbers that in fact equals to the respective levels of both systems. And obvious, while this is is mainly for personal use H1,H2, and so on, can mean whatever the user wants.  

Somewhere we have to be more descriptive that only a number, in some places of the GUI it would be used a descriptive name:

e.g. '**Hiking 3 - Difficult path**' 

and in other ones use '**Hiking 3**' or simply '**H3**' ( e.g. for buttons, icons, ...) 

Proposed default colors ( for track drawing and maybe for icons):

- H1 - yellow
- H2 - green
- H3 - blue
- H4 - red
- H5 - black (?)

Some extra explanation about hiking levels can be included in tooltips and in the wiki.

H1 to H4 fit well with the 4 existing hiking  profiles in the hiking time filter. This opens a possibility to connect those activities with the filter, doing so  different filter parameters could be aplied at once to different track ranges based on their activity (.. if someone picks up that task).

Additionally it could be a place for other Hiking flavours:
- Hiking DAV-OEAV (related to  DIN-33466)
- ...

### Running 

The Hiking schema can be cloned:

eg: 'Running 3 - Difficult path'  / 'Running 3'  /  'R3' / Default color blue

...
