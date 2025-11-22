import inventory_data
import sales_module
import reports_module

def add_flow():
    print("  add item")
    name = input("item name: ")
    cp = float(input("cost price: "))
    sp = float(input("selling price: "))
    qty = int(input("quantity: "))
    ok = inventory_data.add_item(name, cp, sp, qty)
    if ok:
        print("item added")
    else:
        print("item already exists")

def upd_flow():
    print("  update item")
    name = input("item name: ")
    item = inventory_data.get_item(name)
    if item is None:
        print("item not found")
        return

    print("current cp", item["cp"])
    print("current sp", item["sp"])
    print("current qty", item["qty"])
    print("press enter if no change")

    cp_new =  input("new cp: ")
    sp_new = input("new sp: ")
    qty_new = input("new qty: ")

    if cp_new == None:
        cp_val = None
    else:
        cp_val = float(cp_new)

    if sp_new == None:
        sp_val = None
    else:
        sp_val = float(sp_new)

    if qty_new == None:
        qty_val = None
    else:
        qty_val = int(qty_new)

    ok = inventory_data.upd_item(name, cp_val, sp_val, qty_val)
    if ok:
        print("item updated")
    else:
        print("not updated")

def sale_flow():
    print("\nrecord sale")
    name = input("item name: ")
    qty = int(input("quantity sold: "))
    ok, msg, prof = sales_module.sale_item(name, qty)
    print(msg)

def rep_menu():
    while True:
        print(" reports")
        print("1-show inventory")
        print("2-show low stock")
        print("3-profit report")
        print("0-back")
        ch = input("choice: ")
        if ch == "1":
            reports_module.show_report()
        elif ch == "2":
            reports_module.low_stock()
        elif ch == "3":
            reports_module.profit_report()
        elif ch == "0":
            break
        else:
            print("wrong choice")

def main_menu():
    while True:
        print("\ninventory menu")
        print("1-add item")
        print("2-view inventory")
        print("3-update item")
        print("4-record sale")
        print("5-reports")
        print("0-exit")
        ch = input("choice: ")
        if ch == "1":
            add_flow()
        elif ch == "2":
            reports_module.show_report()
        elif ch == "3":
            upd_flow()
        elif ch == "4":
            sale_flow()
        elif ch == "5":
            rep_menu()
        elif ch == "0":
            print("bye")
            break
        else:
            print("wrong choice")
main_menu()
