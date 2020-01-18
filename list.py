import sys
import datetime


f= open("list_doc","r")
sys.stdout.write
list = f.read().splitlines()


for item in list:
    if item == "press 'a' to add an item" or item == "press 'x' to remove an item":
        print(item)
    else :
      print(list.index(item) + 1,item)


u_in = input('')


if u_in == 'a' :
    print('please input the item')
    item = input('')
    list.insert(0, str(item))

if u_in == 'x':
    print('input the number before the item you want to delete')
    u_in2 = int(input())
    f2 = open("success_doc", "w+")
    f2.write( 'You completed ' + list[u_in2-1] + '!                                  ' + str(datetime.datetime.now()))

    list.pop(u_in2 - 1)
    total_succ = f2.read().splitlines()
    print(total_succ)


print('...')
f= open("list_doc","w")

for item in list:
    f.write("%s\n" % item)
f.close()