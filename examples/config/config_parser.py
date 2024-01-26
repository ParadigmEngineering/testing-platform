import yaml
import platform

class parser:
    def __init__(self, filepath):
        self.filepath=filepath
        
    def file_reader(self):
        with open(self.filepath, "r") as file_info:
            data=yaml.load(file_info)
        return data

    def settings_return(self,device):
        print(device)
        #function basically returns settings info to where ever it needs to go, currently it is just printing 

if __name__ == "__main__":
    config = parser("device_config_test.yaml")
    data=config.file_reader()
    devices=data["devices"]
    found=False
    for device in devices:
        if device==platform.system():
            config.settings_return(devices[device]) 
            found=True
    if found==False:
        config.settings_return(data["devices"]["default"])



