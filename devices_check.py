from __future__ import absolute_import, division, print_function, unicode_literals
import sys
if sys.version_info < (3, 0):
    print("ERROR : Run the Python version 3.")
    exit()

import math
import os
import time



class DevicesCheck:
    def __init__(self):
        self.C_END     = "\033[0m"
        self.C_BOLD    = "\033[1m"
        self.C_GREEN   = "\033[32m"
        
    def clearScreen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def getDevicesList(self):
        devices_list = []
        '''old version
        for camera in glob.glob("/dev/video?"):
            # TODO delete error
            cap = cv2.VideoCapture(camera)
            if cap.isOpened():
                devices_list.append(camera)
        return devices_list
        '''
        result = os.popen('v4l2-ctl --list-devices').read()
        result_lists = result.split("\n\n")
        for result_list in result_lists:
            if result_list != '':
                result_list_2 = result_list.split('\n\t')
                devices_list.append(result_list_2[1])
        return devices_list
        
        
    def screenDevices(self):
        
        while True:
            self.clearScreen()
            devices_list = self.getDevicesList()
            self.print_width = float(5)
            self.print_height = math.ceil(len(devices_list) / self.print_width)
                
            for i in range(int(self.print_height)):
                for j in range(int(self.print_width)):
                    if not devices_list:
                        continue
                    print(str(devices_list.pop()) + self.C_BOLD + self.C_GREEN + " [v]"+self.C_END+'  '.ljust(5), end='')
                print("\n")
            time.sleep(0.5)


if __name__ == "__main__":
    devices_check = DevicesCheck()
    devices_check.screenDevices()
