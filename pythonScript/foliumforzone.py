
# || python code for interactive map || #

# --> import dependencies <-- #

import geopandas as gpd
import folium 
import numpy
import folium.plugins
import branca
from folium.plugins import GroupedLayerControl

# --> import necesssary shape files <-- #
mathura = gpd.read_file('Production/IOCL-MATHURA, UTTAR PRADESH/laa_MATHURA.shp')
kol = gpd.read_file('kolhapur/laa_KOLHAPUR.shp')
mangolore = gpd.read_file('Production/MRPL-MANGALORE,KARNATAKA/laa_DAKSHIN KANNAD.shp')
vizakh = gpd.read_file('Production/HPCL-VISAKH,ANDHRA PRADESH/laa_VISHAKHAPATNAM.shp')
haldia = gpd.read_file('Production/IOCL-HALDIA, WEST BENGAL/laa_PURBA MEDINIPUR.shp')
guwahati = gpd.read_file('Production/IOCL-GUWAHATI,ASSAM/laa_KAMRUP.shp')
panipat = gpd.read_file('Production/IOCL-PANIPAT, HARYANA/laa_PANIPAT.shp')


# --> Create maps <-- #

m1 = folium.Map([20.6,79], zoom_start = 4.2)
m2 = folium.Map([20.6,79], zoom_start = 4.2)

fig = branca.element.Figure()
subplt1 = fig.add_subplot(1,2,1)
subplt2 = fig.add_subplot(1,2,2)

subplt1.add_child(m1)
subplt2.add_child(m2)

# --> note coordinates <-- #

mathura_cor = [27.383322,77.685826]
mangolore_cor = [12.983672,74.844177]
vizakh_cor = [17.690318,83.244275]
haldia_cor = [22.052313,88.107832]
guwahati_cor = [26.185304,91.809068]
panipat_cor = [29.476551,76.885337]


# --> define feature group <-- #

default = folium.FeatureGroup(name = "DEFAULT")
mathura_ftr = folium.FeatureGroup(name = "IOCL Mathura")
mangolore_ftr = folium.FeatureGroup(name = "MRPL Mangaluru")
vizakh_ftr = folium.FeatureGroup(name = "HPCL Vishakhapatnam")
haldia_ftr = folium.FeatureGroup(name = "IOCL Haldia")
guwahati_ftr = folium.FeatureGroup(name = "IOCL Guwahati")
panipat_ftr = folium.FeatureGroup(name = "IOCL Panipat")


# --> Add shape files to the map <-- #

folium.GeoJson(kol, zoom_on_click = True).add_to(default)
folium.GeoJson(mathura, zoom_on_click = True).add_to(mathura_ftr)
folium.GeoJson(mangolore, zoom_on_click = True).add_to(mangolore_ftr)
folium.GeoJson(vizakh, zoom_on_click = True).add_to(vizakh_ftr)
folium.GeoJson(haldia, zoom_on_click = True).add_to(haldia_ftr)
folium.GeoJson(guwahati, zoom_on_click = True).add_to(guwahati_ftr)
folium.GeoJson(panipat, zoom_on_click = True).add_to(panipat_ftr)


mass = 500000   # SAMPLE AMOUNT

radius = 2.9*numpy.cbrt(mass)  #taken from aloha tech doc

radius2 = 0.5*radius  #choosed randomly for demonstration purposes.

radius3 = 5*radius

fillred = 0.5
fillyellow = 0.3
fillblue = 0.15

# --> Add features(circles(threat zone)) <-- #
#------------------------------default------------------------------------#
folium.Circle(
    location=[ 16.7, 74.2 ],
    radius=radius3,
    color="black",
    weight=1,
    fill_opacity=fillblue,
    opacity=0.5,
    fill_color="Blue",
    fill=False,  # gets overridden by fill_color
    popup="{} meters".format(radius3),
    tooltip="Low",
).add_to(default)

folium.Circle(
    location=[ 16.7, 74.2 ],
    radius=radius,
    color="black",
    weight=1,
    fill_opacity=fillyellow,
    opacity=0.5,
    fill_color="Yellow",
    fill=False,  # gets overridden by fill_color
    popup="{} meters".format(radius),
    tooltip="Moderate",
).add_to(default)

folium.Circle(
    location=[ 16.7, 74.2 ],
    radius=radius2,
    color="black",
    weight=1,
    fill_opacity=fillred,
    opacity=0.5,
    fill_color="Red",
    fill=False,  # gets overridden by fill_color
    popup="{} meters".format(radius2),
    tooltip="Intense",
).add_to(default)

#---------------------------------mangaluru-----------------------------------#

folium.Circle(
    location=mangolore_cor,
    radius=radius3,
    color="black",
    weight=1,
    fill_opacity=fillblue,
    opacity=0.5,
    fill_color="Blue",
    fill=False,  # gets overridden by fill_color
    popup="{} meters".format(radius3),
    tooltip="Low",
).add_to(mangolore_ftr)

folium.Circle(
    location=mangolore_cor,
    radius=radius,
    color="black",
    weight=1,
    fill_opacity=fillyellow,
    opacity=0.5,
    fill_color="Yellow",
    fill=False,  # gets overridden by fill_color
    popup="{} meters".format(radius),
    tooltip="Moderate",
).add_to(mangolore_ftr)

folium.Circle(
    location=mangolore_cor,
    radius=radius2,
    color="black",
    weight=1,
    fill_opacity=fillred,
    opacity=0.5,
    fill_color="Red",
    fill=False,  # gets overridden by fill_color
    popup="{} meters".format(radius2),
    tooltip="Intense",
).add_to(mangolore_ftr)

#-----------------------------------mathura-------------------------------------#

folium.Circle(
    location=mathura_cor,
    radius=radius3,
    color="black",
    weight=1,
    fill_opacity=fillblue,
    opacity=0.5,
    fill_color="Blue",
    fill=False,  # gets overridden by fill_color
    popup="{} meters".format(radius3),
    tooltip="Low",
).add_to(mathura_ftr)

folium.Circle(
    location=mathura_cor,
    radius=radius,
    color="black",
    weight=1,
    fill_opacity=fillyellow,
    opacity=0.5,
    fill_color="Yellow",
    fill=False,  # gets overridden by fill_color
    popup="{} meters".format(radius),
    tooltip="Moderate",
).add_to(mathura_ftr)

folium.Circle(
    location=mathura_cor,
    radius=radius2,
    color="black",
    weight=1,
    fill_opacity=fillred,
    opacity=0.5,
    fill_color="Red",
    fill=False,  # gets overridden by fill_color
    popup="{} meters".format(radius2),
    tooltip="Intense",
).add_to(mathura_ftr)

#-------------------------------------vizakh---------------------------------------#

folium.Circle(
    location=vizakh_cor,
    radius=radius3,
    color="black",
    weight=1,
    fill_opacity=fillblue,
    opacity=0.5,
    fill_color="Blue",
    fill=False,  # gets overridden by fill_color
    popup="{} meters".format(radius3),
    tooltip="Low",
).add_to(vizakh_ftr)

folium.Circle(
    location=vizakh_cor,
    radius=radius,
    color="black",
    weight=1,
    fill_opacity=fillyellow,
    opacity=0.5,
    fill_color="Yellow",
    fill=False,  # gets overridden by fill_color
    popup="{} meters".format(radius),
    tooltip="Moderate",
).add_to(vizakh_ftr)

folium.Circle(
    location=vizakh_cor,
    radius=radius2,
    color="black",
    weight=1,
    fill_opacity=fillred,
    opacity=0.5,
    fill_color="Red",
    fill=False,  # gets overridden by fill_color
    popup="{} meters".format(radius2),
    tooltip="Intense",
).add_to(vizakh_ftr)

#-----------------------------------haldia---------------------------------#

folium.Circle(
    location=haldia_cor,
    radius=radius3,
    color="black",
    weight=1,
    fill_opacity=fillblue,
    opacity=0.5,
    fill_color="Blue",
    fill=False,  # gets overridden by fill_color
    popup="{} meters".format(radius3),
    tooltip="Low",
).add_to(haldia_ftr)

folium.Circle(
    location=haldia_cor,
    radius=radius,
    color="black",
    weight=1,
    fill_opacity=fillyellow,
    opacity=0.5,
    fill_color="Yellow",
    fill=False,  # gets overridden by fill_color
    popup="{} meters".format(radius),
    tooltip="Moderate",
).add_to(haldia_ftr)

folium.Circle(
    location=haldia_cor,
    radius=radius2,
    color="black",
    weight=1,
    fill_opacity=fillred,
    opacity=0.5,
    fill_color="Red",
    fill=False,  # gets overridden by fill_color
    popup="{} meters".format(radius2),
    tooltip="Intense",
).add_to(haldia_ftr)

#-----------------------------------------guwahati--------------------------------#

folium.Circle(
    location=guwahati_cor,
    radius=radius3,
    color="black",
    weight=1,
    fill_opacity=fillblue,
    opacity=0.5,
    fill_color="Blue",
    fill=False,  # gets overridden by fill_color
    popup="{} meters".format(radius3),
    tooltip="Low",
).add_to(guwahati_ftr)

folium.Circle(
    location=guwahati_cor,
    radius=radius,
    color="black",
    weight=1,
    fill_opacity=fillyellow,
    opacity=0.5,
    fill_color="Yellow",
    fill=False,  # gets overridden by fill_color
    popup="{} meters".format(radius),
    tooltip="Moderate",
).add_to(guwahati_ftr)

folium.Circle(
    location=guwahati_cor,
    radius=radius2,
    color="black",
    weight=1,
    fill_opacity=fillred,
    opacity=0.5,
    fill_color="Red",
    fill=False,  # gets overridden by fill_color
    popup="{} meters".format(radius2),
    tooltip="Intense",
).add_to(guwahati_ftr)

#------------------------------------panipat---------------------------------------#

folium.Circle(
    location=panipat_cor,
    radius=radius3,
    color="black",
    weight=1,
    fill_opacity=fillblue,
    opacity=0.5,
    fill_color="Blue",
    fill=False,  # gets overridden by fill_color
    popup="{} meters".format(radius3),
    tooltip="Low",
).add_to(panipat_ftr)

folium.Circle(
    location=panipat_cor,
    radius=radius,
    color="black",
    weight=1,
    fill_opacity=fillyellow,
    opacity=0.5,
    fill_color="Yellow",
    fill=False,  # gets overridden by fill_color
    popup="{} meters".format(radius),
    tooltip="Moderate",
).add_to(panipat_ftr)

folium.Circle(
    location=panipat_cor,
    radius=radius2,
    color="black",
    weight=1,
    fill_opacity=fillred,
    opacity=0.5,
    fill_color="Red",
    fill=False,  # gets overridden by fill_color
    popup="{} meters".format(radius2),
    tooltip="Intense",
).add_to(panipat_ftr)


m1.add_child(mathura_ftr)
m1.add_child(mangolore_ftr)
m1.add_child(vizakh_ftr)
m1.add_child(haldia_ftr)
m1.add_child(guwahati_ftr)
m1.add_child(panipat_ftr)
m1.add_child(default)


GroupedLayerControl(
    groups={'groups1': [default, mathura_ftr, mangolore_ftr, vizakh_ftr, haldia_ftr, guwahati_ftr, panipat_ftr]},
    collapsed=True,
).add_to(m1)

folium.plugins.MousePosition().add_to(m1)
folium.plugins.MousePosition().add_to(m2)

fig.save('final_demo_map.html') # saves all the elements and map as an html page

# THIS SCRIPT MAKES TWO MAPS. WE ONLY USE ONE ON THE ACTUAL WEBPAGE. THE OTHER IS REPLACED WITH THE WEATHER MAP. 
