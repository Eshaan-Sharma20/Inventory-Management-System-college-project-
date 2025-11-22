import inventory_data
import pricing_module

def sale_item(name, qty_sold):
    item = inventory_data.get_item(name)

    if item is None:
        return False, "item not found"

    if qty_sold <= 0:
        return False, "quantity must be more than 0"

    available = item["qty"]

    if qty_sold > available:
        msg = "not enough stock. only " + str(available) + " left"
        return False, msg

    cp = item["cp"]
    sp = item["sp"]

    p = pricing_module.profit_sale(cp, sp, qty_sold)

    item["qty"] = available - qty_sold
    item["total_profit"] = item["total_profit"] + p

    if p > 0:
        msg = "sale done. profit = " + str(p)
    elif p < 0:
        msg = "sale done. loss = " + str(-p)
    else:
        msg = "sale done. no profit no loss"

    return True, msg, p
