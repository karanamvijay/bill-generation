from datetime import datetime

name = input('Enter your name :')
#list of items in our shop
lists = '''
Rice   Rs 20k/g
suger  Rs 30k/g
salt   Rs 20k/g
oil    Rs 40k/g
panner Rs 50k/g
maggi  Rs 60k/g
boost  Rs 59k/g
colgate Rs 30k/g
'''
#dicleration
price = 0
pricelist = []
totalprice = 0
finalprice = 0
ilist = []
qlist = []
plist = []

#rates for items
# we don't have items in this list will print ["sorry you enterd items not avalable"]
items = {'rice':20,'suger':30,'salt':20,'oil':40,'panner':50,'maggi':60,'boost':59,'colgate':30}
option = int(input('list of items press 1'))
if option == 1:
    print(lists)
for i in range (len(items)):
    inp1 = int(input("if u want to by press 1 or 2 for exit:"))
    if inp1 == 2:
        break
    if inp1 == 1:
        item = input("Enter your items: ")
        quantity= int(input("Enter your Quantity:"))
        if item in items.keys():
            price = quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalammount=gst+totalprice
        else:
            print("sorry you enterd items not avalable")
    else:
        print("you enterd worng number")
    #in this line to generation our bill from vmarket :     
    inp = input("can I bill the items yes or no :")
    if inp == 'yes':
        pass
        if finalammount!=0:
            print(25*"=","vmarket",25*"=")
            print(28*" ","Vmarket SHOP BILL")
            print("Name",name,30*" ","Datetime",datetime.now())
            print(75*"-")
            print("sno",8*" ","items",8*" ","quantity",3*" ","price")

            for i in range(len(pricelist)):
                print(i,8*" ",8*" ",ilist[i],3*" ",qlist[i],8*" ",plist[i])
            print(75*"-")
            print(50*" ","totalAmmount:","Rs",totalprice)
            print(50*" ","gstAmmount:",50*" ","Rs",gst)
            print(75*"-")
            print(20*" ","finalAmmount:","Rs",finalammount)
            print(75*"-")
            print(50*" ","THANKS FOR VISITING OUR SHOP")
            print(75*"-")          



