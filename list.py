import datetime


f= open("list_doc","r+")
list = f.read().splitlines()

def list_disp() :
    print(15* '\n')
    for task in list:
        if task == "press 'a' to add an item" or task == "press 'x' to remove an item" or task == "type 'end' to exit":
                print(task)
        else :
                print(list.index(task) + 1, task)
    print(1 * '\n')

list_disp()
u_in = input('')
while u_in != 'end' :

    if u_in == 'a' :
        print('please input the item')
        item = input('')
        list.insert(0, str(item))
        list_disp()
        u_in = input('')


    if u_in == 'x':
        print('input the number before the item you want to delete')
        u_in2 = int(input())
        f2 = open("success_doc", "a+")
        f2.write( 'You completed ' + list[u_in2-1] + '!' + ' '*(70 - (len('You completed ' + list[u_in2-1]))) + str(datetime.datetime.now()) + '\n')

        f2 = open("success_doc", "r")
        list.pop(u_in2 - 1)
        count = len(f2.readlines())

        list_disp()
        print('Congratulations! You have completed ' + str(count) + ' total tasks!')
        u_in = input('')


    print('...')


    for item in list:
        f.write("%s\n" % item)
f.close()