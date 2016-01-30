"""
Zlotto - Medium-budget brand (medium and long distance)
Aurora - Luxury brand (short, medium and long distance)
Srill - Low-budget brand (short and medium distance)

short distance - 0km to 2500km
medium distance - 2500km to 7500km
long distance - 7500km++
"""

#ALL FUEL MEAUSRES IN GALLONS

import Airplane
import Place
import PlaneObjects

airplane_models_list = PlaneObjects.get_models()
#airplane_models_list = [PlaneObjects.Z200,PlaneObjects.A111,PlaneObjects.S650]

airplane_models_dict = { "Z200": airplane_models_list[1],
                         "A111": airplane_models_list[2],
                         "S650": airplane_models_list[3] }

Delhi = Place.Place('Delhi', 28.6139, 77.2090)
Kochi = Place.Place('Kochi', 9.9700, 76.2800)
"""Chennai = Place.Place('Chennai', , )
Hyderabad = Place.Place('Hyderabad', , )
Mumbai = Place.Place('Mumbai', , )
Kolkata = Place.Place('Kolkata', , )
Calicut = Place.Place('Calicut', , )
Bengaluru = Place.Place('Bengaluru', , )
Thiruvananthapuram = Place.Place('Thiruvananthapuram', , )"""


"""
Example for creating an airplane instance (model=S650, owner=spideyonthego):
    S650_1 = Airplane.Airplane(airplane_models_dict["S650"], 'spideyonthego')

Example for flying an airplane instance (origin=Delhi, destination=Kochi):
    S650_1.fly(Delhi, Kochi)
"""
