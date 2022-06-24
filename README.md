# Cophic (BETA)

ATTENTION! This is still A beta version software. Many function may be unstable while running on your computer 


## About

A desktop recorder for Linux. Built using Python, GTK+ 3 and ffmpeg. It supports recording audio and video on almost all Linux interfaces.

The following formats are currently supported: **mkv**, **avi**, **mp4**, **wmv**, **gif** and **nut** (And only WebM for Wayland's GNOME session). You can stop the recording process easily by right-clicking the icon and choosing "Stop Record". Or middle-clicking the recording icon in the notifications area (but doesn't work on all interfaces).

You can choose the audio input source you want from the list. You can also set the default values you want by simply changing them in the interface, and the program will save them for you for the next time you open it.

### Localization

Cophic supports Many language for it’s app. If you want to help translating the program into your language, fork the repository on GitHub and create a new file under "po" folder with your language ISO code (like fr.po, de.po, cs.po..)

Alternatively,if you don’t know what to translate, you can openthe example.pot file and start with that

## Download

The program requires the pydbus python module, install it first:

    sudo pip install pydbus
    
and then, download it from the source code:
	git clone https://github.com/KucingMunafik/Cophic.git

or you can downloading from the tar.gz package and then, extract it
 
Requirements :gir1.2-appindicator3, gawk, python-gobject, python-urllib3, x11-utils, ffmpeg, pydbus, pulseaudio, xdg-open (or xdg-utils), python-configparser, imagemagick. 

And then run: 

    sudo python setup.py install --root=debian/Cophic --install-layout=deb --install-scripts=/usr/bin/

Run it from python2 it’s doesnt work with python3 if you did’nt have python2 yet install with
	sudo apt-get install python2
    
## License

No License
