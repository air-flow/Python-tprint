import datetime
from datetime import date
import pprint
import random
def tprint(data):
    key_len = CreateColumnDict(data)
    PrintHyphen(key_len)
    PrintColumnName(key_len)
    PrintHyphen(key_len)
    for i in data:
        temp = []
        for key,value in i.items():
            temp.append(str(value).rjust(key_len[key], " "))
        print("|"+"|".join(temp)+"|")
    PrintHyphen(key_len)
def PrintColumnName(key_list):
        temp = []
        for key,value in key_list.items():
            temp.append(str(key).rjust(key_list[key], " "))
        print("|"+"|".join(temp)+"|")
def PrintHyphen(key_list):
    print("+"+"-"*(int(len(key_list))-1+sum(list(key_list.values())))+"+")
def MoreStrLne(data):
    return len(max(map(str,data),key=len)) + 1

def GetValueList(key,data):
    temp = [i[key] for i in data]
    return temp

def GetColumnValue(data):
    key_list = data[0].keys()
    result = []
    for i in key_list:
        temp = GetValueList(i,data)
        temp.append(i)
        result.append(MoreStrLne(temp))
    return result

def CreateColumnDict(data):
    max_len = dict(zip(list(data[0].keys()),GetColumnValue(data)))
    return max_len

def CreateData():
    result = []
    for i in range(1,11,1):
        temp = {"id":i,"name":"","crrent_datetime_date_time_today_":datetime.date.today().strftime('%Y/%m/%d')}
        name = ["a","ab","abc","abcd","abcde"]
        temp["name"] = random.choices(name,k=1)[0]
        result.append(temp)
    return result

def main():
    data = CreateData()
    tprint(data)
if __name__ == "__main__":
    # main()
    pprint.pprint(CreateData())
