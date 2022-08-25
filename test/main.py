from mates.controller import MatesController
from mates.widgets import MatesWidget, getWidgetId

mates = MatesController() # Defaults to ID: 0, no debug messages
    
oldR = 0
oldG = 0
oldB = 0

mates.begin() # Defaults to pin TX:0, RX:1 @9600

button0 = getWidgetId(MatesWidget.MATES_MEDIA_BUTTON, 0)
button1 = getWidgetId(MatesWidget.MATES_MEDIA_BUTTON, 1)
button2 = getWidgetId(MatesWidget.MATES_MEDIA_BUTTON, 2)

reset = {
    button0: 0,
    button1: 1,
    button2: 2,
}

mates.setBacklight(7)

while (True):
    newR = mates.getWidgetValueByIndex(MatesWidget.MATES_MEDIA_SLIDER, 0)
    newG = mates.getWidgetValueByIndex(MatesWidget.MATES_MEDIA_SLIDER, 1)
    newB = mates.getWidgetValueByIndex(MatesWidget.MATES_MEDIA_SLIDER, 2)
           
    if (newR != oldR):
        mates.setLedDigitsShortValue(0, newR)
        mates.setMediaColorLedValue(0, newR, 0, 0)
        oldR = newR

    if (newG != oldG):
        mates.setLedDigitsShortValue(1, newG)
        mates.setMediaColorLedValue(1, 0, newG, 0)
        oldG = newG

    if (newB != oldB):
        mates.setLedDigitsShortValue(2, newB)
        mates.setMediaColorLedValue(2, 0, 0, newB)
        oldB = newB
        
    while (mates.getButtonEventCount() > 0):
        btn = mates.getNextButtonEvent()
        mates.setWidgetValueByIndex(MatesWidget.MATES_MEDIA_SLIDER, reset[btn], 0)
