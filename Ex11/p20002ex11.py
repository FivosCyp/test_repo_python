def myfunction(mydict):
    somelist = []
    if isinstance(mydict, dict):
        somelist += mydict.keys()
        mydict = mydict.values()
    for values in mydict:
        if isinstance(values, list) or isinstance(values, dict) or isinstance(values, set) or isinstance(values, tuple):
            somelist += myfunction(values)
    return somelist
def most_frequent(List):
    counter = 0
    num = List[0]
    for i in List:
        curr_frequency = List.count(i)
        if (curr_frequency > counter):
            counter = curr_frequency
            num = i
    return num
my_file = eval(open("myfile.txt").read())
new_list = myfunction(my_file)
most_used_key = most_frequent(new_list)
print(new_list)
print(most_used_key)
