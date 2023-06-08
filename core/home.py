import pandas as pd

commands_list = pd.read_csv("home_commands.csv")

class smart_home():
    
    def home_controller(command):
        if commands_list[]:   
            print('Ok')
        pass

home = smart_home()

smart_home.home_controller("ligar lâmpada quarto")