import sys
f= open("list_doc","w+")
sys.stdout.write
list = []
list2 = ['Add item to list? (press a)']
list.extend(list2)
print(list)
u_in = input('')
if u_in == 'a' :
    print('please input the item')
    item = input('')
    list.insert(0, item)

print('...')
sys.stdout.write(str(list))
f.close()