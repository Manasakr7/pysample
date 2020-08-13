import xlrd
class task(Exception):
    pass
def login():
    a = input("Enter The Username :")
    b = input("Enter The Password :")

    print('-'*35)
    print("WLCOME TO McDonald's...", a)
    print('-' * 35)
    print("1. VEGETARIAN PIZZA")
    print("2. NON-VEGETARIAN PIZZA")

    choice = int(input("SELECT YOUR CHOICE :"))
    if choice == 1:
        fileobj = "C:\\Users\\Megha\\Documents\\taskdb.xlsx"
        wb=xlrd.open_workbook(fileobj)
        sheet = wb.sheet_by_index(0)
        for col in range(1,2):
            print((sheet.cell(3,0).value),(sheet.cell(3,1).value),(sheet.cell(3,2).value))
            print('-'*35)
            print((sheet.cell(4, 0).value), (sheet.cell(4, 1).value), (sheet.cell(4, 2).value))
            print((sheet.cell(5, 0).value),(sheet.cell(5, 1).value),(sheet.cell(5, 2).value))
            print((sheet.cell(6, 0).value),(sheet.cell(6, 1).value),(sheet.cell(6, 2).value))
            print((sheet.cell(7, 0).value),(sheet.cell(7, 1).value),(sheet.cell(7, 2).value))
            print((sheet.cell(8, 0).value),(sheet.cell(8, 1).value),(sheet.cell(8, 2).value))
            print('-' * 35)
        item=int(input("ENTER THE DISH NUMBER :"))
        if item==1:
            print('-' * 35)
            print((sheet.cell(4, 0).value), (sheet.cell(4, 1).value), (sheet.cell(4, 2).value))
            item_price = sheet.cell(4,2).value
            print('-' * 35)
        elif item==2:
            print('-' * 35)
            print((sheet.cell(5, 0).value), (sheet.cell(5, 1).value), (sheet.cell(5, 2).value))
            item_price = sheet.cell(5, 2).value
            print('-' * 35)
        elif item==3:
            print('-' * 35)
            print((sheet.cell(6, 0).value), (sheet.cell(6, 1).value), (sheet.cell(6, 2).value))
            item_price = sheet.cell(6, 2).value
            print('-' * 35)
        elif item==4:
            print('-' * 35)
            print((sheet.cell(7, 0).value), (sheet.cell(7, 1).value), (sheet.cell(7, 2).value))
            item_price = sheet.cell(7, 2).value
            print('-' * 35)
        elif item==5:
            print('-' * 35)
            print((sheet.cell(8, 0).value), (sheet.cell(8, 1).value), (sheet.cell(8, 2).value))
            item_price = sheet.cell(8, 2).value
            print('-' * 35)
        else:
            raise task("CHOOSE THE CORRECT OPTION...!!")
        item_quant=int(input("ENTER THE NUMBER OF QUANTITIES :"))
        subtotal=int(item_price*item_quant)
        print('-' * 50)
        print("DEAR CUSTOMER...YOUR TOTAL AMOUNT IS :",subtotal)
        print('-' * 50)
        print("******************* THANK YOU *******************")
    elif choice == 2:
        fileobj = "C:\\Users\\Megha\\Documents\\taskdb.xlsx"
        wb = xlrd.open_workbook(fileobj)
        sheet = wb.sheet_by_index(1)
        for col in range(1,2):
            print((sheet.cell(3, 0).value), (sheet.cell(3, 1).value), (sheet.cell(3, 2).value))
            print('-' * 35)
            print((sheet.cell(4, 0).value), (sheet.cell(4, 1).value), (sheet.cell(4, 2).value))
            print((sheet.cell(5, 0).value), (sheet.cell(5, 1).value), (sheet.cell(5, 2).value))
            print((sheet.cell(6, 0).value), (sheet.cell(6, 1).value), (sheet.cell(6, 2).value))
            print((sheet.cell(7, 0).value), (sheet.cell(7, 1).value), (sheet.cell(7, 2).value))
            print((sheet.cell(8, 0).value), (sheet.cell(8, 1).value), (sheet.cell(8, 2).value))
            print('-' * 35)
        item = int(input("ENTER THE DISH NUMBER :"))
        if item == 1:
            print('-' * 35)
            print((sheet.cell(4, 0).value), (sheet.cell(4, 1).value), (sheet.cell(4, 2).value))
            item_price = sheet.cell(4, 2).value
            print('-' * 35)
        elif item == 2:
            print('-' * 35)
            print((sheet.cell(5, 0).value), (sheet.cell(5, 1).value), (sheet.cell(5, 2).value))
            item_price = sheet.cell(5, 2).value
            print('-' * 35)
        elif item == 3:
            print('-' * 35)
            print((sheet.cell(6, 0).value), (sheet.cell(6, 1).value), (sheet.cell(6, 2).value))
            item_price = sheet.cell(6, 2).value
            print('-' * 35)
        elif item == 4:
            print('-' * 35)
            print((sheet.cell(7, 0).value), (sheet.cell(7, 1).value), (sheet.cell(7, 2).value))
            item_price = sheet.cell(7, 2).value
            print('-' * 35)
        elif item==5:
            print('-' * 35)
            print((sheet.cell(8, 0).value), (sheet.cell(8, 1).value), (sheet.cell(8, 2).value))
            item_price = sheet.cell(8, 2).value
            print('-' * 35)
        else:
            raise task("CHOOSE THE CORRECT OPTION...!!")
        item_quant=int(input("ENTER THE NUMBER OF QUANTITIES :"))
        subtotal=int(item_price*item_quant)
        print('-'*50)
        print("DEAR CUSTOMER...YOUR TOTAL AMOUNT IS  :",subtotal)
        print('-' * 50)
        print("******************* THANK YOU *******************")
    else:
        raise task("CHOOSE THE CORRECT ONE!!.. ")
login()
