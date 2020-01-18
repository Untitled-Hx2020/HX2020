import sys
f= open("list_doc","r")
sys.stdout.write
list = f.read().splitlines()


for item in list:
    if item == "press 'a' to add an item":
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
    u_in2 = input()



print('...')
f= open("list_doc","w")

for item in list:
    f.write("%s\n" % item)
f.close()