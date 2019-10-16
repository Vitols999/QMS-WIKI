[Prev](DocGisItemsRte) (Routes) | [Home](Home) | [Manual](DocMain) | [Index](AxAdvIndex) | (Areas) [Next](DocGisItemsArea)
- - -

# Waypoints

A waypoint is a coordinate with data attached. This can be a point of interest, a geocache or a georeferenced image. If you move the mouse close enough to a waypoint it gets highlighted by a red circle:

![Waypoint Highlight](images/DocGisItemsWpt/WptHighlight.png)

If you click on the highlighted waypoint you get a short on-screen-summary of the waypoint information and a toolbar with a few options:

![WptBubble.png](images/DocGisItemsWpt/WptBubble.png)


|   |   |   |
|---|---|---|
| ![Edit/Details](images/DocGisItemsWpt/EditDetails.png) | Edit/Show Details | [Show details of the waypoint and edit attached data.](#-view--edit-details)   |
| ![Copy](images/DocGisItemsWpt/Copy.png)                | Copy              | Copy the waypoint into another project. |
| ![Delete](images/DocGisItemsWpt/DeleteOne.png)         | Delete            | Delete the waypoint. This also deletes data associated with the waypoint, such as photos. |
| ![Show Bubble](images/DocGisItemsWpt/Bubble.png)       | Show Bubble       | When enabled, the waypoint's content is shown as a static bubble. |
| ![Move](images/DocGisItemsWpt/WptMove.png)             | Move              | [Move the waypoint to another location.](#-move-waypoint) |
| ![Project](images/DocGisItemsWpt/WptProj.png)          | Project           | [Project the waypoint - This is copying the waypoint and to move to copy a given distance and bearing](#-project-waypoint) |
| ![Set elevation](images/DocGisItemsWpt/SetEle.png)     | Replace elevation | Replace waypoint elevation with elevation from DEM data |
| ![Edit proximity](images/DocGisItemsWpt/WptEditProx.png)  | Edit proximity | Edit/set proximity radius of waypoint (graphically) |
| ![Delete proximity](images/DocGisItemsWpt/WptDelProx.png) | Delete proximity | Delete proximity radius of waypoint |
| ![No-go](images/DocGisItemsWpt/NoGo.png)                  | Set no-go        | Activate/deactivate proximity range as [no-go area](AdvRoutes#using-no-go-areas-and-lines)|
| ![Search web](images/DocGisItemsWpt/SearchWeb.png)        | Search web       | [Search for information about the waypoint position on selected websites](DocFaqMaps#how-to-find-information-about-a-position-a-poi-in-the-web) |


## ![EditDetails](images/DocGisItemsWpt/EditDetails.png) View / Edit Details

![Waypoint Details](images/DocGisItemsWpt/WptDetails.png)

|   |   |   |
|---|---|---|
| ![Icon](images/DocGisItemsWpt/PinRed.png)     | Icon    | Shows the currently selected Icon / provides a list of available Icon when clicked |
| ![Tainted](images/DocGisItemsWpt/Tainted.png) | Tainted | When shown, the Waypoint was imported and modified (for details see [Waypoints, Tracks & Co](DocGisItems)) |
| ![Lock](images/DocGisItemsWpt/Lock.png)       | Locked  | When shown, the Waypoint is locked - that is cannot be modified until unlocked (for details see [Waypoints, Tracks & Co](DocGisItems)) |

In addition, the waypoint's position, elevation and a text browser to display links, description and comment are shown.
These can be changed by clicking on the blue, underlined labels.

### Custom Icons
QMapShack ships with a bunch of default icons, which are likely to be displayed correctly on the most GPS devices.

If you want to use your own icons, you need to add them to

* `~/.config/QLandkarte/WaypointIcons` (*nix-type systems)
* `c:\Users\my_user_name\.config\QLandkarte\WaypointIcons` (Windows)
* `???` (OSX)

Icon files must be in PNG or BMP format with size 22x22. 

When adding an icon *Photo.png*, the icon will be listed as *Photo* in QMapShack.

### The Photo Album

In addition to general information, such as position, name and a description, QMapShack allows attaching photos to a waypoint.
This functionality comes with several limitations, as it is primarily meant to provide a quick overview over the specific location - it is not intended to organize your collection of photos.

|   |   |   |
|---|---|---|
| ![Add Image](images/DocGisItemsWpt/AddImage.png) | Add (a) new image(s)  | Imports one or more new images. **Photos are scaled down on import** |
| ![Del Image](images/DocGisItemsWpt/DelImage.png) | Delete selected image | Remove selected image (i.e. the image with the yellow frame) |

**Photos are not exported to GPX.** Use either a Database or the QMS format for saving photos along with waypoints.

## ![WptMove](images/DocGisItemsWpt/WptMove.png) Move Waypoint

(_valid starting with QMS patch version  676511d9ba16 (2016-12-22)_)

To move a waypoint to a new location 

* left-click the waypoint on the map.
* Select the `Move waypoint to new location` icon from the info window that pops-up.
* The mouse cursor changes to the `Move` icon.
* Move the mouse pointer to the new location (don't click).
* The distance of the new to the old waypoint and the direction of change are shown.
* If the new location is not in the map view: left-click on the map and __don't release__ the mouse button.
* The map is attached to the mouse.
* Move the map to the wanted location and release the mouse button.
* The map is fixed again.
* Move the mouse to the wanted new location of the waypoint.
* Left-click to fix the new position of the waypoint.


![Move Waypoint](images/DocGisItemsWpt/Move.png)


## ![WptProj](images/DocGisItemsWpt/WptProj.png) Project Waypoint

Different to moving the waypoint this will create a clone of the waypoint. You have to give an explicit distance and bearing the waypoint is moved. You might want to change the icon and the name.

![Project Waypoint](images/DocGisItemsWpt/Projection.png)

## Geocaches

(_valid starting with QMS patch version  4b38874cbd9d (2019-01-20)_)

Geocaches are waypoints with special additional information. If this additional information is saved in a typical `<groundspeak:cache>` extension block of a waypoint in a GPX file, it can be displayed by QMS.

The waypoint icon shows the type of the geocache (traditional cache, multi-cache, virtual cache, webcam cache, ...).

The edit window differs from the one of a normal waypoint. It displays the additional geocache information in read-only mode using several tabs:

![Geocache info window](images/DocGisItemsWpt/GeocachInfo.png "Geocache info window")

_Remark:_ There are no fixed rules for defining attributes of geocaches. QMS supports only the handling of attributes defined in conformity with the rules used in [https://www.geocaching.com](https://www.geocaching.com). 




- - -
[Prev](DocGisItemsRte) (Routes) | [Home](Home) | [Manual](DocMain) | [Index](AxAdvIndex) | [Top](#) | (Areas) [Next](DocGisItemsArea)
