import datetime
import pprint
import random
def tprint(data):
    column = data[0].keys()
    print(column)
    for i in data:
        # print(list(i.values()))
        # i[0].rjust(MoreStrLne(i), ' ')
        # print("|".join(map(str,list(i.values()))))
        pass
def MoreStrLne(data):
    # data = list(range(1,100,1))
    # return max(data,key=len())
    # print(data)
    return len(max(map(str,data),key=len))

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
def CreateData():
    result = []
    for i in range(1,11,1):
        temp = {"id":i,"name":"","crrent_datetime_date_time_today_":datetime.date.today().strftime('%Y/%m/%d')}
        name = ["a","ab","abc","abcd","abcde"]
        temp["name"] = random.choices(name,k=1)[0]
        result.append(temp)
    return result
if __name__ == "__main__":
    # MoreStrLne()
    # GetValueList("id",)
    data = CreateData()
    max_len = GetColumnValue(data)
    print(GetColumnValue(data))