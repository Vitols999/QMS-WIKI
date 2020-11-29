[Prev](DocFaqData) (Databases and projects) | [Home](Home) | [Manual](DocMain) | [Index](AxAdvIndex) | (Routing) [Next](DocFaqRouting)
- - -

***Table of contents***

* [Frequently Asked Questions - Data handling](#user-content-frequently-asked-questions---data-handling)
    * [How to create waypoint from POI (point of interest) in map?](#user-content-how-to-create-waypoint-from-poi-point-of-interest-in-map)
    * [How to find distance between waypoints](#user-content-how-to-find-distance-between-waypoints)
    * [Which track data is saved in GPX files?](#user-content-which-track-data-is-saved-in-gpx-files)
    * [How to access data from legacy Garmin devices?](#user-content-how-to-access-data-from-legacy-garmin-devices)
    * [What is the difference between speed and gpxtpx:speed?](#user-content-what-is-the-difference-between-speed-and-gpxtpxspeed)
    * [How to remove DEM info from elevation graph?](#user-content-how-to-remove-dem-info-from-elevation-graph)
    * [How to edit tracks without losing track data?](#user-content-how-to-edit-tracks-without-losing-track-data)
    * [How to compose a track from pieces of other tracks?](#user-content-how-to-compose-a-track-from-pieces-of-other-tracks)

* * * * * * * * * *
 
# Frequently Asked Questions - Data handling

## How to create waypoint from POI (point of interest) in map?

If the mouse pointer is moved on a POI in a vector map, a small blue circle around this POI pops-up. Right-click to open the context menu and select the menu entry
`Add POI as waypoint`. The POI name and its coordinates are used in the new waypoint.

![Waypoint from POI](images/DocFaq/WPTfromPOI.jpg "Waypoint created from POI")

## How to find distance between waypoints

* _Find the direct distance from a waypoint to some other point:_ set a waypoint and move it to the other point.
  This will give you the distance and the course (direction) to the other point. When done abort the operation (right mouse click) and remove the waypoint.

    ![Distance between waypoints](images/DocFaq/WPTDistance.jpg "Distance between waypoints")

* _Find a defined distance from several waypoints:_ add the distance as proximity to the waypoints.

    ![Set waypoint proximity](images/DocFaq/WPTProximity.jpg "Set waypoint proximity")

    ![Waypoint distances](images/DocFaq/WPTDistances.jpg "Waypoint distances")


* _Find the street distance or the direct distance between several points:_ start to create a track with or without routing.

    ![Direct track distance](images/DocFaq/Directtrack.jpg "Direct track distance")

    ![Routed track distance](images/DocFaq/Routedtrack.jpg "Routed track distance")

## Which track data is saved in GPX files?

(_valid starting with QMS patch version 7ac34c818ec1/2016-12-06_)

QMS supports 2 kinds of GPX files:

* GPX files that follow strictly the rules of the GPX 1.1 standard,
* GPX files using additional extensions (_special format_).

In both cases the following track data is saved in the GPX file:

* track name,
* location of each trackpoint,
* timestamp of each trackpoint (if available),
* elevation of each trackpoint (if available).

The additional extensions used in the _special format_ provide information about

* the track history (can't be re-activated when GPX file is re-loaded into QMS),
* the track display color
* the type of trackpoint (trackpoint created by routing engine (so-called subpoint) or
  trackpoint created by user interaction, hidden trackpoint, activity)

Trackpoints created by a routing engine can't be edited by the user whereas trackpoints
created by a user can be
edited (compare section ["Edit items with multiple points"](DocGisItemsEditMultiple)).

## How to access data from legacy Garmin devices?

_(inspired by [newsgroup discussion](https://sourceforge.net/p/qlandkartegt/mailman/message/35994128))_

The internal memory of legacy Garmin devices (e.g. the well-known Garmin GPS 60Csx) can't be connected as a USB drive to the computer even if they are connected 
via USB to the computer.. Thus, data in the internal
memory (e.g. the so-called ActiveLogs or waypoints saved in the device) can't be accessed directly from QMS.

[`GPSBabel`](https://www.gpsbabel.org) (available for Windows, MacOS, and Linux) can be used to download tracks and waypoints stored in the internal memory of
a Garmin GPS device by using the command:

    gpsbabel -t -w -i garmin -f usb: -o gpx -F gpsdata.gpx

Drag and drop the output file `gpsdata.gpx` to the QMS workspace or call

    qmapshack.exe gpsdata.gpx
    
to see the tracks and waypoints.

Compare the GPSBabel documentation for more details.

## What is the difference between speed and gpxtpx:speed?

Various GPS receivers record different data for trackpoints. Some Garmin navigators use for this purpose
a special [GPX trackpoint extension](https://www8.garmin.com/xmlschemas/TrackPointExtensionv2.xsd "Garmin gpxtpx trackpoint extension")
named `gpxtpx`. One of the data fields within this extension is `gpxtpx:speed`. It records the speed at the given trackpoint.
This speed is measured in meters per second whereas the calculated speed at a trackpoint is measured in kilometers per hour.

QMS reads this speed value and can display it in form of a graph in the track edit window.

A similar data field is `gpxtpx:course`. This field contains an angle measured in degrees in a clockwise direction from the true north line
(the _course_).

Compare also section 
[Recorded and calculated track data](DocGisItemsTrk#user-content-recorded-and-calculated-tracks).


![Recorded gpxtpx:speed vs. speed graphs](images/DocFaq/FaqGpxTpxSpeed.jpg "Recorded gpxtpx:speed vs. speed graphs")


## How to remove DEM info from elevation graph?

_(inspired by newsgroup discussion ["Option to disable DEM plot in track profile view"](https://sourceforge.net/p/qlandkartegt/mailman/message/35962352))_ 


Assume

* a (recorded) track has elevation information,
* DEM data is available for the area in which the track is located, 
* DEM data is activated in the view in which the track is displayed,
* the (extended) track profile is activated for the track.

Then the track elevation profile
displays the recorded elevation together with the elevation obtained from the DEM data (red line).

To remove the DEM data from the track profile proceed as follows:

* clone the existing view (use menu entries `View - Clone map view`),
* deactivate DEM data in the cloned view,
* open the track profile in the cloned view.

Now, the track profile shows only the elevation data of the track.

_Hint:_ Use the track profile in the map view, not the one in the track edit window!

## How to edit tracks without losing track data?

_(inspired by newsgroup discussion [How to edit this track?](https://sourceforge.net/p/qlandkartegt/mailman/message/35965052))_

Trackpoint data of tracks recorded by a GPS device consists not only of a position and a timestamp. Modern devices record different amounts of other (fitness) information
such as elevation, cadence, pulse rate, temperature ...

While recording a track on a GPS device, the quality of GPS signals may vary. Signals may be weak or even disappear due to various reasons. 
In such a case the recorded track data is not reliable or even completely wrong.
A need occurs to remove such non-reliable or wrong data by editing the track manually.

QMS offers the following track editing methods:

* Edit track in map window by going into the **track edit mode** and removing their single trackpoints. 

    This method is very convenient because it is easy to identify and remove wrong trackpoints.

    The _disadvantage_ of this method is that all trackpoint information except the position gets lost for all remaining trackpoints.

* Edit track using **range selection**.

    This method can be used in the map window or in the track edit window.

    If working in the map window:

    * click the track, 
    * click the range selection icon,
    * select the range of the track(points) that should be removed.

    By that, the selected trackpoints are hidden and do not add to the statistics. If you want to remove them permanently:
  
    * go to the track edit window of the track,
    * click the `Filter` tab,
    * open the `Reduce visible points` filter group,
    * run the `Remove trackpoints` filter.

    This procedure removes the selected range of trackpoints from the track without losing information from other trackpoints.

* Edit track using the **cut tool (scissors)**.

    If working in the map window:

    * click the track, 
    * click the cut tool (scissors) icon at the first trackpoint that should be removed,  
    * select option `Keep both parts of the track` and click `Ok`. The range of trackpoints to be removed is now at the start of one of the track parts.
    * Cut the track again to remove the remaining wrong trackpoints at the start of the track part (use option `Delete first part ...` resp. `Keep first part ...` properly!).
    * If necessary, merge the remaining track parts into a new track.
        
    
_Warning:_ As long as you stay in the QMapShack universe - using the database or the QMS files - you can revert all these steps in the history. However, if you save to a GPX file the data will be lost permanently. In this case, save a backup copy of the track before editing it!


Even as it is possible to remove incorrectly recorded trackpoints with both methods, the latter is the recommended one. The intended use-case for the track edit mode is to create artificial tracks to plan a tour. That is why additional data like timestamps and sensor data is removed as it won't be valid when moving points or combining different track fragments.

## How to compose a track from pieces of other tracks?

_(topic inspired by a discussion in [mendiak.net][Mendiak])_

Assume, that you have several tracks as demonstrated in the next image with 3 tracks:

![Existing tracks][TrkExist]

The task is to compose a new track from adjacent pieces of these existing tracks. The wanted new track is shown in the next image (the magenta line):

![Wanted new track][TrkWanted]

QMS offers various ways to build this new track:

* _Using [splits of tracks][TrkCut]:_
    * Cut the given tracks into pieces necessary for the new track.
    * If necessary, [reverse track pieces][TrkReverse] with wrong orientation (in the example, the red track has wrong orientation).
    * [Join the required pieces][TrkCombine] into a new track.
    
    This approach is quite cumbersome and requires many single steps.
    
* _Using [track ranges][TrkRange]:_
    * Select the track pieces necessary for the new track as ranges of the given tracks and copy them as new track pieces.
    * If necessary, [reverse track pieces][TrkReverse] with wrong orientation.
    * [Join the required pieces][TrkCombine] into a new track.
    
    This approach is less cumbersome than the previous one but still requires many single steps.
    
* _Using [track routing][TrkRouting0]:_
    * [Select the first point of the new track][TrkNew]. If necessary, change the zoom level of the map to hit an existing track as exactly as possible.
    * In the options toolbar select the routing option `T` (press key `T`).
    * Move the mouse pointer along the first existing track segment. The track under the mouse will be highlighted in yellow.
    
        ![Routing following tracks][TrkRouting]
        
    * When hitting the next existing track, left-click to fix the first new track part.
    * Follow the next existing track as long as necessary and so on.
    * [Save the new track][TrkNew] after reaching its endpoint. 

    This approach is again less cumbersome than the previous one and should be preferred. It avoids dealing with a lot of single track pieces.

[Mendiak]: https://www.mendiak.net/viewtopic.php?t=61085&p=760483#p760483 "Compose tracks from pieces"

[TrkCut]:     DocGisItemsTrk#user-content-cut-track
[TrkReverse]: DocGisItemsTrk#user-content-view--edit-details
[TrkCombine]: DocGisItemsTrk#user-content-combine-tracks
[TrkRange]:   DocGisItemsTrkRange#user-content-select-track-range-in-map-view
[TrkNew]:     DocGisItemsRte#user-content-use-map-window
[TrkRouting0]: DocGisItemsRouting#user-content-description-of-routing-methods-in-qmapshack


[TrkExist]:   images/DocFaq/TracksExist.png   "3 existing tracks"
[TrkWanted]:  images/DocFaq/TrackWanted.png   "Wanted new track"
[TrkRouting]: images/DocFaq/TrackRouting.png  "Routing following tracks"

- - -
[Prev](DocFaqData) (Databases and projects) | [Home](Home) | [Manual](DocMain) | [Index](AxAdvIndex) | [Top](#) | (Routing) [Next](DocFaqRouting)
