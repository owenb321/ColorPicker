#Prismatik ColorPicker plugin

##Description
Assigns a static color for individual LEDs in the backlight

## Version 0.1

##Dependencies
* Python 2.7
* Prismatik (tested on 5.11.1)

##Installation
* Install Python 2.7
* Download the ZIP from the repository
* Unzip to a new local folder
* In Prismatik:
  * Enable the API
    * Enable `Expert mode` under `Profiles`
    * Check `Enable server` under `Experimental`
* Place the unzipped folder in the Prismatik plugins directory (e.g. `C:\Users\owenb321\Prismatik\Plugins\ColorPicker`)
* Adjust settings in the ColorPicker.ini file
* Refresh the plugin list in Prismatik

##Configuration
Settings are configured in the `ColorPicker.ini` file.
* Main
  * These are used by Prismatik to identify the plugin
* Lightpack
  * `host` - Address of the API server. `127.0.0.1` is the local machine.
  * `port` - API server port number. `3636` is the Prismatik default.
* LEDColors
  * In this section, list the LED numbers assigned by Prismatik followed by the RGB value you want to set for that LED (e.g. '2: 255,255,255' would make LED #2 white)
* Animate
  * `type` - Selects animation type; 0 = No animation, 1 = Pulsing
  * `interval` - Sets the time in seconds between animation frames. The smoothness setting in Prismatik will also affect the animation style.