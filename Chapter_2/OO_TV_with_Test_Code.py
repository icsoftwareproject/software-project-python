# TV class with test code

class TV():
    def __init__(self):
        self.isOn = False
        self.isMuted = False
        # Some default list of channels
        self.channelList = [2, 4, 5, 7, 9, 11, 20, 36, 44, 54, 65]  
        self.nChannels = len(self.channelList)
        self.channelIndex = 0
        self.VOLUME_MINIMUM = 0  # constant
        self.VOLUME_MAXIMUM = 10  # constant
        self.volume = self.VOLUME_MAXIMUM // 2  # integer divide
        
    def power(self):
        self.isOn = not self.isOn   # toggle

    def volumeUp(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False  # changing the volume while isMuted, unmutes the sound
        if self.volume < self.VOLUME_MAXIMUM:
            self.volume = self.volume + 1

    def volumeDown(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False  # changing the volume while muted, unmutes the sound
        if self.volume > self.VOLUME_MINIMUM:
            self.volume = self.volume - 1

    def channelUp(self):
        if not self.isOn:
            return
        self.channelIndex = self.channelIndex + 1
        if self.channelIndex == self.nChannels:
            self.channelIndex = 0  # wrap around to the first channel

    def channelDown(self):
        if not self.isOn:
            return
        self.channelIndex = self.channelIndex - 1
        if self.channelIndex < 0:
            self.channelIndex = self.nChannels - 1    # wrap around to the top channel

    def mute(self):
        if not self.isOn:
            return
        self.isMuted = not self.isMuted

    def setChannel(self, newChannel):
        if newChannel in self.channelList:
            self.channelIndex = self.channelList.index(newChannel)
        # if the newChannel is not in our list of channels, don't do anything

    def showInfo(self):
        print()
        print('TV Status:')
        if self.isOn:
            print('    TV is: On')
            print('    Channel is:', self.channelList[self.channelIndex])
            if self.isMuted:
                print('    Volume is:', self.volume, '(sound is muted)')
            else:
                print('    Volume is:', self.volume)
        else:
            print('    TV is: Off')


# Main code
oTV = TV()  # create the TV object

# Turn the TV on and show the status
oTV.power()
oTV.showInfo()

# Change the channel up twice,  raise the volume twice, show status
oTV.channelUp()
oTV.channelUp()
oTV.volumeUp()
oTV.volumeUp()
oTV.showInfo()

# Turn the TV off, show status, turn TV on, show status
oTV.power()
oTV.showInfo()
oTV.power()
oTV.showInfo()

# Lower the volume, mute the sound, show status
oTV.volumeDown()
oTV.mute()
oTV.showInfo()

# Change the channel to 11, unmute the sound, show status
oTV.setChannel(11)

# [Note] you might expect Python to generate an error here, due to a 
# mismatch in the number of arguments (one) and the number of paramters
# (two). In practice, Python is doing a bit of behind-the-scenes work to 
# make the syntax easier to follow. 

# <object>.<method>(<any arguments>)

# Python takes <object> you specify in the call and rearranges it to 
# to become the first argument. Any values in the parentheses of the 
# method call are considered the subsequent argument(s). Thus, Python 
# makes it appear that you wrote this instead: 

# <method of object>(<object>, <any arguments>)

# def setChannel(self, newChannel)

oTV.mute()
oTV.showInfo()

# [Note] One interesting thing to note is that we don't realy keep track
# of the current channel. Instead, we keep track of the index of the current
# channel, which allows us to get the current channel at anny time by 
# using self.channelList[self.channelIndex]