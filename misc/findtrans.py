import os
import re

gt5path = 'E:\Documents\GitHub\GT5-Unofficial\src\main\java'
gtpppath = 'E:\Documents\GitHub\GTplusplus\src\main\java'
bartpath = r'E:\Documents\GitHub\bartworks\src\main\java\com\github\bartimaeusnek'
tecpath = r'E:\Documents\GitHub\TecTech\src\main\java\com\github\technus\tectech'
kubapath = 'E:\Documents\GitHub\KubaTech\src\main\java\kubatech'
kekzpath = 'E:\Documents\GitHub\KekzTech\src\main\java'
ggpath = 'E:\Documents\GitHub\GoodGenerator\src\main\java\goodgenerator'
corepath = r'E:\Documents\GitHub\NewHorizonsCoreMod\src\main\java\com\dreammaster'
lathpath = 'E:\Documents\GitHub\GTNH-Lanthanides\src\main\java\com\elisis\gtnhlanth'

path = [gt5path, gtpppath, bartpath, tecpath, kubapath, kekzpath, ggpath, corepath, lathpath]

def get_files_list(raw_dir):
    files_list = []
    for filepath,dirnames,filenames in os.walk(raw_dir):
        for filename in filenames:
            files_list.append(filepath+'\\'+filename)
    return files_list

def gettrans(path):
    trans = []
    for i in path:
        with open(i, 'r', encoding="UTF-8+") as g:
              for line in g:
                  m = re.findall("trans\(\"(.*?)\",.*?\"(.*?)\"\)", line)
                  if m != []:
                      for j in m:
                          trans.append(j)
    return trans

def list_get_files_list(list):
    tsil = []
    for i in list:
        tsil.append(get_files_list(i))
    return tsil

def list_gettrans(list):
    tsil = []
    for i in list:
        tsil.append(gettrans(i))
    return tsil

listfiles = list_get_files_list(path)
translist = []

with open('dupekey.txt', 'w', encoding="UTF-8+") as f:
    listrans = list_gettrans(listfiles)
    for i in listrans:
        translist = translist + i
    translist.sort()
    for index in range(len(translist)):
        # if translist[index][1] == "Needs Cleanroom & LowGrav":
        #     print("1")
        if index == 0:
            f.write("addStringLocalization(\"Interaction_DESCRIPTION_Index_{}\", \"{}\");\r".format(translist[index][0], translist[index][1]))
        else:
            if(translist[index][0] == translist[index - 1][0] and translist[index][1] != translist[index - 1][1]):
                f.write("DUPEaddStringLocalization(\"Interaction_DESCRIPTION_Index_{}\", \"{}\");\r".format(translist[index][0],translist[index][1]))
            elif(translist[index][0] != translist[index - 1][0] and translist[index][1] != translist[index - 1][1]):
                f.write("addStringLocalization(\"Interaction_DESCRIPTION_Index_{}\", \"{}\");\r".format(translist[index][0],translist[index][1]))




