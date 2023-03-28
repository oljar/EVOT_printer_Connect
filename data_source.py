import fillpdf
from fillpdf import fillpdfs
import re
from tkinter import filedialog
import os
from tkinter import *
from tkinter import ttk
from default_value import *





def open_pattern_File():

    global path_in
    path_in = filedialog.askdirectory(initialdir = default_path_in)



def get_data ():
    path_plate = os.path.join(path_in, 'tabliczka.pdf')
    path_cert = os.path.join(path_in, 'atest.pdf')
    path_protocol = os.path.join(path_in, 'protocol.pdf')



    data_plate = fillpdfs.get_form_fields(path_plate)
    data_cert = fillpdfs.get_form_fields(path_cert)
    data_protocol =  fillpdfs.get_form_fields(path_protocol)


    print(f'asd{data_protocol}')

    get_data.selected_ahu_value = data_plate['evo']
    #

    try :
        pos = re.search("R|L$", (data_plate['supply']))
        get_data.selected_supply_value = (data_plate['supply'])[:(pos.span())[0]]

    except :
        get_data.selected_supply_value = data_plate['supply']

    try :
        get_data.ahu_range = re.findall(r'\d+',get_data.selected_supply_value)[0] # wielkość centrali
    except :
        get_data.ahu_range = ''

    try :
        get_data.selected_exhaust_value = (data_plate['exhaust'])[:(pos.span())[0]]
    except:
        get_data.selected_exhaust_value = data_plate['exhaust']

    try:
        get_data.entry_supply_flow_value = data_plate['air flow s']
    except:
        get_data.entry_supply_flow_value = ''


    try:
        get_data.entry_exhaust_flow_value = data_plate['air flow e']
    except:
        get_data.entry_exhaust_flow_value = ''

    try:
        get_data.entry_supply_pressure_value = data_plate['external press s']
    except:
        get_data.entry_supply_pressure_value = ''

    try:
        get_data.entry_exhaust_pressure_value = data_plate['external press e']
    except:
        get_data.entry_exhaust_pressure_value = ''


    get_data.symbol_electric_heater_value = data_cert['Pole tekstowe 8'].split('\r')[1]
    get_data.electric_heater_plate_value_in = data_plate['electric heater s']
    get_data.mass_value= data_plate['weight t']
    version_type=('jhj','kjkjhk','ccccc')
    get_data.symbol_water_heater_value = data_cert['Pole tekstowe 8'].split('\r')[0]
    get_data.water_heater_plate_value = data_plate['heatre I s']
    get_data.symbol_reverse_exchanger_value = "symbol_reverse_exchanger_value"
    get_data.reverse_heater_plate_value = "reverse_heater_plate_value"
    get_data.symbol_water_cooler_value = data_cert['Pole tekstowe 7'].split('\r')[0]
    get_data.water_cooler_plate_value = data_plate['cooler s'].split(';')[0]
    get_data.symbol_refrageration_cooler_value = data_cert['Pole tekstowe 7'].split('\r')[1]
    get_data.refrageration_cooler_plate_value = data_plate['cooler s'].split(';')[1]
    get_data.symbol_EC_supply_fan_value = data_cert['Pole tekstowe 27'].split('\r')[0]
    get_data.power_EC_supply_fan_value  = data_cert['Pole tekstowe 9'].split()[0]
    get_data.voltage_EC_supply_fan_value = data_cert['Pole tekstowe 10'].split()[0]
    get_data.frequency_EC_supply_fan_value = data_cert['Pole tekstowe 11'].split()[0]
    get_data.quantity_EC_supply_fan_value = 1
    try:
        get_data.symbol_EC_exhaust_fan_value = data_cert['Pole tekstowe 27'].split('\r')[1]
    except:
        get_data.symbol_EC_exhaust_fan_value =''

    get_data.power_EC_exhaust_fan_value =  data_cert['Pole tekstowe 9'].split()[1]
    get_data.voltage_EC_exhaust_fan_value = data_cert['Pole tekstowe 10'].split()[1]
    get_data.frequency_EC_exhaust_fan_value = data_cert['Pole tekstowe 11'].split()[1]
    get_data.quantity_EC_exhaust_fan_value = 1

   #AC
    get_data.symbol_AC_supply_fan_value = data_cert['Pole tekstowe 27'].split('\r')[0]
    get_data.power_AC_supply_fan_value = data_cert['Pole tekstowe 9'].split()[0]

    get_data.voltage_AC_supply_fan_value = data_cert['Pole tekstowe 10'].split()[0]
    get_data.frequency_AC_supply_fan_value = data_cert['Pole tekstowe 11'].split()[0]
    get_data.quantity_AC_supply_fan_value = 1

    try:
        get_data.symbol_AC_exhaust_fan_value = data_cert['Pole tekstowe 27'].split('\r')[1]
    except :
        get_data.symbol_AC_exhaust_fan_value = ''

    get_data.power_AC_exhaust_fan_value = data_cert['Pole tekstowe 9'].split()[1]
    get_data.voltage_AC_exhaust_fan_value = data_cert['Pole tekstowe 10'].split()[1]
    get_data.frequency_AC_exhaust_fan_value = data_cert['Pole tekstowe 11'].split()[1]
    get_data.quantity_AC_exhaust_fan_value = 1
    get_data.symbol_supply_damper_value = f'{get_data.ahu_range} STD_SLCR'
    get_data.symbol_exaust_damper_value = f'{get_data.ahu_range} STD_SLCR'

    get_data.symbol_cross_heat_exchanger_value = f'Wym. przeciwprądowy EVOT {get_data.ahu_range} CPR H'


    get_data.symbol_rotor_heat_exchanger_value = f'Zespół wym. obrotowego EVOT {get_data.ahu_range} RR'

    get_data.additional_exuipment_value = "additional_exuipment_value_1"
    get_data.unit_water_cooler = data_plate ['cooler u'].split(';')[0]
    get_data.unit_refrageration_cooler = data_plate['cooler u'].split(';')[1]


    s_and_p_value = "s_and_p_value_1"



    return get_data





data_filter_plate= fillpdfs.get_form_fields('data/filtr_tabliczka.pdf')
data_filter_02_plate= fillpdfs.get_form_fields('data/filtr_tabliczka.pdf')




try :

    get_data ()


except:
    data_plate = fillpdfs.get_form_fields('data/tabliczka_PL.pdf')
    data_cert = fillpdfs.get_form_fields('data/atest.pdf')
    protocol = fillpdfs.get_form_fields('data/protocol.pdf')







    get_data.water_heater_plate_value = "odśwież"
    print(data_plate)
    print('######')
    print(data_cert)
    print('######')
    print(protocol)
    print('######')




    get_data.selected_ahu_value = data_plate['evo']

    try:
        get_data.entry_supply_flow_value = data_plate['air flow s']
    except:
        get_data.entry_supply_flow_value = ''

    try:
        get_data.entry_exhaust_flow_value = data_plate['air flow e']
    except:
        get_data.entry_exhaust_flow_value = ''

    try:
        get_data.entry_supply_pressure_value = data_plate['external press s']
    except:
        get_data.entry_supply_pressure_value = ''

    try:
        get_data.entry_exhaust_pressure_value = data_plate['external press e']
    except:
        get_data.entry_exhaust_pressure_value = ''

    #

    try :
        pos = re.search("R|L$", (data_plate['supply']))
        get_data.selected_supply_value = (data_plate['supply'])[:(pos.span())[0]]
    except:
        get_data.selected_supply_value = (data_plate['supply'])


    try :
        get_data.ahu_range = re.findall(r'\d+',get_data.selected_supply_value)[0] # wielkość centrali
    except:
        get_data.ahu_range = ''


    try :
        get_data.selected_exhaust_value = (data_plate['exhaust'])[:(pos.span())[0]]
    except:
        get_data.selected_exhaust_value = (data_plate['exhaust'])


    get_data.symbol_electric_heater_value = 'odśwież'
    get_data.electric_heater_plate_value_in = 'odśwież'
    get_data.mass_value= data_plate['weight t']
    version_type=('jhj','kjkjhk','ccccc')
    get_data.symbol_water_heater_value = 'odśwież'
    get_data.water_heater_plate_value = 'odśwież'
    get_data.symbol_reverse_exchanger_value = 'odśwież'
    get_data.reverse_heater_plate_value = 'odśwież'
    get_data.symbol_water_cooler_value = 'odśwież'
    get_data.water_cooler_plate_value = 'odśwież'


    get_data.symbol_refrageration_cooler_value = 'odśwież'
    get_data.refrageration_cooler_plate_value = 'odśwież'

    get_data.symbol_EC_supply_fan_value = 'odśwież'
    get_data.power_EC_supply_fan_value  = 'odśwież'
    get_data.voltage_EC_supply_fan_value = 'odśwież'
    get_data.frequency_EC_supply_fan_value = 'odśwież'
    get_data.quantity_EC_supply_fan_value = 'odśwież'
    get_data.symbol_EC_exhaust_fan_value = 'odśwież'
    get_data.power_EC_exhaust_fan_value =  'odśwież'
    get_data.voltage_EC_exhaust_fan_value = 'odśwież'
    get_data.frequency_EC_exhaust_fan_value = 'odśwież'
    get_data.quantity_EC_exhaust_fan_value = 'odśwież'
    get_data.power_AC_supply_fan_value = 'odśwież'
    get_data.symbol_AC_supply_fan_value = 'odśwież'
    get_data.voltage_AC_supply_fan_value = 'odśwież'
    get_data.frequency_AC_supply_fan_value = 'odśwież'
    get_data.quantity_AC_supply_fan_value = 1
    get_data.symbol_AC_exhaust_fan_value = 'odśwież'
    get_data.power_AC_exhaust_fan_value = 'odśwież'
    get_data.voltage_AC_exhaust_fan_value = 'odśwież'
    get_data.frequency_AC_exhaust_fan_value = 'odśwież'
    get_data.quantity_AC_exhaust_fan_value = 1



    # symbol_G4_supply_filter_value = data_cert['Pole tekstowe 12'].split('/')[1]
    # quantity_G4_supply_filter_value = data_cert['Pole tekstowe 12'].split('/')[2]
    # symbol_M5_supply_filter_value = data_cert['Pole tekstowe 12'].split('/')[1]
    # quantity_M5_supply_filter_value = data_cert['Pole tekstowe 12'].split('/')[2]
    # symbol_F7_supply_filter_value = data_cert['Pole tekstowe 12'].split('/')[1]
    # quantity_F7_supply_filter_value = data_cert['Pole tekstowe 12'].split('/')[2]
    # symbol_F9_supply_filter_value = data_cert['Pole tekstowe 12'].split('/')[1]
    # quantity_F9_supply_filter_value = data_cert['Pole tekstowe 12'].split('/')[2]
    # symbol_G4_exhaust_filter_value = data_cert['Pole tekstowe 25'].split('/')[1]
    # quantity_G4_exhaust_filter_value = data_cert['Pole tekstowe 25'].split('/')[2]
    # symbol_M5_exhaust_filter_value = data_cert['Pole tekstowe 25'].split('/')[1]
    # quantity_M5_exhaust_filter_value = data_cert['Pole tekstowe 25'].split('/')[2]
    # symbol_F7_exhaust_filter_value = data_cert['Pole tekstowe 25'].split('/')[1]
    # quantity_F7_exhaust_filter_value = data_cert['Pole tekstowe 25'].split('/')[2]
    # symbol_F9_exhaust_filter_value  = data_cert['Pole tekstowe 25'].split('/')[1]
    # quantity_F9_exhaust_filter_value = data_cert['Pole tekstowe 25'].split('/')[2]



    get_data.symbol_supply_damper_value = 'odśwież'
    get_data.symbol_exaust_damper_value = 'odśwież'





    get_data.additional_exuipment_value = 'odśwież'
    s_and_p_value = "s_and_p_value_1"



