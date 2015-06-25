"""first try for a testing program   ---   18/16/2015"""

""" organisation:
    - load files : 3 setting files and file created by user
    - for each parameter, /!\ which one first? /!\
        - run the program for k values of the parameter
        - save the result
        - choose the best value and use it for the next steps
    - analyze (generate KPIs)
    - parse the results into an Excel file
"""

""" /!\ BEFORE LAUNCH /!\
    - check the video path (make one try to be sure)
"""

from tools import Tools
from parameters import Parameters
import time
from donnees import Donnees
from analysis import Analysis
from xlswriter import Xlswriter
import subprocess


debut = time.time()

"""importing parameters files"""
tools = Tools()
settings = Parameters(tools.openYml("caracteristiques_video.yml"))

""" parameters management strategy:
    - each file is loaded as a canvas.
    - creation of a parameter dictionary -> no : dictionary mix them all..
    - every time we run the program, we change one parameter in the canvas and dump it into a parameter file.
        + open backup, parse it, empty it, close it.
        + copy CAM3 and change the name
    - at the end of one parameter, launch the analysis program <and decide the value to adopt for this parameter> -> and changes at the end for a medium value.
"""

# script to call a command:
# >>> import os
# >>> import subprocess
# >>> subprocess.call(['./exe'])
# >>> subprocess.call(['cp', 'cam3.avi', 'results/new name.avi'])
# >>> subprocess.call(['vlc', 'name.avi', 'vlc://quit'])

settings.addOut(tools.openYml("outside.yml"))
settings.addDrone(tools.openYml("drones.yml"))

# TODO clear next lines to clean the project of any testing line ( until line a = {} )
data = Donnees("main test")
f = open("testDonnees.txt", "w")

t = tools.import_result()
t.printMe(f)
# data.appendResult("history10", t)
data.printMe(f)


a = {}  # dictionary of analysis
xls = Xlswriter()


""" --- history --- + --- 10 to 100 --- """
i = 10
while i < 110:
    stri = "history"
    name = stri + str(i)
    settings.change(stri, i)
    # subprocess.call(['./exe'])
    t = tools.import_result()
    data.appendResult(name, t)
    a[name] = Analysis(name, settings)
    a[name].addResult(t)
    subprocess.call(['cp', 'cam3.avi', 'results/'+name+'.avi'])
    i += 20
""" --- points_min --- + --- 3 to 15 --- ""
i = 3
while i < 15:
    stri = "points_min"
    name = stri + str(i)
    settings.change(stri, i)
    # subprocess.call(['./exe'])
    t = tools.openBackup()
    data.appendResult(name, t)
    a[name] = Analysis(name, settings)
    a[name].addResult(t)
    subprocess.call(['cp', 'cam3.avi', 'results/'+name+'.avi'])
    i += 3
"" --- surface_min --- + --- 5 to 50 --- ""
i = 5
while i < 55:
    stri = "surface_min"
    name = stri + str(i)
    settings.change(stri, i)
    # subprocess.call(['./exe'])
    t = tools.openBackup()
    data.appendResult(name, t)
    a[name] = Analysis(name, settings)
    a[name].addResult(t)
    subprocess.call(['cp', 'cam3.avi', 'results/'+name+'.avi'])
    i += 10
"" --- between_target --- ++ --- 100 to 1000 --- ""
i = 100
while i < 1000:
    stri = "between_target"
    name = stri + str(i)
    settings.change(stri, i)
    # subprocess.call(['./exe'])
    t = tools.openBackup()
    data.appendResult(name, t)
    a[name] = Analysis(name, settings)
    a[name].addResult(t)
    subprocess.call(['cp', 'cam3.avi', 'results/'+name+'.avi'])
    i += 100
"" --- distance_3d and distance_pixel --- ++ --- 0.5 to 5 and 20 to 200 --- ""
i = 0.5
while i < 5:
    stri = "distance_3d"
    name = stri + str(i)
    settings.change(stri, i)
    settings.change("distance_pixel", i/40)
    # subprocess.call(['./exe'])
    t = tools.openBackup()
    data.appendResult(name, t)
    a[name] = Analysis(name, settings)
    a[name].addResult(t)
    subprocess.call(['cp', 'cam3.avi', 'results/'+name+'.avi'])
    i += 0.5
"" --- size_min --- ++ --- 2 to 50 --- ""
i = 2
while i < 52:
    stri = "size_min"
    name = stri + str(i)
    settings.change(stri, i)
    # subprocess.call(['./exe'])
    t = tools.openBackup()
    data.appendResult(name, t)
    a[name] = Analysis(name, settings)
    a[name].addResult(t)
    subprocess.call(['cp', 'cam3.avi', 'results/'+name+'.avi'])
    i += 5"""

""" et maintenant, petite seance de visionnage de CAM3 des familles."""

i = 10
while i < 110:
    name = "history" + str(i)
    # subprocess.call(['vlc', 'results/'+name+'.avi', 'vlc://quit'])  # reading CAM3 and closing it at the end
    temp = input("nombre de faux positifs :    **attention : ne taper que des chiffres! ou alors exit pour arreter le programme***\n")  # reading the number
    if temp == "exit":
        raise NameError('arret volontaire du processus. For the watch.')
    a[name].addFalsep(temp)  # sending it to the analysis module
    xls.add_analysis(a[name], name, i)
    i += 20

"""i = 3
while i < 15:
    name = "points_min" + str(i)
    subprocess.call(['vlc', 'results/'+name+'.avi', 'vlc://quit'])  # reading CAM3 and closing it at the end
    temp = input("nombre de faux positifs :    **attention : ne taper que des chiffres! ou alors exit pour arreter le programme***\n")  # reading the number
    if temp == "exit":
        raise NameError('arret volontaire du processus. For the watch.')
    a[name].addFalsep(temp)  # sending it to the analysis module
    xls.add_analysis(a[name])
    i += 3

i = 5
while i < 55:
    name = "surface_min" + str(i)
    subprocess.call(['vlc', 'results/'+name+'.avi', 'vlc://quit'])  # reading CAM3 and closing it at the end
    temp = input("nombre de faux positifs :    **attention : ne taper que des chiffres! ou alors exit pour arreter le programme***\n")  # reading the number
    if temp == "exit":
        raise NameError('arret volontaire du processust. For the watch.')
    a[name].addFalsep(temp)  # sending it to the analysis module
    xls.add_analysis(a[name])
    i += 10

i = 100
while i < 1000:
    name = "between_target" + str(i)
    subprocess.call(['vlc', 'results/'+name+'.avi', 'vlc://quit'])  # reading CAM3 and closing it at the end
    temp = input("nombre de faux positifs :    **attention : ne taper que des chiffres! ou alors exit pour arreter le programme***\n")  # reading the number
    if temp == "exit":
        raise NameError('arret volontaire du processus. For the watch.')
    a[name].addFalsep(temp)  # sending it to the analysis module
    xls.add_analysis(a[name])
    i += 100

i = 0.5
while i < 5:
    name = "distance_3d" + str(i)
    subprocess.call(['vlc', 'results/'+name+'.avi', 'vlc://quit'])  # reading CAM3 and closing it at the end
    temp = input("nombre de faux positifs :    **attention : ne taper que des chiffres! ou alors exit pour arreter le programme***\n")  # reading the number
    if temp == "exit":
        raise NameError('arret volontaire du processus. For the watch.')
    a[name].addFalsep(temp)  # sending it to the analysis module
    xls.add_analysis(a[name])
    i += 0.5

i = 2
while i < 52:
    name = "size_min" + str(i)
    subprocess.call(['vlc', 'results/'+name+'.avi', 'vlc://quit'])  # reading CAM3 and closing it at the end
    temp = input("nombre de faux positifs :    **attention : ne taper que des chiffres! ou alors exit pour arreter le programme***\n")  # reading the number
    if temp == "exit":
        raise NameError('arret volontaire du processus. For the watch.')
    a[name].addFalsep(temp)  # sending it to the analysis module
    xls.add_analysis(a[name])
    i += 5"""

xls.write()


fin = time.time()
print("fini en", fin - debut, "secondes")
