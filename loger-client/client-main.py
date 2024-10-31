
from tkinter import *
from tkinter import ttk
from time import gmtime, strftime
import time
import re
import requests
import argparse

#setting up varbs and parsing arguements
transTable = str.maketrans('', '', "(),',[]")
parser = argparse.ArgumentParser()
parser.add_argument('-dt', dest='downtime', type=int)
parser.add_argument('-l', dest='loop')
args = parser.parse_args()
if args.loop:
    loop = False
else:
    loop = True
if args.downtime:
    downtime = args.downtime
else:
    downtime = 30
url = 'https://loger-ochre.vercel.app/api/ToServe.js'
#downtime is the downtime between each request in seconds

def main():
    timestamp = requests.post(url)
    timestamp = timestamp.json()
    difftime = {}
    pytime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    def format(s):
        total = {}
        total['y'] = int(s[:4])
        total['m'] = int(s[5:7])
        total['d'] = int(s[8:10])
        total['h'] = int(s[11:13])
        total['x'] = int(s[14:16])
        total['s'] = int(s[17:19])
        return total
    def difference(jt, pt):
        jstime = jt
        pytime = pt
        form = 'ymdhxs'
        new = []
        for k in range(len(form)):
            jti = int(jstime[form[k]])
            pti = int(pytime[form[k]])
            val = [12, 30, 24, 60, 60]
            if ((pti - jti) < 0) and (k > 0):
                new.append((val[k - 1] + pti) - jti)
                new[k - 1] -= 1
            else:
                new.append(pti - jti)
        return new
    for i in timestamp:
        one = str(i)
        difftime = re.sub("[A-Z]+", " ", one)
        difftime = difftime.translate(transTable)
        difftime = difftime[:-4]
        print(difftime, pytime)
        delta = (difference(format(difftime), format(pytime)))
        labels = ['Years, ', 'Months, ', 'Days, ',  'Hours, ', 'Minutes, and', ' Seconds.']
        print(delta)
        root = Tk()
        frm = ttk.Frame(root, padding=50)
        frm.grid(column=15, row=15)
        ttk.Label(frm, text="it has been ").grid(column=0, row=0)
        ttk.Button(frm, text="Quit", command=root.destroy).grid(column=5, row=5)
        for i in range(0, 12, 2):
            ttk.Label(frm, text=delta[int(i / 2)]).grid(column=i + 1, row=0)
        for i in range(1, 13, 2):
            ttk.Label(frm, text=labels[int(i / 2)]).grid(column=i + 1, row=0)
        ttk.Label(frm, text='since your attention was requested').grid(column=0, row=1)
        root.mainloop()
for i in range(10000):
    main()
    if (loop):
        try:
            time.sleep(downtime)
        except KeyboardInterrupt:
            print("THIS BROADCAST HAS BEEN INTERUPPED BY 66.6 BALLS FMMMMM")
            print("*AIR HORNN*")
            break
    else:
        break
