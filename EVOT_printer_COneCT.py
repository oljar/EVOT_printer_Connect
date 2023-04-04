import datetime

from fan_source import *
from data_source import *
from check_and_probe import *
from filter_source import *
from fillpdf import fillpdfs
from default_value import *
from heat_exchanger_source import *
import requests
import urllib3
from tkinter import messagebox

urllib3.disable_warnings()



class Application (Frame):
    def __init__(self,master):


        super(Application,self).__init__(master)


    #  heater

        self.example_fan_number_value = IntVar()
        self.symbol_EC_supply_fan_value = StringVar()
        self.power_EC_supply_fan_value = StringVar()
        self.voltage_EC_supply_fan_value = StringVar()
        self.frequency_EC_supply_fan_value = StringVar()
        self.quantity_EC_supply_fan_value = StringVar()
        self.symbol_EC_exhaust_fan_value = StringVar()
        self.power_EC_exhaust_fan_value = StringVar()
        self.voltage_EC_exhaust_fan_value = StringVar()
        self.frequency_EC_exhaust_fan_value = StringVar()
        self.quantity_EC_exhaust_fan_value = StringVar()

        self.symbol_AC_supply_fan_value = StringVar()
        self.power_AC_supply_fan_value = StringVar()
        self.voltage_AC_supply_fan_value = StringVar()
        self.frequency_AC_supply_fan_value = StringVar()
        self.quantity_AC_supply_fan_value = StringVar()
        self.symbol_AC_exhaust_fan_value = StringVar()
        self.power_AC_exhaust_fan_value = StringVar()
        self.voltage_AC_exhaust_fan_value = StringVar()
        self.frequency_AC_exhaust_fan_value = StringVar()
        self.quantity_AC_exhaust_fan_value = StringVar()

        self.quantity_supply_filter_value = StringVar()
        self.quantity_supply_filter_02_value = StringVar()

        self.quantity_exhaust_filter_value = StringVar()
        self.quantity_exhaust_filter_02_value = StringVar()





        self.settings()
        self.connect_modul()
        self.flow_type_choice()
        self.identity()
        self.heater_choice()
        self.cooler_choice()
        self.fan_choice()
        self.supply_type_filter_choice()
        self.supply_type_filter_02_choice()

        self.exhaust_type_filter_choice()
        self.exhaust_type_filter_02_choice()

        self.supply_filter_choice()
        self.supply_filter_02_choice()

        self.exhaust_filter_choice()
        self.exhaust_filter_02_choice()

        self.heat_exchanger_choice()
        self.damper_choice()
        self.s_and_p()
        self.accept()
        self.additional_equip_choice()
        self.quantity_comment_water_heater = 0
        self.quantity_comment_reverse_exchanger =0
        self.quantity_comment_water_cooler = 0
        self.quantity_comment_refrageration_cooler = 0
        self.myToken =0
        self.qfan_sup_EC = ''
        self.qfan_exh_EC = ''
        self.qfan_sup_AC = ''
        self.qfan_exh_AC = ''
        self.main_folder_name = 'Atest_tabliczka_protokół_ZP3'







        self.update_supply_fan_EC_value()
        self.update_exhaust_fan_EC_value()
        self.update_supply_fan_AC_value()
        self.update_exhaust_fan_AC_value()

        self.style = ttk.Style()



        #   default choice
        self.heater_choice_value.set(4)
        self.cooler_choice_value.set(4)
        self.fan_choice_value.set(4)

        self.supply_filter_choice_value.set(5)
        self.supply_filter_02_choice_value.set(5)


        self.exhaust_filter_choice_value.set(5)
        self.exhaust_filter_02_choice_value.set(5)


        self.heat_exchanger_choice_value.set(5)
        self.damper_choice_value.set(4)
        self.add_equip_choice_value.set(2)

        self.supply_type_filter_choice_value.set(1)
        self.supply_type_filter_02_choice_value.set(1)

        self.exhaust_type_filter_choice_value.set(1)
        self.exhaust_type_filter_02_choice_value.set(1)

        self.flow_type_choice_value.set(1)

        self.example_fan_number_value.set(1)

        self.quantity_supply_filter_value.set('')
        self.quantity_supply_filter_02_value.set('')

        self.quantity_exhaust_filter_value.set('')
        self.quantity_exhaust_filter_02_value.set('')

        self.numer_Characters_Enrty = 18





        ########################################################################################################################

    def approval_name_date(self):
        if  self.aproval_switch.get() == True :
            self.entry_data.insert(END, self.actual_date)
            print ('Tak')



        elif self.aproval_switch.get() == False :
            self.entry_data.delete(0, END)



    def settings(self):

        self.settings_frame = ttk.LabelFrame(tab0)


        self.settings_frame.pack(anchor=SW, ipadx=20, padx=20)
        self.inspector_name_value = StringVar()
        self.lbl_inspector_name = ttk.Label(self.settings_frame, text="kontroler KJ").grid(row=1, column=1, padx=10, pady=(10,3))
        self.inspector_name = ('Jarosław Olszewski','Dominik Tański','Marcin Elmanowski')
        self.combobox_suplly = ttk.Combobox(self.settings_frame, values=self.inspector_name, textvariable=self.inspector_name_value).grid(row=1, column=2,  padx=10, pady=(10,3))

        self.aproval_switch = BooleanVar(value=0)

        self.approve_name_date = ttk.Checkbutton(self.settings_frame, text ='Wstaw', command = self.approval_name_date ,onvalue = True, offvalue = False,
                                                     variable = self.aproval_switch ).grid(row=1, column=4, padx=10, pady=(10,3))






        self.password = StringVar()
        self.lbl_pass = ttk.Label(self.settings_frame, text="hasło").grid(row=2, column=1, padx=10, pady=3)
        self.entry_pass = ttk.Entry(self.settings_frame, show="*", textvariable=self.password)
        self.entry_pass.grid(row=2, column=2, padx=10, ipadx=10, pady=(10, 3))


        self.selected_ahu_value = StringVar()
        self.lbl_type = ttk.Label(self.settings_frame, text="typ EVO-T").grid(row=5, column=1, padx=10, pady=3)
        self.entry_type = ttk.Entry(self.settings_frame, textvariable= self.selected_ahu_value)
        self.entry_type.insert(END,get_data.selected_ahu_value)
        self.entry_type.config(state = DISABLED)
        self.entry_type.grid(row=5, column=2,padx=10,ipadx=10, pady=(10,3))


        self.data_value = StringVar()
        self.data=ttk.Label(self.settings_frame ,text = "data").grid(row =15,column = 1,padx=10,pady=(10,3))
        self.entry_data=ttk.Entry(self.settings_frame,textvariable = self.data_value  )
        self.actual_date = datetime.datetime.today().strftime('%d-%m-%Y')

        self.entry_data.grid(row =15 ,column = 2,padx=1,pady=(10,3), ipadx=10 )

        # folder with pattern choice
        self.pattern_choice_frame = ttk.LabelFrame(tab0)
        self.pattern_choice_frame.pack(anchor=W, padx=15)
        self.text_folder = Label(self.pattern_choice_frame,text='Lokalizacja wzorców').grid(row = 1, column = 1, padx=20 , pady=(20,3))
        self.open_button=ttk.Button(self.pattern_choice_frame,text = "folder", command = open_pattern_File).grid(row = 1, column = 15, padx=(20,40) , pady=(20,3) )
        self.text_folder = Label(self.pattern_choice_frame,text='Pobierz z wybranej lokalizacji').grid(row = 15, column = 1 , padx=(25,65) , pady=(30,20))
        self.apply_button=ttk.Button(self.pattern_choice_frame,command = self.run_id ,text = "pobierz")
        self.apply_button.grid(row = 15, column = 15, padx=(22,40) , pady=(30,20) )
        self.accept_english_switch = BooleanVar(value=0)
        self.accept_english = ttk.Checkbutton(self.settings_frame, text='Angielski', onvalue=True, offvalue=False,variable=self.accept_english_switch)
        self.accept_english.grid(row=1, column=20, padx=10, pady=(10, 3))




    def connect_modul(self):

        self.connect_frame = ttk.LabelFrame(tab0)

        self.connect_frame.pack(anchor=SW, padx=20, ipady=5)
        self.order_connect_value = StringVar()
        self.lbl_order_connect = ttk.Label(self.connect_frame, text="order").grid(row=2, column=1, padx=20)
        self.entry_order_connect = ttk.Entry(self.connect_frame, textvariable=self.order_connect_value)
        self.entry_order_connect.grid(row=2, column=2, padx=10, ipadx=10, pady=(10, 3))
        self.get_connect_button = ttk.Button(self.connect_frame, command = self.get_server_data, text="get data").grid(row=2, column=5, padx=10, pady=(10, 3))


    def run_id(self):
        try:
            get_data()
            self.identity_frame.destroy()
            self.identity()
            self.apply_button.config(text='ok')

        except:
            self.apply_button.config(text='błąd')



        self.update_supply_fan_AC_value()
        self.update_exhaust_fan_AC_value()

        if self.entry_type.get() == 'EVO-T+' and (self.symbol_ahu_range.get()) == '8000':
            self.example_fan_number_value.set(3)



        self.update_supply_fan_EC_value()
        self.update_exhaust_fan_EC_value()













    def update_supply_fan_EC_value(self):
        try:
            self.symbol_EC_supply_fan_value.set(symbol_EC_supply_fan_value[str(self.symbol_ahu_range.get())+'_'+ str(self.example_fan_number_value.get())])
        except:
            pass


        try:
            self.power_EC_supply_fan_value.set(power_EC_supply_fan_value[str(self.symbol_ahu_range.get())+'_'+ str(self.example_fan_number_value.get())])
        except:
            pass



        try:
            self.voltage_EC_supply_fan_value.set(voltage_EC_supply_fan_value[str(self.symbol_ahu_range.get())+'_'+ str(self.example_fan_number_value.get())])
        except:
            pass


        try:
            self.frequency_EC_supply_fan_value.set(frequency_EC_supply_fan_value[str(self.symbol_ahu_range.get())+'_'+ str(self.example_fan_number_value.get())])
        except:
            pass


        try:
            self.quantity_EC_supply_fan_value.set(quantity_EC_supply_fan_value[str(self.symbol_ahu_range.get())+'_'+ str(self.example_fan_number_value.get())])
        except:
            pass




    def update_exhaust_fan_EC_value(self):

        try:
            self.symbol_EC_exhaust_fan_value.set(symbol_EC_exhaust_fan_value[str(self.symbol_ahu_range.get())+'_'+ str(self.example_fan_number_value.get())])
        except:
            pass

        try:
            self.power_EC_exhaust_fan_value.set(power_EC_exhaust_fan_value[str(self.symbol_ahu_range.get()) + '_' + str(self.example_fan_number_value.get())])
        except:
            pass

        try:
            self.power_EC_exhaust_fan_value.set(power_EC_exhaust_fan_value[str(self.symbol_ahu_range.get()) + '_' + str(self.example_fan_number_value.get())])
        except:
            pass

        try:
            self.voltage_EC_exhaust_fan_value.set(voltage_EC_exhaust_fan_value[str(self.symbol_ahu_range.get()) + '_' + str(self.example_fan_number_value.get())])
        except:
            pass

        try:
            self.frequency_EC_exhaust_fan_value.set(frequency_EC_exhaust_fan_value[str(self.symbol_ahu_range.get()) + '_' + str(self.example_fan_number_value.get())])
        except:
            pass

        try:
            self.quantity_EC_exhaust_fan_value.set(quantity_EC_exhaust_fan_value[str(self.symbol_ahu_range.get()) + '_' + str(self.example_fan_number_value.get())])
        except:
            pass






    def update_supply_fan_AC_value(self):
        try:
            self.symbol_AC_supply_fan_value.set(symbol_AC_supply_fan_value[str(self.symbol_ahu_range.get()) + '_' + str(self.example_fan_number_value.get())])
        except:
            pass

        try:
            self.power_AC_supply_fan_value.set(power_AC_supply_fan_value[str(self.symbol_ahu_range.get()) + '_' + str(self.example_fan_number_value.get())])
        except:
            pass

        try:
            self.voltage_AC_supply_fan_value.set(voltage_AC_supply_fan_value[str(self.symbol_ahu_range.get()) + '_' + str(self.example_fan_number_value.get())])
        except:
            pass

        try:
            self.frequency_AC_supply_fan_value.set(frequency_AC_supply_fan_value[str(self.symbol_ahu_range.get()) + '_' + str(self.example_fan_number_value.get())])
        except:
            pass

        try:
            self.quantity_AC_supply_fan_value.set(quantity_AC_supply_fan_value[str(self.symbol_ahu_range.get()) + '_' + str(self.example_fan_number_value.get())])
        except:
            pass

    def update_exhaust_fan_AC_value(self):
        try:
            self.symbol_AC_exhaust_fan_value.set(symbol_AC_exhaust_fan_value[str(self.symbol_ahu_range.get()) + '_' + str(self.example_fan_number_value.get())])
        except:
            pass

        try:
            self.power_AC_exhaust_fan_value.set(power_AC_exhaust_fan_value[str(self.symbol_ahu_range.get()) + '_' + str(self.example_fan_number_value.get())])
        except:
            pass

        try:
            self.power_AC_exhaust_fan_value.set(power_AC_exhaust_fan_value[str(self.symbol_ahu_range.get()) + '_' + str(self.example_fan_number_value.get())])
        except:
            pass

        try:
            self.voltage_AC_exhaust_fan_value.set(voltage_AC_exhaust_fan_value[str(self.symbol_ahu_range.get()) + '_' + str(self.example_fan_number_value.get())])
        except:
            pass

        try:
            self.frequency_AC_exhaust_fan_value.set(frequency_AC_exhaust_fan_value[str(self.symbol_ahu_range.get()) + '_' + str(self.example_fan_number_value.get())])
        except:
            pass

        try:
            self.quantity_AC_exhaust_fan_value.set(quantity_AC_exhaust_fan_value[str(self.symbol_ahu_range.get()) + '_' + str(self.example_fan_number_value.get())])
        except:
            pass











    def flow_type_choice(self):
        self.lfradio = ttk.LabelFrame(tab1,text='AHU')
        self.lfradio.pack()
        self.flow_type_choice_value = IntVar()
        self.supply_exhuaust_ahu_choice = ttk.Radiobutton(self.lfradio, text="Nawiewno - Wywiewna", variable = self.flow_type_choice_value, value=1, comman=self.supply_exhuaust_ahu_function).grid(row=0, column=0, padx=20, pady=5)
        self.supply_ahu_choice = ttk.Radiobutton(self.lfradio, text="Nawiewna", variable = self.flow_type_choice_value, value=2, comman=self.supply_ahu_function).grid(row=0, column=5, padx=20, pady=5)
        self.exhaust_ahu_choice = ttk.Radiobutton(self.lfradio, text="Wywiewna", variable = self.flow_type_choice_value, value=3, comman=self.exhaust_ahu_function).grid(row=0, column=10, padx=20, pady=5)



    def supply_exhuaust_ahu_function(self):

        self.update_supply_fan_EC_value()
        self.update_exhaust_fan_EC_value()
        self.update_supply_fan_AC_value()
        self.update_exhaust_fan_AC_value()

        self.entry_type_supply.config(state=ACTIVE)
        self.entry_type_supply.delete(0, END)
        self.entry_type_supply.insert(END, get_data.selected_supply_value)

        self.entry_type_exhaust.config(state=ACTIVE)
        self.entry_type_exhaust.delete(0, END)
        self.entry_type_exhaust.insert(END, get_data.selected_supply_value)







        self.fan_choice_value.set(4)
        try:
            self.lframe_fan.destroy()
        except:
            pass





    def supply_ahu_function(self):
        self.update_supply_fan_EC_value()
        self.update_supply_fan_AC_value()


        self.symbol_EC_exhaust_fan_value.set('')
        self.power_EC_exhaust_fan_value.set('')
        self.voltage_EC_exhaust_fan_value.set('')
        self.frequency_EC_exhaust_fan_value.set('')
        self.quantity_EC_exhaust_fan_value.set(' ')

        self.symbol_AC_exhaust_fan_value.set('')
        self.power_AC_exhaust_fan_value.set('')
        self.voltage_AC_exhaust_fan_value.set('')
        self.frequency_AC_exhaust_fan_value.set('')
        self.quantity_AC_exhaust_fan_value.set(' ')



        self.entry_type_supply.config(state=ACTIVE)
        self.entry_type_supply.delete(0, END)
        self.entry_type_supply.insert(END, get_data.selected_supply_value)
        self.entry_type_exhaust.delete(0, END)
        self.entry_type_exhaust.config(state=DISABLED)





        self.fan_choice_value.set(4)
        try:
            self.lframe_fan.destroy()
        except:
            pass




    def exhaust_ahu_function(self):

        self.update_exhaust_fan_EC_value()
        self.update_exhaust_fan_AC_value()

        self.symbol_EC_supply_fan_value.set('')
        self.power_EC_supply_fan_value.set('')
        self.voltage_EC_supply_fan_value.set('')
        self.frequency_EC_supply_fan_value.set('')
        self.quantity_EC_supply_fan_value.set('')

        self.symbol_AC_supply_fan_value.set('')
        self.power_AC_supply_fan_value.set('')
        self.voltage_AC_supply_fan_value.set('')
        self.frequency_AC_supply_fan_value.set('')
        self.quantity_AC_supply_fan_value.set('')

        self.entry_type_exhaust.config(state=ACTIVE)
        self.entry_type_exhaust.delete(0, END)
        self.entry_type_exhaust.insert(END, get_data.selected_supply_value)
        self.entry_type_supply.delete(0, END)
        self.entry_type_supply.config(state=DISABLED)





        self.fan_choice_value.set(4)
        try:
            self.lframe_fan.destroy()
        except:
            pass







    def identity(self):


        self.identity_frame = ttk.LabelFrame(tab1)

        self.symbol_ahu_range = StringVar()
        self.entry_ahu_range = Entry(self.settings_frame, textvariable=self.symbol_ahu_range)
        self.entry_ahu_range.insert(END, get_data.ahu_range)



        self.identity_frame.pack(anchor=W, padx=15)

   #   serial
        self.entry_serial_value = StringVar()
        self.lbl_serial=ttk.Label(self.identity_frame ,text = "Nr seryjny").grid(row =1,column = 1,padx=10,pady=(10,3))
        self.entry_serial=ttk.Entry(self.identity_frame,textvariable = self.entry_serial_value)
        self.entry_serial.grid(row=1, column=2, padx=1, pady=(10, 3), ipadx=10)

    # order
        self.entry_order_value = StringVar()
        self.lbl_order=ttk.Label(self.identity_frame,text = "Zlecenie").grid(row = 5,column = 1,padx=10,pady=3)
        self.entry_order=ttk.Entry(self.identity_frame, textvariable = self.entry_order_value)
        self.entry_order.grid(row =5,column = 2,padx=1,pady=3,ipadx=10 )
    # project
        self.entry_project_value = StringVar()
        self.lbl_project=ttk.Label(self.identity_frame ,text = "Projekt").grid(row = 10,column = 1,padx=10,pady=3)
        self.entry_project=ttk.Entry(self.identity_frame, textvariable = self.entry_project_value)
        self.entry_project.grid(row =10,column = 2,padx=1,pady=3, ipadx=10 )
   #  system
        self.entry_system_value = StringVar()
        self.lbl_system = ttk.Label(self.identity_frame, text="System").grid(row=15, column=1, padx=10, pady=3)
        self.entry_system = ttk.Entry(self.identity_frame, textvariable = self.entry_system_value).grid(row=15, column=2, padx=1, pady=3, ipadx=10)



   #   type
        self.selected_ahu_value = StringVar()
        self.lbl_type = ttk.Label(self.identity_frame, text="typ EVO-T").grid(row=20, column=1, padx=10, pady=3)

        self.entry_type = ttk.Entry(self.identity_frame, textvariable = self.selected_ahu_value )
        #self.entry_type.config(state=DISABLED)
        self.entry_type.insert(END,get_data.selected_ahu_value)
        self.entry_type.grid(row=20, column=2, padx=10, pady=3,ipadx=10)



    # supply
        self.selected_supply_value = StringVar()
        self.lbl_supply = ttk.Label(self.identity_frame, text="nawiew - wykonanie").grid(row=25, column=1, padx=10, pady=3)
        self.entry_type_supply = ttk.Entry(self.identity_frame, textvariable = self.selected_supply_value)
        self.entry_type_supply.insert(END,get_data.selected_supply_value)
        self.entry_type_supply.grid(row=25, column=2,  pady=3, ipadx=10)



    # supply_execution
        self.selected_supply_execution_value = StringVar()
        self.version_supply_execution = ('L', 'R', '')

        self.combobox_suplly_execution = ttk.Combobox(self.identity_frame, values=self.version_supply_execution, width = 5 ,textvariable = self.selected_supply_execution_value )
        self.combobox_suplly_execution.config(state=DISABLED)
        self.combobox_suplly_execution.grid(row=25, column=10)
    #supply_flow

        self.entry_supply_flow_value = StringVar()
        self.lbl_supply_flow = ttk.Label(self.identity_frame, text="    N - wydatek powietrza [m3/h]").grid(row=30, column=1, padx=10, pady=3)
        self.entry_supply_flow = ttk.Entry(self.identity_frame, textvariable = self.entry_supply_flow_value)
        self.entry_supply_flow.insert(END, get_data.entry_supply_flow_value)
        self.entry_supply_flow.grid(row=30, column=2, padx=1, pady=3, ipadx=10)

    # supply_pressure

        self.entry_supply_pressure_value = StringVar()
        self.lbl_supply_pressure = ttk.Label(self.identity_frame, text="   N - spręż dyspozycyjny [Pa]").grid(row=35, column=1, padx=10, pady=3)
        self.entry_supply_pressure = ttk.Entry(self.identity_frame, textvariable = self.entry_supply_pressure_value )
        self.entry_supply_pressure.insert(END, get_data.entry_supply_pressure_value)
        self.entry_supply_pressure.grid(row=35, column=2, padx=1, pady=3, ipadx=10)




    #exhaust
        self.selected_exhaust_value = StringVar()
        self.lbl_exhaust = ttk.Label(self.identity_frame, text="wywiew - wykonanie").grid(row=40, column=1, padx=10, pady=3)
        self.entry_type_exhaust = ttk.Entry(self.identity_frame, textvariable = self.selected_exhaust_value)
        self.entry_type_exhaust.insert(END, get_data.selected_exhaust_value)
        self.entry_type_exhaust.grid(row=40, column=2 ,  pady=3, ipadx=10)




    # exhaust_execution
        self.selected_exhaust_execution_value = StringVar()
        self.version_exhaust_execution = ('L', 'R','')
        self.combobox_exhaust_execution = ttk.Combobox(self.identity_frame, values=self.version_exhaust_execution, textvariable=self.selected_exhaust_execution_value, width = 5 )
        self.combobox_exhaust_execution.config(state=DISABLED)
        self.combobox_exhaust_execution.grid(row=40, column=10)

    # exhaust_flow
        self.entry_exhaust_flow_value  = StringVar()
        self.lbl_exhaust_flow = ttk.Label(self.identity_frame, text="    W - wydatek powietrza [m3/h]").grid(row=45, column=1, padx=10, pady=3)
        self.entry_exhaust_flow = ttk.Entry(self.identity_frame, textvariable = self.entry_exhaust_flow_value )
        self.entry_exhaust_flow.insert(END, get_data.entry_exhaust_flow_value)
        self.entry_exhaust_flow.grid(row=45, column=2, padx=1, pady=3, ipadx=10)


    # exhaust_pressure
        self.entry_exhaust_pressure_value = StringVar()
        self.lbl_exhaust_pressure = ttk.Label(self.identity_frame, text="   W - spręż dyspozycyjny [Pa]").grid(row=50, column=1, padx=10, pady=3)
        self.entry_exhaust_pressure = ttk.Entry(self.identity_frame, textvariable = self.entry_exhaust_pressure_value )
        self.entry_exhaust_pressure.insert(END, get_data.entry_exhaust_pressure_value)
        self.entry_exhaust_pressure.grid(row=50, column=2, padx=1, pady=3, ipadx=10)



    # mass
        self.mass_value = StringVar()
        self.mass=ttk.Label(self.identity_frame ,text = "masa urządzenia [kg]").grid(row = 55,column = 1,padx=10,pady=3)
        self.entry_mass=ttk.Entry(self.identity_frame,textvariable = self.mass_value)
        self.entry_mass.insert(END,get_data.mass_value)
        self.entry_mass.grid(row = 55 ,column = 2,padx=1,pady=3, ipadx=10 )



    #
        self.destiny_value = StringVar()
        self.destiny = ttk.Label(self.identity_frame, text="przeznaczenie").grid(row=60, column=1, padx=10, pady=3)
        self.entry_destiny = ttk.Entry(self.identity_frame, textvariable=self.destiny_value)
        self.entry_destiny.grid(row=60, column=2, padx=1, pady=3, ipadx=10)



#heater
    ############################################################################################################################

    def heater_choice(self):
            self.lfradio = ttk.LabelFrame(tab2)
            self.lfradio.pack( )
            self.heater_choice_value = IntVar()
            self.electric_heater = ttk.Radiobutton(self.lfradio,text = "nagrzewnica elektryczna", variable = self.heater_choice_value, value = 1,command = self.electric_heater_function ).grid(row =0,column = 0,padx=20, pady = 5 )
            self.water_heater = ttk.Radiobutton(self.lfradio,text = "nagrzewnica wodna", variable = self.heater_choice_value, value = 2, command = self.water_heater_function ).grid(row =0,column = 5,padx=20,pady = 5)
            self.reverse_exchanger = ttk.Radiobutton(self.lfradio, text="wymiennik rewersyjny", variable = self.heater_choice_value, value= 3,command = self.reverse_exchanger_function ).grid(row = 0,column = 15 ,padx=20,pady = 5)
            self. lackoff_heater = ttk.Radiobutton(self.lfradio, text="brak", variable = self.heater_choice_value , value= 4, command = self.lackoff_heater_function ).grid (row = 0,column = 20,padx=20, pady = 5)



    def electric_heater_function(self):

            try :

                self.lframe.destroy()
            except:
                pass

            finally:



                self.lframe = ttk.LabelFrame(tab2)
                self.lframe.pack( anchor = W, padx=7)


                #symbol electric heater
                self.symbol_electric_heater_value = StringVar()
                self.lbl_symbol_electric_heater = ttk.Label(self.lframe, text="typ NE" ).grid(row=5, column=1,padx=1)
                self.entry_symbol_electric_heater = ttk.Entry(self.lframe, textvariable = self.symbol_electric_heater_value, width = 30)
                self.entry_symbol_electric_heater.insert(END,get_data.symbol_electric_heater_value )
                self.entry_symbol_electric_heater.grid(row=5, column=5, padx=2)



                # heater data  for plate
                self.electric_heater_plate_value = StringVar()
                self.lbl_plate_electric_heater = ttk.Label(self.lframe, text="dane" ).grid(row=10, column=1,padx=1,pady = 10)
                self.entry_plate_electric_heater = ttk.Entry(self.lframe, textvariable = self.electric_heater_plate_value,width = 30)
                self.entry_plate_electric_heater.insert(END, get_data.electric_heater_plate_value_in)
                self.entry_plate_electric_heater.grid(row=10, column=5, padx=2, ipadx=4,pady=10 )



                #
                #explanation
                self.explanation = ttk.Label(self.lframe, text="moc zima [kW] / ilość sekcji x moc sekcji [i x kW]/ napięcie zasialania [V] " ).grid(row=15, column=1,padx=1,pady = 10, columnspan = 5 )



    def water_heater_function(self):

            try :
                self.lframe.destroy()
            except:
                pass
            finally:

                #water heater symbol
                self.lframe = ttk.LabelFrame(tab2)

                self.lframe.pack( anchor = W)

                self.lframe.pack( anchor = W, padx=7)

                self.symbol_water_heater_value = StringVar()
                self.lbl_symbol_water_heater = ttk.Label(self.lframe, text="typ WN" ).grid(row=5, column=1,padx = 3)
                self.entry_symbol_water_heater = ttk.Entry(self.lframe, textvariable = self.symbol_water_heater_value,width = 30 )
                self.entry_symbol_water_heater.insert(END, get_data.symbol_water_heater_value)
                self.entry_symbol_water_heater.grid(row=5, column=5, padx = 3)


                # water heater data  for plate
                self.water_heater_plate_value = StringVar()
                self.lbl_plate_water_heater = ttk.Label(self.lframe, text="dane" ).grid(row=10, column=1,padx=1,pady = 10)
                self.entry_plate_water_heater = ttk.Entry(self.lframe, textvariable=self.water_heater_plate_value, width=30)
                #self.entry_plate_water_heater.insert(END, )

                self.entry_plate_water_heater.insert(END, get_data.water_heater_plate_value)



                self.entry_plate_water_heater.grid(row=10, column=5, padx=2, ipadx=4, pady=10)


                #explanation
                self.explanation = ttk.Label(self.lframe, text="zasilanie-powrót [stC] / moc zima [kW]/ spadek ciśnienia [kPa]" ).grid(row=15, column=1,padx=1,pady = 10, columnspan = 5 )

                # commnet in check and probe
                self.quantity_comment_water_heater +=1

                if self.accept_english_switch.get():
                    c_p_water_heater = check_probe_water_heater_ENG
                else:
                    c_p_water_heater = check_probe_water_heater


                if self.quantity_comment_water_heater == 1:
                    self.txt_s_and_p.insert(END, c_p_water_heater  + '\n')



    def reverse_exchanger_function(self):

            try :
                self.lframe.destroy()
            except:
                pass
            finally:
                self.lframe = ttk.LabelFrame(tab2)

                self.lframe.pack( anchor = W)

                self.lframe.pack( anchor = W, padx=7)

                self.symbol_reverse_exchanger_value = StringVar()
                self.lbl_reverse_exchanger = ttk.Label(self.lframe, text=" typ RE").grid(row=5, column=1, padx =3)
                self.entry_reverse_exchanger = ttk.Entry(self.lframe, textvariable=self.symbol_reverse_exchanger_value,width = 30)
                self.entry_reverse_exchanger.insert(END, get_data.symbol_reverse_exchanger_value)
                self.entry_reverse_exchanger.grid(row=5, column=5,padx = 3)



                # reverse heater data  for plate
                self.reverse_heater_plate_value = StringVar()
                self.lbl_plate_reverse_heater = ttk.Label(self.lframe, text="dane" ).grid(row=10, column=1,padx=1,pady = 10)
                self.entry_plate_reverse_heater = ttk.Entry(self.lframe, textvariable = self.reverse_heater_plate_value,width = 30)
                self.entry_plate_reverse_heater.insert(END, get_data.reverse_heater_plate_value)
                self.entry_plate_reverse_heater.grid(row=10, column=5, padx=2, ipadx=4,pady=10 )

                #explanation
                self.explanation = ttk.Label(self.lframe, text="moc lato [KW] / czynnik " ).grid(row=15, column=1,padx=1,pady = 10, columnspan = 5 )

                # commnet in check and probe
                self.quantity_comment_reverse_exchanger +=1

                if self.accept_english_switch.get() :
                    c_p_reverse_exchanger = check_probe_reverse_exchanger_ENG
                else :
                    c_p_reverse_exchanger = check_probe_reverse_exchanger




                if self.quantity_comment_reverse_exchanger == 1:
                    self.txt_s_and_p.insert(END, c_p_reverse_exchanger +'\n')




    def lackoff_heater_function(self):

        try :
            self.lframe.destroy()
        except :
            pass





#cooler
#######################################################################################################################

    def cooler_choice(self):
        self.lfradio = ttk.LabelFrame(tab3)
        self.lfradio.pack( )
        self.cooler_choice_value = IntVar()
        self.water_cooler = ttk.Radiobutton(self.lfradio,text = "chłodnica wodna ", variable = self.cooler_choice_value, value = 1,command = self.water_cooler_function).grid(row =0,column = 0,padx=20, pady = 5 )
        self.refrageration_cooler = ttk.Radiobutton(self.lfradio,text = "chłodnica freonowa", variable = self.cooler_choice_value, value = 2, command = self.refrageration_cooler_function ).grid(row =0,column = 5,padx=20,pady = 5)
        self. lackoff_cooler = ttk.Radiobutton(self.lfradio, text="brak", variable = self.cooler_choice_value , value= 4, command = self.lackoff_cooler_function ).grid (row = 0,column = 20,padx=20, pady = 5)







    def water_cooler_function(self):

        try :
            self.lframe.destroy()
        except:
            pass
        finally:

            #water cooler symbol
            self.lframe = ttk.LabelFrame(tab3)

            self.lframe.pack( anchor = W)

            self.lframe.pack( anchor = W, padx=7)

            self.symbol_water_cooler_value = StringVar()
            self.lbl_symbol_water_cooler= ttk.Label(self.lframe, text="typ CHW" ).grid(row=5, column=1,padx = 3)
            self.entry_symbol_water_cooler = ttk.Entry(self.lframe, textvariable = self.symbol_water_cooler_value,width = 30 )
            self.entry_symbol_water_cooler.insert(END, get_data.symbol_water_cooler_value)
            self.entry_symbol_water_cooler.grid(row=5, column=5, padx = 3)


            # water cooler data  for plate
            self.water_cooler_plate_value = StringVar()
            self.lbl_plate_water_cooler = ttk.Label(self.lframe, text="dane" ).grid(row=10, column=1, padx=2, ipadx=4, pady=10)
            self.entry_plate_water_cooler = ttk.Entry(self.lframe, textvariable=self.water_cooler_plate_value, width=30)
            self.entry_plate_water_cooler.insert(END, get_data.water_cooler_plate_value)
            self.entry_plate_water_cooler.grid(row=10, column=5, padx=2, ipadx=4, pady=10)

            #explanation
            self.explanation = ttk.Label(self.lframe, text="[zasilanie - powrót [stC] / moc lato [kW]/ spadek ciśnienia [kPa]" ).grid(row=15, column=1,padx=1,pady = 10, columnspan = 5 )


            # commnet in check and probe
            self.quantity_comment_water_cooler +=1

            if self.accept_english_switch.get():
                c_p_water_cooler =  check_probe_water_cooler_ENG
            else:
                c_p_water_cooler =  check_probe_water_cooler

            if self.quantity_comment_water_cooler == 1:
                self.txt_s_and_p.insert(END, c_p_water_cooler)




    def refrageration_cooler_function(self):

        try :
            self.lframe.destroy()
        except:
            pass
        finally:

            #water cooler symbol
            self.lframe = ttk.LabelFrame(tab3)

            self.lframe.pack( anchor = W)

            self.lframe.pack( anchor = W, padx=7)

            self.symbol_refrageration_cooler_value = StringVar()
            self.lbl_symbol_refrageration_cooler = ttk.Label(self.lframe, text="typ CHF" ).grid(row=5, column=1,padx = 3)
            self.entry_symbol_refrageration_cooler = ttk.Entry(self.lframe, textvariable = self.symbol_refrageration_cooler_value,width = 30 )
            self.entry_symbol_refrageration_cooler.insert(END, get_data.symbol_refrageration_cooler_value)
            self.entry_symbol_refrageration_cooler.grid(row=5, column=5, padx = 3)


            # water cooler data  for plate
            self.refrageration_cooler_plate_value = StringVar()
            self.lbl_plate_refrageration_cooler = ttk.Label(self.lframe, text="dane" ).grid(row=10, column=1,padx=1,pady = 10)
            self.entry_plate_refrageration_cooler = ttk.Entry(self.lframe, textvariable=self.refrageration_cooler_plate_value, width=30)
            self.entry_plate_refrageration_cooler.insert(END, get_data.refrageration_cooler_plate_value )
            self.entry_plate_refrageration_cooler.grid(row=10, column=5, padx=2, ipadx=4, pady=10)

            #explanation
            self.explanation = ttk.Label(self.lframe, text=" moc lato [kW]/ czynnik" ).grid(row=15, column=1,padx=1,pady = 10, columnspan = 5 )

            # commnet in check and probe
            self.quantity_comment_refrageration_cooler +=1

            if self.accept_english_switch.get():
                c_p_refrageration_cooler = check_probe_refrageration_cooler_ENG
            else:
                c_p_refrageration_cooler = check_probe_refrageration_cooler

            if self.quantity_comment_refrageration_cooler == 1:
                self.txt_s_and_p.insert(END, c_p_refrageration_cooler )






    def lackoff_cooler_function(self):
        try :
            self.lframe.destroy()
        except :
            pass


#Fans
#######################################################################################################################

    def fan_choice(self):
        self.lfradio = ttk.LabelFrame(tab4,text='FAN')
        self.lfradio.pack( )
        self.fan_choice_value = IntVar()
        self.EC_fan = ttk.Radiobutton(self.lfradio, text ="EC wentylator ", variable = self.fan_choice_value, value = 1, command = self.EC_fan_function).grid(row =0, column = 0, padx=20, pady = 5)
        self.AC_fan = ttk.Radiobutton(self.lfradio, text ="AC wentylator ", variable = self.fan_choice_value, value = 2, command = self.AC_fan_function).grid(row =0, column = 5, padx=20, pady = 5)
        self.lackoff_supply_fan = ttk.Radiobutton(self.lfradio, text="brak", variable = self.fan_choice_value, value= 4, command = self.lackoff_fan_function).grid (row = 0, column = 20, padx=20, pady = 5)
        self.example_fan_number()



    def EC_fan_function(self):



        try :
            self.lframe_fan.destroy()
        except:
            pass
        finally:

            #supply_fan symbol

            self.symbol_EC_supply_fan_value.trace('w',self.validation_show_red)
            self.lframe_fan = ttk.LabelFrame(tab4, text= "EC - wentylator")
            self.lframe_fan.pack( anchor = W, padx=7 )
            self.lbl_symbol_EC_supply_fan= ttk.Label(self.lframe_fan, text="nawiew-typ-EC" ).grid(row=5, column=1,padx = 3,pady = 10)
            self.entry_symbol_EC_supply_fan = ttk.Entry(self.lframe_fan, textvariable = self.symbol_EC_supply_fan_value,width = 18,style="StyleECSupply.TEntry" )
            self.entry_symbol_EC_supply_fan.grid(row=5, column=5, padx=(0,50) )



            # Power - EC_supply_fan

            self.lbl_power_plate_EC_supply_fan = ttk.Label(self.lframe_fan, text="moc [kW]" ).grid(row=10, column=1,padx=1,pady = 10)
            self.entry_power_plate_EC_supply_fan = ttk.Entry(self.lframe_fan, textvariable=self.power_EC_supply_fan_value , width=10)
            self.entry_power_plate_EC_supply_fan.grid(row=10, column=5, padx=(0,100))

            # Voltage - EC_supply_fan


            self.lbl_voltage_plate_EC_supply_fan = ttk.Label(self.lframe_fan, text="napięcie zasilania [V]" ).grid(row=15, column=1,padx=1,pady = 10)
            self.entry_voltage_plate_EC_supply_fan = ttk.Entry(self.lframe_fan, textvariable=self.voltage_EC_supply_fan_value, width=10)
            self.entry_voltage_plate_EC_supply_fan.grid(row=15, column=5, padx=(0,100))

            # frequency - EC_supply_fan


            self.lbl_frequency_plate_EC_supply_fan = ttk.Label(self.lframe_fan, text="częstotliwość [Hz]").grid(row=20, column=1,padx=1, pady=10)
            self.entry_frequency_plate_EC_supply_fan = ttk.Entry(self.lframe_fan, textvariable=self.frequency_EC_supply_fan_value, width=10)
            self.entry_frequency_plate_EC_supply_fan.grid(row=20, column=5, padx=(0, 100))

            # quantity - EC_supply_fan


            self.lbl_quantity_EC_supply_fan = ttk.Label(self.lframe_fan, text="ilość").grid(row=25, column=1, padx=1, pady=10)
            self.entry_quantity_plate_EC_supply_fan = ttk.Entry(self.lframe_fan, textvariable=self.quantity_EC_supply_fan_value, width=10)
            self.entry_quantity_plate_EC_supply_fan.grid(row=25, column=5, padx=(0, 100))

            # Symbol - EC_exhaust_fan-

            self.symbol_EC_exhaust_fan_value.trace('w', self.validation_show_red)

            self.lbl_symbol_EC_exhaust_fan= ttk.Label(self.lframe_fan, text="wywiew-typ-EC" ).grid(row=5, column=10,padx = 3,pady = 10)
            self.entry_symbol_EC_exhaust_fan = ttk.Entry(self.lframe_fan, textvariable = self.symbol_EC_exhaust_fan_value, width = 18 ,style="StyleECExhaust.TEntry")
            self.entry_symbol_EC_exhaust_fan.grid(row=5, column=15, padx=(0,50))

            # Power - EC_exhaust_fan

            self.lbl_power_plate_EC_exhaust_fan = ttk.Label(self.lframe_fan, text="moc [kW]" ).grid(row=10, column=10,padx=1,pady = 10)
            self.entry_power_plate_EC_exhaust_fan = ttk.Entry(self.lframe_fan, textvariable=self.power_EC_exhaust_fan_value, width=10)
            self.entry_power_plate_EC_exhaust_fan.grid(row=10, column=15, padx=(0,100))


            self.lbl_voltage_plate_EC_exhaust_fan = ttk.Label(self.lframe_fan, text="napięcie zasilania [V]" ).grid(row=15, column=10,padx=1,pady = 10)
            self.entry_voltage_plate_EC_exhaust_fan = ttk.Entry(self.lframe_fan, textvariable=self.voltage_EC_exhaust_fan_value, width=10)
            self.entry_voltage_plate_EC_exhaust_fan.grid(row=15, column=15, padx=(0,100))


            self.lbl_frequency_plate_EC_exhaust_fan = ttk.Label(self.lframe_fan, text="częstotliwość [Hz]").grid(row=20, column=10,padx=1, pady=10)
            self.entry_frequency_plate_EC_exhaust_fan = ttk.Entry(self.lframe_fan, textvariable=self.frequency_EC_exhaust_fan_value, width=10)
            self.entry_frequency_plate_EC_exhaust_fan .grid(row=20, column=15, padx=(0, 100))



            self.lbl_quantity_EC_exhaust_fan = ttk.Label(self.lframe_fan, text="ilość").grid(row=25, column=10, padx=1, pady=10)
            self.entry_quantity_plate_EC_exhaust_fan = ttk.Entry(self.lframe_fan, textvariable=self.quantity_EC_exhaust_fan_value, width=10)
            self.entry_quantity_plate_EC_exhaust_fan.grid(row=25, column=15, padx=(0, 100))






    def AC_fan_function(self):

            try:
                self.lframe_fan.destroy()
            except:
                pass
            finally:

                # AC supply
                self.symbol_AC_supply_fan_value.trace('w', self.validation_show_red)
                self.lframe_fan = ttk.LabelFrame(tab4, text = "AC - wentylator")
                self.lframe_fan.pack(anchor=W, padx=7)



                self.lbl_symbol_AC_supply_fan = ttk.Label(self.lframe_fan, text="nawiew-typ-AC").grid(row=5, column=1, padx=3, pady=10)
                self.entry_symbol_AC_supply_fan = ttk.Entry(self.lframe_fan, textvariable=self.symbol_AC_supply_fan_value, width=18,style="StyleACSupply.TEntry" )
                self.entry_symbol_AC_supply_fan.grid(row=5, column=5, padx=(0,50))

                # Power - AC_supply_fan

                self.lbl_power_plate_AC_supply_fan = ttk.Label(self.lframe_fan, text="moc [kW]").grid(row=10, column=1, padx=1, pady=10)
                self.entry_power_plate_AC_supply_fan = ttk.Entry(self.lframe_fan, textvariable=self.power_AC_supply_fan_value, width=10)
                self.entry_power_plate_AC_supply_fan.grid(row=10, column=5, padx=(0, 100))

                #Voltage - AC_supply_fan


                self.lbl_voltage_plate_AC_supply_fan = ttk.Label(self.lframe_fan, text="napięcie zasilania [V]").grid(row=15, column=1, padx=1, pady=10)
                self.entry_voltage_plate_AC_supply_fan = ttk.Entry(self.lframe_fan, textvariable=self.voltage_AC_supply_fan_value, width=10)
                self.entry_voltage_plate_AC_supply_fan.grid(row=15, column=5, padx=(0, 100))

                # frequency- AC_supply_fan


                self.lbl_frequency_plate_AC_supply_fan = ttk.Label(self.lframe_fan, text="częstotliwość [Hz]").grid(row=20, column=1, padx=1, pady=10)
                self.entry_frequency_plate_AC_supply_fan = ttk.Entry(self.lframe_fan, textvariable=self.frequency_AC_supply_fan_value, width=10)
                self.entry_frequency_plate_AC_supply_fan.grid(row=20, column=5, padx=(0, 100))

                # quantity- AC_supply_fan


                self.lbl_quantity_AC_supply_fan = ttk.Label(self.lframe_fan, text="ilość").grid(row=25, column=1, padx=1, pady=10)
                self.entry_quantity_plate_AC_supply_fan = ttk.Entry(self.lframe_fan, textvariable=self.quantity_AC_supply_fan_value, width=10)
                self.entry_quantity_plate_AC_supply_fan.grid(row=25, column=5, padx=(0, 100))




                # AC exhaust

                self.symbol_AC_exhaust_fan_value.trace('w', self.validation_show_red)

                self.lbl_symbol_AC_exhaust_fan = ttk.Label(self.lframe_fan, text="wywiew-typ-AC").grid(row=5, column=10, padx=3, pady=10)
                self.entry_symbol_AC_exhaust_fan = ttk.Entry(self.lframe_fan, textvariable=self.symbol_AC_exhaust_fan_value, width=18,style="StyleACExhaust.TEntry")
                self.entry_symbol_AC_exhaust_fan.grid(row=5, column=15, padx=(0,50))

                # Power - AC_exhaust_fan

                self.lbl_power_plate_AC_exhaust_fan = ttk.Label(self.lframe_fan, text="moc [kW]").grid(row=10, column=10, padx=1, pady=10)
                self.entry_power_plate_AC_exhaust_fan = ttk.Entry(self.lframe_fan, textvariable=self.power_AC_exhaust_fan_value, width=10)
                self.entry_power_plate_AC_exhaust_fan.grid(row=10, column=15, padx=(0, 100))


                self.lbl_voltage_plate_AC_exhaust_fan = ttk.Label(self.lframe_fan, text="napięcie zasilania [V]").grid(row=15, column=10, padx=1, pady=10)
                self.entry_voltage_plate_AC_exhaust_fan = ttk.Entry(self.lframe_fan, textvariable=self.voltage_AC_exhaust_fan_value, width=10)
                self.entry_voltage_plate_AC_exhaust_fan.grid(row=15, column=15, padx=(0, 100))



                self.lbl_frequency_plate_AC_exhaust_fan = ttk.Label(self.lframe_fan, text="częstotliwość [Hz]").grid(row=20, column=10, padx=1, pady=10)
                self.entry_frequency_plate_AC_exhaust_fan = ttk.Entry(self.lframe_fan, textvariable=self.frequency_AC_exhaust_fan_value, width=10)
                self.entry_frequency_plate_AC_exhaust_fan.grid(row=20, column=15, padx=(0, 100))



                self.lbl_quantity_AC_exhaust_fan = ttk.Label(self.lframe_fan, text="ilość").grid(row=25, column=10, padx=1, pady=10)
                self.entry_quantity_plate_AC_exhaust_fan = ttk.Entry(self.lframe_fan, textvariable=self.quantity_AC_exhaust_fan_value, width=10)
                self.entry_quantity_plate_AC_exhaust_fan.grid(row=25, column=15, padx=(0, 100))




    def validation_show_red (self, *args):
        if len(self.symbol_EC_supply_fan_value.get())>self.numer_Characters_Enrty:
            self.style.configure(
                "StyleECSupply.TEntry",
                foreground = 'red',
            )
        else:
            self.style.configure(
                "StyleECSupply.TEntry",
                foreground='black',
            )


        if len(self.symbol_AC_supply_fan_value.get()) > self.numer_Characters_Enrty:
            self.style.configure(
                "StyleACSupply.TEntry",
                foreground='red',
            )
        else:
            self.style.configure(
                "StyleACSupply.TEntry",
                foreground='black',
            )
        if len(self.symbol_EC_exhaust_fan_value.get()) > self.numer_Characters_Enrty:
            self.style.configure(
                "StyleECExhaust.TEntry",
                foreground='red',
            )
        else:
            self.style.configure(
                "StyleECExhaust.TEntry",
                foreground='black',
            )

        if len(self.symbol_AC_exhaust_fan_value.get()) > self.numer_Characters_Enrty:
            self.style.configure(
                "StyleACExhaust.TEntry",
                foreground='red',
            )
        else:
            self.style.configure(
                "StyleACExhaust.TEntry",
                foreground='black',
            )





    def lackoff_fan_function(self) :
        try:
            self.lframe_fan.destroy()
        except:
            pass






    def example_fan_number(self):
        self.lframe_example_number = ttk.LabelFrame(tab4, text="nr")
        self.lframe_example_number.pack()

        self.example_fan_number_value.set(1)

        spinbox = Spinbox(self.lframe_example_number, from_=1, to=10, textvariable=self.example_fan_number_value, command = self.execution_fan_function)

        spinbox.pack(ipady = 4)



    def execution_fan_function(self):

       print(self.example_fan_number_value.get())
       if self.fan_choice_value.get() == 1 :
           self.EC_fan_function()
           if self.flow_type_choice_value.get() == 1:
                self.update_supply_fan_EC_value()
                self.update_exhaust_fan_EC_value()
           elif self.flow_type_choice_value.get() == 2:
               self.update_supply_fan_EC_value()
           elif self.flow_type_choice_value.get() == 3:
                self.update_exhaust_fan_EC_value()


       elif self.fan_choice_value.get() == 2 :
           self.AC_fan_function()
           if self.flow_type_choice_value.get() == 1:
                self.update_supply_fan_AC_value()
                self.update_exhaust_fan_AC_value()
           elif self.flow_type_choice_value.get() == 2:
                self.update_supply_fan_AC_value()
           elif self.flow_type_choice_value.get() == 3:
                self.update_exhaust_fan_AC_value()
       else:
           self.lackoff_fan_function()




####################################################################################################################################





###################################################################################################################################


    def supply_filter_choice(self):


        self.lfradio = ttk.LabelFrame(tab5)
        self.lfradio.pack( )
        self.supply_filter_choice_value = IntVar()
        self.supply_filter_choice_name_value = StringVar()
        self.symbol_supply_filter_value = ''

        self.G4_supply_filter = ttk.Radiobutton(self.lfradio, text = "G4", variable = self.supply_filter_choice_value, value = 1, command = self.G4_supply_filter_function)
        self.G4_supply_filter.grid(row =0, column = 0, padx=20, pady = 5)
        self.M5_supply_filter = ttk.Radiobutton(self.lfradio, text = "M5", variable = self.supply_filter_choice_value, value = 2, command = self.M5_supply_filter_function)
        self.M5_supply_filter.grid(row =0, column = 5, padx=20, pady = 5)
        self.F7_supply_filter = ttk.Radiobutton(self.lfradio, text = "F7", variable = self.supply_filter_choice_value, value = 3, command = self.F7_supply_filter_function)
        self.F7_supply_filter.grid(row =0, column = 10, padx=20, pady = 5)
        self.F9_supply_filter = ttk.Radiobutton(self.lfradio, text = "F9", variable = self.supply_filter_choice_value, value = 4, command = self.F9_supply_filter_function)
        self.F9_supply_filter.grid(row=0, column=15, padx=20, pady=5)
        self.lackoff_supply_filter_function = ttk.Radiobutton(self.lfradio, text="brak", variable = self.supply_filter_choice_value, value= 5, command = self.lackoff_supply_filter_function).grid (row = 0, column = 20, padx=20, pady = 5)



    def supply_type_filter_choice(self):

        self.lfradio = ttk.LabelFrame(tab5)
        self.lfradio.pack( )
        self.supply_type_filter_choice_value = IntVar()
        self.supply_filter_casette = ttk.Radiobutton(self.lfradio, text="działkowy", variable=self.supply_type_filter_choice_value, value=1, comman = self.supply_filter_plate_data)
        self.supply_filter_casette.grid(row=0,column=0,padx=20,pady=5)
        self.supply_filter_pocket = ttk.Radiobutton(self.lfradio, text="kieszeniowy", variable=self.supply_type_filter_choice_value, value=2,  comman = self.supply_filter_plate_data)
        self.supply_filter_pocket.grid(row=0, column=5, padx=20, pady=5)
        self.supply_filter_minipleat = ttk.Radiobutton(self.lfradio, text="minipleat", variable=self.supply_type_filter_choice_value, value=3, comman=self.supply_filter_plate_data)
        self.supply_filter_minipleat.grid(row=0, column=10, padx=20, pady=5)

    def G4_supply_filter_function(self):

        try:
            self.lframe.destroy()

        except:
            pass
        finally:

            # supply filter G4  symbol
            self.lframe = ttk.LabelFrame(tab5)
            self.lframe.pack(anchor=W)
            self.lframe.pack(anchor=W, padx=15)
            self.symbol_G4_supply_filter_value = StringVar()
            self.lbl_symbol_G4_supply_filter = ttk.Label(self.lframe, text="nawiew - wymiar filtru G4").grid(row=5, column=1, padx=3, pady=10)
            self.entry_symbol_G4_supply_filter = ttk.Entry(self.lframe, textvariable=self.symbol_G4_supply_filter_value, width=30)
            self.entry_symbol_G4_supply_filter.insert(END, symbol_G4_supply_filter_value[str(self.symbol_ahu_range.get()) + '_' + str(self.supply_type_filter_choice_value.get())])
            self.entry_symbol_G4_supply_filter.grid(row=10, column=1, padx=1)
            self.supply_filter_choice_name_value.set('G4')
            self.symbol_supply_filter_value = self.symbol_G4_supply_filter_value




            #  supply filter G4 quantity
            self.quantity_G4_supply_filter_value = StringVar()
            self.lbl_quantity_G4_supply_filter = ttk.Label(self.lframe, text="ilość").grid(row=5, column=5, padx=3, pady=10)
            self.entry_quantity_G4_supply_filter = ttk.Entry(self.lframe, textvariable=self.quantity_G4_supply_filter_value, width=10)

            self.entry_quantity_G4_supply_filter.insert(END, quantity_G4_supply_filter_value )
            self.entry_quantity_G4_supply_filter.grid(row=10, column=5, padx=1)
            self.quantity_supply_filter_value = self.quantity_G4_supply_filter_value




            #   explanation
            self.lbl = ttk.Label(self.lframe, text="[szer. x wys. x gł.]").grid(row=15, column=1, padx=3, pady=10)
            self.lbl = ttk.Label(self.lframe, text="[sztuk]").grid(row=15, column=5, padx=3, pady=10)




            self.supply_filter_casette.configure(state=DISABLED)
            self.supply_filter_pocket.configure(state=DISABLED)
            self.supply_filter_minipleat.configure(state=DISABLED)

            if self.supply_type_filter_choice_value.get() == 1 or  self.supply_type_filter_choice_value.get() == 2 :
                self.supply_filter_plate_data()


    def M5_supply_filter_function(self):
        try:
            self.lframe.destroy()
        except:
            pass
        finally:

            # supply filter M5  symbol
            self.lframe = ttk.LabelFrame(tab5)
            self.lframe.pack(anchor=W)
            self.lframe.pack(anchor=W, padx=15)
            self.symbol_M5_supply_filter_value = StringVar()
            self.lbl_symbol_M5_supply_filter = ttk.Label(self.lframe, text="nawiew - wymiar filtru M5").grid(row=5, column=1, padx=3, pady=10)
            self.entry_symbol_M5_supply_filter = ttk.Entry(self.lframe, textvariable=self.symbol_M5_supply_filter_value, width=30)
            self.entry_symbol_M5_supply_filter.insert(END, symbol_M5_supply_filter_value[str(self.symbol_ahu_range.get()) + '_' + str(self.supply_type_filter_choice_value.get())])
            self.entry_symbol_M5_supply_filter.grid(row=10, column=1, padx=1)
            self.supply_filter_choice_name_value.set('M5')
            self.symbol_supply_filter_value = self.symbol_M5_supply_filter_value


            #  supply filter M5 quantity
            self.quantity_M5_supply_filter_value = StringVar()
            self.lbl_quantity_M5_supply_filter = ttk.Label(self.lframe, text="ilość").grid(row=5, column=5, padx=3, pady=10)
            self.entry_quantity_M5_supply_filter = ttk.Entry(self.lframe, textvariable=self.quantity_M5_supply_filter_value, width=10)
            self.entry_quantity_M5_supply_filter.insert(END, quantity_M5_supply_filter_value )
            self.entry_quantity_M5_supply_filter.grid(row=10, column=5, padx=1)
            self.quantity_supply_filter_value = self.quantity_M5_supply_filter_value


            #   explanation
            self.lbl = ttk.Label(self.lframe, text="[szer. x wys. x gł.]").grid(row=15, column=1, padx=3, pady=10)
            self.lbl = ttk.Label(self.lframe, text="[sztuk]").grid(row=15, column=5, padx=3, pady=10)


            self.supply_filter_casette.configure(state=DISABLED)
            self.supply_filter_pocket.configure(state=DISABLED)
            self.supply_filter_minipleat.configure(state=DISABLED)

            if self.supply_type_filter_choice_value.get() == 1 or  self.supply_type_filter_choice_value.get() == 2 :
                self.supply_filter_plate_data()


    def F7_supply_filter_function(self):
        try:
            self.lframe.destroy()
        except:
            pass
        finally:

            # supply filter F7  symbol
            self.lframe = ttk.LabelFrame(tab5)
            self.lframe.pack(anchor=W)
            self.lframe.pack(anchor=W, padx=15)
            self.symbol_F7_supply_filter_value = StringVar()
            self.lbl_symbol_F7_supply_filter = ttk.Label(self.lframe, text="nawiew - wymiar filtru F7").grid(row=5, column=1, padx=3, pady=10)
            self.entry_symbol_F7_supply_filter = ttk.Entry(self.lframe, textvariable=self.symbol_F7_supply_filter_value, width=30)
            self.entry_symbol_F7_supply_filter.insert(END, symbol_F7_supply_filter_value[str(self.symbol_ahu_range.get()) + '_' + str(self.supply_type_filter_choice_value.get())])
            self.entry_symbol_F7_supply_filter.grid(row=10, column=1, padx=1)
            self.supply_filter_choice_name_value.set('F7')
            self.symbol_supply_filter_value = self.symbol_F7_supply_filter_value


            #  supply filter F7 quantity
            self.quantity_F7_supply_filter_value = StringVar()
            self.lbl_quantity_F7_supply_filter = ttk.Label(self.lframe, text="ilość").grid(row=5, column=5, padx=3, pady=10)
            self.entry_quantity_F7_supply_filter = ttk.Entry(self.lframe, textvariable=self.quantity_F7_supply_filter_value, width=10)
            self.entry_quantity_F7_supply_filter.insert(END, quantity_F7_supply_filter_value)
            self.entry_quantity_F7_supply_filter.grid(row=10, column=5, padx=1)
            self.quantity_supply_filter_value = self.quantity_F7_supply_filter_value



            #   explanation
            self.lbl = ttk.Label(self.lframe, text="[szer. x wys. x gł.]").grid(row=15, column=1, padx=3, pady=10)
            self.lbl = ttk.Label(self.lframe, text="[sztuk]").grid(row=15, column=5, padx=3, pady=10)



            self.supply_filter_casette.configure(state=DISABLED)
            self.supply_filter_pocket.configure(state=DISABLED)
            self.supply_filter_minipleat.configure(state=DISABLED)


            if self.supply_type_filter_choice_value.get() == 3 or  self.supply_type_filter_choice_value.get() == 2 :
                self.supply_filter_plate_data()

    def F9_supply_filter_function(self):
        try:
            self.lframe.destroy()
        except:
            pass
        finally:

            # supply filter F9  symbol
            self.lframe = ttk.LabelFrame(tab5)
            self.lframe.pack(anchor=W)
            self.lframe.pack(anchor=W, padx=15)

            self.symbol_F9_supply_filter_value = StringVar()
            self.lbl_symbol_F9_supply_filter = ttk.Label(self.lframe, text="nawiew - wymiar filtru F9").grid(row=5, column=1, padx=3, pady=10)
            self.entry_symbol_F9_supply_filter = ttk.Entry(self.lframe, textvariable=self.symbol_F9_supply_filter_value, width=30)
            self.entry_symbol_F9_supply_filter.insert(END, symbol_F9_supply_filter_value[str(self.symbol_ahu_range.get()) + '_' + str(self.supply_type_filter_choice_value.get())])
            self.entry_symbol_F9_supply_filter.grid(row=10, column=1, padx=1)
            self.supply_filter_choice_name_value.set('F9')


            #  supply filter F9 quantity
            self.quantity_F9_supply_filter_value = StringVar()
            self.lbl_quantity_F9_supply_filter = ttk.Label(self.lframe, text="ilość").grid(row=5, column=5, padx=3, pady=10)
            self.entry_quantity_F9_supply_filter = ttk.Entry(self.lframe, textvariable=self.quantity_F9_supply_filter_value, width=10)
            self.entry_quantity_F9_supply_filter.insert(END, quantity_F9_supply_filter_value )
            self.entry_quantity_F9_supply_filter.grid(row=10, column=5, padx=1)
            self.symbol_supply_filter_value = self.symbol_F9_supply_filter_value
            self.quantity_supply_filter_value = self.quantity_F9_supply_filter_value


            #   explanation
            self.lbl = ttk.Label(self.lframe, text="[szer. x wys. x gł.]").grid(row=15, column=1, padx=3, pady=10)
            self.lbl = ttk.Label(self.lframe, text="[sztuk]").grid(row=15, column=5, padx=3, pady=10)

            self.supply_filter_casette.configure(state=DISABLED)
            self.supply_filter_pocket.configure(state=DISABLED)
            self.supply_filter_minipleat.configure(state=DISABLED)


            if self.supply_type_filter_choice_value.get() == 3 or  self.supply_type_filter_choice_value.get() == 2 :
                self.supply_filter_plate_data()

    def lackoff_supply_filter_function(self) :
        try:
            self.lframe.destroy()

        except:
            pass
        try:
            self.supply_filter_casette.configure(state=ACTIVE)
            self.supply_filter_pocket.configure(state=ACTIVE)
            self.supply_filter_minipleat.configure(state=ACTIVE)
        except:
            pass


####

    def supply_filter_plate_data(self) :

        supply_filter_class = self.supply_filter_choice_name_value.get()


        self.entry_supply_filter_plate_type_value = StringVar()



        self.entry_supply_filter_plate_type = ttk.Entry(self.lframe, width=30, textvariable=self.entry_supply_filter_plate_type_value )
        self.supply_filter_type = entry_supply_filter_plate_type_value[str(self.symbol_ahu_range.get() + '_' +  str(self.supply_type_filter_choice_value.get()))] + ' ' + supply_filter_class
        self.entry_supply_filter_plate_type.insert(END, self.supply_filter_type )
        self.entry_supply_filter_plate_type.grid(row=20, column=1, padx=10)
        self.lbl = ttk.Label(self.lframe, text="Typ").grid(row=20, column=5, padx=10, pady=10)

        #  filter_class

        self.entry_supply_filter_plate_filter_class_value = StringVar()
        self.entry_supply_filter_plate_filter_class = ttk.Entry(self.lframe, width=30, textvariable=self.entry_supply_filter_plate_filter_class_value)
        self.entry_supply_filter_plate_filter_class.insert(END, supply_filter_class + ' / ' + entry_supply_filter_plate_filter_class_value[str(supply_filter_class + '_' + str(self.supply_type_filter_choice_value.get()))])
        self.entry_supply_filter_plate_filter_class.grid(row=35, column=1, padx=10)
        self.lbl = ttk.Label(self.lframe, text="klasa filtra").grid(row=35, column=5, padx=10, pady=10)

        #  Kind of filter

        self.entry_supply_filter_plate_kind_value = StringVar()
        self.entry_supply_filter_plate_kind = ttk.Entry(self.lframe, width=30, textvariable=self.entry_supply_filter_plate_kind_value )
        self.entry_supply_filter_plate_kind.insert(END, entry_supply_filter_plate_kind_value[str(self.symbol_ahu_range.get() + '_' +  str(self.supply_type_filter_choice_value.get()))])
        if self.accept_english_switch.get() :
            self.entry_supply_filter_plate_kind.delete(0, 'end')
            self.entry_supply_filter_plate_kind.insert(END, entry_supply_filter_plate_kind_value_EN[str(self.symbol_ahu_range.get() + '_' + str(self.supply_type_filter_choice_value.get()))])

        self.entry_supply_filter_plate_kind.grid(row=25, column=1, padx=10)
        self.lbl = ttk.Label(self.lframe, text="Rodzaj").grid(row=25, column=5, padx=10, pady=10)




        #  initial pressure drop

        self.entry_supply_filter_plate_initial_pressure_drop_value = StringVar()


        self.entry_supply_filter_plate_initial_pressure_drop = ttk.Entry(self.lframe, width=30, textvariable=self.entry_supply_filter_plate_initial_pressure_drop_value)
        self.entry_supply_filter_plate_initial_pressure_drop.grid(row=40, column=1, padx=10)
        self.lbl = ttk.Label(self.lframe, text="Opór początkowy").grid(row=40, column=5, padx=10, pady=10)

        #  Recomended_final_pressure_drop

        self.entry_supply_filter_plate_recom_final_pressure_drop_value = StringVar()

        self.entry_supply_filter_plate_recom_final_pressure_drop = ttk.Entry(self.lframe, width=30, textvariable=self.entry_supply_filter_plate_recom_final_pressure_drop_value)
        self.entry_supply_filter_plate_recom_final_pressure_drop.grid(row=45, column=1, padx=10)
        self.lbl = ttk.Label(self.lframe, text="Zal. opór końcowy ").grid(row=45, column=5, padx=10, pady=10)







#############################################################################################################################################

        ###################################################################################################################################
        ###################################################################################################################################

    def supply_filter_02_choice(self):

        self.lfradio = ttk.LabelFrame(tab12)
        self.lfradio.pack()
        self.supply_filter_02_choice_value = IntVar()
        self.supply_filter_02_choice_name_value = StringVar()
        self.symbol_supply_filter_02_value = ''

        self.G4_supply_filter_02 = ttk.Radiobutton(self.lfradio, text="G4", variable=self.supply_filter_02_choice_value, value=1, command=self.G4_supply_filter_02_function)
        self.G4_supply_filter_02.grid(row=0, column=0, padx=20, pady=5)
        self.M5_supply_filter_02 = ttk.Radiobutton(self.lfradio, text="M5", variable=self.supply_filter_02_choice_value, value=2, command=self.M5_supply_filter_02_function)
        self.M5_supply_filter_02.grid(row=0, column=5, padx=20, pady=5)
        self.F7_supply_filter_02 = ttk.Radiobutton(self.lfradio, text="F7", variable=self.supply_filter_02_choice_value, value=3, command=self.F7_supply_filter_02_function)
        self.F7_supply_filter_02.grid(row=0, column=10, padx=20, pady=5)
        self.F9_supply_filter_02 = ttk.Radiobutton(self.lfradio, text="F9", variable=self.supply_filter_02_choice_value, value=4, command=self.F9_supply_filter_02_function)
        self.F9_supply_filter_02.grid(row=0, column=15, padx=20, pady=5)
        self.lackoff_supply_filter_02_function = ttk.Radiobutton(self.lfradio, text="brak", variable=self.supply_filter_02_choice_value, value=5, command=self.lackoff_supply_filter_02_function).grid(row=0, column=20, padx=20, pady=5)

    def supply_type_filter_02_choice(self):

        self.lfradio = ttk.LabelFrame(tab12)
        self.lfradio.pack()
        self.supply_type_filter_02_choice_value = IntVar()
        self.supply_filter_02_casette = ttk.Radiobutton(self.lfradio, text="działkowy", variable=self.supply_type_filter_02_choice_value, value=1, comman=self.supply_filter_02_plate_data)
        self.supply_filter_02_casette.grid(row=0, column=0, padx=20, pady=5)
        self.supply_filter_02_pocket = ttk.Radiobutton(self.lfradio, text="kieszeniowy", variable=self.supply_type_filter_02_choice_value, value=2, comman=self.supply_filter_02_plate_data)
        self.supply_filter_02_pocket.grid(row=0, column=5, padx=20, pady=5)
        self.supply_filter_02_minipleat = ttk.Radiobutton(self.lfradio, text="minipleat", variable=self.supply_type_filter_02_choice_value, value=3, comman=self.supply_filter_02_plate_data)
        self.supply_filter_02_minipleat.grid(row=0, column=10, padx=20, pady=5)

    def G4_supply_filter_02_function(self):

        try:
            self.lframe.destroy()

        except:
            pass
        finally:

            # supply filter_02 G4  symbol
            self.lframe = ttk.LabelFrame(tab12)
            self.lframe.pack(anchor=W)
            self.lframe.pack(anchor=W, padx=15)
            self.symbol_G4_supply_filter_02_value = StringVar()
            self.lbl_symbol_G4_supply_filter_02 = ttk.Label(self.lframe, text="nawiew - wymiar filtru G4").grid(row=5, column=1, padx=3, pady=10)
            self.entry_symbol_G4_supply_filter_02 = ttk.Entry(self.lframe, textvariable=self.symbol_G4_supply_filter_02_value, width=30)
            self.entry_symbol_G4_supply_filter_02.insert(END, symbol_G4_supply_filter_value[str(self.symbol_ahu_range.get()) + '_' + str(self.supply_type_filter_02_choice_value.get())])
            self.entry_symbol_G4_supply_filter_02.grid(row=10, column=1, padx=1)
            self.supply_filter_02_choice_name_value.set('G4')
            self.symbol_supply_filter_02_value = self.symbol_G4_supply_filter_02_value

            #  supply filter_02 G4 quantity
            self.quantity_G4_supply_filter_02_value = StringVar()
            self.lbl_quantity_G4_supply_filter_02 = ttk.Label(self.lframe, text="ilość").grid(row=5, column=5, padx=3, pady=10)
            self.entry_quantity_G4_supply_filter_02 = ttk.Entry(self.lframe, textvariable=self.quantity_G4_supply_filter_02_value, width=10)

            self.entry_quantity_G4_supply_filter_02.insert(END, quantity_G4_supply_filter_value)
            self.entry_quantity_G4_supply_filter_02.grid(row=10, column=5, padx=1)
            self.quantity_supply_filter_02_value = self.quantity_G4_supply_filter_02_value

            #   explanation
            self.lbl = ttk.Label(self.lframe, text="[szer. x wys. x gł.]").grid(row=15, column=1, padx=3, pady=10)
            self.lbl = ttk.Label(self.lframe, text="[sztuk]").grid(row=15, column=5, padx=3, pady=10)

            self.supply_filter_02_casette.configure(state=DISABLED)
            self.supply_filter_02_pocket.configure(state=DISABLED)
            self.supply_filter_02_minipleat.configure(state=DISABLED)

            if self.supply_type_filter_02_choice_value.get() == 1 or self.supply_type_filter_02_choice_value.get() == 2:
                self.supply_filter_02_plate_data()

    def M5_supply_filter_02_function(self):
        try:
            self.lframe.destroy()
        except:
            pass
        finally:

            # supply filter_02 M5  symbol
            self.lframe = ttk.LabelFrame(tab12)
            self.lframe.pack(anchor=W)
            self.lframe.pack(anchor=W, padx=15)
            self.symbol_M5_supply_filter_02_value = StringVar()
            self.lbl_symbol_M5_supply_filter_02 = ttk.Label(self.lframe, text="nawiew - wymiar filtru M5").grid(row=5, column=1, padx=3, pady=10)
            self.entry_symbol_M5_supply_filter_02 = ttk.Entry(self.lframe, textvariable=self.symbol_M5_supply_filter_02_value, width=30)
            self.entry_symbol_M5_supply_filter_02.insert(END, symbol_M5_supply_filter_value[str(self.symbol_ahu_range.get()) + '_' + str(self.supply_type_filter_02_choice_value.get())])
            self.entry_symbol_M5_supply_filter_02.grid(row=10, column=1, padx=1)
            self.supply_filter_02_choice_name_value.set('M5')
            self.symbol_supply_filter_02_value = self.symbol_M5_supply_filter_02_value

            #  supply filter_02 M5 quantity
            self.quantity_M5_supply_filter_02_value = StringVar()
            self.lbl_quantity_M5_supply_filter_02 = ttk.Label(self.lframe, text="ilość").grid(row=5, column=5, padx=3, pady=10)
            self.entry_quantity_M5_supply_filter_02 = ttk.Entry(self.lframe, textvariable=self.quantity_M5_supply_filter_02_value, width=10)
            self.entry_quantity_M5_supply_filter_02.insert(END, quantity_M5_supply_filter_value)
            self.entry_quantity_M5_supply_filter_02.grid(row=10, column=5, padx=1)
            self.quantity_supply_filter_02_value = self.quantity_M5_supply_filter_02_value

            #   explanation
            self.lbl = ttk.Label(self.lframe, text="[szer. x wys. x gł.]").grid(row=15, column=1, padx=3, pady=10)
            self.lbl = ttk.Label(self.lframe, text="[sztuk]").grid(row=15, column=5, padx=3, pady=10)

            self.supply_filter_02_casette.configure(state=DISABLED)
            self.supply_filter_02_pocket.configure(state=DISABLED)
            self.supply_filter_02_minipleat.configure(state=DISABLED)

            if self.supply_type_filter_02_choice_value.get() == 1 or self.supply_type_filter_02_choice_value.get() == 2:
                self.supply_filter_02_plate_data()

    def F7_supply_filter_02_function(self):
        try:
            self.lframe.destroy()
        except:
            pass
        finally:

            # supply filter_02 F7  symbol
            self.lframe = ttk.LabelFrame(tab12)
            self.lframe.pack(anchor=W)
            self.lframe.pack(anchor=W, padx=15)
            self.symbol_F7_supply_filter_02_value = StringVar()
            self.lbl_symbol_F7_supply_filter_02 = ttk.Label(self.lframe, text="nawiew - wymiar filtru F7").grid(row=5, column=1, padx=3, pady=10)
            self.entry_symbol_F7_supply_filter_02 = ttk.Entry(self.lframe, textvariable=self.symbol_F7_supply_filter_02_value, width=30)
            self.entry_symbol_F7_supply_filter_02.insert(END, symbol_F7_supply_filter_value[str(self.symbol_ahu_range.get()) + '_' + str(self.supply_type_filter_02_choice_value.get())])
            self.entry_symbol_F7_supply_filter_02.grid(row=10, column=1, padx=1)
            self.supply_filter_02_choice_name_value.set('F7')
            self.symbol_supply_filter_02_value = self.symbol_F7_supply_filter_02_value

            #  supply filter_02 F7 quantity
            self.quantity_F7_supply_filter_02_value = StringVar()
            self.lbl_quantity_F7_supply_filter_02 = ttk.Label(self.lframe, text="ilość").grid(row=5, column=5, padx=3, pady=10)
            self.entry_quantity_F7_supply_filter_02 = ttk.Entry(self.lframe, textvariable=self.quantity_F7_supply_filter_02_value, width=10)
            self.entry_quantity_F7_supply_filter_02.insert(END, quantity_F7_supply_filter_value)
            self.entry_quantity_F7_supply_filter_02.grid(row=10, column=5, padx=1)
            self.quantity_supply_filter_02_value = self.quantity_F7_supply_filter_02_value

            #   explanation
            self.lbl = ttk.Label(self.lframe, text="[szer. x wys. x gł.]").grid(row=15, column=1, padx=3, pady=10)
            self.lbl = ttk.Label(self.lframe, text="[sztuk]").grid(row=15, column=5, padx=3, pady=10)

            self.supply_filter_02_casette.configure(state=DISABLED)
            self.supply_filter_02_pocket.configure(state=DISABLED)
            self.supply_filter_02_minipleat.configure(state=DISABLED)

            if self.supply_type_filter_02_choice_value.get() == 3 or self.supply_type_filter_02_choice_value.get() == 2:
                self.supply_filter_02_plate_data()

    def F9_supply_filter_02_function(self):
        try:
            self.lframe.destroy()
        except:
            pass
        finally:

            # supply filter_02 F9  symbol
            self.lframe = ttk.LabelFrame(tab12)
            self.lframe.pack(anchor=W)
            self.lframe.pack(anchor=W, padx=15)

            self.symbol_F9_supply_filter_02_value = StringVar()
            self.lbl_symbol_F9_supply_filter_02 = ttk.Label(self.lframe, text="nawiew - wymiar filtru F9").grid(row=5, column=1, padx=3, pady=10)
            self.entry_symbol_F9_supply_filter_02 = ttk.Entry(self.lframe, textvariable=self.symbol_F9_supply_filter_02_value, width=30)
            self.entry_symbol_F9_supply_filter_02.insert(END, symbol_F9_supply_filter_value[str(self.symbol_ahu_range.get()) + '_' + str(self.supply_type_filter_02_choice_value.get())])
            self.entry_symbol_F9_supply_filter_02.grid(row=10, column=1, padx=1)
            self.supply_filter_02_choice_name_value.set('F9')

            #  supply filter_02 F9 quantity
            self.quantity_F9_supply_filter_02_value = StringVar()
            self.lbl_quantity_F9_supply_filter_02 = ttk.Label(self.lframe, text="ilość").grid(row=5, column=5, padx=3, pady=10)
            self.entry_quantity_F9_supply_filter_02 = ttk.Entry(self.lframe, textvariable=self.quantity_F9_supply_filter_02_value, width=10)
            self.entry_quantity_F9_supply_filter_02.insert(END, quantity_F9_supply_filter_value)
            self.entry_quantity_F9_supply_filter_02.grid(row=10, column=5, padx=1)
            self.symbol_supply_filter_02_value = self.symbol_F9_supply_filter_02_value
            self.quantity_supply_filter_02_value = self.quantity_F9_supply_filter_02_value

            #   explanation
            self.lbl = ttk.Label(self.lframe, text="[szer. x wys. x gł.]").grid(row=15, column=1, padx=3, pady=10)
            self.lbl = ttk.Label(self.lframe, text="[sztuk]").grid(row=15, column=5, padx=3, pady=10)

            self.supply_filter_02_casette.configure(state=DISABLED)
            self.supply_filter_02_pocket.configure(state=DISABLED)
            self.supply_filter_02_minipleat.configure(state=DISABLED)

            if self.supply_type_filter_02_choice_value.get() == 3 or self.supply_type_filter_02_choice_value.get() == 2:
                self.supply_filter_02_plate_data()

    def lackoff_supply_filter_02_function(self):
        try:
            self.lframe.destroy()

        except:
            pass
        try:
            self.supply_filter_02_casette.configure(state=ACTIVE)
            self.supply_filter_02_pocket.configure(state=ACTIVE)
            self.supply_filter_02_minipleat.configure(state=ACTIVE)
        except:
            pass

    ####

    def supply_filter_02_plate_data(self):

        supply_filter_02_class = self.supply_filter_02_choice_name_value.get()

        self.entry_supply_filter_02_plate_type_value = StringVar()

        self.entry_supply_filter_02_plate_type = ttk.Entry(self.lframe, width=30, textvariable=self.entry_supply_filter_02_plate_type_value)
        self.supply_filter_02_type = entry_supply_filter_plate_type_value[str(self.symbol_ahu_range.get() + '_' + str(self.supply_type_filter_02_choice_value.get()))] + ' ' + supply_filter_02_class
        self.entry_supply_filter_02_plate_type.insert(END, self.supply_filter_02_type)
        self.entry_supply_filter_02_plate_type.grid(row=20, column=1, padx=10)
        self.lbl = ttk.Label(self.lframe, text="Typ").grid(row=20, column=5, padx=10, pady=10)

        #  filter_02_class

        self.entry_supply_filter_02_plate_filter_02_class_value = StringVar()
        self.entry_supply_filter_02_plate_filter_02_class = ttk.Entry(self.lframe, width=30, textvariable=self.entry_supply_filter_02_plate_filter_02_class_value)
        self.entry_supply_filter_02_plate_filter_02_class.insert(END, supply_filter_02_class + ' / ' + entry_supply_filter_plate_filter_class_value[str(supply_filter_02_class) + '_' + str(self.supply_type_filter_02_choice_value.get())])
        self.entry_supply_filter_02_plate_filter_02_class.grid(row=35, column=1, padx=10)
        self.lbl = ttk.Label(self.lframe, text="klasa filtra").grid(row=35, column=5, padx=10, pady=10)

        #  Kind of filter_02

        self.entry_supply_filter_02_plate_kind_value = StringVar()
        self.entry_supply_filter_02_plate_kind = ttk.Entry(self.lframe, width=30, textvariable=self.entry_supply_filter_02_plate_kind_value)
        self.entry_supply_filter_02_plate_kind.insert(END, entry_supply_filter_plate_kind_value[str(self.symbol_ahu_range.get() + '_' + str(self.supply_type_filter_02_choice_value.get()))])
        if self.accept_english_switch.get():
            self.entry_supply_filter_02_plate_kind.delete(0, 'end')
            self.entry_supply_filter_02_plate_kind.insert(END, entry_supply_filter_plate_kind_value_EN[str(self.symbol_ahu_range.get() + '_' + str(self.supply_type_filter_02_choice_value.get()))])

        self.entry_supply_filter_02_plate_kind.grid(row=25, column=1, padx=10)
        self.lbl = ttk.Label(self.lframe, text="Rodzaj").grid(row=25, column=5, padx=10, pady=10)

        #  initial pressure drop

        self.entry_supply_filter_02_plate_initial_pressure_drop_value = StringVar()

        self.entry_supply_filter_02_plate_initial_pressure_drop = ttk.Entry(self.lframe, width=30, textvariable=self.entry_supply_filter_02_plate_initial_pressure_drop_value)
        self.entry_supply_filter_02_plate_initial_pressure_drop.grid(row=40, column=1, padx=10)
        self.lbl = ttk.Label(self.lframe, text="Opór początkowy").grid(row=40, column=5, padx=10, pady=10)

        #  Recomended_final_pressure_drop

        self.entry_supply_filter_02_plate_recom_final_pressure_drop_value = StringVar()

        self.entry_supply_filter_02_plate_recom_final_pressure_drop = ttk.Entry(self.lframe, width=30, textvariable=self.entry_supply_filter_02_plate_recom_final_pressure_drop_value)
        self.entry_supply_filter_02_plate_recom_final_pressure_drop.grid(row=45, column=1, padx=10)
        self.lbl = ttk.Label(self.lframe, text="Zal. opór końcowy ").grid(row=45, column=5, padx=10, pady=10)

    ##############################################################################################################################################



    def exhaust_filter_choice(self):
        self.lfradio = ttk.LabelFrame(tab6)
        self.lfradio.pack( )
        self.exhaust_filter_choice_name_value = StringVar()
        self.exhaust_filter_choice_value = IntVar()
        self.symbol_exhaust_filter_value = ''

        self.G4_filter = ttk.Radiobutton(self.lfradio, text = "G4", variable = self.exhaust_filter_choice_value, value = 1, command = self.G4_exhaust_filter_function)
        self.G4_filter.grid(row=0, column=0, padx=20, pady=5)
        self.M5_filter = ttk.Radiobutton(self.lfradio, text = "M5", variable = self.exhaust_filter_choice_value, value = 2, command = self.M5_exhaust_filter_function)
        self.M5_filter.grid(row=0, column=5, padx=20, pady=5)
        self.F7_filter = ttk.Radiobutton(self.lfradio, text = "F7", variable = self.exhaust_filter_choice_value, value = 3, command = self.F7_exhaust_filter_function)
        self.F7_filter.grid(row =0, column = 10, padx=20, pady = 5)
        self.F9_filter = ttk.Radiobutton(self.lfradio, text = "F9", variable = self.exhaust_filter_choice_value, value = 4, command = self.F9_exhaust_filter_function)
        self.F9_filter.grid(row =0, column = 15, padx=20, pady = 5)
        self.lackoff_exhaust_fan = ttk.Radiobutton(self.lfradio, text="brak", variable = self.exhaust_filter_choice_value, value= 5, command = self.lackoff_exhaust_filter_function).grid (row = 0, column = 20, padx=20, pady = 5)

    def exhaust_type_filter_choice(self):



        self.lfradio = ttk.LabelFrame(tab6)
        self.lfradio.pack()
        self.exhaust_type_filter_choice_value = IntVar()
        self.exhaust_filter_casette = ttk.Radiobutton(self.lfradio, text="działkowy", variable=self.exhaust_type_filter_choice_value, value=1, comman=self.exhaust_filter_plate_data)
        self.exhaust_filter_casette.grid(row=0, column=0, padx=20, pady=5)
        self.exhaust_filter_packet = ttk.Radiobutton(self.lfradio, text="kieszeniowy", variable=self.exhaust_type_filter_choice_value, value=2, comman=self.exhaust_filter_plate_data)
        self.exhaust_filter_packet.grid(row=0, column=5, padx=20, pady=5)
        self.exhaust_filter_minipleat = ttk.Radiobutton(self.lfradio, text="minipleat", variable=self.exhaust_type_filter_choice_value, value=3, comman=self.exhaust_filter_plate_data)
        self.exhaust_filter_minipleat.grid(row=0, column=15, padx=20, pady=5)


    def G4_exhaust_filter_function(self):
        try:
            self.lframe.destroy()
        except:
            pass
        finally:

            # exhaust filter G4  symbol
            self.lframe = ttk.LabelFrame(tab6)
            self.lframe.pack(anchor=W)
            self.lframe.pack(anchor=W, padx=15)
            self.symbol_G4_exhaust_filter_value = StringVar()
            self.lbl_symbol_G4_exhaust_filter = ttk.Label(self.lframe, text="wywiew - wymiar filtru G4").grid(row=5, column=1, padx=3, pady=10)
            self.entry_symbol_G4_exhaust_filter = ttk.Entry(self.lframe, textvariable=self.symbol_G4_exhaust_filter_value, width=30)
            self.entry_symbol_G4_exhaust_filter.insert(END, symbol_G4_exhaust_filter_value[str(self.symbol_ahu_range.get() + '_' + str(self.exhaust_type_filter_choice_value.get()))])
            self.entry_symbol_G4_exhaust_filter .grid(row=10, column=1, padx=1)
            self.exhaust_filter_choice_name_value.set('G4')
            self.symbol_exhaust_filter_value = self.symbol_G4_exhaust_filter_value




            #  exhaust filter G4 quantity
            self.quantity_G4_exhaust_filter_value = StringVar()
            self.lbl_quantity_G4_exhaust_filter = ttk.Label(self.lframe, text="ilość").grid(row=5, column=5, padx=3, pady=10)
            self.entry_quantity_G4_exhaust_filter = ttk.Entry(self.lframe, textvariable=self.quantity_G4_exhaust_filter_value, width=10)
            self.entry_quantity_G4_exhaust_filter.insert(END, quantity_G4_exhaust_filter_value)
            self.entry_quantity_G4_exhaust_filter.grid(row=10, column=5, padx=1)
            self.quantity_exhaust_filter_value = self.quantity_G4_exhaust_filter_value


            #   explanation
            self.lbl = ttk.Label(self.lframe, text="[szer. x wys. x gł.]").grid(row=15, column=1, padx=3, pady=10)
            self.lbl = ttk.Label(self.lframe, text="[sztuk]").grid(row=15, column=5, padx=3, pady=10)



            self.exhaust_filter_casette.configure(state=DISABLED)
            self.exhaust_filter_packet.configure(state=DISABLED)
            self.exhaust_filter_minipleat.configure(state=DISABLED)

            if self.exhaust_type_filter_choice_value.get() == 1 or  self.exhaust_type_filter_choice_value.get() == 2 :
                self.exhaust_filter_plate_data()




    def M5_exhaust_filter_function(self):
        try:
            self.lframe.destroy()
        except:
            pass
        finally:

            # exhaust filter M5  symbol
            self.lframe = ttk.LabelFrame(tab6)
            self.lframe.pack(anchor=W)
            self.lframe.pack(anchor=W, padx=15)
            self.symbol_M5_exhaust_filter_value = StringVar()
            self.lbl_symbol_M5_exhaust_filter = ttk.Label(self.lframe, text="wywiew - wymiar filtru M5").grid(row=5, column=1, padx=3, pady=10)
            self.entry_symbol_M5_exhaust_filter = ttk.Entry(self.lframe, textvariable=self.symbol_M5_exhaust_filter_value, width=30)
            self.entry_symbol_M5_exhaust_filter.insert(END, symbol_M5_exhaust_filter_value[str(self.symbol_ahu_range.get()+ '_' + str(self.exhaust_type_filter_choice_value.get()))])
            self.entry_symbol_M5_exhaust_filter.grid(row=10, column=1, padx=1)
            self.exhaust_filter_choice_name_value.set('M5')
            self.symbol_exhaust_filter_value = self.symbol_M5_exhaust_filter_value




            #  exhaust filter M5 quantity
            self.quantity_M5_exhaust_filter_value = StringVar()
            self.lbl_quantity_M5_exhaust_filter = ttk.Label(self.lframe, text="ilość").grid(row=5, column=5, padx=3, pady=10)
            self.entry_quantity_M5_exhaust_filter = ttk.Entry(self.lframe, textvariable=self.quantity_M5_exhaust_filter_value, width=10)
            self.entry_quantity_M5_exhaust_filter.insert(END, quantity_M5_exhaust_filter_value )
            self.entry_quantity_M5_exhaust_filter.grid(row=10, column=5, padx=1)
            self.quantity_exhaust_filter_value = self.quantity_M5_exhaust_filter_value



            #   explanation
            self.lbl = ttk.Label(self.lframe, text="[szer. x wys. x gł.]").grid(row=15, column=1, padx=3, pady=10)
            self.lbl = ttk.Label(self.lframe, text="[sztuk]").grid(row=15, column=5, padx=3, pady=10)



            self.exhaust_filter_casette.configure(state=DISABLED)
            self.exhaust_filter_packet.configure(state=DISABLED)
            self.exhaust_filter_minipleat.configure(state=DISABLED)

            if self.exhaust_type_filter_choice_value.get() == 1 or  self.exhaust_type_filter_choice_value.get() == 2 :
                self.exhaust_filter_plate_data()


    def F7_exhaust_filter_function(self):

        try:
            self.lframe.destroy()
        except:
            pass
        finally:

            # exhaust filter F7  symbol
            self.lframe = ttk.LabelFrame(tab6)
            self.lframe.pack(anchor=W)
            self.lframe.pack(anchor=W, padx=15)
            self.symbol_F7_exhaust_filter_value = StringVar()
            self.lbl_symbol_F7_exhaust_filter = ttk.Label(self.lframe, text="wywiew - wymiar filtru F7").grid(row=5, column=1, padx=3, pady=10)
            self.entry_symbol_F7_exhaust_filter = ttk.Entry(self.lframe, textvariable=self.symbol_F7_exhaust_filter_value, width=30)
            self.entry_symbol_F7_exhaust_filter.insert(END, symbol_F7_exhaust_filter_value[str(self.symbol_ahu_range.get() + '_' + str(self.exhaust_type_filter_choice_value.get()))])
            self.entry_symbol_F7_exhaust_filter.grid(row=10, column=1, padx=1)
            self.exhaust_filter_choice_name_value.set('F7')
            self.symbol_exhaust_filter_value = self.symbol_F7_exhaust_filter_value



            #  exhaust filter F7 quantity
            self.quantity_F7_exhaust_filter_value = StringVar()
            self.lbl_quantity_F7_exhaust_filter = ttk.Label(self.lframe, text="ilość").grid(row=5, column=5, padx=3, pady=10)
            self.entry_quantity_F7_exhaust_filter = ttk.Entry(self.lframe, textvariable=self.quantity_F7_exhaust_filter_value, width=10)
            self.entry_quantity_F7_exhaust_filter.insert(END, quantity_F7_exhaust_filter_value)
            self.entry_quantity_F7_exhaust_filter.grid(row=10, column=5, padx=1)
            self.quantity_exhaust_filter_value = self.quantity_F7_exhaust_filter_value


            #   explanation
            self.lbl = ttk.Label(self.lframe, text="[szer. x wys. x gł.]").grid(row=15, column=1, padx=3, pady=10)
            self.lbl = ttk.Label(self.lframe, text="[sztuk]").grid(row=15, column=5, padx=3, pady=10)



            self.exhaust_filter_casette.configure(state=DISABLED)
            self.exhaust_filter_packet.configure(state=DISABLED)
            self.exhaust_filter_minipleat.configure(state=DISABLED)

            if self.exhaust_type_filter_choice_value.get() == 3 or  self.exhaust_type_filter_choice_value.get() == 2 :
                self.exhaust_filter_plate_data()


    def F9_exhaust_filter_function(self):
        try:
            self.lframe.destroy()
        except:
            pass
        finally:

            # exhaust filter F9  symbol
            self.lframe = ttk.LabelFrame(tab6)
            self.lframe.pack(anchor=W)
            self.lframe.pack(anchor=W, padx=15)
            self.symbol_F9_exhaust_filter_value = StringVar()
            self.lbl_symbol_F9_exhaust_filter = ttk.Label(self.lframe, text="wywiew - wymiar filtru F9").grid(row=5, column=1, padx=3, pady=10)
            self.entry_symbol_F9_exhaust_filter = ttk.Entry(self.lframe, textvariable=self.symbol_F9_exhaust_filter_value, width=30)
            self.entry_symbol_F9_exhaust_filter.insert(END, symbol_F9_exhaust_filter_value[str(self.symbol_ahu_range.get() + '_' + str(self.exhaust_type_filter_choice_value.get()))])
            self.entry_symbol_F9_exhaust_filter.grid(row=10, column=1, padx=1)
            self.exhaust_filter_choice_name_value.set('F9')
            self.symbol_exhaust_filter_value = self.symbol_F9_exhaust_filter_value



            #  exhaust filter F9 quantity
            self.quantity_F9_exhaust_filter_value = StringVar()
            self.lbl_quantity_F9_exhaust_filter = ttk.Label(self.lframe, text="ilość").grid(row=5, column=5, padx=3, pady=10)
            self.entry_quantity_F9_exhaust_filter = ttk.Entry(self.lframe, textvariable=self.quantity_F9_exhaust_filter_value, width=10)
            self.entry_quantity_F9_exhaust_filter.insert(END, quantity_F9_exhaust_filter_value)
            self.entry_quantity_F9_exhaust_filter.grid(row=10, column=5, padx=1)
            self.quantity_exhaust_filter_value = self.quantity_F9_exhaust_filter_value




            #   explanation
            self.lbl = ttk.Label(self.lframe, text="[szer. x wys. x gł.]").grid(row=15, column=1, padx=3, pady=10)
            self.lbl = ttk.Label(self.lframe, text="[sztuk]").grid(row=15, column=5, padx=3, pady=10)



            self.exhaust_filter_casette.configure(state=DISABLED)
            self.exhaust_filter_packet.configure(state=DISABLED)
            self.exhaust_filter_minipleat.configure(state=DISABLED)

            if self.exhaust_type_filter_choice_value.get() == 3 or  self.exhaust_type_filter_choice_value.get() == 2 :
                self.exhaust_filter_plate_data()


    def lackoff_exhaust_filter_function(self) :
        try:
            self.lframe.destroy()

        except:
            pass

        try:
            self.exhaust_filter_casette.configure(state=NORMAL)
            self.exhaust_filter_packet.configure(state=NORMAL)
            self.exhaust_filter_minipleat.configure(state=NORMAL)
        except:
            pass


    def exhaust_filter_plate_data(self):
        exhaust_filter_class = self.exhaust_filter_choice_name_value.get()



        self.entry_exhaust_filter_plate_type_value = StringVar()

        self.entry_exhaust_filter_plate_type = ttk.Entry(self.lframe, width=30, textvariable=self.entry_exhaust_filter_plate_type_value)

        self.exhaust_filter_type = entry_exhaust_filter_plate_type_value[str(self.symbol_ahu_range.get()) + '_' + str(self.exhaust_type_filter_choice_value.get())] + ' ' + exhaust_filter_class
        self.entry_exhaust_filter_plate_type.insert(END, self.exhaust_filter_type)
        self.entry_exhaust_filter_plate_type.grid(row=20, column=1, padx=10)
        self.lbl = ttk.Label(self.lframe, text="Typ").grid(row=20, column=5, padx=10, pady=10)




        #  filter_class

        self.entry_exhaust_filter_plate_filter_class_value = StringVar()

        self.entry_exhaust_filter_plate_filter_class = ttk.Entry(self.lframe, width=30, textvariable=self.entry_exhaust_filter_plate_filter_class_value)

        self.entry_exhaust_filter_plate_filter_class.insert(END, exhaust_filter_class + ' / ' + entry_exhaust_filter_plate_filter_class_value[str(exhaust_filter_class + '_' + str(self.exhaust_type_filter_choice_value.get()))])
        self.entry_exhaust_filter_plate_filter_class.grid(row=35, column=1, padx=10)
        self.lbl = ttk.Label(self.lframe, text="klasa filtra").grid(row=35, column=5, padx=10, pady=10)

        #  Kind of filter

        self.entry_exhaust_filter_plate_kind_value = StringVar()
        kind_of = 'rodzaj'

        self.entry_exhaust_filter_plate_kind = ttk.Entry(self.lframe, width=30, textvariable=self.entry_exhaust_filter_plate_kind_value)
        self.entry_exhaust_filter_plate_kind.insert(END, entry_exhaust_filter_plate_kind_value[str(self.symbol_ahu_range.get())+ '_' + str(self.exhaust_type_filter_choice_value.get())])
        if self.accept_english_switch.get():
            self.entry_exhaust_filter_plate_kind.delete(0, 'end')
            self.entry_exhaust_filter_plate_kind.insert(END, entry_exhaust_filter_plate_kind_value_EN[str(self.symbol_ahu_range.get()) + '_' + str(self.exhaust_type_filter_choice_value.get())])

        self.entry_exhaust_filter_plate_kind.grid(row=25, column=1, padx=10)
        self.lbl = ttk.Label(self.lframe, text="Rodzaj").grid(row=25, column=5, padx=10, pady=10)

        #  initial pressure drop

        self.entry_exhaust_filter_plate_initial_pressure_drop_value = StringVar()

        self.entry_exhaust_filter_plate_initial_pressure_drop = ttk.Entry(self.lframe, width=30, textvariable=self.entry_exhaust_filter_plate_initial_pressure_drop_value)
        self.entry_exhaust_filter_plate_initial_pressure_drop.grid(row=40, column=1, padx=10)
        self.lbl = ttk.Label(self.lframe, text="Opór początkowy").grid(row=40, column=5, padx=10, pady=10)

        #  Recomended_final_pressure_drop

        self.entry_exhaust_filter_plate_recom_final_pressure_drop_value = StringVar()

        self.entry_exhaust_filter_plate_recom_final_pressure_drop = ttk.Entry(self.lframe, width=30, textvariable=self.entry_exhaust_filter_plate_recom_final_pressure_drop_value)
        self.entry_exhaust_filter_plate_recom_final_pressure_drop.grid(row=45, column=1, padx=10)
        self.lbl = ttk.Label(self.lframe, text="Zal. opór końcowy ").grid(row=45, column=5, padx=10, pady=10)

    ####################################################################

    def exhaust_filter_02_choice(self):
        self.lfradio = ttk.LabelFrame(tab13)
        self.lfradio.pack()
        self.exhaust_filter_02_choice_name_value = StringVar()
        self.exhaust_filter_02_choice_value = IntVar()
        self.symbol_exhaust_filter_02_value = ''

        self.G4_filter_02 = ttk.Radiobutton(self.lfradio, text="G4", variable=self.exhaust_filter_02_choice_value, value=1, command=self.G4_exhaust_filter_02_function)
        self.G4_filter_02.grid(row=0, column=0, padx=20, pady=5)
        self.M5_filter_02 = ttk.Radiobutton(self.lfradio, text="M5", variable=self.exhaust_filter_02_choice_value, value=2, command=self.M5_exhaust_filter_02_function)
        self.M5_filter_02.grid(row=0, column=5, padx=20, pady=5)
        self.F7_filter_02 = ttk.Radiobutton(self.lfradio, text="F7", variable=self.exhaust_filter_02_choice_value, value=3, command=self.F7_exhaust_filter_02_function)
        self.F7_filter_02.grid(row=0, column=10, padx=20, pady=5)
        self.F9_filter_02 = ttk.Radiobutton(self.lfradio, text="F9", variable=self.exhaust_filter_02_choice_value, value=4, command=self.F9_exhaust_filter_02_function)
        self.F9_filter_02.grid(row=0, column=15, padx=20, pady=5)
        self.lackoff_exhaust_fan = ttk.Radiobutton(self.lfradio, text="brak", variable=self.exhaust_filter_02_choice_value, value=5, command=self.lackoff_exhaust_filter_02_function).grid(row=0, column=20, padx=20, pady=5)

    def exhaust_type_filter_02_choice(self):
        self.lfradio = ttk.LabelFrame(tab13)
        self.lfradio.pack()
        self.exhaust_type_filter_02_choice_value = IntVar()
        self.exhaust_filter_02_casette = ttk.Radiobutton(self.lfradio, text="działkowy", variable=self.exhaust_type_filter_02_choice_value, value=1, comman=self.exhaust_filter_02_plate_data)
        self.exhaust_filter_02_casette.grid(row=0, column=0, padx=20, pady=5)
        self.exhaust_filter_02_packet = ttk.Radiobutton(self.lfradio, text="kieszeniowy", variable=self.exhaust_type_filter_02_choice_value, value=2, comman=self.exhaust_filter_02_plate_data)
        self.exhaust_filter_02_packet.grid(row=0, column=5, padx=20, pady=5)
        self.exhaust_filter_02_minipleat = ttk.Radiobutton(self.lfradio, text="minipleat", variable=self.exhaust_type_filter_02_choice_value, value=3, comman=self.exhaust_filter_02_plate_data)
        self.exhaust_filter_02_minipleat.grid(row=0, column=15, padx=20, pady=5)

    def G4_exhaust_filter_02_function(self):
        try:
            self.lframe.destroy()
        except:
            pass
        finally:

            # exhaust filter_02 G4  symbol
            self.lframe = ttk.LabelFrame(tab13)
            self.lframe.pack(anchor=W)
            self.lframe.pack(anchor=W, padx=15)
            self.symbol_G4_exhaust_filter_02_value = StringVar()
            self.lbl_symbol_G4_exhaust_filter_02 = ttk.Label(self.lframe, text="wywiew - wymiar filtru G4").grid(row=5, column=1, padx=3, pady=10)
            self.entry_symbol_G4_exhaust_filter_02 = ttk.Entry(self.lframe, textvariable=self.symbol_G4_exhaust_filter_02_value, width=30)
            self.entry_symbol_G4_exhaust_filter_02.insert(END, symbol_G4_exhaust_filter_value[str(self.symbol_ahu_range.get() + '_' + str(self.exhaust_type_filter_02_choice_value.get()))])
            self.entry_symbol_G4_exhaust_filter_02.grid(row=10, column=1, padx=1)
            self.exhaust_filter_02_choice_name_value.set('G4')
            self.symbol_exhaust_filter_02_value = self.symbol_G4_exhaust_filter_02_value

            #  exhaust filter_02 G4 quantity
            self.quantity_G4_exhaust_filter_02_value = StringVar()
            self.lbl_quantity_G4_exhaust_filter_02 = ttk.Label(self.lframe, text="ilość").grid(row=5, column=5, padx=3, pady=10)
            self.entry_quantity_G4_exhaust_filter_02 = ttk.Entry(self.lframe, textvariable=self.quantity_G4_exhaust_filter_02_value, width=10)
            self.entry_quantity_G4_exhaust_filter_02.insert(END, quantity_G4_exhaust_filter_value)
            self.entry_quantity_G4_exhaust_filter_02.grid(row=10, column=5, padx=1)
            self.quantity_exhaust_filter_02_value = self.quantity_G4_exhaust_filter_02_value

            #   explanation
            self.lbl = ttk.Label(self.lframe, text="[szer. x wys. x gł.]").grid(row=15, column=1, padx=3, pady=10)
            self.lbl = ttk.Label(self.lframe, text="[sztuk]").grid(row=15, column=5, padx=3, pady=10)

            self.exhaust_filter_02_casette.configure(state=DISABLED)
            self.exhaust_filter_02_packet.configure(state=DISABLED)
            self.exhaust_filter_02_minipleat.configure(state=DISABLED)

            if self.exhaust_type_filter_02_choice_value.get() == 1 or self.exhaust_type_filter_02_choice_value.get() == 2:
                self.exhaust_filter_02_plate_data()

    def M5_exhaust_filter_02_function(self):
        try:
            self.lframe.destroy()
        except:
            pass
        finally:

            # exhaust filter_02 M5  symbol
            self.lframe = ttk.LabelFrame(tab13)
            self.lframe.pack(anchor=W)
            self.lframe.pack(anchor=W, padx=15)
            self.symbol_M5_exhaust_filter_02_value = StringVar()
            self.lbl_symbol_M5_exhaust_filter_02 = ttk.Label(self.lframe, text="wywiew - wymiar filtru M5").grid(row=5, column=1, padx=3, pady=10)
            self.entry_symbol_M5_exhaust_filter_02 = ttk.Entry(self.lframe, textvariable=self.symbol_M5_exhaust_filter_02_value, width=30)
            self.entry_symbol_M5_exhaust_filter_02.insert(END, symbol_M5_exhaust_filter_value[str(self.symbol_ahu_range.get() + '_' + str(self.exhaust_type_filter_02_choice_value.get()))])
            self.entry_symbol_M5_exhaust_filter_02.grid(row=10, column=1, padx=1)
            self.exhaust_filter_02_choice_name_value.set('M5')
            self.symbol_exhaust_filter_02_value = self.symbol_M5_exhaust_filter_02_value

            #  exhaust filter_02 M5 quantity
            self.quantity_M5_exhaust_filter_02_value = StringVar()
            self.lbl_quantity_M5_exhaust_filter_02 = ttk.Label(self.lframe, text="ilość").grid(row=5, column=5, padx=3, pady=10)
            self.entry_quantity_M5_exhaust_filter_02 = ttk.Entry(self.lframe, textvariable=self.quantity_M5_exhaust_filter_02_value, width=10)
            self.entry_quantity_M5_exhaust_filter_02.insert(END, quantity_M5_exhaust_filter_value)
            self.entry_quantity_M5_exhaust_filter_02.grid(row=10, column=5, padx=1)
            self.quantity_exhaust_filter_02_value = self.quantity_M5_exhaust_filter_02_value

            #   explanation
            self.lbl = ttk.Label(self.lframe, text="[szer. x wys. x gł.]").grid(row=15, column=1, padx=3, pady=10)
            self.lbl = ttk.Label(self.lframe, text="[sztuk]").grid(row=15, column=5, padx=3, pady=10)

            self.exhaust_filter_02_casette.configure(state=DISABLED)
            self.exhaust_filter_02_packet.configure(state=DISABLED)
            self.exhaust_filter_02_minipleat.configure(state=DISABLED)

            if self.exhaust_type_filter_02_choice_value.get() == 1 or self.exhaust_type_filter_02_choice_value.get() == 2:
                self.exhaust_filter_02_plate_data()

    def F7_exhaust_filter_02_function(self):
        try:
            self.lframe.destroy()
        except:
            pass
        finally:

            # exhaust filter_02 F7  symbol
            self.lframe = ttk.LabelFrame(tab13)
            self.lframe.pack(anchor=W)
            self.lframe.pack(anchor=W, padx=15)
            self.symbol_F7_exhaust_filter_02_value = StringVar()
            self.lbl_symbol_F7_exhaust_filter_02 = ttk.Label(self.lframe, text="wywiew - wymiar filtru F7").grid(row=5, column=1, padx=3, pady=10)
            self.entry_symbol_F7_exhaust_filter_02 = ttk.Entry(self.lframe, textvariable=self.symbol_F7_exhaust_filter_02_value, width=30)
            self.entry_symbol_F7_exhaust_filter_02.insert(END, symbol_F7_exhaust_filter_value[str(self.symbol_ahu_range.get() + '_' + str(self.exhaust_type_filter_02_choice_value.get()))])
            self.entry_symbol_F7_exhaust_filter_02.grid(row=10, column=1, padx=1)
            self.exhaust_filter_02_choice_name_value.set('F7')
            self.symbol_exhaust_filter_02_value = self.symbol_F7_exhaust_filter_02_value

            #  exhaust filter_02 F7 quantity
            self.quantity_F7_exhaust_filter_02_value = StringVar()
            self.lbl_quantity_F7_exhaust_filter_02 = ttk.Label(self.lframe, text="ilość").grid(row=5, column=5, padx=3, pady=10)
            self.entry_quantity_F7_exhaust_filter_02 = ttk.Entry(self.lframe, textvariable=self.quantity_F7_exhaust_filter_02_value, width=10)
            self.entry_quantity_F7_exhaust_filter_02.insert(END, quantity_F7_exhaust_filter_value)
            self.entry_quantity_F7_exhaust_filter_02.grid(row=10, column=5, padx=1)
            self.quantity_exhaust_filter_02_value = self.quantity_F7_exhaust_filter_02_value

            #   explanation
            self.lbl = ttk.Label(self.lframe, text="[szer. x wys. x gł.]").grid(row=15, column=1, padx=3, pady=10)
            self.lbl = ttk.Label(self.lframe, text="[sztuk]").grid(row=15, column=5, padx=3, pady=10)

            self.exhaust_filter_02_casette.configure(state=DISABLED)
            self.exhaust_filter_02_packet.configure(state=DISABLED)
            self.exhaust_filter_02_minipleat.configure(state=DISABLED)

            if self.exhaust_type_filter_02_choice_value.get() == 3 or self.exhaust_type_filter_02_choice_value.get() == 2:
                self.exhaust_filter_02_plate_data()

    def F9_exhaust_filter_02_function(self):
        try:
            self.lframe.destroy()
        except:
            pass
        finally:

            # exhaust filter_02 F9  symbol
            self.lframe = ttk.LabelFrame(tab13)
            self.lframe.pack(anchor=W)
            self.lframe.pack(anchor=W, padx=15)
            self.symbol_F9_exhaust_filter_02_value = StringVar()
            self.lbl_symbol_F9_exhaust_filter_02 = ttk.Label(self.lframe, text="wywiew - wymiar filtru F9").grid(row=5, column=1, padx=3, pady=10)
            self.entry_symbol_F9_exhaust_filter_02 = ttk.Entry(self.lframe, textvariable=self.symbol_F9_exhaust_filter_02_value, width=30)
            self.entry_symbol_F9_exhaust_filter_02.insert(END, symbol_F9_exhaust_filter_value[str(self.symbol_ahu_range.get() + '_' + str(self.exhaust_type_filter_02_choice_value.get()))])
            self.entry_symbol_F9_exhaust_filter_02.grid(row=10, column=1, padx=1)
            self.exhaust_filter_02_choice_name_value.set('F9')
            self.symbol_exhaust_filter_02_value = self.symbol_F9_exhaust_filter_02_value

            #  exhaust filter_02 F9 quantity
            self.quantity_F9_exhaust_filter_02_value = StringVar()
            self.lbl_quantity_F9_exhaust_filter_02 = ttk.Label(self.lframe, text="ilość").grid(row=5, column=5, padx=3, pady=10)
            self.entry_quantity_F9_exhaust_filter_02 = ttk.Entry(self.lframe, textvariable=self.quantity_F9_exhaust_filter_02_value, width=10)
            self.entry_quantity_F9_exhaust_filter_02.insert(END, quantity_F9_exhaust_filter_value)
            self.entry_quantity_F9_exhaust_filter_02.grid(row=10, column=5, padx=1)
            self.quantity_exhaust_filter_02_value =  self.quantity_F9_exhaust_filter_02_value

            #   explanation
            self.lbl = ttk.Label(self.lframe, text="[szer. x wys. x gł.]").grid(row=15, column=1, padx=3, pady=10)
            self.lbl = ttk.Label(self.lframe, text="[sztuk]").grid(row=15, column=5, padx=3, pady=10)

            self.exhaust_filter_02_casette.configure(state=DISABLED)
            self.exhaust_filter_02_packet.configure(state=DISABLED)
            self.exhaust_filter_02_minipleat.configure(state=DISABLED)

            if self.exhaust_type_filter_02_choice_value.get() == 3 or self.exhaust_type_filter_02_choice_value.get() == 2:
                self.exhaust_filter_02_plate_data()

    def lackoff_exhaust_filter_02_function(self):
        try:
            self.lframe.destroy()

        except:
            pass

        try:
            self.exhaust_filter_02_casette.configure(state=NORMAL)
            self.exhaust_filter_02_packet.configure(state=NORMAL)
            self.exhaust_filter_02_minipleat.configure(state=NORMAL)
        except:
            pass



    def exhaust_filter_02_plate_data(self):
        exhaust_filter_02_class = self.exhaust_filter_02_choice_name_value.get()

        self.entry_exhaust_filter_02_plate_type_value = StringVar()

        self.entry_exhaust_filter_02_plate_type = ttk.Entry(self.lframe, width=30, textvariable=self.entry_exhaust_filter_02_plate_type_value)

        self.exhaust_filter_02_type = entry_exhaust_filter_plate_type_value[str(self.symbol_ahu_range.get()) + '_' + str(self.exhaust_type_filter_02_choice_value.get())] + ' ' + exhaust_filter_02_class
        self.entry_exhaust_filter_02_plate_type.insert(END, self.exhaust_filter_02_type)
        self.entry_exhaust_filter_02_plate_type.grid(row=20, column=1, padx=10)
        self.lbl = ttk.Label(self.lframe, text="Typ").grid(row=20, column=5, padx=10, pady=10)

        #  filter_02_class

        self.entry_exhaust_filter_02_plate_filter_02_class_value = StringVar()

        self.entry_exhaust_filter_02_plate_filter_02_class = ttk.Entry(self.lframe, width=30, textvariable=self.entry_exhaust_filter_02_plate_filter_02_class_value)

        self.entry_exhaust_filter_02_plate_filter_02_class.insert(END, exhaust_filter_02_class + ' / ' + entry_exhaust_filter_plate_filter_class_value[str(exhaust_filter_02_class)+ '_' + str(self.exhaust_type_filter_02_choice_value.get())])
        self.entry_exhaust_filter_02_plate_filter_02_class.grid(row=35, column=1, padx=10)
        self.lbl = ttk.Label(self.lframe, text="klasa filtra").grid(row=35, column=5, padx=10, pady=10)

        #  Kind of filter_02

        self.entry_exhaust_filter_02_plate_kind_value = StringVar()
        kind_of = 'rodzaj'

        self.entry_exhaust_filter_02_plate_kind = ttk.Entry(self.lframe, width=30, textvariable=self.entry_exhaust_filter_02_plate_kind_value)
        self.entry_exhaust_filter_02_plate_kind.insert(END, entry_exhaust_filter_plate_kind_value[str(self.symbol_ahu_range.get()) + '_' + str(self.exhaust_type_filter_02_choice_value.get())])
        if self.accept_english_switch.get():
            self.entry_exhaust_filter_02_plate_kind.delete(0, 'end')
            self.entry_exhaust_filter_02_plate_kind.insert(END, entry_exhaust_filter_plate_kind_value_EN[str(self.symbol_ahu_range.get()) + '_' + str(self.exhaust_type_filter_02_choice_value.get())])

        self.entry_exhaust_filter_02_plate_kind.grid(row=25, column=1, padx=10)
        self.lbl = ttk.Label(self.lframe, text="Rodzaj").grid(row=25, column=5, padx=10, pady=10)

        #  initial pressure drop

        self.entry_exhaust_filter_02_plate_initial_pressure_drop_value = StringVar()

        self.entry_exhaust_filter_02_plate_initial_pressure_drop = ttk.Entry(self.lframe, width=30, textvariable=self.entry_exhaust_filter_02_plate_initial_pressure_drop_value)
        self.entry_exhaust_filter_02_plate_initial_pressure_drop.grid(row=40, column=1, padx=10)
        self.lbl = ttk.Label(self.lframe, text="Opór początkowy").grid(row=40, column=5, padx=10, pady=10)

        #  Recomended_final_pressure_drop

        self.entry_exhaust_filter_02_plate_recom_final_pressure_drop_value = StringVar()

        self.entry_exhaust_filter_02_plate_recom_final_pressure_drop = ttk.Entry(self.lframe, width=30, textvariable=self.entry_exhaust_filter_02_plate_recom_final_pressure_drop_value)
        self.entry_exhaust_filter_02_plate_recom_final_pressure_drop.grid(row=45, column=1, padx=10)
        self.lbl = ttk.Label(self.lframe, text="Zal. opór końcowy ").grid(row=45, column=5, padx=10, pady=10)








#########################################################################################################################################
    def heat_exchanger_choice(self):
        self.heat_exchanger_radio = ttk.LabelFrame(tab7)
        self.heat_exchanger_radio.pack( )
        self.heat_exchanger_choice_value = IntVar()
        self.cross_heat_echanger_in_radio= ttk.Radiobutton(self.heat_exchanger_radio, text = "Wymiennik - przeciwprądowy", variable = self.heat_exchanger_choice_value, value = 1, command = self.cross_heat_exchanger_in).grid(row =0, column = 0, padx=20, pady = 5)
        self.rotor_heat_echanger_in_radio = ttk.Radiobutton(self.heat_exchanger_radio, text=  "Wymiennik - obrotowy", variable = self.heat_exchanger_choice_value, value=2, command=self.rotor_heat_exchanger_in).grid(row=0, column=10, padx=20, pady=5)
        self.lackoff_heat_exchanger_radio = ttk.Radiobutton(self.heat_exchanger_radio, text="brak", variable = self.heat_exchanger_choice_value, value= 5, command = self.lackoff_heat_exchanger).grid (row = 0, column = 20, padx=20, pady = 5)



    def cross_heat_exchanger_in(self):

        try:
                self.lframe.destroy()

        except:
            pass

        finally:
                self.lframe = ttk.LabelFrame(tab7)
                self.lframe.pack(anchor=W, padx=15)
                self.symbol_heat_exchanger_value = StringVar()
                self.lbl_symbol_heat_exchanger = ttk.Label(self.lframe, text="wymiennik przeciwprądowy - typ").grid(row=5, column=10, padx=3, pady=10)
                self.entry_heat_exchanger = ttk.Entry(self.lframe, textvariable=self.symbol_heat_exchanger_value , width=50)

                if self.accept_english_switch.get() :
                    self.entry_heat_exchanger.insert(END, symbol_cross_heat_exchanger_value_EN[str(self.symbol_ahu_range.get())])

                else:
                    self.entry_heat_exchanger.insert(END, symbol_cross_heat_exchanger_value[str(self.symbol_ahu_range.get())])

                self.entry_heat_exchanger.grid(row=5, column=15, padx=1)

    def rotor_heat_exchanger_in(self):

        try:
                self.lframe.destroy()

        except:
            pass

        finally:
                self.lframe = ttk.LabelFrame(tab7)
                self.lframe.pack(anchor=W, padx=15)
                self.symbol_heat_exchanger_value = StringVar()
                self.lbl_symbol_heat_exchanger = ttk.Label(self.lframe, text="wymiennik obrotowy- typ").grid(row=5, column=10, padx=3, pady=10)
                self.entry_heat_exchanger = ttk.Entry(self.lframe, textvariable=self.symbol_heat_exchanger_value, width=50)
                self.entry_heat_exchanger.insert(END, symbol_rotor_value[str(self.symbol_ahu_range.get())])
                self.entry_heat_exchanger.grid(row=5, column=15, padx=1)


    def lackoff_heat_exchanger(self) :
        try:
            self.lframe.destroy()
        except:
            pass




    def damper_choice(self):

            self.lfradio = ttk.LabelFrame(tab8)
            self.lfradio.pack( )
            self.damper_choice_value = IntVar()
            self.supply_damper_radio = ttk.Radiobutton(self.lfradio,text = "tłumik_nawiew", variable = self.damper_choice_value, value = 1,command = self.damper_supply).grid(row =0,column = 0,padx=20, pady = 5 )
            self.exhaust_damper_radio = ttk.Radiobutton(self.lfradio,text = "tłumik_wywiew", variable = self.damper_choice_value, value = 2, command = self.damper_exhaust ).grid(row=0,column = 5,padx=20,pady = 5)
            self.both_damper_radio = ttk.Radiobutton(self.lfradio, text="oba", variable = self.damper_choice_value, value= 3,command = self.damper_both ).grid(row =0,column = 15 , padx=20,pady = 5)
            self.lackoff_damper_radio = ttk.Radiobutton(self.lfradio, text="brak", variable = self.damper_choice_value , value= 4, command = self.lackoff_damper ).grid (row = 0,column = 20,padx=20, pady = 5)



    def damper_supply(self):

        try:
            self.damper_frame.destroy()
        except:
            pass
        finally:



                self.damper_frame = ttk.LabelFrame(tab8)
                self.damper_frame.pack(anchor=W, padx=15)

                self.symbol_supply_damper_value = StringVar()
                self.lbl_supply_symbol_damper = ttk.Label(self.damper_frame, text="tłumik nawiew - typ").grid(row=5, column=10, padx=3, pady=10)
                self.entry_damper = ttk.Entry(self.damper_frame, textvariable=self.symbol_supply_damper_value , width=30)

                self.entry_damper.insert(END, get_data.symbol_supply_damper_value)
                self.entry_damper.grid(row=5, column=15, padx=1)

    def damper_exhaust(self):

        try:
            self.damper_frame.destroy()
        except:
            pass
        finally:

                self.damper_frame = ttk.LabelFrame(tab8)
                self.damper_frame.pack(anchor=W, padx=15)

                self.symbol_exaust_damper_value = StringVar()
                self.lbl_symbol_exhaust_damper = ttk.Label(self.damper_frame, text="tłumik wywiew - typ").grid(row=10, column=10, padx=3, pady=10)
                self.entry_damper = ttk.Entry(self.damper_frame, textvariable=self.symbol_exaust_damper_value , width=30)
                self.entry_damper.insert(END, get_data.symbol_exaust_damper_value)
                self.entry_damper.grid(row=10, column=15, padx=1)


    def damper_both(self):
        try:
               self.damper_frame.destroy()
        except:
            pass
        finally:

                self.damper_frame = ttk.LabelFrame(tab8)
                self.damper_frame.pack(anchor=W, padx=15)


                self.symbol_supply_damper_value = StringVar()
                self.lbl_supply_symbol_damper = ttk.Label(self.damper_frame, text="tłumik nawiew - typ").grid(row=5, column=10, padx=3, pady=10)
                self.entry_damper = ttk.Entry(self.damper_frame, textvariable=self.symbol_supply_damper_value, width=30)
                self.entry_damper.insert(END, get_data.symbol_supply_damper_value)
                self.entry_damper.grid(row=5, column=15, padx=1)

                self.symbol_exaust_damper_value = StringVar()
                self.lbl_symbol_exhaust_damper = ttk.Label(self.damper_frame, text="tłumik wywiew - typ").grid(row=10, column=10, padx=3, pady=10)
                self.entry_damper = ttk.Entry(self.damper_frame, textvariable=self.symbol_exaust_damper_value, width=30)
                self.entry_damper.insert(END, get_data.symbol_exaust_damper_value)
                self.entry_damper.grid(row=10, column=15, padx=1)



    def lackoff_damper(self):
        try:
              self.damper_frame.destroy()
        except:
                pass
        finally:
                pass


    def additional_equip_choice(self):

        self.lfradio = ttk.LabelFrame(tab9)
        self.lfradio.pack( side = TOP)
        self.add_equip_choice_value = IntVar()
        self.add_equip_radio = ttk.Radiobutton(self.lfradio, text="off", variable = self.add_equip_choice_value, value = 2, command = self.lackoff_additional ).grid (row = 0,column = 20,padx=20, pady = 5)
        self.add_equip_radio = ttk.Radiobutton(self.lfradio,text = "on", variable = self.add_equip_choice_value, value = 1,command = self.additional_exuipment).grid(row =0,column = 0,padx=20, pady = 5 )


    def additional_exuipment(self):
        try:
            self.additional_exuipment_frame.destroy()
        except:
            pass
        finally:
            self.additional_exuipment_frame = ttk.LabelFrame(tab9)
           # self.additional_exuipment_frame.pack(anchor=W, padx=15)
            self.additional_exuipment_frame.pack(side=BOTTOM)
            self.lbl_additional_equipment= ttk.Label(self.additional_exuipment_frame, text="wyposażenie dodatkowe").grid(row=5, column=10, padx=3, pady=10)
            self.txt_additional_equipment = Text(self.additional_exuipment_frame , width=50, height = 19, )
            self.txt_additional_equipment.insert("1.0", get_data.additional_exuipment_value)
            self.txt_additional_equipment.grid(row=5, column=15, padx=1)


    def lackoff_additional(self):
        try:
            self.additional_exuipment_frame.destroy()
        except:
            pass
        finally:
            pass



    def s_and_p(self):


        self.s_and_p_frame = ttk.LabelFrame(tab10)
        self.s_and_p_frame.pack(anchor=W, padx=15)
        self.lbl_s_and_p= ttk.Label(self.s_and_p_frame, text="sprawdzenie i próby" ).grid(row=5, column=10, padx=3, pady=10)
        self.txt_s_and_p = Text(self.s_and_p_frame , width=50, height = 20)
        self.txt_s_and_p.grid(row=5, column=15, padx=1)



    def accept(self):


        self.accept_frame = ttk.LabelFrame(tab11)
        self.accept_frame.pack()
        self.text_folder = Label(self.accept_frame,text='Lokalizacja plików tabliczka i świadectwo KJ').grid(row = 1, column = 1, padx=20 , pady=(20,3))
        self.save_button=ttk.Button(self.accept_frame, text = "wybierz folder", command = self.choice_newdir).grid(row = 1, column = 15, padx=20, pady=(20, 3))
        self.text_folder = Label(self.accept_frame,text='Zapisz w wybranej lokalizacji').grid(row = 15, column = 1 , padx=20 , pady=(30,20))
        self.accept_button=ttk.Button(self.accept_frame,text = "zapisz", command = self.save_newpdf )
        self.accept_button.grid(row=15, column=15, padx=20, pady=(30, 20))





    def choice_newdir(self):
        self.accept_button.config(text = 'zapisz')
        self.path_out = filedialog.askdirectory(initialdir = default_path_out)





    def save_newpdf(self):
        space = '  ;  '
        self.accept_button.config(text='zapisz')

        try:
            production_year =  re.findall(r'2\d\d\d', self.data_value.get())[0]
        except:
            production_year = datetime.datetime.today().strftime('%Y')


        data_atest_out= {'Pole tekstowe 1': self.selected_ahu_value.get(), 'Pole tekstowe 2': self.entry_serial_value.get(), 'Pole tekstowe 3': self.selected_supply_value.get() + self.selected_supply_execution_value.get(),
                        'Pole tekstowe 4': self.selected_exhaust_value.get() + self.selected_exhaust_execution_value.get(), 'Pole tekstowe 5': self.entry_supply_flow_value.get() + '\r' + self.entry_exhaust_flow_value.get(),
                        'Pole tekstowe 6': self.entry_supply_pressure_value.get()+'\r'+self.entry_exhaust_pressure_value.get(),'Pole tekstowe 7': '','Pole tekstowe 8': '',
                         'Pole tekstowe 9': '', 'Pole tekstowe 10': '', 'Pole tekstowe 11': '', 'Pole tekstowe 12': '', 'Pole tekstowe 16': '',
                         'Pole tekstowe 17': '', 'Pole tekstowe 18': 'qqq' , 'Pole tekstowe 19': '', 'Pole tekstowe 23':'Sprawdzenie i próby', 'Pole tekstowe 24':'Inspection and tests:',
                         'Pole tekstowe 25': '', 'Pole tekstowe 26': '','Pole tekstowe 27': '', 'Pole tekstowe 28': '', 'Pole tekstowe 29': ''}


        data_tabliczka_out= {'supply': self.selected_supply_value.get() + self.selected_supply_execution_value.get(), 'evo': self.selected_ahu_value.get() ,
                             'exhaust': self.selected_exhaust_value.get() + self.selected_exhaust_execution_value.get(),
                             'year prod': production_year, 'serial no': self.entry_serial_value.get(),
                             'prod order no': self.entry_order_value.get(), 'air flow s': self.entry_supply_flow_value.get(), 'fan set s': '', 'fan set e': '',
                             'air flow e': self.entry_exhaust_flow_value.get(), 'external press s': self.entry_supply_pressure_value.get(), 'fan el mot s': '',
                             'fan el mot e': '', 'external press e': self.entry_exhaust_pressure_value.get(), 'heatre I s': '', 'comp un s': '',
                             'comp un e': '', 'heatre I e': '', 'heatre II s': '', 'cooler s':'', 'pre filt 1 s':'', 'pre filt 1 e':'', 'heatre II e': '',
                             'electric heater s': '', 'pre filt 2 s': '', 'pre filt 2 e': '', 'sec filt 2 s': '', 'sec filt 2 e': '',
                             'electric heater e': '', 'pre filt 3 s': '', 'pre filt 3 e': '', 'sec filt 3 s': '', 'sec filt 3 e': '', 'cooler e': '',
                             'Humidifier s': '', 'sec filt 1 s': '', 'sec filt 1 e': '', 'sec filt 4 s': '', 'sec filt 4 e': '', 'Humidifier e':'',
                             'pump el motor t':'', 'heat recovery t': '', 'weight t': '', 'air flow': 'Wydatek powietrza',
                             'fan set': 'Silnik rotora/p-py gl.', 'external press': 'Ciśnienie dyspozycyjne', 'fan el mot': 'Wentylator', 'heatre I': 'Nagrzewnica I wodna',
                             'comp un': 'Silnik wentylatora', 'heatre II': 'Nagrzewnica II', 'pre filt 1': 'Agr. chłodniczy', 'electric heater': 'Nagrzewnica elektryczna',
                             'pre filt 2': 'Filtr wstępny', 'sec filt 2': 'Filtr II stopnia', 'cooler': 'Chłodnica', 'pre filt 3': 'Filtr wstępny',
                             'sec filt 3': 'Filtr III stopnia', 'Humidifier': 'Nawilżacz', 'sec filt 1': 'Filtr II stopnia', 'sec filt 4': 'Filtr III stopnia',
                             'pump el motor': 'Silnik p-py nawilż.', 'heat recovery': 'Odzysk ciepła', 'weight': 'Masa', 'air flow u': 'm³/h', 'fan set u': 'kW/V',
                             'external press u': 'Pa', 'fan el mot u': 'typ', 'comp un u': 'kW/V', 'heatre II u': 'typ', 'pre filt 1 u': ' V/Arozr/Amax',
                             'pre filt 2 u': 'typ/rozm/szt.', 'sec filt 2 u': 'typ/rozm/szt.', 'cooler u': '°C/kW/kPa ','heatre I u': '°C/kW/kPa',
                             'pre filt 3 u': 'typ/rozm/szt.', 'sec filt 3 u': 'typ/rozm/szt.', 'Humidifier u': '[kg/h]/kW/V', 'sec filt 1 u': 'typ/rozm/szt.',
                             'sec filt 4 u': 'typ/rozm/szt.', 'pump el motor u': 'kW/V/A', 'heat recovery u': 'typ', 'weight u': 'kg', 'cooler e 1': ''}

        data_tabliczka_out_ENG = {'supply': self.selected_supply_value.get() + self.selected_supply_execution_value.get(), 'evo': self.selected_ahu_value.get(),
                              'exhaust': self.selected_exhaust_value.get() + self.selected_exhaust_execution_value.get(),
                              'year prod': production_year, 'serial no': self.entry_serial_value.get(),
                              'prod order no': self.entry_order_value.get(), 'air flow s': self.entry_supply_flow_value.get(), 'fan set s': '', 'fan set e': '',
                              'air flow e': self.entry_exhaust_flow_value.get(), 'external press s': self.entry_supply_pressure_value.get(), 'fan el mot s': '',
                              'fan el mot e': '', 'external press e': self.entry_exhaust_pressure_value.get(), 'heatre I s': '', 'comp un s': '',
                              'comp un e': '', 'heatre I e': '', 'heatre II s': '', 'cooler s': '', 'pre filt 1 s': '', 'pre filt 1 e': '', 'heatre II e': '',
                              'electric heater s': '', 'pre filt 2 s': '', 'pre filt 2 e': '', 'sec filt 2 s': '', 'sec filt 2 e': '',
                              'electric heater e': '', 'pre filt 3 s': '', 'pre filt 3 e': '', 'sec filt 3 s': '', 'sec filt 3 e': '', 'cooler e': '',
                              'Humidifier s': '', 'sec filt 1 s': '', 'sec filt 1 e': '', 'sec filt 4 s': '', 'sec filt 4 e': '', 'Humidifier e': '',
                              'pump el motor t': '', 'heat recovery t': '', 'weight t': '', 'air flow': 'Air flow','heatre I u': '°C/kW/kPa',
                              'fan set': 'Rotary drive/glycol pump', 'external press': 'External pressure', 'fan el mot': 'Fan set', 'heatre I': 'Heater I',
                              'comp un': 'Fan el. motor', 'heatre II': 'Heater II', 'pre filt 1': 'Compressors unit', 'electric heater': 'Electric heater',
                              'pre filt 2': 'Preliminary filter', 'sec filt 2': 'Secondary filter', 'cooler': 'Cooler', 'pre filt 3': 'Preliminary filter',
                              'sec filt 3': 'Secondary filter', 'Humidifier': 'Humidifier', 'sec filt 1': 'Secondary filter', 'sec filt 4': '',
                              'pump el motor': 'Pump el. motor of hum.', 'heat recovery': 'Heat recovery', 'weight': 'Weight', 'air flow u': 'm³/h', 'fan set u': 'kW/V',
                              'external press u': 'Pa', 'fan el mot u': 'type', 'comp un u': 'kW/V', 'heatre II u': '°C/kW/kPa',
                              'pre filt 1 u': ' V/Astart/Amax',
                              'pre filt 2 u': 'type/size/pcs', 'sec filt 2 u': 'type/size/pcs', 'cooler u': '°C/kW/kPa ',
                              'pre filt 3 u': 'type/size/pcs', 'sec filt 3 u': 'type/size/pcs', 'Humidifier u': '[kg/h]/kW/V', 'sec filt 1 u': 'type/size/pcs',
                              'sec filt 4 u': 'type/size/pcs', 'pump el motor u': 'kW/V/A', 'heat recovery u': 'type', 'weight u': 'kg', 'cooler e 1': ''}



        if self.accept_english_switch.get():

            data_tabliczka_out = data_tabliczka_out_ENG


        data_protocol_out = {'nr centrali 1': '', 'typ centrali 2': f'{self.selected_supply_value.get()} {self.selected_supply_execution_value.get()}/{self.selected_exhaust_execution_value.get()}',
                             'typ centrali 3': 'Typ centrali', 'nr 2': self.entry_system_value.get(),
                             'nr centrali 2': self.entry_serial_value.get(),'2': 'Zgodność wykonania z KDC i wytycznymi.', '3': 'Kompletność wyposażenia.', '4': 'Sprawdzenie silnika w ruchu.',
                             '5': 'Sprawdzenie wymiennika obrotowego w ruchu.', '6': 'Próba szczelności instalacji:',
                             '5a 2': 'chłodniczej  (2,8 MPa)', '5b 2': 'glikolowej (0,5 MPa)', '7': 'Etykiety i znaczniki.  ', '8': 'Oznaczenia kierunku przepływu przez wymienniki.',
                             '9': 'Czystość wewnątrz i na zewnątrz centrali.      ', '10': 'Zgodność automatyki ze specyfikacją.', 'nr centrali 3': 'Nr centrali',
                             'þÿ\x00u\x00k\x01B\x00 \x00c\x00h\x00l\x00o\x00d\x00n\x00i\x00c\x00z\x00y\x00 \x002': '----------------------',
                             'þÿ\x00u\x00k\x01B\x00 \x00c\x00h\x00l\x00o\x00d\x00n\x00i\x00c\x00z\x00y\x00 \x003': 'Układ chłodniczy:', 'data 2': '',
                             'þÿ\x00o\x00d\x00e\x00b\x00r\x00a\x01B\x00 \x002': '',
                             'przeznaczenie 2': self.destiny_value.get(), 'oznaczenie produktu 2': self.entry_project_value.get(), 'þÿ\x00u\x00k\x01B\x00 '
                                                                                                                        '\x00g\x00l\x00i\x00k\x00o\x00w\x00y\x00 '
                                                                                                              '\x002': '----------------------',
                             'þÿ\x00u\x00k\x01B\x00 \x00g\x00l\x00i\x00k\x00o\x00w\x00y\x00 \x003': 'Układ glikolowy:', 'uwaga 2': '----------------------', 'uwaga 3': 'Uwagi:',
                             'Pole wyboru 21': 'Off', 'Pole wyboru 22': 'Off', 'Pole wyboru 23': 'Tak', 'Pole wyboru 24': 'Tak', 'Pole wyboru 25': 'Tak', 'Pole wyboru 26': 'Tak',
                             'Pole wyboru 27': 'Off', 'Pole wyboru 28': 'Off', 'Pole wyboru 29': 'Off', 'Pole wyboru 30': 'Off', 'Pole wyboru 31': 'Tak', 'Pole wyboru 32': 'Tak',
                             'Pole wyboru 33': 'Off', 'Pole wyboru 34': 'Off', 'Pole wyboru 35': 'Off', 'Pole wyboru 36': 'Off', 'Pole wyboru 37': 'Tak', 'Pole wyboru 38': 'Tak',
                             'Pole wyboru 39': 'Tak', 'Pole wyboru 40': 'Tak', 'Head 2': '        PROTOKÓŁ ODBIORU CENTRALI'}


#   heater

        if self.heater_choice_value.get() == 1:
            data_tabliczka_out['electric heater s'] = self.electric_heater_plate_value.get()
            data_atest_out['Pole tekstowe 8'] = self.symbol_electric_heater_value.get()
            if self.selected_ahu_value.get() =='EVO-T+':
                data_tabliczka_out['electric heater u'] = "typ"
                if self.accept_english_switch.get():
                    data_tabliczka_out['electric heater u'] = "type"
            else:
                data_tabliczka_out['electric heater u'] = "kW[kW/V]"
        elif self.heater_choice_value.get() == 2:
            data_tabliczka_out['heatre I s'] = self.water_heater_plate_value.get()
            data_atest_out['Pole tekstowe 8'] = self.symbol_water_heater_value.get()
            if self.selected_ahu_value.get() == 'EVO-T+':
                data_tabliczka_out['heatre I u'] = 'typ'
                if self.accept_english_switch.get():
                    data_tabliczka_out['heatre I u'] = 'type'
            else:
                data_tabliczka_out_ENG['heatre I u'] = '°C/kW/kPa'

        elif self.heater_choice_value.get() == 3:
            data_tabliczka_out['cooler s'] = self.reverse_heater_plate_value.get()
            data_atest_out['Pole tekstowe 7'] = self.symbol_reverse_exchanger_value.get()
        elif self.heater_choice_value.get() == 4:
            data_tabliczka_out['electric heater s'] =''
            data_tabliczka_out['heatre I s'] = ''
            data_atest_out['Pole tekstowe 8'] = ''

        ######

            # Unit heater plate


        #   cooler
        if self.cooler_choice_value.get() == 1:
            data_tabliczka_out['cooler s'] = self.water_cooler_plate_value.get()
            data_atest_out['Pole tekstowe 7'] = self.symbol_water_cooler_value.get()
            data_tabliczka_out['cooler u'] = get_data.unit_water_cooler
        elif self.cooler_choice_value.get() == 2:
            data_tabliczka_out['cooler s'] = self.refrageration_cooler_plate_value.get()
            data_atest_out['Pole tekstowe 7'] = self.symbol_refrageration_cooler_value.get()
            data_tabliczka_out['cooler u'] = 'kW/czynnik'
            data_tabliczka_out_ENG['cooler u'] = 'kW/refrigerant'
        elif self.cooler_choice_value.get() == 4:
            data_tabliczka_out['cooler s'] = ''
            data_atest_out['Pole tekstowe 7'] = ''
        ######

#   fan EC

        if self.fan_choice_value.get() == 1:
                try:
                    self.quantity_EC_supply_fan_value = int(self.quantity_EC_supply_fan_value.get())
                except:
                    self.quantity_EC_supply_fan_value =1




                if int(self.quantity_EC_supply_fan_value) > 1 :
                    self.qfan_sup_EC = str(self.quantity_EC_supply_fan_value) + ' x '
                elif self.quantity_EC_supply_fan_value == 1 :
                    self.qfan_sup_EC = ''
                else :
                    self.qfan_sup_EC = ''
                    self.quantity_EC_supply_fan_value = ''

                try:
                    self.quantity_EC_exhaust_fan_value = int(self.quantity_EC_exhaust_fan_value.get())
                except:
                    self.quantity_EC_exhaust_fan_value = 1


                if int(self.quantity_EC_exhaust_fan_value) > 1:
                    self.qfan_exh_EC = str(self.quantity_EC_exhaust_fan_value) + ' x '
                elif self.quantity_EC_exhaust_fan_value == 1:
                    self.qfan_exh_EC = ''
                else:
                    self.qfan_exh_EC = ''
                    self.quantity_EC_exhaust_fan_value = ''





                data_tabliczka_out['fan el mot s'] = self.symbol_EC_supply_fan_value.get()

                data_tabliczka_out['fan el mot e'] = self.symbol_EC_exhaust_fan_value.get()



                data_atest_out['Pole tekstowe 27'] = self.qfan_sup_EC + self.symbol_EC_supply_fan_value.get() + '\r' + self.qfan_exh_EC + self.symbol_EC_exhaust_fan_value.get()
                data_atest_out['Pole tekstowe 9'] = self.qfan_sup_EC + self.power_EC_supply_fan_value.get()  + '\r' +  self.qfan_exh_EC + self.power_EC_exhaust_fan_value.get()
                data_atest_out['Pole tekstowe 10'] = self.voltage_EC_supply_fan_value.get() + '\r' + self.voltage_EC_exhaust_fan_value.get()
                data_atest_out['Pole tekstowe 11'] = self.frequency_EC_supply_fan_value.get() + '\r' + self.frequency_EC_exhaust_fan_value.get()



                try:
                    if float(self.power_EC_supply_fan_value.get()) > 0 :
                        data_tabliczka_out['comp un s'] = self.qfan_sup_EC + self.power_EC_supply_fan_value.get() + ' / ' + self.voltage_EC_supply_fan_value.get()
                    else:
                        data_tabliczka_out['comp un s'] = ''
                except:
                    data_tabliczka_out['comp un s'] = ''



                try:
                    if float(self.power_EC_exhaust_fan_value.get()) >0 :
                        data_tabliczka_out['comp un e'] = self.qfan_exh_EC  + self.power_EC_exhaust_fan_value.get() + ' / ' + self.voltage_EC_exhaust_fan_value.get()
                    else:
                        data_tabliczka_out['comp un e'] = ''
                except:
                    data_tabliczka_out['comp un e'] = ''


        #    fan AC


        elif self.fan_choice_value.get() == 2:
            try:
                self.quantity_AC_supply_fan_value = int(self.quantity_AC_supply_fan_value.get())
            except:
                self.quantity_AC_supply_fan_value = 1

            if int(self.quantity_AC_supply_fan_value) > 1:

                self.qfan_sup_AC =  str(self.quantity_AC_supply_fan_value )+ ' x '

            elif self.quantity_AC_supply_fan_value == 1:
                self.qfan_sup_AC = ''
            else:
                self.qfan_sup_AC = ''
                self.quantity_AC_supply_fan_value = ''

            try:
                self.quantity_AC_exhaust_fan_value = int(self.quantity_AC_exhaust_fan_value.get())
            except:
                self.quantity_AC_exhaust_fan_value = 1

            if int(self.quantity_AC_exhaust_fan_value) > 1:

                self.qfan_exh_AC =  str(self.quantity_AC_exhaust_fan_value) + ' x '

            elif self.quantity_AC_exhaust_fan_value == 1:
                self.qfan_exh_AC = ''
            else:
                self.qfan_exh_AC = ''
                self.quantity_AC_exhaust_fan_value = ''






            data_tabliczka_out['fan el mot s'] = self.symbol_AC_supply_fan_value.get()
            data_tabliczka_out['fan el mot e'] = self.symbol_AC_exhaust_fan_value.get()


            data_atest_out['Pole tekstowe 27'] = self.qfan_sup_AC + self.symbol_AC_supply_fan_value.get() + '\r' + self.qfan_exh_AC + self.symbol_AC_exhaust_fan_value.get()
            data_atest_out['Pole tekstowe 9'] = self.qfan_sup_AC + self.power_AC_supply_fan_value.get() + '\r' + self.qfan_exh_AC +  self.power_AC_exhaust_fan_value.get()
            data_atest_out['Pole tekstowe 10'] = self.voltage_AC_supply_fan_value.get() + '\r' + self.voltage_AC_exhaust_fan_value.get()
            data_atest_out['Pole tekstowe 11'] = self.frequency_AC_supply_fan_value.get() + '\r' + self.frequency_AC_exhaust_fan_value.get()


            try:
                if float(self.power_AC_supply_fan_value.get()) > 0 :
                    data_tabliczka_out['comp un s'] = self.qfan_sup_AC + self.power_AC_supply_fan_value.get() + ' / ' + self.voltage_AC_supply_fan_value.get()

                else:
                    data_tabliczka_out['comp un s'] = ''
            except:
                data_tabliczka_out['comp un s'] = ''

            try:
                if float(self.power_AC_exhaust_fan_value.get()) >0 :
                    data_tabliczka_out['comp un e'] = self.qfan_exh_AC + self.power_AC_exhaust_fan_value.get()  + ' / ' + self.voltage_AC_exhaust_fan_value.get()
                else:
                    data_tabliczka_out['comp un e'] = ''
            except:
                data_tabliczka_out['comp un e'] = ''



                # lack off

        elif self.fan_choice_value.get() == 4:


            data_tabliczka_out['fan el mot s'] = ''

            data_tabliczka_out['fan el mot e'] = ''

            data_atest_out['Pole tekstowe 27'] = ''

            data_atest_out['Pole tekstowe 9'] =  ''

            data_atest_out['Pole tekstowe 10'] = ''

            data_atest_out['Pole tekstowe 11'] = ''

            data_tabliczka_out['comp un s'] = ''

            data_tabliczka_out['comp un e'] = ''


       ######

# filters


        if self.supply_filter_choice_value.get() == 1 :


            try:
                self.symbol_G4_supply_filter_value_A = ((self.symbol_G4_supply_filter_value.get()).split('  '))[0]
                data_tabliczka_out['pre filt 2 s'] = 'G4/' + self.symbol_G4_supply_filter_value_A + '/' + self.quantity_G4_supply_filter_value.get()


            except:
                self.symbol_G4_supply_filter_value_A = ''

            try:
                self.symbol_G4_supply_filter_value_B = ((self.symbol_G4_supply_filter_value.get()).split('  '))[1]
                data_tabliczka_out['pre filt 3 s'] = 'G4/' + self.symbol_G4_supply_filter_value_B + '/' + self.quantity_G4_supply_filter_value.get()

            except:
                self.symbol_G4_supply_filter_value_B = ''

            data_atest_out['Pole tekstowe 12'] = 'G4/' + self.symbol_G4_supply_filter_value_A + '/' + self.quantity_G4_supply_filter_value.get()

            if self.symbol_G4_supply_filter_value_B != '':
                data_atest_out['Pole tekstowe 12'] =  data_atest_out['Pole tekstowe 12'] + '\r' +'G4/' + self.symbol_G4_supply_filter_value_B + '/' + self.quantity_G4_supply_filter_value.get()



        if self.supply_filter_choice_value.get() == 2 :


            try:
                self.symbol_M5_supply_filter_value_A = ((self.symbol_M5_supply_filter_value.get()).split('  '))[0]
                data_tabliczka_out['pre filt 2 s'] = 'M5/' + self.symbol_M5_supply_filter_value_A + '/' + self.quantity_M5_supply_filter_value.get()
            except:
                self.symbol_M5_supply_filter_value_A = ''

            try:
                self.symbol_M5_supply_filter_value_B = ((self.symbol_M5_supply_filter_value.get()).split('  '))[1]
                data_tabliczka_out['pre filt 3 s'] = 'M5/' + self.symbol_M5_supply_filter_value_B + '/' + self.quantity_M5_supply_filter_value.get()
            except:
                self.symbol_M5_supply_filter_value_B = ''

            data_atest_out['Pole tekstowe 12'] = 'M5/' + self.symbol_M5_supply_filter_value_A + '/' + self.quantity_M5_supply_filter_value.get()

            if self.symbol_M5_supply_filter_value_B != '':
                data_atest_out['Pole tekstowe 12'] = data_atest_out['Pole tekstowe 12'] + '\r' + 'M5/' + self.symbol_M5_supply_filter_value_B + '/' +self.quantity_M5_supply_filter_value.get()





        if self.supply_filter_choice_value.get() == 3 :

            try:
                self.symbol_F7_supply_filter_value_A = ((self.symbol_F7_supply_filter_value.get()).split('  '))[0]
                data_tabliczka_out['pre filt 2 s'] = 'F7/' + self.symbol_F7_supply_filter_value_A + '/' + self.quantity_F7_supply_filter_value.get()
            except:
                self.symbol_F7_supply_filter_value_A = ''

            try:
                self.symbol_F7_supply_filter_value_B = ((self.symbol_F7_supply_filter_value.get()).split('  '))[1]
                data_tabliczka_out['pre filt 3 s'] = 'F7/' + self.symbol_F7_supply_filter_value_B + '/' + self.quantity_F7_supply_filter_value.get()
            except:
                self.symbol_F7_supply_filter_value_B = ''

            data_atest_out['Pole tekstowe 12'] = 'F7/ ' + self.symbol_F7_supply_filter_value_A + '/' + self.quantity_F7_supply_filter_value.get()

            if self.symbol_F7_supply_filter_value_B != '':
                data_atest_out['Pole tekstowe 12'] = data_atest_out['Pole tekstowe 12'] + '\r' + 'F7/' + self.symbol_F7_supply_filter_value.get() + '/' +self.quantity_F7_supply_filter_value.get()


        if self.supply_filter_choice_value.get() == 4 :

            try:
                self.symbol_F9_supply_filter_value_A = ((self.symbol_F9_supply_filter_value.get()).split('  '))[0]
                data_tabliczka_out['pre filt 2 s'] = 'F9/' + self.symbol_F9_supply_filter_value_A + '/' + self.quantity_F9_supply_filter_value.get()
            except:
                self.symbol_F9_supply_filter_value_A = ''

            try:
                self.symbol_F9_supply_filter_value_B = ((self.symbol_F9_supply_filter_value.get()).split('  '))[1]
                data_tabliczka_out['pre filt 3 s'] = 'F9/' + self.symbol_F9_supply_filter_value_B + '/' + self.quantity_F9_supply_filter_value.get()
            except:
                self.symbol_F9_supply_filter_value_B = ''

            data_atest_out['Pole tekstowe 12'] = 'F9/' + self.symbol_F9_supply_filter_value_A + '/' + self.quantity_F9_supply_filter_value.get()

            if self.symbol_F9_supply_filter_value_B != '':
                data_atest_out['Pole tekstowe 12'] = data_atest_out['Pole tekstowe 12'] + '\r'+'F9/'+self.symbol_F9_supply_filter_value_B + '/' +self.quantity_F9_supply_filter_value.get()


        if self.supply_filter_choice_value.get() == 5 :
                    data_tabliczka_out['pre filt 2 s'] = ''
                    data_atest_out['Pole tekstowe 12'] = ''



        if self.supply_filter_02_choice_value.get() == 1 and self.supply_filter_02_choice_value!=0:



            try:
                self.symbol_G4_supply_filter_02_value_A = ((self.symbol_G4_supply_filter_02_value.get()).split('  '))[0]
                data_tabliczka_out['sec filt 1 s'] = 'G4/' + self.symbol_G4_supply_filter_02_value_A + '/' + self.quantity_G4_supply_filter_02_value.get()
            except:
                self.symbol_G4_supply_filter_02_value_A = ''

            try:
                self.symbol_G4_supply_filter_02_value_B = ((self.symbol_G4_supply_filter_02_value.get()).split('  '))[1]
                data_tabliczka_out['sec filt 2 s'] = 'G4/' + self.symbol_G4_supply_filter_02_value_B + '/' + self.quantity_G4_supply_filter_02_value.get()
            except:
                self.symbol_G4_supply_filter_02_value_B = ''


            data_atest_out['Pole tekstowe 12'] = data_atest_out['Pole tekstowe 12'] + '\r' + 'G4/' + self.symbol_G4_supply_filter_02_value_A  + '/' + self.quantity_G4_supply_filter_02_value.get()

            if self.symbol_G4_supply_filter_02_value_B != '':
                data_atest_out['Pole tekstowe 12'] = data_atest_out['Pole tekstowe 12'] + '\r' + 'G4/' + self.symbol_G4_supply_filter_value_B + '/' + self.quantity_G4_supply_filter_02_value.get()







        if self.supply_filter_02_choice_value.get() == 2 and self.supply_filter_02_choice_value!=0:

            try:
                self.symbol_M5_supply_filter_02_value_A = ((self.symbol_M5_supply_filter_02_value.get()).split('  '))[0]
                data_tabliczka_out['sec filt 1 s'] = 'M5/' + self.symbol_M5_supply_filter_02_value_A + '/' + self.quantity_M5_supply_filter_02_value.get()
            except:
                self.symbol_M5_supply_filter_02_value_A = ''

            try:
                self.symbol_M5_supply_filter_02_value_B = ((self.symbol_M5_supply_filter_02_value.get()).split('  '))[1]
                data_tabliczka_out['sec filt 2 s'] = 'M5/' + self.symbol_M5_supply_filter_02_value_B + '/' + self.quantity_M5_supply_filter_02_value.get()
            except:
                self.symbol_M5_supply_filter_02_value_B = ''


            data_atest_out['Pole tekstowe 12'] = data_atest_out['Pole tekstowe 12'] + '\r' + 'M5/' + self.symbol_M5_supply_filter_02_value_A + '/' + self.quantity_M5_supply_filter_02_value.get()

            if self.symbol_M5_supply_filter_02_value_B != '':
                data_atest_out['Pole tekstowe 12'] = data_atest_out['Pole tekstowe 12'] + '\r' + 'M5/' + self.symbol_M5_supply_filter_02_value_B + '/' + self.quantity_M5_supply_filter_02_value.get()

        if self.supply_filter_02_choice_value.get() == 3 and self.supply_filter_02_choice_value!=0:

            try:
                self.symbol_F7_supply_filter_02_value_A = ((self.symbol_F7_supply_filter_02_value.get()).split('  '))[0]
                data_tabliczka_out['sec filt 1 s'] = 'F7/' + self.symbol_F7_supply_filter_02_value_A + '/' + self.quantity_F7_supply_filter_02_value.get()
            except:
                self.symbol_F7_supply_filter_02_value_A = ''

            try:
                self.symbol_F7_supply_filter_02_value_B = ((self.symbol_F7_supply_filter_02_value.get()).split('  '))[1]
                data_tabliczka_out['sec filt 2 s'] = 'F7/' + self.symbol_F7_supply_filter_02_value_B + '/' + self.quantity_F7_supply_filter_02_value.get()
            except:
                self.symbol_F7_supply_filter_02_value_B = ''

            data_atest_out['Pole tekstowe 12'] = data_atest_out['Pole tekstowe 12'] + '\r' + 'F7/' + self.symbol_F7_supply_filter_02_value_A + '/' + self.quantity_F7_supply_filter_02_value.get()

            if self.symbol_F7_supply_filter_02_value_B != '':
                data_atest_out['Pole tekstowe 12'] = data_atest_out['Pole tekstowe 12'] + '\r' + 'F7/' + self.symbol_F7_supply_filter_02_value_B + '/' + self.quantity_F7_supply_filter_02_value.get()

        if self.supply_filter_02_choice_value.get() == 4 and self.supply_filter_02_choice_value!=0:

            try:
                self.symbol_F9_supply_filter_02_value_A = ((self.symbol_F9_supply_filter_02_value.get()).split('  '))[0]
                data_tabliczka_out['sec filt 1 s'] = 'F9/' + self.symbol_F9_supply_filter_02_value_A + '/' + self.quantity_F9_supply_filter_02_value.get()
            except:
                self.symbol_F9_supply_filter_02_value_A = ''

            try:
                self.symbol_F9_supply_filter_02_value_B = ((self.symbol_F9_supply_filter_02_value.get()).split('  '))[1]
                data_tabliczka_out['sec filt 2 s'] = 'F9/' + self.symbol_F9_supply_filter_02_value_B + '/' + self.quantity_F9_supply_filter_02_value.get()
            except:
                self.symbol_F9_supply_filter_02_value_B = ''

            data_atest_out['Pole tekstowe 12'] = data_atest_out['Pole tekstowe 12'] + '\r' + 'F9/' + self.symbol_F9_supply_filter_02_value_A + '/' + self.quantity_F9_supply_filter_02_value.get()

            if self.symbol_F9_supply_filter_02_value_B != '':
                data_atest_out['Pole tekstowe 12'] = data_atest_out['Pole tekstowe 12'] + '\r' + 'F9/' + self.symbol_F9_supply_filter_02_value_B + '/' + self.quantity_F9_supply_filter_02_value.get()

        if self.supply_filter_02_choice_value.get() == 5 and self.supply_filter_02_choice_value!=0:
            data_tabliczka_out['sec filt 1 s'] = ''
            data_atest_out['Pole tekstowe 12'] = data_atest_out['Pole tekstowe 12']




        if self.exhaust_filter_choice_value.get() == 1 :


            try:
                self.symbol_G4_exhaust_filter_value_A = ((self.symbol_G4_exhaust_filter_value.get()).split('  '))[0]
                data_tabliczka_out['pre filt 2 e'] = 'G4/' + self.symbol_G4_exhaust_filter_value_A + '/' + self.quantity_G4_exhaust_filter_value.get()
            except:
                self.symbol_G4_exhaust_filter_value_A = ''

            try:
                self.symbol_G4_exhaust_filter_value_B = ((self.symbol_G4_exhaust_filter_value.get()).split('  '))[1]
                data_tabliczka_out['pre filt 3 e'] = 'G4/' + self.symbol_G4_exhaust_filter_value_B + '/' + self.quantity_G4_exhaust_filter_value.get()
            except:
                self.symbol_G4_exhaust_filter_value_B = ''



            data_atest_out['Pole tekstowe 25'] = 'G4/' + self.symbol_G4_exhaust_filter_value_A + '/' + self.quantity_G4_exhaust_filter_value.get()

            if self.symbol_G4_exhaust_filter_value_B != '':
                data_atest_out['Pole tekstowe 25'] = data_atest_out['Pole tekstowe 25'] + '\r' + 'G4/' + self.symbol_G4_exhaust_filter_value_B + '/' + self.quantity_G4_exhaust_filter_value.get()






        if self.exhaust_filter_choice_value.get() == 2 :

            try:
                self.symbol_M5_exhaust_filter_value_A = ((self.symbol_M5_exhaust_filter_value.get()).split('  '))[0]
                data_tabliczka_out['pre filt 2 e'] = 'M5/' + self.symbol_M5_exhaust_filter_value_A + '/' + self.quantity_M5_exhaust_filter_value.get()
            except:
                self.symbol_M5_exhaust_filter_value_A = ''

            try:
                self.symbol_M5_exhaust_filter_value_B = ((self.symbol_M5_exhaust_filter_value.get()).split('  '))[1]
                data_tabliczka_out['pre filt 3 e'] = 'M5/' + self.symbol_M5_exhaust_filter_value_B + '/' + self.quantity_M5_exhaust_filter_value.get()
            except:
                self.symbol_M5_exhaust_filter_value_B = ''


            data_atest_out['Pole tekstowe 25'] = 'M5/' + self.symbol_M5_exhaust_filter_value_A + '/' + self.quantity_M5_exhaust_filter_value.get()

            if self.symbol_M5_exhaust_filter_value_B != '':
                data_atest_out['Pole tekstowe 25'] = data_atest_out['Pole tekstowe 25'] + '\r' + 'M5/' + self.symbol_M5_exhaust_filter_value_B + '/' + self.quantity_M5_exhaust_filter_value.get()

        if self.exhaust_filter_choice_value.get() == 3 :

            try:
                self.symbol_F7_exhaust_filter_value_A = ((self.symbol_F7_exhaust_filter_value.get()).split('  '))[0]
                data_tabliczka_out['pre filt 2 e'] = 'F7/' + self.symbol_F7_exhaust_filter_value_A + '/' + self.quantity_F7_exhaust_filter_value.get()
            except:
                self.symbol_F7_exhaust_filter_value_A = ''

            try:
                self.symbol_F7_exhaust_filter_value_B = ((self.symbol_F7_exhaust_filter_value.get()).split('  '))[1]
                data_tabliczka_out['pre filt 3 e'] = 'F7/' + self.symbol_F7_exhaust_filter_value_B + '/' + self.quantity_F7_exhaust_filter_value.get()
            except:
                self.symbol_F7_exhaust_filter_value_B = ''

            data_atest_out['Pole tekstowe 25'] = 'F7/' + self.symbol_F7_exhaust_filter_value_A + '/' + self.quantity_F7_exhaust_filter_value.get()

            if self.symbol_F7_exhaust_filter_value_B != '':
                data_atest_out['Pole tekstowe 25'] = data_atest_out['Pole tekstowe 25'] + '\r' + 'F7/' + self.symbol_F7_exhaust_filter_value_B + '/' + self.quantity_F7_exhaust_filter_value.get()

        if self.exhaust_filter_choice_value.get() == 4 :

            try:
                self.symbol_F9_exhaust_filter_value_A = ((self.symbol_F9_exhaust_filter_value.get()).split('  '))[0]
                data_tabliczka_out['pre filt 2 e'] = 'F9/' + self.symbol_F9_exhaust_filter_value_A + '/' + self.quantity_F9_exhaust_filter_value.get()
            except:
                self.symbol_F9_exhaust_filter_value_A = ''

            try:
                self.symbol_F9_exhaust_filter_value_B = ((self.symbol_F9_exhaust_filter_value.get()).split('  '))[1]
                data_tabliczka_out['pre filt 3 e'] = 'F9/' + self.symbol_F9_exhaust_filter_value_B + '/' + self.quantity_F9_exhaust_filter_value.get()
            except:
                self.symbol_F9_exhaust_filter_value_B = ''


            data_atest_out['Pole tekstowe 25'] = 'F9/' + self.symbol_F9_exhaust_filter_value_A + '/' + self.quantity_F9_exhaust_filter_value.get()

            if self.symbol_F9_exhaust_filter_value_B != '':
                data_atest_out['Pole tekstowe 25'] = data_atest_out['Pole tekstowe 25'] + '\r' + 'F9/' + self.symbol_F9_exhaust_filter_value_B + '/' + self.quantity_F9_exhaust_filter_value.get()


        if self.exhaust_filter_choice_value.get() == 5 :
            data_tabliczka_out['pre filt 2 e'] = ''
            data_atest_out['Pole tekstowe 25'] = ''





        if self.exhaust_filter_02_choice_value.get() == 1 and self.exhaust_filter_02_choice_value != 0:

            try:
                self.symbol_G4_exhaust_filter_02_value_A = ((self.symbol_G4_exhaust_filter_02_value.get()).split('  '))[0]
                data_tabliczka_out['sec filt 1 e'] = 'G4/' + self.symbol_G4_exhaust_filter_02_value_A + '/' + self.quantity_G4_exhaust_filter_02_value.get()
            except:
                self.symbol_G4_exhaust_filter_02_value_A = ''

            try:
                self.symbol_G4_exhaust_filter_02_value_B = ((self.symbol_G4_exhaust_filter_02_value.get()).split('  '))[1]
                data_tabliczka_out['sec filt 2 e'] = 'G4/' + self.symbol_G4_exhaust_filter_02_value_B + '/' + self.quantity_G4_exhaust_filter_02_value.get()
            except:
                self.symbol_G4_exhaust_filter_02_value_B = ''

            data_atest_out['Pole tekstowe 25'] = data_atest_out['Pole tekstowe 25'] + '\r' + 'G4/' + self.symbol_G4_exhaust_filter_02_value_A + '/' + self.quantity_G4_exhaust_filter_02_value.get()

            if self.symbol_G4_exhaust_filter_02_value_B != '':
                data_atest_out['Pole tekstowe 25'] = data_atest_out['Pole tekstowe 25'] + '\r' + 'G4/' + self.symbol_G4_exhaust_filter_02_value_B + '/' + self.quantity_G4_exhaust_filter_02_value.get()

        if self.exhaust_filter_02_choice_value.get() == 2 and self.exhaust_filter_02_choice_value != 0:

            try:
                self.symbol_M5_exhaust_filter_02_value_A = ((self.symbol_M5_exhaust_filter_02_value.get()).split('  '))[0]
                data_tabliczka_out['sec filt 1 e'] = 'M5/' + self.symbol_M5_exhaust_filter_02_value_A + '/' + self.quantity_M5_exhaust_filter_02_value.get()
            except:
                self.symbol_M5_exhaust_filter_02_value_A = ''

            try:
                self.symbol_M5_exhaust_filter_02_value_B = ((self.symbol_M5_exhaust_filter_02_value.get()).split('  '))[1]
                data_tabliczka_out['sec filt 2 e'] = 'M5/' + self.symbol_M5_exhaust_filter_02_value_B + '/' + self.quantity_M5_exhaust_filter_02_value.get()
            except:
                self.symbol_M5_exhaust_filter_02_value_B = ''


            data_atest_out['Pole tekstowe 25'] = data_atest_out['Pole tekstowe 25'] + '\r' + 'M5/' + self.symbol_M5_exhaust_filter_02_value_A + '/' + self.quantity_M5_exhaust_filter_02_value.get()

            if self.symbol_M5_exhaust_filter_02_value_B != '':
                data_atest_out['Pole tekstowe 25'] = data_atest_out['Pole tekstowe 25'] + '\r' + 'M5/' + self.symbol_M5_exhaust_filter_02_value_B + '/' + self.quantity_M5_exhaust_filter_02_value.get()


        if self.exhaust_filter_02_choice_value.get() == 3 and self.exhaust_filter_02_choice_value != 0:
            try:
                self.symbol_F7_exhaust_filter_02_value_A = ((self.symbol_F7_exhaust_filter_02_value.get()).split('  '))[0]
                data_tabliczka_out['sec filt 1 e'] = 'F7/' + self.symbol_F7_exhaust_filter_02_value_A + '/' + self.quantity_F7_exhaust_filter_02_value.get()
            except:
                self.symbol_F7_exhaust_filter_02_value_A = ''

            try:
                self.symbol_F7_exhaust_filter_02_value_B = ((self.symbol_F7_exhaust_filter_02_value.get()).split('  '))[1]
                data_tabliczka_out['sec filt 2 e'] = 'F7/' + self.symbol_F7_exhaust_filter_02_value_B + '/' + self.quantity_F7_exhaust_filter_02_value.get()
            except:
                self.symbol_F7_exhaust_filter_02_value_B = ''

            data_atest_out['Pole tekstowe 25'] = data_atest_out['Pole tekstowe 25'] + '\r' + 'F7/' + self.symbol_F7_exhaust_filter_02_value_A + '/' + self.quantity_F7_exhaust_filter_02_value.get()

            if self.symbol_F7_exhaust_filter_02_value_B != '':
                data_atest_out['Pole tekstowe 25'] = data_atest_out['Pole tekstowe 25'] + '\r' + 'F7/' + self.symbol_F7_exhaust_filter_02_value_B + '/' + self.quantity_F7_exhaust_filter_02_value.get()


        if self.exhaust_filter_02_choice_value.get() == 4 and self.exhaust_filter_02_choice_value != 0:

            try:
                self.symbol_F9_exhaust_filter_02_value_A = ((self.symbol_F9_exhaust_filter_02_value.get()).split('  '))[0]
                data_tabliczka_out['sec filt 1 e'] = 'F9/' + self.symbol_F9_exhaust_filter_02_value_A + '/' + self.quantity_F9_exhaust_filter_02_value.get()
            except:
                self.symbol_F9_exhaust_filter_02_value_A = ''

            try:
                self.symbol_F9_exhaust_filter_02_value_B = ((self.symbol_F9_exhaust_filter_02_value.get()).split('  '))[1]
                data_tabliczka_out['sec filt 2 e'] = 'F9/' + self.symbol_F9_exhaust_filter_02_value_B + '/' + self.quantity_F9_exhaust_filter_02_value.get()
            except:
                self.symbol_F9_exhaust_filter_02_value_B = ''

            data_atest_out['Pole tekstowe 25'] = data_atest_out['Pole tekstowe 25'] + '\r' + 'F9/' + self.symbol_F9_exhaust_filter_02_value_A + '/' + self.quantity_F9_exhaust_filter_02_value.get()

            if self.symbol_F9_exhaust_filter_02_value_B != '':
                data_atest_out['Pole tekstowe 25'] = data_atest_out['Pole tekstowe 25'] + '\r' + 'F9/' + self.symbol_F9_exhaust_filter_02_value_B + '/' + self.quantity_F9_exhaust_filter_02_value.get()

        if self.exhaust_filter_02_choice_value.get() == 5 and self.exhaust_filter_02_choice_value != 0:
            data_tabliczka_out['sec filt 1 e'] = ''
            data_atest_out['Pole tekstowe 25'] = data_atest_out['Pole tekstowe 25']




#### heat_recovery

        if self.heat_exchanger_choice_value.get() == 1 or self.heat_exchanger_choice_value.get() == 2 :
            if self.damper_choice_value.get() == 1 or self.damper_choice_value.get() == 2 or self.damper_choice_value.get() == 3 or self.add_equip_choice_value.get() == 1:
                self.add_line = ''
            else:
                self.add_line = '\r'

            data_tabliczka_out['heat recovery t'] = '\r' + ' '+self.symbol_heat_exchanger_value.get()
            data_atest_out['Pole tekstowe 16'] = self.add_line + ' ' + self.symbol_heat_exchanger_value.get()

        elif self.heat_exchanger_choice_value.get() == 5 :
            data_tabliczka_out['heat recovery t'] = ''
            data_atest_out['Pole tekstowe 16'] = ''



# dampers





        if  self.damper_choice_value.get() == 1 :
            data_tabliczka_out['sec filt 4 s'] = ' ' + self.symbol_supply_damper_value.get()
            data_tabliczka_out['sec filt 4 e'] = ''
            data_tabliczka_out['sec filt 4'] = 'Tłumik'
            data_atest_out['Pole tekstowe 16'] = data_atest_out['Pole tekstowe 16'] + '\r'+ ' ' + self.symbol_supply_damper_value.get()
            if self.accept_english_switch.get():
                data_tabliczka_out['sec filt 4'] = 'Silencer'


        if  self.damper_choice_value.get() == 2 :
            data_tabliczka_out['sec filt 4 e'] = ' ' + self.symbol_exaust_damper_value.get()
            data_tabliczka_out['sec filt 4 s'] = ''
            data_tabliczka_out['sec filt 4'] = 'Tłumik'
            data_atest_out['Pole tekstowe 16'] = data_atest_out['Pole tekstowe 16'] + '\r'+ ' ' + self.symbol_exaust_damper_value.get()
            if self.accept_english_switch.get():
                data_tabliczka_out['sec filt 4'] = 'Silencer'

        if  self.damper_choice_value.get() == 3 :
            data_tabliczka_out['sec filt 4 e'] = ' ' + self.symbol_exaust_damper_value.get()
            data_tabliczka_out['sec filt 4 s'] =  ' ' + self.symbol_supply_damper_value.get()
            data_tabliczka_out['sec filt 4'] = 'Tłumik'
            data_atest_out['Pole tekstowe 16'] = data_atest_out['Pole tekstowe 16'] + '\r'+ ' ' + self.symbol_supply_damper_value.get() + ' ; ' + self.symbol_exaust_damper_value.get()
            if self.accept_english_switch.get():
                data_tabliczka_out['sec filt 4'] = 'Silencer'



#   additionals

        if self.add_equip_choice_value.get() == 1:
            data_atest_out['Pole tekstowe 16'] = data_atest_out['Pole tekstowe 16'] + '\r' + ' '+ self.txt_additional_equipment.get("1.0",END)

        elif self.add_equip_choice_value.get() == 2:
            data_atest_out['Pole tekstowe 16'] = data_atest_out['Pole tekstowe 16']

 #   S&P

        # data_atest_out['Pole tekstowe 17'] = self.txt_s_and_p.get("1.0",END)
        data_atest_out['Pole tekstowe 17'] = (self.txt_s_and_p.get("1.0",END).strip())
        print (data_atest_out['Pole tekstowe 17'])

#   Projekt


#   AHU

        data_atest_out['Pole tekstowe 26'] = self.entry_system_value.get()



    # Projekt

        data_atest_out['Pole tekstowe 19'] = self.entry_project_value.get()
        data_tabliczka_out['project no'] = self.entry_project_value.get() +'  '+self.entry_system_value.get()


    #Date
        data_atest_out['Pole tekstowe 18'] = self.data_value.get()


    # Inspector Name
        if  self.aproval_switch.get() == True :
            data_atest_out['Pole tekstowe 29']  = 'Specjalista d/s kontroli jakości' + '\r'+  self.inspector_name_value.get()
        elif  self.aproval_switch.get() == False :
            data_atest_out['Pole tekstowe 29'] = 'Specjalista d/s kontroli jakości' + '\r'



    # Mass

        data_tabliczka_out['weight t'] = self.mass_value.get()


   ###################  filter plate

        data_filter_plate_out = data_filter_plate

        try :
            data_filter_plate_out['Typ'] = self.supply_filter_type
        except:
            data_filter_plate_out['Typ'] = ''

        try:
            data_filter_plate_out['Rfilt'] = self.entry_supply_filter_plate_kind_value.get()

        except:
            data_filter_plate_out['Rfilt'] = ''

        try:
            data_filter_plate_out['Max P'] = self.entry_supply_flow_value.get()
        except:
            data_filter_plate_out['Max P'] = ''



        #############################################################

        try:
            self.symbol_supply_filter_plate_value_A = ((self.symbol_supply_filter_value.get()).split('  '))[0]

        except:
            self.symbol_supply_filter_plate_value_A = ''


        try:
            self.symbol_supply_filter_plate_value_B = ((self.symbol_supply_filter_value.get()).split('  '))[1]


        except:
            self.symbol_supply_filter_plate_value_B = ''


        data_filter_plate_out['Wymiar'] = self.symbol_supply_filter_plate_value_A + '/' +  self.quantity_supply_filter_value.get()

        if self.symbol_supply_filter_plate_value_B != '':
            data_filter_plate_out['Wymiar'] = data_filter_plate_out['Wymiar'] + '\r' + self.symbol_supply_filter_plate_value_B + '/' + self.quantity_supply_filter_value.get()

    #############################################################



        try:
            data_filter_plate_out['Klasa'] = self.entry_supply_filter_plate_filter_class_value.get()
        except:
            data_filter_plate_out['Klasa'] = ''

        try:
            data_filter_plate_out['Opor'] = self.entry_supply_filter_plate_initial_pressure_drop_value.get()
        except:
            data_filter_plate_out['Opor'] = ''

        try:
            data_filter_plate_out['Zalec'] = self.entry_supply_filter_plate_recom_final_pressure_drop_value.get()
        except:
            data_filter_plate_out['Zalec'] = ''

        try:
            data_filter_plate_out['Proj'] = self.entry_project_value.get()
        except:
            data_filter_plate_out['Proj'] = ''




        try:
            data_filter_plate_out['Typ1'] = self.exhaust_filter_type
        except:
            data_filter_plate_out['Typ1'] = ''

        try:
            data_filter_plate_out['Rfilt1'] = self.entry_exhaust_filter_plate_kind_value.get()
        except:
            data_filter_plate_out['Rfilt1'] = ''


        try:
            data_filter_plate_out['Max P1'] = self.entry_exhaust_flow_value.get()
        except:
            data_filter_plate_out['Max P1'] = ''
#####################################################################################################################################


        try:
            self.symbol_exhaust_filter_plate_value_A = ((self.symbol_exhaust_filter_value.get()).split('  '))[0]

        except:
            self.symbol_exhaust_filter_plate_value_A = ''

        try:
            self.symbol_exhaust_filter_plate_value_B = ((self.symbol_exhaust_filter_value.get()).split('  '))[1]


        except:
            self.symbol_exhaust_filter_plate_value_B = ''

        data_filter_plate_out['Wymiar1'] = self.symbol_exhaust_filter_plate_value_A + '/' + self.quantity_exhaust_filter_value.get()

        if self.symbol_exhaust_filter_plate_value_B != '':
            data_filter_plate_out['Wymiar1'] = data_filter_plate_out['Wymiar1'] + '\r' + self.symbol_exhaust_filter_plate_value_B + '/' + self.quantity_exhaust_filter_value.get()

#########################################################################################################################

        try :
            data_filter_plate_out['Klasa1'] = self.entry_exhaust_filter_plate_filter_class_value.get()
        except:
            data_filter_plate_out['Klasa1'] = ''


        try:
            data_filter_plate_out['Opor1'] = self.entry_exhaust_filter_plate_initial_pressure_drop_value.get()
        except:
            data_filter_plate_out['Opor1'] = ''

        try:

            data_filter_plate_out['Zalec1'] = self.entry_exhaust_filter_plate_recom_final_pressure_drop_value.get()
        except:
            data_filter_plate_out['Zalec1'] = ''


        try:
            data_filter_plate_out['Proj1'] = self.entry_project_value.get()
        except:
            data_filter_plate_out['Proj1'] = ''


        ###################  filter plate 02


        data_filter_02_plate_out = data_filter_02_plate

        try:
            data_filter_02_plate_out['Typ'] = self.supply_filter_02_type
        except:
            data_filter_02_plate_out['Typ'] = ''

        try:
            data_filter_02_plate_out['Rfilt'] = self.entry_supply_filter_02_plate_kind_value.get()

        except:
            data_filter_02_plate_out['Rfilt'] = ''

        try:
            data_filter_02_plate_out['Max P'] = self.entry_supply_flow_value.get()
        except:
            data_filter_02_plate_out['Max P'] = ''



###########################################################################################################
        try:
            self.symbol_supply_filter_02_plate_value_A = ((self.symbol_supply_filter_02_value.get()).split('  '))[0]

        except:
            self.symbol_supply_filter_02_plate_value_A = ''

        try:
            self.symbol_supply_filter_02_plate_value_B = ((self.symbol_supply_filter_02_value.get()).split('  '))[1]


        except:
            self.symbol_supply_filter_02_plate_value_B = ''

        data_filter_02_plate_out['Wymiar'] = self.symbol_supply_filter_02_plate_value_A + '/' + self.quantity_supply_filter_02_value.get()

        if self.symbol_supply_filter_02_plate_value_B != '':
            data_filter_02_plate_out['Wymiar'] = data_filter_02_plate_out['Wymiar'] + '\r' + self.symbol_supply_filter_02_plate_value_B + '/' + self.quantity_supply_filter_02_value.get()

        ##########################################################################################################
        try:
            data_filter_02_plate_out['Klasa'] = self.entry_supply_filter_02_plate_filter_02_class_value.get()
        except:
            data_filter_02_plate_out['Klasa'] = ''

        try:
            data_filter_02_plate_out['Opor'] = self.entry_supply_filter_02_plate_initial_pressure_drop_value.get()
        except:
            data_filter_02_plate_out['Opor'] = ''

        try:
            data_filter_02_plate_out['Zalec'] = self.entry_supply_filter_02_plate_recom_final_pressure_drop_value.get()
        except:
            data_filter_02_plate_out['Zalec'] = ''

        try:
            data_filter_02_plate_out['Proj'] = self.entry_project_value.get()
        except:
            data_filter_02_plate_out['Proj'] = ''

############################################################################################################################################




        try:
            data_filter_02_plate_out['Typ1'] = self.exhaust_filter_02_type
        except:
            data_filter_02_plate_out['Typ1'] = ''

        try:
            data_filter_02_plate_out['Rfilt1'] = self.entry_exhaust_filter_02_plate_kind_value.get()
        except:
            data_filter_02_plate_out['Rfilt1'] = ''


        try:
            data_filter_02_plate_out['Max P1'] = self.entry_exhaust_flow_value.get()
        except:
            data_filter_02_plate_out['Max P1'] = ''
###########################################################################################################################

        try:
            self.symbol_exhaust_filter_02_plate_value_A = ((self.symbol_exhaust_filter_02_value.get()).split('  '))[0]

        except:
            self.symbol_exhaust_filter_02_plate_value_A = ''

        try:
            self.symbol_exhaust_filter_02_plate_value_B = ((self.symbol_exhaust_filter_02_value.get()).split('  '))[1]


        except:
            self.symbol_exhaust_filter_02_plate_value_B = ''

        data_filter_02_plate_out['Wymiar1'] = self.symbol_exhaust_filter_02_plate_value_A + '/' + self.quantity_exhaust_filter_02_value.get()

        if self.symbol_exhaust_filter_02_plate_value_B != '':
            data_filter_02_plate_out['Wymiar1'] = data_filter_02_plate_out['Wymiar1'] + '\r' + self.symbol_exhaust_filter_02_plate_value_B + '/' + self.quantity_exhaust_filter_02_value.get()



#######################################################################################################


        try :
            data_filter_02_plate_out['Klasa1'] = self.entry_exhaust_filter_02_plate_filter_02_class_value.get()
        except:
            data_filter_02_plate_out['Klasa1'] = ''


        try:
            data_filter_02_plate_out['Opor1'] = self.entry_exhaust_filter_02_plate_initial_pressure_drop_value.get()
        except:
            data_filter_02_plate_out['Opor1'] = ''

        try:

            data_filter_02_plate_out['Zalec1'] = self.entry_exhaust_filter_02_plate_recom_final_pressure_drop_value.get()
        except:
            data_filter_02_plate_out['Zalec1'] = ''


        try:
            data_filter_02_plate_out['Proj1'] = self.entry_project_value.get()
        except:
            data_filter_02_plate_out['Proj1'] = ''





        #save
        if (os.path.split(self.path_out))[1] == self.main_folder_name:
            path_new_folder = self.path_out
        else :

            path_new_folder = os.path.join(self.path_out, self.main_folder_name)
            try:
                os.makedirs(path_new_folder)
            except:
                messagebox.showinfo('Warning','Poszę wejść do folderu Atesty....')


        try:

            path_new_subfolder = os.path.join(path_new_folder, self.entry_project_value.get() + '_' + self.entry_system_value.get())
            os.makedirs(path_new_subfolder)

            path_protocol_out = os.path.join(path_new_subfolder, self.entry_project_value.get()+ '_' + self.entry_system_value.get()+'_protokół_odbioru.pdf')
            path_plate_out = os.path.join(path_new_subfolder, self.entry_project_value.get()+ '_' + self.entry_system_value.get()+'_tabliczka.pdf')
            #path_atest_out = os.path.join(path_new_folder, self.entry_project_value.get()+ '_' + self.entry_system_value.get()+'_atest.pdf')
            path_atest_out = os.path.join(path_new_subfolder, 'Atest ' + self.entry_serial_value.get() + ' ' + self.entry_system_value.get() + '.pdf')
            path_filter_plate_out = os.path.join(path_new_subfolder, self.entry_project_value.get()+ '_' + self.entry_system_value.get()+'_tabliczka_filtra.pdf')



            path_filter_02_plate_out = os.path.join(path_new_subfolder, self.entry_project_value.get() + '_' + self.entry_system_value.get() + '_tabliczka_filtra_02.pdf')


            fillpdfs.write_fillable_pdf('data/protocol.pdf', path_protocol_out, data_protocol_out, flatten=False)
            if self.accept_english_switch.get() :
                if self.selected_ahu_value.get() == 'EVO-T+':
                    fillpdfs.write_fillable_pdf('data/tabliczka_EN_EPP.pdf', path_plate_out, data_tabliczka_out, flatten=False)
                else:
                    fillpdfs.write_fillable_pdf('data/tabliczka_EN.pdf', path_plate_out, data_tabliczka_out, flatten=False)

            else:
                if self.selected_ahu_value.get() == 'EVO-T+':
                    fillpdfs.write_fillable_pdf('data/tabliczka_PL_EPP.pdf', path_plate_out, data_tabliczka_out, flatten=False)
                else:
                    fillpdfs.write_fillable_pdf('data/tabliczka_PL.pdf', path_plate_out, data_tabliczka_out, flatten=False)




            fillpdfs.write_fillable_pdf('data/atest.pdf', path_atest_out, data_atest_out, flatten=False)

            fillpdfs.write_fillable_pdf('data/filtr_tabliczka.pdf', path_filter_plate_out, data_filter_plate_out, flatten=False)


            if self.supply_filter_02_choice_value.get() != 5 or self.exhaust_filter_02_choice_value.get() != 5:
                fillpdfs.write_fillable_pdf('data/filtr_tabliczka.pdf', path_filter_02_plate_out, data_filter_02_plate_out, flatten=False)



            self.accept_button.config(text = 'ok')

        except:
            messagebox.showerror('error', 'Coś poszło nie tak !')
      #




    #    self.path_out = filedialog.askdirectory()


    def get_server_data(self):
        self.entry_order.delete(0, 'end')
        self.entry_order.insert(END, self.order_connect_value.get())
        self.get_tocken()


########################################################################################################################


    def get_tocken(self):
        username = ''
        if self.inspector_name_value.get()  =='Jarosław Olszewski':
            username = 'jolszewski'
        elif self.inspector_name_value.get()  =='Dominik Tański':
            username = 'dtanski'
        elif self.inspector_name_value.get()  =='Marcin Elmanowski':
            username = 'melmanowski'


        if self.myToken ==0:
            self.myToken = requests.post('https://api.klimor.pl/token', {"password": str(self.password.get()), "username": username}, verify=False)

        if self.myToken.status_code ==200 or self.myToken.status_code ==201  :
            self.entry_pass.grid_remove()
            self.data_getter()





    def data_getter(self):

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        # myUrl = 'https://api-nj.klimor.pl/api/ahuacceptedreport'
        order_number_string ='00000'+ self.order_connect_value.get()
        myUrl_1 = 'https://api-cart.klimor.pl/api/public/device/aufnr/'+ order_number_string +'/projectDetails'

        # import project number
        headers = {'Authorization': str(self.myToken.json()),
                   'accept': '*/*',
                   'Content-Type': 'application/json',
                   }
        response_myUrl_1 = requests.get(myUrl_1, headers=headers, verify=False)

        try:
            project_nr_myUrl_1 = (response_myUrl_1.json())['iprojNew']

            self.entry_project.delete(0, 'end')
            self.entry_project.insert(END, str(project_nr_myUrl_1))
        except:
            self.entry_project.insert(END,'')


        try:
            project_destiny = (response_myUrl_1.json())['iname']
            self.entry_destiny.delete(0, 'end')
            self.entry_destiny.insert(END, str(project_destiny))
        except:
            self.entry_destiny.insert(END, '')



        myUrl_2 = 'https://prace.klimor.pl/api/serialNumber/orderNo/'+ order_number_string

        response_myUrl_2 = requests.get(myUrl_2 , headers=headers, verify=False)

        try:
            project_destiny = (response_myUrl_2.json())['sernr']
            self.entry_serial.delete(0, 'end')
            self.entry_serial.insert(END, str(project_destiny))
        except:
            self.entry_serial.insert(END, '')







########################################################################################################################

window = Tk()
window.title("EVOT_printer")
window.geometry('810x480')

tab_parent = ttk.Notebook(window)

tab0 = ttk.Frame(tab_parent)
tab1 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)
tab3 = ttk.Frame(tab_parent)
tab4 = ttk.Frame(tab_parent)
tab5 = ttk.Frame(tab_parent)
tab6 = ttk.Frame(tab_parent)
tab7 = ttk.Frame(tab_parent)
tab8 = ttk.Frame(tab_parent)
tab9 = ttk.Frame(tab_parent)
tab10 = ttk.Frame(tab_parent)
tab11 = ttk.Frame(tab_parent)
tab12 = ttk.Frame(tab_parent)
tab13 = ttk.Frame(tab_parent)

tab_parent.add(tab0,text = 'ustaw')
tab_parent.add(tab1,text = 'identyfikacja')
tab_parent.add(tab2,text = 'nagrzewnica')
tab_parent.add(tab3,text = 'chłodnica')
tab_parent.add(tab4,text = 'wentylatory')
tab_parent.add(tab5,text = 'flt-nawiew')
tab_parent.add(tab12,text = 'flt-naw_02')
tab_parent.add(tab6,text = 'flt-wywiew')
tab_parent.add(tab13,text = 'flt-wyw_02')
tab_parent.add(tab7,text = 'odzysk')
tab_parent.add(tab8,text = 'tłumik')
tab_parent.add(tab9,text = 'wypos')
tab_parent.add(tab10,text = 's&p')
tab_parent.add(tab11,text = 'akcept')


tab_parent.pack(expand = 1, fill = 'both')




app =Application(window)



#check

window.mainloop()


