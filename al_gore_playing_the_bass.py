import json
import re
import math as mt
def dmsToCoords(dms: str) -> str:
    deg, minutes, seconds =  re.split('[°\']', dms)
    coords = (float(deg) + float(minutes) / 60 + float(seconds) / (60 * 60))
    return (coords)

def euclidianDist(x2, x1, y2, y1):
    return mt.sqrt(((x2 -x1) ** 2) + ((y2 -  y1) ** 2))

with open ("trains.json", mode="r") as read:
    data = read.read()
    jdata = json.loads(data)
    NcoordList = []
    WcoordList = []
    diffList = []
    timelist = []
    for i in range(len(jdata["Trains"])):
        dms = (jdata["Trains"][i]["ncoordinates"])
        coords = dmsToCoords(dms)
        NcoordList.append(coords)
        dms = (jdata["Trains"][i]["wcoordinates"])
        coords = dmsToCoords(dms)
        WcoordList.append(coords)
    for train1 in range(len(WcoordList)):
        for train2 in range(len(WcoordList)):
            train2data, train1data = jdata['Trains'][train2], jdata['Trains'][train1]
            train1time, train2time = int(re.sub(':', "", train1data['time'])), int(re.sub(':', "", train2data['time']))
            if (train1data['type'] == train2data['type']) and train2 != train1:
                difference = (train2time - train1time if train2time > train1time else train1time - train2time)
                while len(str(difference)) < 4:
                    difference = ('0' + str(difference))
                print(difference, train1, train2)
                timelist.append([difference, train1, train2])
                    
                    
    '''for k in range(len(WcoordList)):
        for i in range(len(WcoordList)):
            difference = euclidianDist(WcoordList[i], WcoordList[k], NcoordList[i], NcoordList[k])
            if (difference < 0.05) and (i != k):
                diffList.append([i, k])
    for data in diffList: 
        boolean = (jdata["Trains"][data[0]]['dow'] == jdata["Trains"][data[1]]['dow'])
        if boolean:
            print(jdata['Trains'][data[0]]['type'], jdata['Trains'][data[1]]['type'])'''


