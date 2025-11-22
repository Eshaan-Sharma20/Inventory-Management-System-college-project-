import inventory_data

def show_report():
    items = inventory_data.all_items()
    print("\ninventory:")
    if not items:
        print("no items")
        return

    print("name  cp  sp  qty")
    for k in items:
        i = items[k]
        print(i["name"] + "  " + str(i["cp"]) + "  " + str(i["sp"]) + "  " + str(i["qty"]))

def low_stock():
    items = inventory_data.all_items()
    limit = 30
    print("  low stock items (< " + str(limit) + ")")
    found = False
    for k in items:
        i = items[k]
        if i["qty"] < limit:
            print(i["name"] + "   " + str(i["qty"]))
            found = True
    if not found:
        print("none")

def profit_report():
    items = inventory_data.all_items()
    print("    profit report:")
    if not items:
        print("no items")
        return

    total = 0.0
    for k in items:
        i = items[k]
        p = i["total_profit"]
        total = total + p

        if p > 0:
            print(i["name"] + " profit: " + str(p))
        elif p < 0:
            print(i["name"] + " loss: " + str(-p))
        else:
            print(i["name"] + " no profit no loss")

    if total > 0:
        print("overall profit: " + str(total))
    elif total < 0:
        print("overall loss: " + str(-total))
    else:
        print("overall: 0")
