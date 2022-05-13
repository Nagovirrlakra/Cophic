#!/usr/bin/python
from distutils.core import setup
from subprocess import call
from glob import glob
from os.path import splitext, split

data_files = [ ("share/cophic", ["ui/ui.glade"]),
                    ("share/pixmaps", ["data/Cophic.png"]),
                     ("share/applications", ["data/Cophic.desktop"]) ] 

po_files = glob("po/*.po")
for po_file in po_files:
  lang = splitext(split(po_file)[1])[0]
  mo_path = "locale/{}/LC_MESSAGES/Cophic.mo".format(lang)
  call("mkdir -p locale/{}/LC_MESSAGES/".format(lang), shell=True)
  call("msgfmt {} -o {}".format(po_file, mo_path), shell=True)
locales = map(lambda i: ('share/'+i, [i+'/Cophic.mo', ]), glob('locale/*/LC_MESSAGES'))

data_files.extend(locales)

setup(name = "Cophic-screen-Recorder",
      version = "3.2.3",
      description = "Record your desktop easily using a simple GUI",
      author = "The_Anuan", 
      author_email = "hypocriticalcat@pm.me",
      url = "null",
      license='GPLv3',
      scripts=['Cophic'],
      data_files=data_files)
