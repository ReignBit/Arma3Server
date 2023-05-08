import os

import keys


def mods(d):
    mods = []

    # Find mod folders
    for m in os.listdir(d):
        moddir = os.path.join(d, m)
        if os.path.isdir(moddir):
            mods.append(moddir)
            keys.copy(moddir)


    def getIndex(item):
    try:
        return int(item.split("@")[1].split("_")[0])
    except:
        return math.inf 
    mods.sort(key=getIndex)
    return mods
