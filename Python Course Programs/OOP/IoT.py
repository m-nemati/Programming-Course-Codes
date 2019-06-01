class Device:
    counter = 0

    def __init__(self, ip, mac, name):
        self.ip_address = ip
        self.mac_address = mac
        self.name = name
        Device.counter += 1

    def get_ip(self):
        # print ('My IP Address is: %s' %self.ip_address)
        return self.ip_address

class TV(Device):
    def turn_on(self):
        print ('Please Wait...')

    def turn_off(self):
        print ('Shoting down ...')

class SmartTV(TV):
    def turn_on(self):
        print ('Automatic Power On')

dv1 = Device('192.168.1.10', '4a2312bc', 'lampp')
print (dv1.get_ip())
tv1 = TV('192.168.1.11', '4abb12bc', 'LG' )
print (tv1.get_ip())
tv1.turn_on()